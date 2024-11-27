from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os
from google.oauth2 import id_token
from google.auth.transport.requests import Request as GoogleRequest
from urllib.parse import urlencode

load_dotenv()

app = FastAPI()

# Load environment variables
GOOGLE_CLIENT_ID = "496139202565-e5m4te5nre9mhq8nllev4t84pglh7k0j.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_REDIRECT_URI = "http://127.0.0.1:8000/auth/callback"

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_SCOPE = "openid email profile"

@app.get("/login")
async def login():
    # Generate Google OAuth 2.0 URL
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "response_type": "code",
        "scope": GOOGLE_SCOPE,
        "access_type": "offline",
        "prompt": "consent",
    }
    url = f"{GOOGLE_AUTH_URL}?{urlencode(params)}"
    return RedirectResponse(url)

@app.get("/auth/callback")
async def auth_callback(code: str):
    import requests

    # Exchange the authorization code for tokens
    token_data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    token_response = requests.post(GOOGLE_TOKEN_URL, data=token_data)
    token_response_data = token_response.json()
    
    print(token_response_data)

    if "error" in token_response_data:
        raise HTTPException(status_code=400, detail=token_response_data["error_description"])

    id_token_jwt = token_response_data["id_token"]

    # Verify and decode the ID token
    try:
        id_info = id_token.verify_oauth2_token(id_token_jwt, GoogleRequest(), GOOGLE_CLIENT_ID)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid ID token")

    # Extract user information from the ID token
    user_email = id_info.get("email")
    user_name = id_info.get("name")

    return {"message": f"Welcome, {user_name}!", "email": user_email}

