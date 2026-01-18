
from helper import load_data



def main():

    my_company = load_data("data.json")


    while True:
        print("\n--- MENU ---")
        print("1. Balance")
        print("2. Sale")
        print("3. Purchase")
        print("4. Account")
        print("5. List")
        print("6. Warehouse")
        print("7. Review")
        print("8. Exit")

        choice = input("Choose option: ")


        if choice == '1':
            print("Balance:", my_company.balance)

        elif choice == '2':
            product = input("Product name")
            if product not in my_company.warehouse:
                print("Product not found in warehouse!")
                continue

            price = float(input("Sale price: "))
            quantity = int(input("Quantity: "))

            if my_company.warehouse[product]["quantity"] < quantity:
                print("Not enough quantity.")
                continue

            income = price * quantity
            my_company.warehouse[product]["quantity"] -= quantity
            my_company.balance += income
            my_company.operations.append(("sale", product, price, quantity))
            print("Sale completed.")

        elif choice == '3':
            product = input("Product name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            if quantity <= 0 or price < 0:
                raise ValueError("Invalid price or quantity")

            cost = price * quantity
            if my_company.balance < cost:
                print("Insufficient funds.")
                continue

            if product not in my_company.warehouse:
                my_company.warehouse[product] = {"price": price, "quantity": quantity}
            else:
                my_company.warehouse[product]["quantity"] += quantity

            my_company.balance -= cost
            my_company.operations.append(("purchase", product, price, quantity))
            print("Purchase completed.")

        elif choice == '4':
            print("Current balance:", my_company.balance)

        elif choice == '5':
            if not my_company.warehouse:
                print("Warehouse is empty.")
            else:
                for product, info in my_company.warehouse.items():
                    print(f"{product}: price={info['price']}, quantity={info['quantity']}")

        elif choice == '6':
            product = input("Product name: ")
            if product in my_company.warehouse:
                print(my_company.warehouse[product])
            else:
                print("Product not found.")

        elif choice == '7':
            if not my_company.operations:
                print("No operations recorded.")
            else:
                for i, op in enumerate(my_company.operations):
                    print(f"{i}: {op}")


        elif choice == '8':
            my_company.save_to_file("data.json")
            print("Data saved. Program ending.")
            break
        else:

            print("Wrong option")

main()