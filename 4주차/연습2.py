# 세 숫자를 입력받아, 가장 큰 수를 출력하는 프로그램을 작성하세요.

max = 0
num1 = int(input())
num2 = int(input())
num3 = int(input())

if(num1 > max): 
    max = num1
    if(num2 > max): 
        max = num2
        if(num3 > max): max = num3
    else:
        if(num3 > max): max = num3

print(f'{max}')