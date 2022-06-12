
# github link:
# https://github.com/yuna478/store

import os
import csv
import code

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
          while 1:
               print(" ____________________________ \n"
                    "|                            |\n"
                    "|      1- show                |\n"
                    "|                            |\n"
                    "|     b- back  e- exit       |\n"
                    "|____________________________|\n")
               a= input ('your choice:')
               if a=='b':
                    break
               elif a=='1':
                    code.show()
               elif a=='E' or a=='e' :
                    exit(0)
               else:
                    print("incorrect input")     
                    pass
     elif a=='2':
          while 1:
               print(" ____________________________ \n"
                    "|                            |\n"
                    "|      1- add                |\n"
                    "|      2- remove             |\n"
                    "|      3- show               |\n"
                    "|      4- edit               |\n"
                    "|     b- back  e- exit       |\n"
                    "|____________________________|\n")
               a= input ('your choice:')
               if a=='3':
                    code.show()
               elif a=='2':
                    code.remove()
               elif a=='4':
                    code.edit()
               elif a=='b':
                    break
               elif a=='1':
                    code.add()
               elif a=='E' or a=='e' :
                    exit(0)
               else:
                    print("incorrect input")     
                    pass
     elif a=='E' or a=='e' :
          exit(0)
     else:
          print("incorrect input")