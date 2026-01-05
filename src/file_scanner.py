import hashlib
import requests
import os
import time
try:
    from config import VT_API_KEY, DEMO_MODE
except ImportError:
    VT_API_KEY = ""
    DEMO_MODE = True

class FileScanner:
    def __init__(self):
        self.api_url = "https://www.virustotal.com/api/v3/files/"
        self.headers = {"x-apikey": VT_API_KEY}

    def get_file_hash(self, filepath):
        """Generates SHA-256 hash (The industry standard fingerprint)."""
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            # Read file in chunks to handle large files efficiently
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def check_virustotal(self, file_hash):
        """Queries VirusTotal API to see if other AVs detected this."""
        if DEMO_MODE or not VT_API_KEY or VT_API_KEY == "YOUR_KEY_HERE":
            return "⚠️ DEMO MODE: Cloud scan skipped (No API Key set)."

        print(f"[*] Querying VirusTotal Cloud for: {file_hash[:15]}...")
        
        try:
            response = requests.get(self.api_url + file_hash, headers=self.headers)
            
            if response.status_code == 200:
                stats = response.json().get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
                malicious = stats.get("malicious", 0)
                if malicious > 0:
                    return f"❌ DANGER: {malicious} security vendors flagged this file as MALWARE!"
                else:
                    return "✅ CLEAN: VirusTotal found no threats."
            elif response.status_code == 404:
                return "❓ UNKNOWN: File hash not found in VirusTotal database."
            elif response.status_code == 401:
                return "❌ ERROR: Invalid API Key."
            else:
                return f"⚠️ API Error: {response.status_code}"
                
        except Exception as e:
            return f"❌ Connection Error: {e}"

    def scan(self, filepath):
        if not os.path.exists(filepath):
            return "❌ ERROR: File not found."

        try:
            # 1. Calculate Hash locally
            file_hash = self.get_file_hash(filepath)
            print(f"[*] File Fingerprint (SHA256): {file_hash}")

            # 2. Check Cloud
            result = self.check_virustotal(file_hash)
            return result
            
        except Exception as e:
            return f"❌ Error scanning file: {e}"