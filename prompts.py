def debug_prompt(code):
    return f"""
Analyze this code:
{code}

Give:
1. Errors
2. Reasons
3. Fix
4. Corrected Code
"""

def explain_prompt(code):
    return f"Explain this code step by step:\n{code}"

def optimize_prompt(code):
    return f"""
Optimize this code:
{code}

Give improved version + explanation
"""

def security_prompt(code):
    return f"""
Check this code for security issues:
{code}

Give vulnerabilities + fixes
"""

def test_prompt(code):
    return f"Generate pytest test cases:\n{code}"

def convert_prompt(code, lang):
    return f"Convert this code to {lang}:\n{code}"