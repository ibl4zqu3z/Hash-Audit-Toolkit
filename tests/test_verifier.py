from hash_audit.verifier import hash_text

def test_sha256():
    result = hash_text("test", "sha256")
    assert len(result) == 64
