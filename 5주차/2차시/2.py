# todo 2 : 정수 하나를 입력받아, 카운트다운 하는 프로그램을 만들어 봅시다.
num = int(input())

for i in range(num + 1): 
    print(f'{num}')
    num -= 1