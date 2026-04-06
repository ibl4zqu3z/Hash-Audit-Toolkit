import hashlib
from pathlib import Path

def hash_file(filepath: str, algorithm: str = "sha256") -> dict:
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"No existe el fichero: {filepath}")

    hasher = hashlib.new(algorithm)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)

    return {
        "filepath": str(path),
        "size_bytes": path.stat().st_size,
        "algorithm": algorithm,
        "hash": hasher.hexdigest(),
    }
