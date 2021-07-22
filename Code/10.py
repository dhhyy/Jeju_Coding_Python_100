print('숫자를 입력')
data = int(input())

if data > 10:
    if data % 2 == 0:
        print('10보다 큰 짝수')
    else:
        print('10보다 큰 홀수')
else:
    if data % 2 == 0:
        print('10보다 작은 짝수')
    else:
        print('10보다 작은 홀수')