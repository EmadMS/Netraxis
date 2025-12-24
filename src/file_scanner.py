import hashlib

class FileScanner:
    def __init__(self):
        # MVP: Known bad hashes (MD5).
        # This hash is for the EICAR test file (a harmless industry-standard virus test file).
        self.malware_db = {
            "44d88612fea8a8f36de82e1278abb02f": "EICAR Test Virus"
        }

    def scan(self, filepath):
        print(f"[*] Scanning File: {filepath}...")
        try:
            # Read file in binary mode
            with open(filepath, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            
            if file_hash in self.malware_db:
                return f"⚠️ DANGER: Detected {self.malware_db[file_hash]}"
            return "✅ SAFE: File appears clean."
            
        except FileNotFoundError:
            return "❌ ERROR: File not found. Check the path."