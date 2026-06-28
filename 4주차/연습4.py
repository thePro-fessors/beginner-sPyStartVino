# 입력받은 문자가 소문자면 대문자로, 대문자면 소문자로 변환하세요.

# 소문자를 판별하는 함수는 islower() 입니다.

string = input()

if(string.islower()): print(string.upper())
else: print(string.lower())