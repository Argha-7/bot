# Instagram Comment Bot 🤖

> Har 10 minute mein automatically Instagram pe comment karta hai — computer off hone pe bhi!
> GitHub Actions use karta hai (bilkul FREE!)

---

## ⚙️ Setup — Step by Step

### Step 1: GitHub Account Banao
- [github.com](https://github.com) pe sign up karo (free hai)

### Step 2: Naya Repository Banao
- GitHub pe `+` button click karo → `New repository`
- Name: `instagram-bot` (koi bhi naam)
- **Private** select karo (password safe rahega)
- `Create repository` click karo

### Step 3: Yeh Files Upload Karo
Repository mein **"uploading an existing file"** click karo aur yeh teen files upload karo:
- `instagram_bot.py`
- `requirements.txt`
- `.github/workflows/comment_bot.yml`

### Step 4: GitHub Secrets Mein Credentials Add Karo
Repository → `Settings` → `Secrets and variables` → `Actions` → `New repository secret`

| Secret Name | Value |
|-------------|-------|
| `INSTAGRAM_USERNAME` | Aapka Instagram username |
| `INSTAGRAM_PASSWORD` | Aapka Instagram password |
| `POST_URL` | Jis post pe comment karna hai (full URL) |
| `COMMENT_TEXT` | Jo comment post karna hai (optional, default text hai) |

### Step 5: Actions Enable Karo
- Repository → `Actions` tab → `I understand my workflows, go ahead and enable them`

---

## ✅ Ho Gaya!
Ab GitHub Actions **khud-ba-khud har 10 minute mein** bot run karega.

Aap `Actions` tab mein dekh sakte ho ki bot chal raha hai ya nahi.

---

## ⚠️ Important Notes
- **Instagram rate limit** se bachne ke liye 10 minute ka interval rakha hai
- Agar account **2FA** enabled hai toh pehle disable karo
- Bot detection se bachne ke liye ek hi post pe baar baar comment karne se account ban ho sakta hai — dhyan rakhein
