import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

EMAIL = "user1@organisation-a.com" # adjust if necessary
PASSWORD = "Test" # adjust if necessary
AUTHORIZED_BUCKET_NAME = "example-knowledge-organisation-a" # adjust if necessary
UNAUTHORIZED_BUCKET_NAME = "example-knowledge-organisation-b" # adjust if necessary

URL = os.getenv("SUPABASE_PUBLIC_URL")
KEY = os.getenv("ANON_KEY")

client = create_client(URL,KEY)

# Authentification: User Login
user = client.auth.sign_in_with_password({
            "email": EMAIL,
            "password": PASSWORD
        })
token = user.session.access_token
client.auth.set_session(token, "")

# Accessing restricted buckets
def access_bucket(bucket_name):
    try:
        bucket = client.storage.get_bucket(bucket_name)
        print(bucket)
    except Exception as e:
        print(e.args)

access_bucket(AUTHORIZED_BUCKET_NAME)
access_bucket(UNAUTHORIZED_BUCKET_NAME)