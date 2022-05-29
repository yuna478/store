import os 
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
               pass
     elif a=='E' or a=='e' :
          exit(0)
     else:
          print("incorrect input")
 