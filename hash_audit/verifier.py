import hashlib

def hash_text(text: str, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    hasher.update(text.encode("utf-8"))
    return hasher.hexdigest()
