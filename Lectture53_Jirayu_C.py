price = int(input("Enter Price :"))


def VatCalculate(price):
    return price + (price*7/100)


print(VatCalculate(price))