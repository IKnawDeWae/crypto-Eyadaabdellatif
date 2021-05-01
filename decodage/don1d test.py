def flatten(lst):
    return [i for sublst in lst for i in sublst]



def decdon():
  i=0
  s='642531'
  n = 1
  m=s
  while i < n :
    i=i+1
    m=m[::-1]
    half = len(m) // 2 
    m =flatten(zip(m[:half], m[half:]))
    print (m)

decdon()