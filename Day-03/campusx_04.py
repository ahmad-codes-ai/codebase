while True:
    print("1. cm to ft")
    print("2. km to miles")
    print("3. USD to INR")
    print("4. exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        cm = float(input("Enter cm: "))
        print(f"{cm * 0.0328}")
    elif choice == 2:
        km = float(input("Enter km: "))
        print(f"{km * 0.621}")
    elif choice == 3:
        usd = float(input("Enter USD: "))
        print(f"{usd * 83}")
    elif choice == 4:
        break
    else:
        print("Invalid")
