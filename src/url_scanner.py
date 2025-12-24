class URLScanner:
    def __init__(self):
        # MVP: Simple blocklist.
        # Future: Replace with AI phishing detection model.
        self.unsafe_domains = ["malware-test.com", "fake-login.net"]

    def scan(self, url):
        print(f"[*] Scanning URL: {url}...")
        for domain in self.unsafe_domains:
            if domain in url:
                return "⚠️ UNSAFE: Known malicious domain detected."
        return "✅ SAFE: No threats found in database."