# GoScrap - AI-Powered Scrap Management System

**Scrap Management with a Smart, Eco-Friendly Approach powered by AI**

GoScrap is a modern web application that revolutionizes scrap management by combining traditional scrap collection services with AI-powered image analysis. Upload images of scrap materials and receive instant price estimates using Google Gemini AI.

## 🚀 Quick Start

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Install Node.js dependencies (for Tailwind CSS)
npm install

# 3. Build Tailwind CSS
npm run build-css-prod

# 4. Configure environment variables
# Copy env.example to .env and add your GEMINI_API_KEY
# Or edit GoScrap_Project/settings.py directly

# 5. Run database migrations
python manage.py migrate

# 6. Start development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## 📋 Features

- 🤖 **AI-Powered Analysis**: Upload images of scrap materials and get instant price estimates using Google Gemini AI
- 📊 **Scrap Calculator**: Calculate scrap prices manually with material type and weight
- 📋 **Rate Card**: View current market rates for various materials (copper, aluminum, iron, plastic, paper, etc.)
- 📅 **Schedule Pickup**: Book scrap collection appointments online
- 👤 **User Authentication**: Secure sign up and sign in functionality
- 🎨 **Modern UI**: Beautiful, responsive design built with Tailwind CSS

## 🛠 Tech Stack

### Backend
- **Framework**: Django 4.1.2
- **Language**: Python 3.8+
- **Database**: SQLite (development), PostgreSQL-ready (production)
- **AI Integration**: Google Gemini 1.5 Flash API
- **Image Processing**: Pillow 10.0.0+

### Frontend
- **Styling**: Tailwind CSS 3.4.1
- **Build Tool**: Tailwind CLI
- **Templates**: Django Templates (HTML)

### APIs & Services
- **AI Service**: Google Generative AI (Gemini 1.5 Flash)

## 📖 Documentation

- **[PROJECT_SUBMISSION.md](PROJECT_SUBMISSION.md)**: Comprehensive project documentation with all submission requirements
- **[ARCHITECTURE.md](ARCHITECTURE.md)**: Detailed system architecture, components, and data flow
- **[AI_SETUP.md](AI_SETUP.md)**: Step-by-step guide for setting up Google Gemini API
- **[env.example](env.example)**: Environment variables template

## 🔧 Setup & Run Guide

### Prerequisites
- Python 3.8 or higher
- Node.js 14.x or higher
- npm (Node Package Manager)
- Google Gemini API key ([Get it here](https://makersuite.google.com/app/apikey))

### Detailed Setup Instructions

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd GoScrap
```

#### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Install Node.js Dependencies
```bash
npm install
```

#### 5. Build Tailwind CSS
```bash
# Production build (minified)
npm run build-css-prod

# Development build (watch mode)
npm run build-css
```

#### 6. Configure Environment Variables

**Option A: Using .env file (Recommended)**
```bash
# Copy the example file
copy env.example .env  # Windows
cp env.example .env     # Linux/Mac

# Edit .env and add your API key
GEMINI_API_KEY=your-api-key-here
```

**Option B: Direct in settings.py**
Edit `GoScrap_Project/settings.py` and set:
```python
GEMINI_API_KEY = "your-api-key-here"
```

#### 7. Run Database Migrations
```bash
python manage.py migrate
```

#### 8. Create Superuser (Optional, for admin access)
```bash
python manage.py createsuperuser
```

#### 9. Run Development Server
```bash
python manage.py runserver
```

#### 10. Access the Application
Open your browser and navigate to: `http://127.0.0.1:8000`

## 🔑 Environment Variables

See [env.example](env.example) for all required environment variables.

**Key Variables:**
- `GEMINI_API_KEY`: Google Gemini API key (required for AI features)
- `SECRET_KEY`: Django secret key (required)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

**⚠️ Important**: Never commit `.env` file with real API keys or secrets to version control.

## 🎯 Core Features

### AI-Powered Scrap Analyzer
- Upload images of scrap materials
- Automatic material type identification (copper, aluminum, iron, plastic, paper, etc.)
- Real-time price estimation based on current Indian market rates
- Detailed analysis including condition assessment and weight estimation

### Scrap Calculator
- Manual calculation tool for material type and weight
- Supports multiple material types
- Instant price calculation

### Rate Card
- View current market rates for all materials
- Visual representation of different scrap types
- Transparent pricing information

### Schedule Pickup
- Online appointment booking system
- Select preferred date and time
- Streamlined collection process

## 📁 Project Structure

```
GoScrap/
├── GoScrap/                  # Main Django app
│   ├── views.py             # View functions including AI analyzer
│   ├── urls.py              # URL routing
│   ├── models.py            # Database models
│   └── ...
├── GoScrap_Project/         # Django project settings
│   ├── settings.py          # Django settings (includes GEMINI_API_KEY)
│   └── urls.py              # Main URL configuration
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── home.html            # Home page
│   ├── ai_analyze.html      # AI analyzer page
│   ├── calculator.html      # Calculator page
│   ├── ratecard.html        # Rate card page
│   ├── schedule.html        # Schedule pickup page
│   ├── signin.html          # Login page
│   ├── signup.html          # Registration page
│   └── about.html           # About page
├── static/                  # Static files
│   ├── css/
│   │   ├── input.css        # Tailwind source
│   │   └── output.css       # Compiled Tailwind CSS
│   ├── javascript/
│   │   └── calculator.js    # Calculator logic
│   └── ...
├── package.json             # Node.js dependencies
├── tailwind.config.js       # Tailwind configuration
├── requirements.txt         # Python dependencies
├── env.example              # Environment variables template
├── manage.py                # Django management script
├── PROJECT_SUBMISSION.md    # Comprehensive project documentation
├── ARCHITECTURE.md          # System architecture documentation
└── README.md                # This file
```

## 🔌 Key APIs & Endpoints

### Main Routes
- `GET /` - Home page
- `GET /home` - Home page
- `GET /about` - About page
- `GET /ratecard` - Rate card display
- `GET /calculator` - Scrap calculator
- `GET /signin` - User login page
- `GET /signup` - User registration page
- `GET /schedule_pickup` - Pickup scheduling page
- `GET /ai_analyze` - AI analyzer page
- `POST /ai_analyze` - AI image analysis endpoint

### AI Analysis API
**Endpoint**: `POST /ai_analyze`  
**Request**: Multipart form data with image file  
**Response**: JSON with analysis results

```json
{
  "success": true,
  "analysis": {
    "material_type": "copper",
    "material_description": "Clean copper wires",
    "condition": "good",
    "estimated_weight_kg": "5.0",
    "estimated_price_per_kg": "425",
    "total_estimated_value": "2125",
    "additional_notes": "..."
  },
  "image": "data:image/png;base64,..."
}
```

## 🗄 Database Schema

Currently using Django's default User model for authentication. The application is designed to be extended with:
- **UserProfile**: Extended user information
- **ScrapOrder**: Scrap collection orders
- **MaterialRate**: Dynamic rate management
- **PickupSchedule**: Appointment scheduling

## 🚀 Deployment

### Current Status
The application is configured for local development. For production deployment, see [PROJECT_SUBMISSION.md](PROJECT_SUBMISSION.md) for deployment details.

### Production Checklist
- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Use environment variables for sensitive data
- [ ] Set up PostgreSQL or MySQL database
- [ ] Configure static file serving (WhiteNoise or CDN)
- [ ] Set up SSL/HTTPS
- [ ] Configure proper security headers
- [ ] Set up error logging and monitoring

## 🧪 Development Commands

```bash
# Rebuild Tailwind CSS (watch mode for development)
npm run build-css

# Production CSS build (minified)
npm run build-css-prod

# Run Django migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic

# Run tests (when implemented)
python manage.py test
```

## 📊 Impact & Metrics

- **Time Saved**: ~90% reduction in time to get price estimate
- **Accessibility**: 24/7 availability vs. business hours only
- **Transparency**: Real-time rate information
- **AI Analysis Response Time**: ~2-5 seconds per image
- **Page Load Time**: <1 second (with compiled CSS)

## 🔮 What's Next

See [PROJECT_SUBMISSION.md](PROJECT_SUBMISSION.md) for detailed information on:
- Known limitations
- Planned improvements
- Future enhancements

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [AI Setup Guide](AI_SETUP.md)

## 📝 License

This project is developed for HUSHH AI company.

## 👥 Contributing

For project submission requirements and guidelines, refer to [PROJECT_SUBMISSION.md](PROJECT_SUBMISSION.md).
