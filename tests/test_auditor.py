from hash_audit.auditor import audit_hash_with_wordlist

def test_match():
    result = audit_hash_with_wordlist(
        "5f4dcc3b5aa765d61d8327deb882cf99",
        "wordlists/demo.txt",
        "md5"
    )
    assert result["status"] == "match"
