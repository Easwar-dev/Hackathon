import streamlit as st


# CONFIG & STATE
st.set_page_config(page_title="Lab TA", page_icon="👨‍🏫", layout="wide")

# Initialize "Memory" to track hints AND analysis results
if 'hint_count' not in st.session_state:
    st.session_state.hint_count = 0
if 'last_code' not in st.session_state:
    st.session_state.last_code = ""
# NEW: Variable to store the report so it doesn't disappear
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None



# THE LOGIC (Simulated)

def analyze_strict(code):
    # 1. SYNTAX CHECK
    syntax_errors = []
    if "main" not in code:
        syntax_errors.append({"line": "?", "error": "No 'main' function", "fix": "Add 'void main()'"})
    if "printf" in code and ";" not in code.split("printf")[1]:
        syntax_errors.append({"line": "detected", "error": "Missing Semicolon ';'", "fix": "Add ';' at end of line"})

    # 2. LOGIC ERRORS
    logic_error = None
    if "while" in code and "i++" not in code and "i--" not in code:
        logic_error = {
            "name": "Infinite Loop Detected",
            "hints": [
                "Check your while loop condition.",
                "The variable 'i' is never changing.",
                "You need to increment 'i' (i++) inside the loop."
            ],
            "answer": "Add 'i++;' inside the braces {}."
        }

    # 3. SECURITY FLAWS
    security_flaws = []
    if "gets(" in code:
        security_flaws.append({"bad": "gets()", "better": "fgets()", "why": "Buffer Overflow Risk"})
    if "system(" in code:
        security_flaws.append(
            {"bad": "system()", "better": "Avoid shell commands", "why": "Hacker can inject commands"})

    return syntax_errors, logic_error, security_flaws



# 🎨 THE UI
st.title("👨‍🏫 Autonomous Lab TA: Student Mode")
st.markdown("### 📝 Lab Workspace")

code_input = st.text_area("Write your code here:", height=200, value="""#include <stdio.h>
void main() {
    int i=0; 
    while(i<10) {
        printf("Hello");
    }
    char buf[10];
    gets(buf);
}""")

# Smart Reset: If code changes, clear the memory
if code_input != st.session_state.last_code:
    st.session_state.hint_count = 0
    st.session_state.analysis_result = None  # Clear old report
    st.session_state.last_code = code_input

# --- THE MAIN TRIGGER ---
if st.button("🚀 Check My Code"):
    # Run analysis and SAVE result to session_state
    syntax, logic, security = analyze_strict(code_input)
    st.session_state.analysis_result = {
        "syntax": syntax,
        "logic": logic,
        "security": security
    }

# --- DISPLAY RESULTS (Outside the button block) ---
# We check if 'analysis_result' exists in memory. If yes, we show it.
if st.session_state.analysis_result:
    result = st.session_state.analysis_result
    st.divider()

    # 1. SYNTAX
    if result["syntax"]:
        st.subheader("❌ Syntax Errors")
        for item in result["syntax"]:
            st.error(f"**Error:** {item['error']} → **Fix:** `{item['fix']}`")
    else:
        st.success("✅ Syntax is correct.")

    # 2. LOGIC (The Hint Game)
    logic = result["logic"]
    if logic:
        st.subheader("🧠 Logic Check")
        st.warning(f"⚠️ Issue: {logic['name']}")

        hits_used = st.session_state.hint_count

        if hits_used >= 1: st.info(f"💡 Hint 1: {logic['hints'][0]}")
        if hits_used >= 2: st.info(f"💡 Hint 2: {logic['hints'][1]}")
        if hits_used >= 3: st.info(f"💡 Hint 3: {logic['hints'][2]}")

        col1, col2 = st.columns([1, 4])

        # LOGIC FIX: Only show button if hints remain
        if hits_used < 3:
            # We add a unique 'key' to prevent Streamlit confusion
            if col1.button("Show Next Hint", key="hint_btn"):
                st.session_state.hint_count += 1
                st.rerun()
        else:
            st.error(f"🛑 Answer: {logic['answer']}")

    # 3. SECURITY
    if result["security"]:
        st.subheader("🛡️ Security Vulnerabilities")
        for item in result["security"]:
            st.markdown(f"""
            | 🔴 Vulnerable | 🟢 Secure Fix | ⚠️ Why? |
            |---|---|---|
            | `{item['bad']}` | `{item['better']}` | {item['why']} |
            """)