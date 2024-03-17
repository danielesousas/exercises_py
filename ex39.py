N = int(input())

while(N > 0):
  
  valores = input().split()
  a = valores[0]
  b = valores[1]
  
  if a[-len(b):] == b:
    print('encaixa')
  else:
    print('nao encaixa')
    
  N -= 1