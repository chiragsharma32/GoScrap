# AI Feature Setup Guide

## Google Gemini API Setup

The AI Scrap Analyzer feature uses Google's Gemini AI to analyze scrap images and generate price estimates. Follow these steps to set up:

### 1. Get Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 2. Configure the API Key

You have two options:

#### Option A: Environment Variable (Recommended)
Set the environment variable:
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your-api-key-here"

# Windows CMD
set GEMINI_API_KEY=your-api-key-here

# Linux/Mac
export GEMINI_API_KEY="your-api-key-here"
```

#### Option B: Direct in Settings
Edit `GoScrap_Project/settings.py` and replace:
```python
GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY_HERE'
```
with:
```python
GEMINI_API_KEY = 'your-actual-api-key-here'
```

### 3. Usage

1. Navigate to the "AI Analyzer" page from the navigation menu
2. Upload an image of your scrap material
3. Click "Analyze with AI"
4. View the AI-generated analysis including:
   - Material type identification
   - Estimated price per kg
   - Total estimated value
   - Material description and condition
   - Additional notes

### Features

- **Image Analysis**: Uses Gemini 1.5 Flash model for fast image analysis
- **Price Estimation**: Automatically calculates prices based on current Indian scrap market rates
- **Material Detection**: Identifies various scrap types (copper, aluminum, iron, plastic, paper, etc.)
- **Detailed Reports**: Provides comprehensive analysis of scrap condition and value

### Supported Materials

The AI can identify and price:
- Metals: Copper, Brass, Aluminum, Iron, Steel
- Paper Products: Newspaper, Cardboard
- Plastics
- Electronics
- And more!

### Troubleshooting

**Error: "Gemini API key not configured"**
- Make sure you've set the API key in settings.py or as an environment variable
- Restart the Django server after setting the API key

**Error: "Error analyzing image"**
- Check your internet connection
- Verify your API key is valid
- Ensure the image file is not corrupted
- Check that the image format is supported (PNG, JPG, GIF)

### API Rate Limits

Google Gemini API has rate limits. If you encounter rate limit errors:
- Wait a few minutes before trying again
- Consider upgrading your API plan if needed



