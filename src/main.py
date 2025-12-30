import sys
import os
from file_scanner import FileScanner
from url_scanner import URLScanner
from heuristics import HeuristicEngine  # <-- New Import

def start_netraxis():
    print("""
    --- Netraxis AI Security (v0.3 - Heuristics Added) ---
    """)

    url_engine = URLScanner()
    file_engine = FileScanner()
    heuristic_engine = HeuristicEngine() # <-- Initialize Detective

    print("Select Mode:")
    print("[1] URL Scan")
    print("[2] File Scan")
    print("[3] Update Threat Database")
    
    mode = input("\nYour Choice -> ")

    if mode == "1":
        url = input("Enter URL to scan: ")
        
        # 1. Check Database
        db_result = url_engine.scan(url)
        print(f"\n[Database Check] {db_result}")

        # 2. Check Heuristics (The Detective)
        score, reasons = heuristic_engine.check_url(url)
        if score > 0:
            print(f"[Heuristic Check] ⚠️ SUSPICIOUS: Risk Score {score}/10")
            print(f"   Reasons: {', '.join(reasons)}")
        else:
            print("[Heuristic Check] ✅ Clean structure.")
        
    elif mode == "2":
        path = input("Enter file path: ").strip().strip("'").strip('"')
        
        # 1. Check Database
        print(f"\n{file_engine.scan(path)}")
        
        # 2. Check Entropy
        try:
            with open(path, "rb") as f:
                data = f.read()
                entropy = heuristic_engine.calculate_entropy(data)
                print(f"[Heuristic Check] File Entropy: {entropy:.2f}")
                
                if entropy > 7.0:
                    print("   ⚠️ WARNING: High entropy detected. This file might be packed or encrypted malware.")
                elif entropy < 1.0:
                     print("   ℹ️ NOTE: Very low entropy. Likely a text file.")
                else:
                    print("   ✅ Normal entropy levels.")
        except Exception as e:
            print(f"   Could not analyze entropy: {e}")
        
    elif mode == "3":
        url_engine.update_db()
        
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    start_netraxis()