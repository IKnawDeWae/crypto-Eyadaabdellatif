
def don2():
  s=input('code: ')
  n = int(input('nombre de chiffrage souhaiter :'))
  m=s
  i=0
  while i < n:
    i =i+1
    m=m[1::2]+m[0::2]
    m=m[::-1]
    print(m)

don2()