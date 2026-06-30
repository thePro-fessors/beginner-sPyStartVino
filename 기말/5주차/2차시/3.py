# todo 3 : n!을 반복문을 통해 구현하세요. n!란, 1부터 n까지의 곱을 의미합니다.

n = int(input())
sum = 1

for i in range(1, n + 1):
    sum *= i

print(sum)