import subprocess
import os

edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
]

browser_exe = None
for p in edge_paths:
    if os.path.exists(p):
        browser_exe = p
        break

print("Found browser:", browser_exe)

if browser_exe:
    # Run in headless mode with console logging
    cmd = [
        browser_exe,
        "--headless=new",
        "--dump-dom",
        "--enable-logging=stderr",
        "--v=1",
        r"c:\Users\Enrico\Desktop\Giada\the_irish_year.html"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    print("STDOUT length:", len(res.stdout))
    print("STDERR:")
    print(res.stderr[:2000])
