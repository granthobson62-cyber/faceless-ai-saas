import os
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError

# -----------------------------
# Wasabi S3 config
# -----------------------------
WASABI_ACCESS_KEY = os.getenv("WASABI_ACCESS_KEY")
WASABI_SECRET_KEY = os.getenv("WASABI_SECRET_KEY")
WASABI_BUCKET = os.getenv("WASABI_BUCKET")
WASABI_REGION = os.getenv("WASABI_REGION", "us-east-1")
WASABI_ENDPOINT = os.getenv("WASABI_ENDPOINT")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=WASABI_ACCESS_KEY,
    aws_secret_access_key=WASABI_SECRET_KEY,
    region_name=WASABI_REGION,
    endpoint_url=WASABI_ENDPOINT
)

# -----------------------------
# Placeholder video generation
# -----------------------------
def generate_video(language="en"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"videos/video_{language}_{timestamp}.mp4"
    os.makedirs("videos", exist_ok=True)
    with open(filename, "wb") as f:
        f.write(b"Placeholder video for Wasabi storage")
    print(f"[INFO] Video generated locally at {filename}")
    return filename

# -----------------------------
# Upload to Wasabi
# -----------------------------
def upload_to_wasabi(file_path):
    try:
        key = os.path.basename(file_path)
        s3_client.upload_file(file_path, WASABI_BUCKET, key)
        url = f"https://{WASABI_BUCKET}.{WASABI_REGION}.wasabisys.com/{key}"
        print(f"[INFO] Uploaded {file_path} to {url}")
        return url
    except NoCredentialsError as e:
        print(f"[ERROR] Wasabi credentials not found: {e}")
        return None

# -----------------------------
# Main Orchestrator
# -----------------------------
def run_orchestrator(languages=None):
    if languages is None:
        languages = ["en", "es"]

    uploaded_urls = []

    print("[INFO] Starting AI Orchestrator...")

    for lang in languages:
        print(f"[INFO] Generating video for language: {lang}")
        video_file = generate_video(lang)
        url = upload_to_wasabi(video_file)
        if url:
            uploaded_urls.append(url)

    print(f"[INFO] Orchestrator finished.")
    return uploaded_urls

