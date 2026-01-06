import time

# token -> metadata
token_store = {}

def create_token(token: str, ttl: int, max_uses: int):
    token_store[token] = {
        "expiry": time.time() + ttl,
        "uses_left": max_uses
    }

def get_token(token: str):
    return token_store.get(token)

def delete_token(token: str):
    if token in token_store:
        del token_store[token]
