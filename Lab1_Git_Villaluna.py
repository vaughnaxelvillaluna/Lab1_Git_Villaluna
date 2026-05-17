# Git and GitHub Laboratory Activity – Complete Files

Based on your uploaded PDF fileciteturn0file0, these are the files you need for your GitHub upload.

---

# 1. main.py

Save this as `main.py`

```python
print("Lab 1: Version Control")
print("Author: Vaughn Axel Villaluna")
print("Student ID: TUPM-25-0850")
print("Section: BSME 1-BM")
print("Login Feature Enabled")
```

---

# 2. .gitignore

Save this as `.gitignore`

```gitignore
.venv/
__pycache__/
*.pyc
```

---

# 3. README.md

Save this as `README.md`

```md
# Git and GitHub Laboratory Activity

## Student Information
- Name: Vaughn Axel Villaluna
- Student ID: TUPM-25-0850
- Section: BSME 1-BM

## Description
This repository contains the required files for the Git and GitHub laboratory activity.

## Files Included
- main.py
- .gitignore
- README.md

## Features
- Demonstrates Git version control workflow
- Includes basic Python program
- Uses GitHub remote repository synchronization
```

---

# 4. Commands to Run

Open VS Code terminal and run these commands one by one:

```bash
python main.py
```

Expected output:

```text
Lab 1: Version Control
Author: Vaughn Axel Villaluna
Student ID: TUPM-25-0850
Section: BSME 1-BM
Login Feature Enabled
```

---

# 5. Git Commands

Initialize repository:

```bash
git init
```

Add files:

```bash
git add .
```

Commit files:

```bash
git commit -m "Initial commit"
```

Connect to GitHub:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_LINK
```

Push to GitHub:

```bash
git push -u origin main
```

---

# 6. Files You Need to Upload to GitHub

Upload these files:

- main.py
- .gitignore
- README.md

Optional:
- screenshots of terminal output
- screenshots of GitHub repository

---

# 7. Recommended Repository Name

```text
Lab1_Git_Villaluna
```

---

# 8. Suggested Folder Structure

```text
Lab1_Git_Villaluna/
│
├── main.py
├── .gitignore
└── README.md
```

