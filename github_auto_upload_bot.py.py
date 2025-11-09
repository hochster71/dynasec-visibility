import requests
import os
import base64

# ==== CONFIGURATION ====
GITHUB_TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"
REPO_OWNER = "hochster71"
REPO_NAME = "dynasec-visibility"
BRANCH = "Assets"
FILE_PATH = "banner.jpg"
UPLOAD_PATH = "assets/banner.jpg"
COMMIT_MESSAGE = "Auto-upload banner.jpg via Commander AI GitHub Bot"

# ==== SCRIPT ====
def upload_file():
    if not os.path.exists(FILE_PATH):
        print(f"❌ File not found: {FILE_PATH}")
        return

    with open(FILE_PATH, "rb") as f:
        content = f.read()

    b64_content = base64.b64encode(content).decode("utf-8")

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{UPLOAD_PATH}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Check if file exists to get SHA
    response = requests.get(url + f"?ref={BRANCH}", headers=headers)
    sha = response.json().get("sha") if response.status_code == 200 else None

    payload = {
        "message": COMMIT_MESSAGE,
        "content": b64_content,
        "branch": BRANCH
    }

    if sha:
        payload["sha"] = sha

    response = requests.put(url, headers=headers, json=payload)

    if response.status_code in [200, 201]:
        print("✅ Upload successful.")
    else:
        print(f"❌ Upload failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    upload_file()
