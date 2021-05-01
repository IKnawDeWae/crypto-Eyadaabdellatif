
def don2():
  s=123456
  n = 1
  m=s
  i=0
  while i < n:
    i =i+1
    m=m[1::2]+m[0::2]
    m=m[::-1]
    print(m)

don2test()