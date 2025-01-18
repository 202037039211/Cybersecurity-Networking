# SQL Injection Scanner

This tool scans web forms for potential SQL Injection vulnerabilities by submitting various payloads and analyzing responses for common SQL error messages.

## Features:
- Extracts and tests all forms on a given URL.
- Detects common SQL error signatures in server responses.
- Supports both GET and POST methods.

## Requirements:
- Python 3.x
- `requests` and `beautifulsoup4` libraries

## Installation:
1. Clone the repository or copy the code.
2. Install dependencies:
```bash
pip install requests beautifulsoup4
```

---

### **Testing Instructions:**
1. **Set Up Environment:**
   - Replace the `target_url` variable with the URL you want to test.
   - Ensure you have permission to test the target website.

2. **Install Dependencies:**
```bash
pip install requests beautifulsoup4
```

3. **Run the Script:**
```bash
python main.py
```

4. **Interpret Results:**
   - The script will report any detected SQL injection vulnerabilities and the payload used.
   - If no vulnerabilities are found, it will indicate that as well.
