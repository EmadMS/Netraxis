import requests
import os

class URLScanner:
    def __init__(self):
        self.threat_db_path = "data/malicious_urls.txt"
        self.database = set()
        self.load_database()

    def update_db(self):
        """Downloads the latest malware URLs from URLhaus."""
        print("[*] Updating Threat Database from URLhaus...")
        url = "https://urlhaus.abuse.ch/downloads/csv_recent/"
        try:
            response = requests.get(url)
            # Create data folder if it doesn't exist
            os.makedirs("data", exist_ok=True)
            
            # Save raw data
            with open(self.threat_db_path, "w") as f:
                f.write(response.text)
            print("[+] Database updated successfully.")
            self.load_database()
        except Exception as e:
            print(f"[-] Update failed: {e}")

    def load_database(self):
        """Loads the text file into memory for fast searching."""
        if not os.path.exists(self.threat_db_path):
            print("[!] No local database found. Run update first.")
            return

        print("[*] Loading database into memory...")
        with open(self.threat_db_path, "r") as f:
            for line in f:
                if line.startswith("#"): continue
                # URLhaus CSV format is: id,dateadded,url,url_status,...
                parts = line.split(",")
                if len(parts) > 2:
                    malicious_url = parts[2].strip('"')
                    self.database.add(malicious_url)
        print(f"[+] Loaded {len(self.database)} malicious URLs.")

    def scan(self, url):
        if url in self.database:
            return "⚠️ CRITICAL: URL found in global malware database!"
        return "✅ SAFE: Not found in current blacklist."