# - 단어를 길이 순으로 정렬하세요. 길이가 같다면 사전 순으로 정렬하세요.

# 결과: ['bat', 'car', 'atom', 'code', 'apple']

words = ["apple", "bat", "code", "atom", "car"]

print(sorted(words, key = lambda x: (len(x), x)))