from pathlib import Path
from hash_audit.detector import identify_hash
from hash_audit.verifier import hash_text

SUPPORTED = {"md5", "sha1", "sha224", "sha256", "sha384", "sha512"}

def audit_hash_with_wordlist(hash_value: str, wordlist_path: str, algorithm: str | None = None) -> dict:
    hash_value = hash_value.strip().lower()
    if algorithm is None:
        detected = identify_hash(hash_value)
        probable = detected["possible_algorithms"][0]
        if probable.lower() in SUPPORTED:
            algorithm = probable.lower()
        else:
            return {
                "status": "error",
                "summary": "No se pudo inferir el algoritmo. Indícalo con --algorithm."
            }

    wordlist = Path(wordlist_path)
    if not wordlist.exists():
        return {
            "status": "error",
            "summary": f"La wordlist no existe: {wordlist_path}"
        }

    for line in wordlist.read_text(encoding="utf-8", errors="ignore").splitlines():
        candidate = line.strip()
        if not candidate:
            continue
        if hash_text(candidate, algorithm) == hash_value:
            return {
                "status": "match",
                "summary": "Coincidencia encontrada en la wordlist autorizada.",
                "hash": hash_value,
                "algorithm": algorithm,
                "matched_plaintext": candidate,
                "risk": "high",
                "recommendations": [
                    "Restablecer la contraseña.",
                    "Usar Argon2, bcrypt o scrypt.",
                    "Aplicar sal única por credencial."
                ]
            }

    return {
        "status": "not_found",
        "summary": "No hubo coincidencia en la wordlist autorizada.",
        "hash": hash_value,
        "algorithm": algorithm,
        "risk": "unknown",
        "recommendations": [
            "Verificar si el hash está salteado.",
            "Evitar MD5 y SHA1 para contraseñas."
        ]
    }
