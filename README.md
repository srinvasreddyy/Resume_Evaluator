# 📄 Resume Evaluator

> An AI-powered resume screening tool that parses job descriptions and resumes, then evaluates and scores each candidate against the role — automatically.

---

## ✨ Features

- 📋 **JD Parsing** — Extracts required skills, qualifications, responsibilities, and timelines from any job description
- 📄 **Resume Parsing** — Reads PDF and DOCX resumes and extracts structured candidate data
- 🤖 **AI Evaluation** — Scores each candidate's suitability against the JD using an LLM
- 💪 **Strengths & Weaknesses** — Per-candidate breakdown of what fits and what doesn't
- ✅ **Final Verdict** — Hire / No-hire recommendation for every applicant
- 🔒 **Strict Schema Validation** — Pydantic models ensure clean, reliable output every time

---

## 🧠 How It Works

```
Job Description (text)
        │
        ▼
  ┌─────────────┐
  │  JD Parser  │  ──► Extracts: role, required skills, preferred skills,
  └─────────────┘       experience, education, responsibilities, location
        │
        │          Resumes (PDF / DOCX)
        │                 │
        ▼                 ▼
  ┌──────────────────────────┐
  │      Resume Parser       │  ──► Extracts: name, contact, skills,
  └──────────────────────────┘       experience, education, projects
                │
                ▼
  ┌──────────────────────────┐
  │    AI Evaluation Engine  │  ──► Scores suitability (0–10)
  └──────────────────────────┘       + strengths, weaknesses, verdict
                │
                ▼
        📊 Evaluation Report
```

---

## 🗂️ Project Structure

```
Resume_Evaluator/
├── main.py              # Core pipeline — parse JD → parse resumes → evaluate
├── resumes/             # Drop your resume files here (PDF or DOCX)
│   ├── candidate1.pdf
│   └── candidate2.docx
├── .env                 # API keys (never commit this)
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|---|---|
| [Groq](https://groq.com) | LLM inference (fast & free tier available) |
| [Pydantic](https://docs.pydantic.dev) | Structured output schema & validation |
| [PyPDF2](https://pypdf2.readthedocs.io) | PDF text extraction |
| [python-docx](https://python-docx.readthedocs.io) | DOCX text extraction |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Environment variable management |
| [uv](https://docs.astral.sh/uv/) | Fast Python package manager |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Resume_Evaluator.git
cd Resume_Evaluator
```

### 2. Set up the environment

```bash
uv venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

uv add groq pydantic python-docx PyPDF2 python-dotenv
```

### 3. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at [console.groq.com](https://console.groq.com).

### 4. Add resumes

Drop `.pdf` or `.docx` files into the `resumes/` folder.

### 5. Update the Job Description

Open `main.py` and replace the `job_description` variable with your target role's JD.

### 6. Run

```bash
python main.py
```

---

## 📦 Output Example

```json
{
  "applicant_name": "Siri Chandana Vishnubhotla",
  "suitability_score": 8.0,
  "strengths": [
    "Full-stack development with React.js and FastAPI",
    "Strong command of Python, Java, and C",
    "Hands-on ML model integration experience"
  ],
  "weaknesses": [
    "Limited exposure to large-scale distributed systems",
    "No experience with Perl"
  ],
  "final_verdict": "Strong candidate — recommend proceeding to interview stage."
}
```

---

## ⚠️ Groq Free Tier Notes

```python
model = "llama-3.3-70b-versatile"  # recommended
max_tokens = 2000   # resume parsing
max_tokens = 500    # evaluation
```

---

## 🔮 Roadmap

- [ ] Streamlit web UI
- [ ] Ranked candidate leaderboard
- [ ] Weighted per-criterion scoring
- [ ] CSV / PDF export
- [ ] Multi-JD support

---

## 📄 License

MIT License

---

<div align="center">Built with ❤️ using Groq + Pydantic</div>