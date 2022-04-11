A, B = map(int, input().split())

if A >= B:
    if A % B == 0:
        print('Sao multiplos')
    else:
        print('Nao sao multiplos')

if B > A:
    if B % A == 0:
        print('Sao multiplos')
    else:
        print('Nao sao multiplos')