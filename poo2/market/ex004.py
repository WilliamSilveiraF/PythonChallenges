import ex003



while True:
    try:
        price = int(input("Property base price: "))
        choice = int(input("[1] New Property\n[2] Old Property\nChoice: "))

        if choice == 1:
            address = input("Address: ")
            additionalPrice = int(input("Additional price: "))
            house = ex003.New(address, price, additionalPrice)
        elif choice == 2:
            address = input("Address: ")
            house = ex003.Old(address, price)

        print(house.getPrice())
    except EOFError:
        break