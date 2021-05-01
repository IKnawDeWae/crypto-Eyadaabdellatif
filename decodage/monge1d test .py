def flatten(lst):
    return [i for sublst in lst for i in sublst]


def monged():
  s="642135"
  n =1
  i=0
  A=s
  
  while i < n:
    i=i+1
    B = A[:len(A)//2]
    B=B[::-1]
    C = A[len(A)//2:]
    A= C+B
    half = len(A) // 2 
    A = flatten(zip(A[:half], A[half:]))
    print(A)
monged()