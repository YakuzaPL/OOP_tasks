
class Warehouse:

    def __init__(self, product_list):
        self.product_list = product_list

    def display_available_products(self):
        print("Dostępne produkty: ")
        for product in self.product_list:
            print(product)

    def add_product(self):
        product_name = input("Podaj nazwę produktu: ")
        if product_name not in self.product_list:
            self.product_list.append(product_name)
            print(f"Produkt {product_name} został dodady do magazynu.")
        else:
            print("Produkt jest już w magazynie")

    def remove_product(self):
        product_name = input("Podaj nazwę produktu który chcesz usunąć: ")
        if product_name in self.product_list:
            self.product_list.remove(product_name)
            print(f"Z magazynu usunięto {product_name}!")
        else:
            print("Wskazanego produktu nie ma na stane magazynu.")


warehouse = Warehouse(['mleko', 'woda', 'jajka'])

user_choice = 0
while user_choice != 4:

        print("Wprowadź 1 aby wyśiwetlić stan magazynu.")
        print("Wprowadź 2 aby dodać produkt.")
        print("Wprowadź 3 aby usunąc produkt.")
        print("Wprowadź 4 aby zakończyć")

        try:
            user_choice = int(input(">>> "))
        except ValueError:
            print("Podana wartość jest nieprawidłowa.")
        if user_choice == 1:
            warehouse.display_available_products()
        elif user_choice == 2:
            warehouse.add_product()
        elif user_choice == 3:
            warehouse.remove_product()
        elif user_choice == 4:
            break
