
  #e=s[0:][::2]#even 
  #o=s[1:][::2]#odd

def don():
  s=input('code: ')
  n = int(input('nombre de chiffrage souhaiter :'))
  m=s
  i=0
  while i < n:
    i =i+1
    m=m[0::2]+m[1::2]
    m=m[::-1]
    print(m)

don()