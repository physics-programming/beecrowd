dias = int(input())

anos = dias // 365

mes = (dias % 365) // 30

dias = (dias % 365) % 30

print(f'{anos} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')
