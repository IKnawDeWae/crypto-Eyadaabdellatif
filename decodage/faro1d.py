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

main()
faro1d()