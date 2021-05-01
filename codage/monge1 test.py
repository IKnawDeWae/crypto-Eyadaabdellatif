def mongetest():
  i=0
  s='123456'
  m = 1
  n=s
  while i < m :
    i=i+1
    n=n[-1::-2]+n[0::2]#les character de pos -1 en pos -2
    print(n)

mongetest()