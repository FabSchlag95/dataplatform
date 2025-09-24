import os
import requests
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

EMAIL = "user1@organisation-a.com" # adjust if necessary
PASSWORD = "Test" # adjust if necessary
AUTHORIZED_BUCKET_NAME = "example-knowledge-organisation-a" # adjust if necessary
UNAUTHORIZED_BUCKET_NAME = "example-knowledge-organisation-b" # adjust if necessary

SUPABASE_URL = os.getenv("SUPABASE_PUBLIC_URL")
ANON_KEY = os.getenv("ANON_KEY")

supabase: Client = create_client(SUPABASE_URL, ANON_KEY)

# Authentification: User Login
auth_res = supabase.auth.sign_in_with_password({
    "email": EMAIL,
    "password": PASSWORD
})
print(f"Logged in user: {auth_res.user.id}")
access_token = auth_res.session.access_token

# Accessing restricted buckets
STORAGE_URL = f"{SUPABASE_URL}/storage/v1/object/list/"
headers = {
    "Authorization": f"Bearer {access_token}"
}

def access_bucket(bucket_name):
    url = f"{SUPABASE_URL}/{bucket_name}"
    print(f"Request URL: {url}")
    res = requests.get(url, headers=headers)
    print(f"Status: {res.status_code}")
    print(res.json())

access_bucket(AUTHORIZED_BUCKET_NAME)
access_bucket(UNAUTHORIZED_BUCKET_NAME)