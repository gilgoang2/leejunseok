import http.server
import os
import shutil
import socketserver

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

SOURCES = {
    "1.jpg": r"C:\Users\USER\AppData\Local\Temp\claude\C--Users-USER-Desktop-------2-\871cb927-06ef-4263-b65f-865b177bd099\images\1.jpg",
    "2.png": r"C:\Users\USER\AppData\Local\Temp\claude\C--Users-USER-Desktop-------2-\871cb927-06ef-4263-b65f-865b177bd099\images\2.png",
    "3.webp": r"C:\Users\USER\AppData\Local\Temp\claude\C--Users-USER-Desktop-------2-\871cb927-06ef-4263-b65f-865b177bd099\images\3.webp",
}

for name, src in SOURCES.items():
    dst = os.path.join(IMAGES_DIR, name)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copyfile(src, dst)

os.chdir(BASE)
PORT = 5500
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
