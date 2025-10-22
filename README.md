# 🤖 gh-auto-follow

Automatically follow back your GitHub followers using GitHub Actions + Python.

## 🔧 Setup
1. Fork this repository.
2. Go to **Settings → Secrets → Actions** and add:
   - `GH_TOKEN` → Personal Access Token (scope: `user:follow`, `read:user`)
   - `GH_USERNAME` → Your GitHub username
3. Commit changes and let GitHub Actions run automatically every 6 hours.

## 🧠 How It Works
- Fetches your followers
- Checks who you already follow
- Follows back any new users automatically

## ⚙️ Tech Stack
- Python 3.10+
- PyGithub
- GitHub Actions
