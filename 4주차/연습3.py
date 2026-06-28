# 두 명의 사용자(A, B)로부터 "가위", "바위", "보" 중 하나를 입력받습니다. 누가 이겼는지, 혹은 비겼는지 판정하는 프로그램을 만드세요.

p1 = input('p1 의 차례 ')
p2 = input('p2 의 차례 ')

if(p1 == '가위'):
    if(p2 == '가위'): print(f'비김')
    elif(p2 == '바위'): print(f'p2(이/가) 이김')
    else: print(f'p1(이/가) 이김')
if(p1 == '바위'):
    if(p2 == '가위'): print(f'p1(이/가) 이김')
    elif(p2 == '바위'): print(f'비김')
    else: print(f'p2(이/가) 이김')
if(p1 == '보'):
    if(p2 == '가위'): print(f'p2(이/가) 이김')
    elif(p2 == '바위'): print(f'p1(이/가) 이김')
    else: print(f'비김')