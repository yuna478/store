import os
pro={}
id=0
def remove():
     global pro
     a = input('enter the id of the product you want to remove: ')
     while a not in pro.keys():
          print('incorrect id')
          a = input('enter the id of the product you want to remove: ')
     pro.pop(a)
def edit():
     global pro
     a = input('enter the id of the product you want to edit: ')
     while a not in pro.keys():
          print('incorrect id')
          a = input('enter the id of the product you want to edit: ')

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
          c.lower()
          pro[a]['brand']=c
     elif b=='3':
          c= input('enter new price: ')
          pro[a]['price']=c
     elif b=='4':
          c= input('enter new color: ')
          c.lower()
          pro[a]['color']=c
     else:
          print('incorrect input, please retry editing')
def add():
     global id, pro
     id+=1
     size= input("enter size: ")
     brand= input("enter brand: ")
     price= input("enter price: ")
     color= input("enter color: ")
     brand.lower()
     color.lower()
     pro.update({str(id):{'size': size, 'brand': brand, 'price': price, 'color': color}})
def show():
     global pro
     print(" ____________________________ \n"
          "|                            |\n"
          "|  what do you want to show  |\n"
          "|      1- all                |\n"
          "|      2- specific brand     |\n"
          "|      3- specific color     |\n"
          "|      4- price range        |\n"
          "|      5- size range         |\n"
          "|____________________________|\n")
     b=input('your choice: ')
     if b=='1':
          for prod in range(1,len(pro)+1):
               pr=str(prod)
               print(pr+'- size: '+ pro[pr]['size']+ ', brand: '+ pro[pr]['brand']+ ', price: '+ pro[pr]['price']+ ', color: '+ pro[pr]['color'])
     elif b=='2':
          sp=input('enter brand: ')
          sp.lower()
          accept=[]
          for prod in range(1,len(pro)+1):
               pr=str(prod)
               if pro[pr]['brand']==sp:
                    accept.append(pr)
          for pr in accept:
               print(pr+'- size: '+ pro[pr]['size']+ ', brand: '+ pro[pr]['brand']+ ', price: '+ pro[pr]['price']+ ', color: '+ pro[pr]['color'])
     elif b=='3':
          sp=input('enter color: ')
          sp.lower()
          accept=[]
          for prod in range(1,len(pro)+1):
               pr=str(prod)
               if pro[pr]['color']==sp:
                    accept.append(pr)
          for pr in accept:
               print(pr+'- size: '+ pro[pr]['size']+ ', brand: '+ pro[pr]['brand']+ ', price: '+ pro[pr]['price']+ ', color: '+ pro[pr]['color'])
     elif b=='4':
          lo=input('enter minimum price')
          hi=input('enter maximum price')
          accept=[]
          for prod in range(1,len(pro)+1):
               pr=str(prod)
               if pro[pr]['price']>=lo and pro[pr]['price']<=hi:
                    accept.append(pr)
          for prod in accept:
               pr=str(prod)
               print(pr+'- size: '+ pro[pr]['size']+ ', brand: '+ pro[pr]['brand']+ ', price: '+ pro[pr]['price']+ ', color: '+ pro[pr]['color'])
     elif b=='5':
          lo=input('enter minimum size')
          hi=input('enter maximum size')
          accept=[]
          for prod in range(1,len(pro)+1):
               pr=str(prod)
               if pro[pr]['size']>=lo and pro[pr]['size']<=hi:
                    accept.append(pr)
          for prod in accept:
               pr=str(prod)
               print(pr+'- size: '+ pro[pr]['size']+ ', brand: '+ pro[pr]['brand']+ ', price: '+ pro[pr]['price']+ ', color: '+ pro[pr]['color'])
     else:
          print('incorrect input')