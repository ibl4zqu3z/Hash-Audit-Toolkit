from hash_audit.detector import identify_hash

def test_md5_detection():
    result = identify_hash("5f4dcc3b5aa765d61d8327deb882cf99")
    assert "MD5" in result["possible_algorithms"]
