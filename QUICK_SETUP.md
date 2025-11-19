# Quick Setup Guide - Gemini API Key

## Option 1: Use the Setup Script (Easiest)

Run the setup script:
```bash
python setup_gemini_key.py
```

Follow the prompts to enter your API key.

## Option 2: Manual Setup

### Step 1: Get Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy your API key

### Step 2: Configure the API Key

#### Method A: Edit settings.py (Recommended for Development)

1. Open `GoScrap_Project/settings.py`
2. Find this line:
   ```python
   GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'YOUR_GEMINI_API_KEY_HERE')
   ```
3. Replace `'YOUR_GEMINI_API_KEY_HERE'` with your actual API key:
   ```python
   GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'your-actual-api-key-here')
   ```

#### Method B: Set Environment Variable (Recommended for Production)

**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
python manage.py runserver
```

**Windows CMD:**
```cmd
set GEMINI_API_KEY=your-api-key-here
python manage.py runserver
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY="your-api-key-here"
python manage.py runserver
```

### Step 3: Restart Django Server

After setting the API key, restart your Django development server:
```bash
python manage.py runserver
```

## Verify Setup

1. Navigate to the AI Analyzer page: `http://127.0.0.1:8000/ai_analyze`
2. Upload a test image
3. If configured correctly, you should see analysis results
4. If you see an error, double-check your API key

## Troubleshooting

**Error: "Gemini API key not configured"**
- Make sure you've replaced `YOUR_GEMINI_API_KEY_HERE` with your actual key
- Restart the Django server after making changes
- Check that there are no extra spaces or quotes in your API key

**Error: "API key not valid"**
- Verify your API key is correct
- Make sure you copied the entire key
- Check that your Google account has access to Gemini API

**Still having issues?**
- Try setting the environment variable method instead
- Check the console output for more detailed error messages



