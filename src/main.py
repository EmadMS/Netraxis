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
    --- AI-Powered Security Engine (v0.1) ---
    """)

    url_engine = URLScanner()
    file_engine = FileScanner()

    mode = input("Select Mode -> [1] URL Scan  [2] File Scan: ")

    if mode == "1":
        url = input("Enter URL to scan: ")
        print(url_engine.scan(url))
    elif mode == "2":
        path = input("Enter file path (drag and drop file here): ").strip().strip("'")
        print(file_engine.scan(path))
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    start_netraxis()