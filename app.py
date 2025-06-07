from flask import Flask, request, send_file
import os
import zipfile
import socket

app = Flask(_name_)
BASE_DIR = ".vcs"
COMMITS_DIR = os.path.join(BASE_DIR, "commits")
TMP_ZIP = "vcs.zip"  # Consistent zip name

@app.route('/pull', methods=['GET'])
def pull():
    try:
        with zipfile.ZipFile(TMP_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for foldername, _, filenames in os.walk(COMMITS_DIR):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.join(".vcs", os.path.relpath(filepath, BASE_DIR))
                    zipf.write(filepath, arcname)
        return send_file(TMP_ZIP, as_attachment=True, download_name=TMP_ZIP)
    finally:
        if os.path.exists(TMP_ZIP):
            os.remove(TMP_ZIP)

@app.route('/push', methods=['POST'])
def push():
    try:
        if 'file' not in request.files:
            return "No file", 400
        request.files['file'].save(TMP_ZIP)
        with zipfile.ZipFile(TMP_ZIP, 'r') as zipf:
            zipf.extractall()
        return "Push success", 200
    finally:
        if os.path.exists(TMP_ZIP):
            os.remove(TMP_ZIP)

@app.route('/clone', methods=['GET'])
def clone():
    try:
        with zipfile.ZipFile(TMP_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for foldername, _, filenames in os.walk(COMMITS_DIR):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.join(".vcs", os.path.relpath(filepath, BASE_DIR))
                    zipf.write(filepath, arcname)

            config_path = os.path.join(BASE_DIR, "config.txt")
            if os.path.exists(config_path):
                zipf.write(config_path, os.path.join(".vcs", "config.txt"))

        return send_file(TMP_ZIP, as_attachment=True, download_name=TMP_ZIP)
    finally:
        if os.path.exists(TMP_ZIP):
            os.remove(TMP_ZIP)

def get_ip_address():
    try:
        ips = []
        for interface in socket.getaddrinfo(socket.gethostname(), None):
            ip = interface[4][0]
            if isinstance(ip, str) and '.' in ip and not ip.startswith('127.'):
                ips.append(ip)
        if not ips:
            for interface in socket.getaddrinfo(socket.gethostname(), None):
                ip = interface[4][0]
                if isinstance(ip, str) and ':' in ip and not ip.startswith('fe80:'):
                    ips.append(ip)
        return ips if ips else ["127.0.0.1"]
    except:
        return ["127.0.0.1"]

if _name_ == '_main_':
    usable_ips = [ip for ip in get_ip_address() if not ip.startswith('127.')]
    if not usable_ips:
        usable_ips = ["127.0.0.1"]

    print("Repository server starting...")
    os.makedirs(BASE_DIR, exist_ok=True)
    
    server_address = f"{usable_ips[0]}:9000"
    with open(os.path.join(BASE_DIR, "server.info"), 'w') as f:
        f.write(f"{server_address}\n")

    # Print the clone command
    print("\nTo clone this repository, run:")
    print(f"./vcs clone {server_address} <target-directory>")
    print("Replace <target-directory> with where you want the repository or . if you want in current directory\n")

    app.run(host='0.0.0.0', port=9000, debug=True, threaded=True)