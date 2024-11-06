#Define The Menu Of Restaurant
menu = {
    'chinees pizza':400,
    'pasta':500,
    'kurkure burger':600,
    'salad':700,
    'coffee':800,
}

#Greet
print("welcome To Python Restaurat")
print ("chiness pizza: Rs400\npasta: Rs500\nkurkure burger: Rs600\nSalad: Rs700\ncoffee: Rs800")

order_total = 0
#800 + 700 = 1500

item_1 = input("Enter The Name Of item You Want To Order =")
if item_1 in menu:
    order_total += menu[item_1] #0 + 500
    print(f"Your Item {item_1} Has Been Added To Your Order")

else:
    print(f"Order Item {item_1} Is Not Avaialable Yet!")

another_order = input("Do You Want To Add Another Item? (yes/no) ")
if another_order == "yes":
    item_2 = input("Enter The Name Of Second Item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} Has Been Added To Order")
    else:
        print(f"Ordered Item {item_2} Is Not Avaiable!")
print(f"The Total Amount Of Items To Pay Is {order_total}")            

        