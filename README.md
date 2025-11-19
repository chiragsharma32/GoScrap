# GoScrap - HUSHH AI
Scrap Management with a Smart, Eco-Friendly Approach powered by AI

## Features

- 🎨 **Modern UI**: Built with Tailwind CSS for a beautiful, responsive design
- 🤖 **AI-Powered Analysis**: Upload images of scrap materials and get instant price estimates using Google Gemini AI
- 📊 **Scrap Calculator**: Calculate scrap prices manually
- 📋 **Rate Card**: View current market rates for various materials
- 📅 **Schedule Pickup**: Book scrap collection appointments
- 👤 **User Authentication**: Sign up and sign in functionality

## Tech Stack

- **Backend**: Django 4.1.2
- **Frontend**: Tailwind CSS 3.4
- **AI**: Google Gemini 1.5 Flash
- **Database**: SQLite

## Setup Instructions

### 1. Install Dependencies

```bash
pip install django google-generativeai Pillow
```

### 2. Install Node.js Dependencies (for Tailwind CSS)

```bash
npm install
```

### 3. Build Tailwind CSS

```bash
npm run build-css-prod
```

### 4. Configure Gemini API Key

See [AI_SETUP.md](AI_SETUP.md) for detailed instructions on setting up the Google Gemini API key.

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## AI Features

The AI Scrap Analyzer allows users to:
- Upload images of scrap materials
- Get automatic material type identification
- Receive price estimates based on current market rates
- View detailed analysis of material condition and value

For setup instructions, see [AI_SETUP.md](AI_SETUP.md).

## Project Structure

```
GoScrap/
├── GoScrap/              # Main Django app
│   ├── views.py         # View functions including AI analyzer
│   ├── urls.py          # URL routing
│   └── ...
├── GoScrap_Project/     # Django project settings
│   ├── settings.py      # Django settings
│   └── urls.py          # Main URL configuration
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── home.html        # Home page
│   ├── ai_analyze.html  # AI analyzer page
│   └── ...
├── static/              # Static files
│   ├── css/
│   │   ├── input.css    # Tailwind source
│   │   └── output.css   # Compiled Tailwind CSS
│   └── ...
├── package.json         # Node.js dependencies
├── tailwind.config.js   # Tailwind configuration
└── manage.py           # Django management script
```

## Development

### Rebuild Tailwind CSS (watch mode)

```bash
npm run build-css
```

### Production Build

```bash
npm run build-css-prod
```

## License

This project is developed for HUSHH AI company.
