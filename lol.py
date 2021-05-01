import doctest
import random

def flatten(lst):
    return [i for sublst in lst for i in sublst]
def faroo(deck):
    half = len(deck) // 2
    return flatten(zip(deck[:half], deck[half:]))

def melange(shuffle_type, start, end):
    start = shuffle_type(start)
    counter = 1
    while start != end:
        start = shuffle_type(start)
        counter += 1
    return counter

def main():
    doctest.testmod()
    print("n| combien de faro pour etat Initial")
    for length in (4,6,8, 12, 14, 24, 36,54,64, 1024, 2048):
        deck = list(range(length))
        shuffles_needed = melange(faroo, deck, deck)
        print("{} | {}".format(length, shuffles_needed))

def faro1d():
    deck = []
    n = int(input("taille de text: "))
    for i in range(0, n):
        dec = (input('= '))
        deck.append(dec)
    d=int(input("shuffle: "))
    for i in range(1, d):
        half = len(deck) // 2
        deck=flatten(zip(deck[:half], deck[half:]))
        print(deck)

def faro2d():
    deck = []
    n = int(input("taille de text: "))
    for i in range(0, n):
        dec = (input('= '))
        deck.append(dec)
    d=int(input("shuffle: "))
    for i in range(1, d):
        half = len(deck) // 2
        deck=flatten(zip(deck[half:], deck[:half]))
    deck=deck[::-1]
    print(deck)

def faro1():
  deck = [] 
  n = int(input("taille de text: ")) 
  for i in range(0, n): 
      dec = (input('= ')) 
      deck.append(dec)
  half = len(deck) // 2 
  print (flatten(zip(deck[:half], deck[half:])))


def faro2():
  deck = [] 
  n = int(input("taille de text: ")) 
  for i in range(0, n): 
      dec = (input('= ')) 
      deck.append(dec)
  half = len(deck) // 2 
  print (flatten(zip(deck[half:], deck[:half])))

def encrypt(realText, step):
	outText = []
	cryptText = []

	upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
	for Letter in realText:
		if Letter in upper:
			index = upper.index(Letter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = upper[crypting]
			outText.append(newLetter)
		elif Letter in lower:
			index = lower.index(Letter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lower[crypting]
			outText.append(newLetter)
	return outText

def mongecounter():
  n=input("message exemple : ")#message de taille exemplaire
  L=len(n)
  r=0
  m2=0
  k=list(range (L))
  s2=''.join(map(str,k))
  #print (k,s2)
  n2=s2[-1::-2]+s2[0::2]
  while m2 != s2:
    n2=n2[-1::-2]+n2[0::2]
    m2=n2
  
    r=r+1
  print("pour une message de longeur ",L ,"faut",r+1,"monges")
  #print("message initial",m2)
  i=1
  while i<=r:
    n=n[-1::-2]+n[0::2]
    d=n
    i=i+1
  #print("message initial : ",d)

def monge():
  s=input('code: ')
  n=s[-1::-2]+s[0::2]#les character de pos -1 en pos -2
  print(n)

def monged():
  s=input('code: ')
  B = s[:len(s)//2]
  B=B[::-1]
  C = s[len(s)//2:]
  A= C+B
  print(A)
  half = len(A) // 2 
  print (flatten(zip(A[:half], A[half:])))

def monge2():
  s=input('code: ')
  n=s[-2::-2]+s[1::2]#les character de pos -1 en pos -2
  print(n)

def monge2d():
  s=input('code: ')
  B = s[:len(s)//2]
  B=B[::-1]
  C = s[len(s)//2:]
  A= C+B
  print(A)
  half = len(A) // 2 
  print (flatten(zip(A[half:], A[:half])))

def don():
  s=input('code: ')
  #e=s[0:][::2]#even 
  #o=s[1:][::2]#odd
  n=s[0::2]+s[1::2]
  n=n[::-1]
  print(n)

def don2():
  s=input('code: ')
  m=s[1::2]+s[0::2]
  m=m[::-1]
  print(m)

def decdon():
  s=input('code: ')
  m=s[::-1]
  half = len(m) // 2 
  print (flatten(zip(m[:half], m[half:])))

def decdon2():
  s=input('code: ')
  m=s[::-1]
  half = len(m) // 2 
  print (flatten(zip(m[half:], m[:half])))