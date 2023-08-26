import json
import random
import string
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode

app = FastAPI()

client_id = "2e6df8fc1e2743eaa40398b08244759d"

def getRandomStateString():
    return random.choices(string.ascii_lowercase, k=16)

@app.get('/', response_class=RedirectResponse)
async def root():
    redirect_uri = "http://127.0.0.1:8000/auth_callback"
    state = ''.join(getRandomStateString())
    scope = 'user-read-private user-read-email'

    return RedirectResponse('https://accounts.spotify.com/authorize?' + urlencode({
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "state": state,
        "scope": scope
    }))

@app.get('/auth_callback')
async def auth_callback():
    return {"status": "successful"}