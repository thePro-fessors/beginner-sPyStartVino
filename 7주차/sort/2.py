# 다음 languages를 길이가 긴 순으로 정렬하세요, 단 대소문자는 무시합니다. 

languages = ["python", "JavaScript", "C++", "react"]

languages.sort(key = lambda x: (-len(x)))
print(languages)