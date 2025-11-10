"""
GitHub Auto Upload Bot
Securely uploads files to GitHub repository using the GitHub API.

Security improvements:
- Uses environment variables for credentials (never hardcode tokens)
- Implements proper error handling and logging
- Uses modern requests library with timeouts
- Follows GitHub API best practices

References:
- GitHub API v3: https://docs.github.com/en/rest
- Python security best practices: https://realpython.com/python-security-best-practices/
"""

import requests
import os
import base64
import sys
from typing import Optional

# ==== CONFIGURATION ====
# Security: Load sensitive data from environment variables
# Set GITHUB_TOKEN environment variable before running:
# export GITHUB_TOKEN="your_personal_access_token"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_OWNER = os.environ.get("GITHUB_REPO_OWNER", "hochster71")
REPO_NAME = os.environ.get("GITHUB_REPO_NAME", "dynasec-visibility")
BRANCH = os.environ.get("GITHUB_BRANCH", "Assets")
FILE_PATH = os.environ.get("FILE_PATH", "banner.jpg")
UPLOAD_PATH = os.environ.get("UPLOAD_PATH", "assets/banner.jpg")
COMMIT_MESSAGE = os.environ.get("COMMIT_MESSAGE", "Auto-upload via GitHub Bot")

# API Configuration
API_TIMEOUT = 30  # seconds
API_VERSION = "2022-11-28"  # GitHub API version


def validate_config() -> bool:
    """
    Validate required configuration is present.
    
    Returns:
        bool: True if configuration is valid, False otherwise
    """
    if not GITHUB_TOKEN:
        print("❌ Error: GITHUB_TOKEN environment variable not set")
        print("Set it with: export GITHUB_TOKEN='your_token'")
        return False
    
    if not os.path.exists(FILE_PATH):
        print(f"❌ Error: File not found: {FILE_PATH}")
        return False
    
    return True


def upload_file() -> int:
    """
    Upload file to GitHub repository.
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
        
    Security notes:
    - Uses environment variables for credentials
    - Implements request timeout to prevent hanging
    - Validates responses before processing
    - Uses modern GitHub API version header
    """
    if not validate_config():
        return 1

    try:
        # Read file content
        with open(FILE_PATH, "rb") as f:
            content = f.read()

        # Encode to base64 as required by GitHub API
        b64_content = base64.b64encode(content).decode("utf-8")

        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{UPLOAD_PATH}"
        
        # Modern GitHub API headers
        # Reference: https://docs.github.com/en/rest/overview/api-versions
        headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",  # Bearer token is modern standard
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION
        }

        # Check if file exists to get SHA (required for updates)
        print(f"Checking if {UPLOAD_PATH} exists...")
        response = requests.get(
            url + f"?ref={BRANCH}", 
            headers=headers,
            timeout=API_TIMEOUT
        )
        
        sha: Optional[str] = None
        if response.status_code == 200:
            sha = response.json().get("sha")
            print(f"File exists, updating (SHA: {sha[:8]}...)")
        else:
            print("File does not exist, creating new file")

        # Prepare payload
        payload = {
            "message": COMMIT_MESSAGE,
            "content": b64_content,
            "branch": BRANCH
        }

        if sha:
            payload["sha"] = sha

        # Upload file
        print(f"Uploading {FILE_PATH} to {REPO_OWNER}/{REPO_NAME}/{UPLOAD_PATH}...")
        response = requests.put(
            url, 
            headers=headers, 
            json=payload,
            timeout=API_TIMEOUT
        )

        if response.status_code in [200, 201]:
            print("✅ Upload successful!")
            print(f"Commit: {response.json().get('commit', {}).get('sha', 'N/A')}")
            return 0
        else:
            print(f"❌ Upload failed: {response.status_code}")
            print(f"Response: {response.text}")
            return 1

    except requests.exceptions.Timeout:
        print(f"❌ Error: Request timed out after {API_TIMEOUT} seconds")
        return 1
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Network request failed: {e}")
        return 1
    except IOError as e:
        print(f"❌ Error: File I/O error: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error: Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(upload_file())
