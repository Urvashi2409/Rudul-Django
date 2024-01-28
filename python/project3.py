print("Here are the food choices you have\n1. pizza\n2. Burger\n3. Salad\n4. Ice cream\n5. French Fries\n6. Brownie\n7. Sandwich\n8. Pasta\n9. Hotdog\n10. Soup")
print("Pizza has a discount of 50%\nPasta has a discount of 30%\nBurger has a discount of 70%\nice cream has a discount of %50")
choice = input("What do you to have to eat?: ")

if choice == "1":
    print("Here! Have your pizza 🍕")
    discounted_price = 7-7*0.5
    print(f"Here is your bill for the pizza:${discounted_price}")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - discounted_price
    print(f"Here, take your change of ${remaining_money}")

if choice == "2":
    print("Here! Have your burger 🍔")
    discounted_price = 8-8*0.7
    print(f"Here is your bill for the burger:${discounted_price}")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - discounted_price
    print(f"Here, take your change of ${remaining_money}")

if choice == "3":
    print("Here! Have your salad 🥗")
    print("Here is your bill for the salad:$5")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - discounted_price
    print(f"Here, take your change of ${remaining_money}")

if choice == "4":
    print("Here! Have your ice cream 🍨")
    discounted_price = 4-4*0.5
    print("Here is your bill for the ice cream:$4")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - discounted_price
    print(f"Here, take your change of ${remaining_money}")

if choice == "5":
    print("Here! Have your french fries 🍟")
    print("Here is your bill for the french fries:$3")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - 3
    print(f"Here, take your change of ${remaining_money}")

if choice == "6":
    print("Here! Have your brownie 🍫")
    print("Here is your bill for the brownie:$6")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - 6
    print(f"Here, take your change of ${remaining_money}")

if choice == "7":
    print("Here! Have your sandwich 🥪")
    print("Here is your bill for the sanddwich:$7")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - 7
    print(f"Here, take your change of ${remaining_money}")

if choice == "8":
    print("Here! Have your pasta 🍝")
    discounted_price = 8-8*0.3
    print("Here is your bill for the pasta:$8")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - discounted_price
    print(f"Here, take your change of ${remaining_money}")

if choice == "9":
    print("Here! Have your hotdog 🌭")
    print("Here is your bill for the hotdog:$4")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - 4
    print(f"Here, take your change of ${remaining_money}")

if choice == "10":
    print("Here! Have your soup 🍲")
    print("Here is your bill for the soup:$8")
    user_money = int(input("Please pay with cash: "))
    remaining_money = user_money - 8
    print(f"Here, take your change of ${remaining_money}")