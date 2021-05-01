from itertools import product
def bf():
  chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # chars to look for
  password = input('le mot de passe a craquer :') 
  for length in range(1, 5): # taille de code  ici 4 chars
      to_attempt = product(chars, repeat=length)
      
      for attempt in to_attempt:
        trial =(''.join(attempt))
        #print(''.join(attempt)) pour voir le founction de code
        if trial == password:
          print ('le mot de passe est : ',trial)