items=[]
while True:
    print("----------- Welcome to the supermarket -----------")
    print("1. View items \n2. Add items \n3. Purchase items \n4. Search items \n5. Edit items \n6. Exit")
    choice=int(input("Enter the number of your choice: "))

    if choice == 1:
        print("----------- View Items -----------")
        print("The number of items in the inventory are %d " %len(items))
        if len(items)!=0:
            print("Here are all of the items available in a supermarket")
            for item in items:
                for key, value in item.items():
                    print ("%s : %s" %(key, value))
        
    elif choice == 2:
        print("----------- Add Items For Sale -----------")
        print("To add an item, fill in the form")
        item={}
        item["name"] = input("item name: ")
        while True:
            try:
                item["quantity"]= int(input("Item quantity: "))
                break
            except ValueError:
                print("Quantity should only be a number")
        while True:
            try:
                item["price"]= int(input("Price $: "))
                break
            except ValueError:
                print("Price should only be a number")
        print("Item has been successfully added!")
        items.append(item)

    elif choice == 3:
        print("----------- Purchase Items -----------")
        print(items)
        purchase_item = input("Which item would you like to purchase? Enter the name: ")
        purchase_quantity = int(input("Enter the quantity needed: "))
        for item in items:
            if purchase_item.lower()==item["name"].lower():
                if item["quantity"]!=0:
                    if purchase_quantity <= item["quantity"]:
                        print("Pay %d at checkout counter" %(item["price"]* purchase_quantity ))
                        item["quantity"]-= purchase_quantity
                    else:
                        print("The quantity selected is not available")
                else:
                    print("Sorry, item is out of stock")

    elif choice == 4:
        found = False
        print("----------- Search Items -----------")
        find_item = input("Please enter the item name to search the inventory: ")
        for item in items:
            if item["name"].lower() == find_item.lower():
                print(f"The item named {find_item} is displayed below with its details:")
                print(item)
                found = True
                break
        if not found:
            print("Item not found")
                
    elif choice == 5:
        found = False
        print("----------- Edit Items -----------")
        item_name = input("Enter the name of the item you want to edit: ")
        for item in items:
            if item_name.lower() == item["name"].lower():
                print(f"Here are the current details of {item_name}: ")
                print(item)
                item["name"] = input ("item name: ")
                while True:
                    try:
                        item["quantity"] = int(input("item quantity: "))
                        break
                    except ValueError:
                        print("Quantity should only be a number.")
                while True:
                    try:
                        item["price"] = int(input("item price: "))
                        break
                    except ValueError:
                        print("Price should only be a number.")
                print(item)
                found = True
                break
        if not found:
            print("Item not found")
            
    elif choice == 6:
        print("----------- Exited -----------")
        break
    else:
        print("You have entered an invalid option")