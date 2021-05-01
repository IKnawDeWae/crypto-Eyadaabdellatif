
def monge2test():
  i=0
  s='123456'
  m = 1
  n=s
  while i < m :
    i=i+1
    n=n[-2::-2]+n[1::2]#les character de pos -1 en pos -2
    print(n)

monge2test()