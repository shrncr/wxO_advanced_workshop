
# Orchestrate Workshop

Welcome to the **Orchestrate Advanced Workshop**!  
This repository is designed to teach you how to build and run projects in **watsonx Orchestrate** through a series of hands-on labs.  

Each lab is **self-contained**, with guides, starter files, and “final” solutions if you get stuck.  


## 📂 Repository Structure

This project organizes its files as follows:

```text
.
├── README.md (this file)
├── pyproject.toml (contains all dependencies for all labs)
├── .env (Environment file for Orchestrate server)
├── lab-guide-folder (example lab structure)
│   ├── lab-guide.md
│   ├── starter-file.py
│   └── Final_code
│       ├── Final code for lab

```

- **lab-guide-folder** → where you’ll build the lab exercises.  
- **Final_code folder** → completed code, provided only if you need to catch up.  
- **lab-guide.md** → step-by-step instructions for the lab.  



## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/<your-org>/orchestrate-workshop.git
cd orchestrate-workshop
```
### 2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate    # Linux/Mac
# or
.\.venv\Scripts\activate     # Windows
```
### 3. Install dependencies

We’re using uv with pyproject.toml to manage dependencies.

```bash
pip install uv
uv sync
```

This will install all dependencies for every lab into your virtual environment.

### 🔑 Environment Configuration

In the project root there’s an .env file.
Update it with your Orchestrate server credentials before running labs:

ORCHESTRATE_API_KEY=your_api_key_here
ORCHESTRATE_SERVER_URL=https://your.server.url

### 🚀 Running Labs

Navigate to the desired lab’s starter folder.

Follow the lab guide.




If you get stuck or run out of time, the final/ folder contains the completed solution.

### 🙌 Recommendations

Try to work through the labs yourself rather than jumping to the final/ folders. You’ll learn more this way.

The final/ code is just there to help you catch up if needed.
