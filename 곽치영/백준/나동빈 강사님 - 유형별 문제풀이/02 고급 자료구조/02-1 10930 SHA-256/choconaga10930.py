import sys
input = sys.stdin.readline

import hashlib

string = input().strip()
print(hashlib.sha256(string.encode()).hexdigest())