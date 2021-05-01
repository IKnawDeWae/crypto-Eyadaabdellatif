
def monge2():
  i=0
  s=input('code: ')
  m = int(input('nombre de chiffrage souhaiter :'))
  n=s
  while i < m :
    i=i+1
    n=n[-2::-2]+n[1::2]#les character de pos -1 en pos -2
    print(n)

monge2()