# 🛡️ Autonomous Lab TA (Prototype v1)

### *The Security-First AI Tutor for Computer Science Labs*

![Status](https://img.shields.io/badge/Status-Prototype-orange) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)

## 💡 The Problem
In large Computer Science labs, one professor cannot help 60+ students simultaneously. Students often get stuck on simple syntax errors or dangerous security practices, wasting hours waiting for help.

## 🚀 The Solution
**Autonomous Lab TA** is an intelligent coding assistant that acts as a "Strict Tutor." Unlike ChatGPT, it **does not** give the answer immediately. Instead, it guides the student with hints to encourage critical thinking.

### 🌟 Key Features (v1 Prototype)
* **👨‍🏫 Strict Mode:** Hides the answer behind a "3-Hint System" to force students to think.
* **🛡️ Red Team Security Checks:** Instantly flags dangerous functions (like `gets()`, `system()`) that lead to hacks.
* **⚡ Instant Syntax Fixes:** Catches missing semicolons and headers instantly.

---

## 🛠️ How to Run This Project
Follow these steps to run the prototype on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/Easwar-dev/Hackathon.git
cd Hackathon/prototype/
```
### 2. Install Requirements
```bash
pip install -r requirements.txt
```
### 3. Run the App
```bash
streamlit run TA.py
```
The app should open automatically in your browser at http://localhost:8501