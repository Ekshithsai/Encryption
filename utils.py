import hashlib

PATTERN_FILE = "pattern_hash.txt"

def hash_pattern(pattern_list):
    pattern_str = "-".join(map(str, pattern_list))
    return hashlib.sha256(pattern_str.encode()).hexdigest()

def save_hashed_pattern(hashed):
    with open(PATTERN_FILE, "w") as f:
        f.write(hashed)

def load_hashed_pattern():
    try:
        with open(PATTERN_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def verify_pattern(input_pattern):
    return hash_pattern(input_pattern) == load_hashed_pattern()
