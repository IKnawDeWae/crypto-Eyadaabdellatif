def flatten(lst):
    return [i for sublst in lst for i in sublst]
def faroo(deck):
    half = len(deck) // 2
    return flatten(zip(deck[:half], deck[half:]))
def faro2():
  i=0
  deck = input('code :')
  n = int(input('nombre de chiffrage souhaiter :'))
  while i<n :
    i=i+1
    half= deck
    half = len(deck) // 2 
    deck=flatten(zip(deck[half:], deck[:half]))
    print (deck)

faro2()

