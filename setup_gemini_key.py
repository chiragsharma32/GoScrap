"""
Gemini API Key Loader
This script loads the API key from settings.py (no user input required)
"""
import os
import sys

def get_gemini_key():
    """
    Load Gemini API key from Django settings.
    This is a no-op function that simply reads from settings.
    No user input is required.
    """
    try:
        # Add project root to path
        project_root = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, project_root)
        
        # Import Django settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GoScrap_Project.settings')
        import django
        django.setup()
        
        from django.conf import settings
        api_key = settings.GEMINI_API_KEY
        
        if api_key and api_key != "<PASTE_MY_KEY_LOCALLY>":
            return api_key
        else:
            print("Warning: GEMINI_API_KEY not configured in settings.py")
            print("Please edit GoScrap_Project/settings.py and replace <PASTE_MY_KEY_LOCALLY> with your API key")
            return None
    except Exception as e:
        print(f"Error loading API key from settings: {e}")
        return None

if __name__ == '__main__':
    key = get_gemini_key()
    if key:
        print("[OK] API key loaded from settings.py")
    else:
        print("[ERROR] API key not found or not configured")

