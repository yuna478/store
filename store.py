import os
pro=[] 
while 1:
     print(" ____________________________ \n"
          "|                            |\n"
          "|   welcome to my store!!!   |\n"
          "|       choose an option     |\n"
          "|      1. customer menu      |\n"
          "|        2. management       |\n"
          "|          E- exit           |\n"
          "|____________________________|\n")
     a = input("your option: " )
     os.system('cls')
     if a=='1':
          print('under development')
     elif a=='2':
          while 1:
               print(" ____________________________ \n"
          "|                            |\n"
          "|      1- add                |\n"
          "|      2- remove             |\n"
          "|      3- show               |\n"
          "|                            |\n"
          "|____________________________|\n")
          a= input ('your choice:')
          if a=='3':
               print(pro)
          elif a=='2':
               print('under development')
          elif a=='1':
               while 1:
                         a= input("enter in order: size, price ,tag, color")
                         pro .append(a)
                         pass
          elif a=='E' or a=='e' :
                         exit(0)
          else:
                         print("incorrect input")
                         pass
     elif a=='E' or a=='e' :
          exit(0)
     else:
          print("incorrect input")
# https://github.com/yuna478/store