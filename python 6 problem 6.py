def unit_price(diameter, price):
    radius = diameter / 2
    area_cm2 = 3.14159265 * (radius ** 2)
    area_m2 = area_cm2 / 10_000
    unit_price_m2 = price / area_m2

    return unit_price_m2
if __name__ == "__main":
    diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
    price1 = float(input("Enter the price of the first pizza (in euros): "))
    diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
    price2 = float(input("Enter the price of the second pizza (in euros): "))
    unit_price1 = unit_price(diameter1, price1)
    unit_price2 = unit_price(diameter2, price2)
    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas have the same unit price.")