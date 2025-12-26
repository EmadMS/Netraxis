import sys
from file_scanner import FileScanner
from url_scanner import URLScanner

def start_netraxis():
    print("""
    ███╗   ██╗███████╗████████╗██████╗  █████╗ ██╗  ██╗██╗███████╗
    ████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚██╗██╔╝██║██╔════╝
    ██╔██╗ ██║█████╗     ██║   ██████╔╝███████║ ╚███╔╝ ██║███████╗
    ██║╚██╗██║██╔══╝     ██║   ██╔══██╗██╔══██║ ██╔██╗ ██║╚════██║
    ██║ ╚████║███████╗   ██║   ██║  ██║██║  ██║██╔╝ ██╗██║███████║
    ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
    --- AI-Powered Security Engine (v0.2) ---
    """)

    # Initialize engines
    url_engine = URLScanner()
    file_engine = FileScanner()

    # Main Menu
    print("Select Mode:")
    print("[1] URL Scan")
    print("[2] File Scan")
    print("[3] Update Threat Database (Requires Internet)")
    
    mode = input("\nYour Choice -> ")

    if mode == "1":
        url = input("Enter URL to scan: ")
        print(url_engine.scan(url))
        
    elif mode == "2":
        # strips quotes in case user drags/drops file on Mac
        path = input("Enter file path: ").strip().strip("'").strip('"')
        print(file_engine.scan(path))
        
    elif mode == "3":
        url_engine.update_db()
        
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    start_netraxis()