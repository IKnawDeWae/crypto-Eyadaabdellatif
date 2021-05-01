
  #e=s[0:][::2]#even 
  #o=s[1:][::2]#odd

def dontest():
  s=123456
  n = 1
  m=s
  i=0
  while i < n:
    i =i+1
    m=m[0::2]+m[1::2]
    m=m[::-1]
    print(m)

dontest()