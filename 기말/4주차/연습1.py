# 점수를 입력받아 90점 이상이면 A, 80~89 사이이면 B, 70 ~ 79 사이이면 C, 그 이하는 F를 출력하는 프로그램을 작성하세요.

score = int(input())

if(score >= 90): print(f'A')
elif(score >= 80): print(f'B')
elif(score >= 70): print(f'C')
else: print(f'F')