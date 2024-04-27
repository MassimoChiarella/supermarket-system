items=[]
print("----------- Welcome to the supermarket -----------")
print("1. View items /n 2. Add items /n 3. Purchase items /n 4. Search items /n 5.Edit items /n 6. Exit")
Choice=int(input("Enter the number of your choice: "))
if Choice == 1:
    print("----------- View Items -----------")
    print("The number of items in the inventory are %d" %len(items))
if len(items)!=0:
    print("Here are all of the items available in a supermarket")
    for item in items:
        for key, value in item.items():
            print ("%s : %S" %(key, value))