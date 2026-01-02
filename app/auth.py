from fastapi import Depends, HTTPException, Header
import os

API_KEYS = {
    os.getenv("COMPANY_API_KEY"): "company"
}

def authenticate(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return API_KEYS[x_api_key]
