def flatten(lst):
    return [i for sublst in lst for i in sublst]



def decdon2():
  i=0
  s=input('code: ')
  n = int(input('nombre de chiffrage souhaiter :'))
  m=s
  while i < n :
    i=i+1
    m=m[::-1]
    half = len(m) // 2 
    m =flatten(zip(m[half:], m[:half]))
    print (m)

decdon2()