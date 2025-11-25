from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import PickupRequest
import google.generativeai as genai
from PIL import Image
import io
import base64
import json
from supabase import create_client, Client
# Create your views here.

def index(request):
    return render (request, 'home.html')


def home(request):
    return render (request, 'home.html')



def about(request):
    return render (request, 'about.html')


def ratecard(request):
    return render (request, 'ratecard.html')


def calculator(request):
    return render (request, 'calculator.html')


def schedule_pickup(request):
    """Handle pickup scheduling - works with or without authentication"""
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            pickup_date = request.POST.get('pickup_date')
            pickup_time = request.POST.get('pickup_time')
            pickup_address = request.POST.get('pickup_address')
            
            # Create pickup request - use logged in user if available, otherwise None
            pickup = PickupRequest.objects.create(
                user=request.user if request.user.is_authenticated else None,
                name=name,
                email=email,
                phone=phone,
                pickup_date=pickup_date,
                pickup_time=pickup_time,
                pickup_address=pickup_address,
            )
            
            messages.success(request, 'Pickup scheduled successfully! We will contact you soon.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error scheduling pickup: {str(e)}')
            return render(request, 'schedule.html')
    
    # GET request - show form
    return render(request, 'schedule.html')



def signin(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("pass1")

        # Django uses username for authentication, and we store email as username
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('schedule_pickup')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'signin.html', {
        'supabase_url': settings.SUPABASE_URL,
        'supabase_key': settings.SUPABASE_KEY,
    })



def signup(request):
    if request.method == 'POST':
        email = request.POST["email"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        password1 = request.POST["pass1"]
        password2 = request.POST["pass2"]
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html', {
                'supabase_url': settings.SUPABASE_URL,
                'supabase_key': settings.SUPABASE_KEY,
            })

        try:
            # Create user with email as username
            myuser = User.objects.create_user(
                username=email,
                email=email,
                password=password1
            )
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, 'Account created successfully! Please sign in.')
            return redirect('signin')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'signup.html', {
                'supabase_url': settings.SUPABASE_URL,
                'supabase_key': settings.SUPABASE_KEY,
            })

    return render(request, 'signup.html', {
        'supabase_url': settings.SUPABASE_URL,
        'supabase_key': settings.SUPABASE_KEY,
    })


@csrf_exempt
def auth_callback(request):
    """Handle OAuth callback from Supabase Google OAuth"""
    if request.method == 'GET':
        # Get the access token from the URL fragment or query params
        # Supabase OAuth redirects with code in query params
        code = request.GET.get('code')
        
        if code and settings.SUPABASE_URL and settings.SUPABASE_KEY:
            try:
                supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
                
                # Exchange code for session - this might need adjustment based on Supabase Python client version
                try:
                    # Try the newer API first
                    response = supabase.auth.exchange_code_for_session(code)
                except AttributeError:
                    # Fallback for older API versions
                    response = supabase.auth.session_from_url(request.get_full_path())
                
                # Handle the response
                if hasattr(response, 'session') and response.session:
                    session = response.session
                    user_data = session.user
                elif hasattr(response, 'user'):
                    user_data = response.user
                else:
                    # If response structure is different, try to get user from session
                    session_response = supabase.auth.get_session()
                    if session_response and session_response.session:
                        user_data = session_response.session.user
                    else:
                        raise ValueError("Could not retrieve user data from OAuth response")
                
                if user_data:
                    email = user_data.email
                    user_metadata = user_data.user_metadata or {}
                    full_name = user_metadata.get('full_name', '') or user_metadata.get('name', '') or ''
                    
                    # Split full name into first and last name
                    name_parts = full_name.split(' ', 1) if full_name else ['', '']
                    first_name = name_parts[0] if len(name_parts) > 0 else ''
                    last_name = name_parts[1] if len(name_parts) > 1 else ''
                    
                    # Create or get Django user
                    try:
                        user = User.objects.get(email=email)
                    except User.DoesNotExist:
                        # Create new user with a random password (they use OAuth)
                        import secrets
                        random_password = secrets.token_urlsafe(32)
                        user = User.objects.create_user(
                            username=email,
                            email=email,
                            password=random_password
                        )
                    
                    # Update user details
                    if first_name and not user.first_name:
                        user.first_name = first_name
                    if last_name and not user.last_name:
                        user.last_name = last_name
                    user.save()
                    
                    # Log the user in
                    login(request, user)
                    
                    messages.success(request, 'Successfully signed in with Google!')
                    return redirect('schedule_pickup')
                else:
                    raise ValueError("No user data found in OAuth response")
                    
            except Exception as e:
                messages.error(request, f'Error authenticating: {str(e)}')
                return redirect('signin')
    
    # If no code or error, redirect to signin
    return redirect('signin')


def signout(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


def view_pickups(request):
    """View all pickup requests - for admin/owner"""
    if not request.user.is_authenticated or not request.user.is_superuser:
        messages.error(request, 'You need admin access to view pickups.')
        return redirect('home')
    
    pickups = PickupRequest.objects.all()
    return render(request, 'view_pickups.html', {'pickups': pickups})


def ai_analyze(request):
    """AI-powered scrap image analysis using Google Gemini"""
    if request.method == 'POST':
        try:
            # Get uploaded image
            if 'image' not in request.FILES:
                return JsonResponse({'error': 'No image provided'}, status=400)
            
            image_file = request.FILES['image']
            
            # Read image
            image_data = image_file.read()
            image = Image.open(io.BytesIO(image_data))
            
            # Configure Gemini API - read key from settings
            api_key = settings.GEMINI_API_KEY
            
            if not api_key or api_key == "<PASTE_MY_KEY_LOCALLY>":
                return JsonResponse({
                    'error': 'Gemini API key not configured. Please set GEMINI_API_KEY in settings.py.'
                }, status=500)
            
            genai.configure(api_key=api_key)
            
            # List available models and find one that supports vision
            model = None
            try:
                available_models = genai.list_models()
                # Filter models that support generateContent
                supported_models = [m for m in available_models if 'generateContent' in m.supported_generation_methods]
                
                # Prefer models with vision/image capabilities (flash, pro-vision, or 1.5 models)
                vision_models = [m for m in supported_models if any(keyword in m.name.lower() for keyword in ['flash', 'vision', '1.5', '2.0'])]
                
                if vision_models:
                    # Use the first vision-capable model
                    model_name = vision_models[0].name.split('/')[-1]
                    model = genai.GenerativeModel(model_name)
                elif supported_models:
                    # Fallback to any available model
                    model_name = supported_models[0].name.split('/')[-1]
                    model = genai.GenerativeModel(model_name)
                else:
                    return JsonResponse({
                        'error': 'No models with generateContent support found. Please check your API key.'
                    }, status=500)
                    
            except Exception as e:
                # If listing fails, try common model names
                model_names_to_try = [
                    'gemini-1.5-flash',
                    'gemini-1.5-pro',
                    'gemini-pro-vision',
                    'gemini-pro',
                ]
                
                for model_name in model_names_to_try:
                    try:
                        model = genai.GenerativeModel(model_name)
                        break
                    except:
                        continue
                
                if model is None:
                    return JsonResponse({
                        'error': f'Failed to initialize Gemini model: {str(e)}. Please check your API key and model availability.'
                    }, status=500)
            
            # Create prompt for scrap analysis
            prompt = """Analyze this image of scrap material and provide the following information in JSON format:
            {
                "material_type": "type of material (e.g., copper, aluminum, iron, plastic, paper, cardboard, brass, steel, electronics, etc.)",
                "material_description": "detailed description of the material",
                "condition": "condition of the material (e.g., clean, mixed, damaged, etc.)",
                "estimated_weight_kg": "estimated weight in kilograms (if visible or estimable)",
                "estimated_price_per_kg": "estimated price per kg in Indian Rupees based on current scrap market rates",
                "total_estimated_value": "total estimated value in Indian Rupees",
                "additional_notes": "any additional relevant information about the scrap"
            }
            
            Use current Indian scrap market rates:
            - Copper: ₹425/kg
            - Brass: ₹300/kg
            - Aluminum: ₹105/kg
            - Iron: ₹30/kg
            - Steel: ₹37/kg
            - Paper: ₹18/kg
            - Cardboard: ₹10/kg
            - Plastic: ₹10/kg
            
            Provide accurate analysis based on what you see in the image."""
            
            # Analyze image - Gemini API accepts PIL Image directly
            # For newer API versions, pass image as part of content
            try:
                response = model.generate_content([prompt, image])
            except Exception as e:
                # If direct image doesn't work, try with image bytes
                img_bytes = io.BytesIO()
                image.save(img_bytes, format='PNG')
                img_bytes.seek(0)
                response = model.generate_content([prompt, {
                    "mime_type": "image/png",
                    "data": img_bytes.read()
                }])
            
            # Parse response
            response_text = response.text.strip()
            
            # Try to extract JSON from response
            try:
                # Remove markdown code blocks if present
                if '```json' in response_text:
                    response_text = response_text.split('```json')[1].split('```')[0].strip()
                elif '```' in response_text:
                    response_text = response_text.split('```')[1].split('```')[0].strip()
                
                analysis_data = json.loads(response_text)
            except json.JSONDecodeError:
                # If JSON parsing fails, create structured response from text
                analysis_data = {
                    "material_type": "Unknown",
                    "material_description": response_text,
                    "condition": "Unknown",
                    "estimated_weight_kg": "N/A",
                    "estimated_price_per_kg": "N/A",
                    "total_estimated_value": "N/A",
                    "additional_notes": response_text
                }
            
            # Convert image to base64 for display
            img_buffer = io.BytesIO()
            image.save(img_buffer, format='PNG')
            img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
            
            return JsonResponse({
                'success': True,
                'analysis': analysis_data,
                'image': f'data:image/png;base64,{img_base64}'
            })
            
        except Exception as e:
            return JsonResponse({
                'error': f'Error analyzing image: {str(e)}'
            }, status=500)
    
    # GET request - show upload page
    return render(request, 'ai_analyze.html')
