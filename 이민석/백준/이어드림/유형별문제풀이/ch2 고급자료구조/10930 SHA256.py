import sys
sys.stdin=open("input.txt", "rt")
import hashlib
#강의코드
input_data = input()
encoded_data = input_data.encode()
result = hashlib.sha256(encoded_data).hexdigest()
print(result)
