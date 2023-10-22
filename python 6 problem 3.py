
def convert_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

while True:
    gallons = float(input("Enter a quantity in American gallons (or a negative value to quit): "))

    if gallons < 0:
        break
    liters =convert_to_liters(gallons)
    print(f"{gallons} gallons is equal to {liters} liters.")
