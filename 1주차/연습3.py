# - 두 숫자 바꾸기(swap)
# - 숫자 두 개가 변수 a, b에 저장되어 있습니다. a와 b에 저장된 값을 바꾸어 출력해보세요.
# - 예를 들어, a에 5가 들어있고 b에 3이 들어있으면, a에는 이제 3. b에는 이제 5가 들어가야 합니다.

a = int(input())
b = int(input())

temp = a
a = b
b = temp

print(f'{a} {b}')