import math
import re

class HeuristicEngine:
    def __init__(self):
        self.suspicious_tlds = [".xyz", ".top", ".club", ".surf"]

    def check_url(self, url):
        """Analyzes URL structure for phishing signs."""
        risk_score = 0
        reasons = []

        # Check 1: Is it an IP address? (e.g. http://192.168.1.5)
        ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
        if re.search(ip_pattern, url):
            risk_score += 5
            reasons.append("Host is an IP address")

        # Check 2: Is it suspiciously long?
        if len(url) > 75:
            risk_score += 3
            reasons.append("URL is suspiciously long")

        # Check 3: Does it use a 'shady' domain ending?
        for tld in self.suspicious_tlds:
            if url.endswith(tld):
                risk_score += 2
                reasons.append(f"Suspicious TLD ({tld})")

        # Check 4: Too many special chars?
        if url.count("-") > 3 or url.count("@") > 0:
            risk_score += 2
            reasons.append("High special character count")

        return risk_score, reasons

    def calculate_entropy(self, data):
        """Calculates Shannon Entropy to find encrypted/packed code."""
        if not data:
            return 0
        
        entropy = 0
        for x in range(256):
            p_x = float(data.count(bytes([x]))) / len(data)
            if p_x > 0:
                entropy += - p_x * math.log(p_x, 2)
        
        return entropy