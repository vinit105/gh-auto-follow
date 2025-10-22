# gh-auto-follow

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

## 🔐 Security Notes

Token should **not** have repo or admin scopes — only:

- `read:user`
- `user:follow`

Actions are read-only except the follow/unfollow operations.

---

## 🪄 STEP 1 — Generate a GitHub Token

1. Visit: [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. You’ll see two sections:
   - Fine-grained tokens (newer)
   - Personal access tokens (classic)
3. ✅ For this project, use the **classic** type because it’s simpler for user actions.
4. Click **“Generate new token (classic)”**

---

## 🧠 STEP 2 — Configure Your Token

Fill the form like this:

| Field       | What to Choose |
|------------|----------------|
| Note       | `gh-auto-follow bot` |
| Expiration | No expiration (or 90 days if you prefer) |
| Select scopes | ✅ `read:user`<br>✅ `user:follow` |

> Leave everything else unchecked — don’t give repo/admin rights.  
> Click **“Generate token”**.

---

## 🪄 STEP 3 — Copy the Token

You’ll see a long key like: ghp_ABC123xyz...somethinglong


⚠️ **Copy it immediately** — GitHub will never show it again!

---

## 🔐 STEP 4 — Add It as a Secret in Your Repo

1. Go to your repository → **Settings → Secrets and variables → Actions**
2. Click **“New repository secret”**
3. Add:

| Name        | Value                       |
|------------|-----------------------------|
| GH_TOKEN    | (paste your token here)     |
| GH_USERNAME | your GitHub username        |

✅ Done! Secrets are now securely stored.

---

## 🚀 STEP 5 — Run Your GitHub Flow

1. Go to the **Actions** tab in your repository:  https://github.com/
<your-username>/<repo-name>/actions

2. Click on the **“Auto Follow Back”** workflow.
3. Click **“Run workflow”** (top right)
4. Choose the **main branch** → click **Run workflow**.

💥 GitHub will spin up a container and execute your Python script.

---

## ⏱️ STEP 6 — Automated Schedule

The workflow runs automatically based on the cron schedule in:
.github/workflows/auto_follow.yml


- Example: `"*/1 * * * *"` → every 1 minute
- You can change it to run hourly or daily if preferred.

---

## ✅ Summary

- Automatically follows new followers
- Unfollows users who unfollow you
- Can be scheduled via GitHub Actions
- Fully secure — token only has minimal required scopes


## What You Want (Follow Anyone You Like)

If you want to follow a user even if they don’t follow you, we need to change the logic:

Keep a list of “people I want to follow” in the script (hardcoded, in a file, or via a GitHub secret).

During each run, the script will:

Follow all new followers (mutual follow logic)

Follow people in your “favorites” list, even if they don’t follow you

This is separate from cron. Cron just determines how often the script checks GitHub and executes the follow/unfollow logic.

✅ How It Would Look in Code (Conceptually)
- existing mutual-follow logic
```to_follow = followers - following```

- additional: people you want to follow no matter what
```
favorite_users = ["user1", "user2", "user3"]
to_follow += [u for u in favorite_users if u not in following]
```

- then follow all in to_follow
```for user in to_follow:
    follow_user(token, user)```
