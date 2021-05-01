def flatten(lst):
    return [i for sublst in lst for i in sublst]
def faroo(deck):
    half = len(deck) // 2
    return flatten(zip(deck[:half], deck[half:]))
def faro1test():
  i=0
  deck = '123456'
  n = 1
  while i<n :
    i=i+1
    half= deck
    half = len(deck) // 2 
    deck=flatten(zip(deck[:half], deck[half:]))
    print (deck)




faro1test()