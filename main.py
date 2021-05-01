
from lol2 import*
from bruteforce import*
#from lol import*
#made by Eyad
# fonctions caesar 
#j'ai pas reussi a appeler les functions dans un different fichier et avoir le menu au meme temps donc jai tout regroupe dans une seuk functiion
# 
print("1 ==> codage")
print("2 ==> decodage")
print('4 ==> bruteforce')
ker = int(input("votre choix :"))
if ker == 1:
 # print("c → caesar ")
  print("f →  faro")
  print("f2 →  faro2")
  print("m →  monge")
  print("m2 → monge2 ")
  print("d → donne equitable")
  print("d2 → donne equitable2")
  choix  = input ("votre choix de cryptage :  ")
  if choix  == "c" :
   x = input ("votre message = ")
   n = 3
   print (encrypt(x , n))
  #if choix == "d" :
    #x = input ("votre message = ")
    #n = int(input("decalage = "))
    #print (code = encrypt(x , n))
  if choix == "f":
    faro1()
  if choix == "f2":
    faro2()
  if choix == "m":
    monge()
  if choix == "m2":
    monge2()
  if choix =="d":
     don()
  if choix =="d2":
     don2()
if ker ==2 :
  #print("c → caesar ")
   #print("a → affine ")
   #print("d → decalage")
   print("f →  faro")
   print("m →  monge")
   print("m2 → monge 2 ")
   print("g →  faro2")
   print("d → donne equitable")
   print("d2 → donne equitable2")
   choix  = input ("votre choix de cryptage :  ")
   if choix == "f":
     main()
     faro1d()
   if choix =="m":
     monged()
   if choix == "m2":
     monge2d()
   if choix =="g":
     main()
     faro2d()
   if choix =="d":#on utiliose faro pour decoder
     decdon()
   if choix =="d2":#on utilise faro2 pour decoder
     decdon2()
if ker == 3:
  main()
  print()
  print()
  mongecounter()
if ker == 4:
  bf()