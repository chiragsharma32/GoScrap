# How to Upload GoScrap Project to GitHub

## Step 1: Prepare Your Project

### ⚠️ IMPORTANT: Protect Your API Key

Before uploading, make sure your API key is not exposed:

1. Open `GoScrap_Project/settings.py`
2. Replace your actual API key with the placeholder:
   ```python
   GEMINI_API_KEY = "<PASTE_MY_KEY_LOCALLY>"
   ```

**Never commit your real API key to GitHub!**

---

## Step 2: Initialize Git Repository

Open your terminal/command prompt in the project directory and run:

```bash
# Navigate to your project
cd C:\Users\vivek\GoScrap

# Initialize git repository
git init

# Add all files (the .gitignore will exclude sensitive files)
git add .

# Make your first commit
git commit -m "Initial commit: GoScrap project with AI analyzer"
```

---

## Step 3: Create GitHub Repository

### Option A: Using GitHub Website

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Fill in the details:
   - **Repository name**: `GoScrap` (or any name you prefer)
   - **Description**: "Scrap Management System with AI-powered image analysis"
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
4. Click **"Create repository"**

### Option B: Using GitHub CLI (if installed)

```bash
gh repo create GoScrap --public --source=. --remote=origin --push
```

---

## Step 4: Connect and Push to GitHub

After creating the repository on GitHub, you'll see instructions. Run these commands:

```bash
# Add GitHub repository as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/GoScrap.git

# Rename default branch to main (if needed)
git branch -M main

# Push your code to GitHub
git push -u origin main
```

If you're asked for credentials:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your GitHub password)
  - Get one from: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)

---

## Step 5: Verify Upload

1. Go to your GitHub repository page
2. You should see all your files
3. Check that `GoScrap_Project/settings.py` shows the placeholder, not your real API key

---

## Quick Command Summary

```bash
# 1. Initialize git
git init

# 2. Add files
git add .

# 3. Commit
git commit -m "Initial commit: GoScrap project with AI analyzer"

# 4. Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/GoScrap.git

# 5. Push
git branch -M main
git push -u origin main
```

---

## Troubleshooting

### "Repository not found" error
- Check that the repository name and your username are correct
- Make sure you've created the repository on GitHub first

### "Authentication failed"
- Use a Personal Access Token instead of password
- Or use SSH keys for authentication

### "Large files" warning
- The `.gitignore` should exclude large files
- If you have large files, consider using Git LFS

### Want to update later?

```bash
git add .
git commit -m "Your commit message"
git push
```

---

## Security Checklist

Before pushing, verify:
- ✅ API key is replaced with placeholder in `settings.py`
- ✅ `.gitignore` is in place
- ✅ No sensitive data in any files
- ✅ Database file (`db.sqlite3`) is excluded
- ✅ `node_modules/` is excluded

---

## Next Steps After Upload

1. Add a README.md with project description
2. Add screenshots of your website
3. Set up GitHub Pages (optional) for hosting
4. Add collaborators if working in a team



