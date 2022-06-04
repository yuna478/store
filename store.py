import os
pro={}
id=0
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
          "|      4- edit               |\n"
          "|     b- back  e- exit       |\n"
          "|____________________________|\n")
               a= input ('your choice:')
               if a=='3':
                    for prod in range(1,len(pro)+1):
                         pr=str(prod)
                         print(pr+'- size: '+ pro[pr]['size']+ ', brand: '+ pro[pr]['brand']+ ', price: '+ pro[pr]['price']+ ', color: '+ pro[pr]['color'])
               elif a=='2':
                    print('under development')
               elif a=='4':
                    a = input('enter the id of the product you want to edit: ')
                    if a not in pro.keys():
                         print('incorrect id')
                         a = input('enter the id of the product you want to edit: ')
                         if a not in pro.keys():
                              print('incorrect id')
                    os.system('cls')
                    print(" ____________________________ \n"
                         "|                            |\n"
                         "|  what do you want to edit  |\n"
                         "|      1- size               |\n"
                         "|      2- brand              |\n"
                         "|      3- price              |\n"
                         "|      4- color              |\n"
                         "|____________________________|\n")
                    b=input('your choice: ')
                    if b=='1':
                         c= input('enter new size: ')
                         pro[a]['size']=c
                    elif b=='2':
                         c= input('enter new brand: ')
                         pro[a]['brand']=c
                    elif b=='3':
                         c= input('enter new price: ')
                         pro[a]['price']=c
                    elif b=='4':
                         c= input('enter new color: ')
                         pro[a]['color']=c
                    else:
                         print('incorrect input, please retry editing')

               elif a=='b':
                    break
               elif a=='1':
                    id+=1
                    size= input("enter size: ")
                    brand= input("enter brand: ")
                    price= input("enter price: ")
                    color= input("enter color: ")
                    pro.update({str(id):{'size': size, 'brand': brand, 'price': price, 'color': color}})
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