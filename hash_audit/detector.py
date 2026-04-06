import re

HASH_PATTERNS = [
    {"name": "MD5", "regex": r"^[a-fA-F0-9]{32}$"},
    {"name": "SHA1", "regex": r"^[a-fA-F0-9]{40}$"},
    {"name": "SHA224", "regex": r"^[a-fA-F0-9]{56}$"},
    {"name": "SHA256", "regex": r"^[a-fA-F0-9]{64}$"},
    {"name": "SHA384", "regex": r"^[a-fA-F0-9]{96}$"},
    {"name": "SHA512", "regex": r"^[a-fA-F0-9]{128}$"},
]

def identify_hash(hash_value: str) -> dict:
    hash_value = hash_value.strip()
    matches = [item["name"] for item in HASH_PATTERNS if re.match(item["regex"], hash_value)]
    return {
        "hash": hash_value,
        "length": len(hash_value),
        "possible_algorithms": matches or ["Desconocido"]
    }
