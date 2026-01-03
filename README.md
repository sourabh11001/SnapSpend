# SnapSpend — AI-Powered Expense Tracker

A **Full-Stack Financial Intelligence Platform** that uses **FastAPI (Python)** and **Gemini 2.5** to convert unstructured receipt images into clean, structured expense data — with both a production-ready backend and a lightweight browser-only demo version.

SnapSpend provides a mobile-friendly UI, privacy-first storage, and AI-driven receipt parsing.

---

> 📝 **Note (Important)**
>
> The live demo below is a **Client-Side “Lite” version** using **BYOK (Bring Your Own Key)** so it can run safely in the browser and be hosted on GitHub Pages.
>
> The **Full-Stack Production Version (FastAPI backend)** — with secure server-side AI processing — is included in this repository.

🌐 **Live Demo (Lite Version)**  
https://sourabh11001.github.io/SnapSpend/

---

## 🔍 Objective
To build a smart expense tracker that:

- Scans receipts using AI  
- Automatically extracts merchant, date, total, and category  
- Stores expenses locally (privacy-first)  
- Allows filtering, sorting, and PDF export  

while also offering a **single-file HTML version** that runs entirely in the browser.

---

## 🧰 Tools & Technologies Used
- **Python**, **FastAPI** — backend + AI processing  
- **JavaScript**, **Tailwind CSS** — responsive UI  
- **LocalStorage** — privacy-first storage  
- **jsPDF** — PDF export  
- **Gemini Vision API** — receipt extraction  
- **SQLite (optional)** — backend database support  

---

## 🏗 Architecture

> **Lite Version:** Browser (JS) ↔ Gemini API (Direct)  
> **Pro Version:** Browser ↔ FastAPI (Python) ↔ Gemini API (Proxy)  

The **Pro version** implements a **proxy pattern** to:

- secure API keys  
- sanitize inputs  
- centralize AI calls on the server  

This is how production systems are designed.

---

## 📊 Project Workflow
1️⃣ Upload / scan receipt  
2️⃣ AI extracts raw text  
3️⃣ Parsing identifies structured fields  
4️⃣ User confirms edits  
5️⃣ Data stored securely  
6️⃣ Expenses managed, filtered, exported  

---

## 🌐 Two Versions Included

### 1️⃣ Backend + Frontend (Developer / Pro Mode)
- FastAPI backend  
- Secure server-side AI  
- JSON APIs (ready for mobile apps)  
- Easy to extend with auth, dashboards, cloud DB, etc.

### 2️⃣ HTML-Only BYOK Version (GitHub Pages)
- Single standalone HTML file  
- User pastes API key  
- Runs fully in the browser  
- Works offline after first load  

---

## 📈 Key Features
- 📷 AI receipt scanning  
- 💾 Local private storage  
- 🔎 Search, sort, filter  
- 📄 PDF export  
- ➕ Manual add  
- 🗑 Delete transactions  

---

## 🚀 Run the Backend Version

### 1️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Start Server
```bash
uvicorn main:app --reload
```

Frontend connects automatically to `/scan`.  
If your server URL changes, update it in the HTML file.

---

## 🌐 Use the HTML-Only (BYOK) Version

Open:

```
index.html
```

Then:

1️⃣ Open Settings  
2️⃣ Paste Gemini API Key  
3️⃣ Start scanning 🎉  

➡️ Key stays in the **browser only** — never uploaded.

Or deploy via GitHub Pages:

```
https://sourabh11001.github.io/SnapSpend/
```

---

## 📂 Repository Structure
```
📁 SnapSpend/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── snapspend.html
├── requirements.txt
└── README.md
```

---

## 🛡 Git Safety
Do NOT commit:

```
.env
venv/
__pycache__/
*.db
```

---

## ❓ Why Two Versions?

**BYOK Lite Version**  
Fast, cheap to host, private.

**Full-Stack Pro Version**  
Secure, scalable, production-ready.

This demonstrates:

- full-stack architecture  
- secure API design  
- AI integration  
- clean UI development  

---

## 💡 Future Improvements
- Authentication  
- Cloud database sync  
- Analytics dashboard  
- Budget alerts  
- Monthly reports  

---

## 🙌 Contribution
PRs and suggestions welcome.

---

## 📜 License
Open-source — learn, modify, build.

---

⭐ **If you found this helpful, please star the repo!**  
📂 **GitHub Repository:**  
https://github.com/sourabh11001/SnapSpend
