import sys


class Warehouse:

    def __init__(self, product_list):
        self.product_list = product_list

    def display_available_products(self):
        print("Dostępne produkty: ")
        for product in self.product_list:
            print(product)

    def add_product(self):
        self.product_name = input("Podaj nazwę produktu: ")
        if self.product_name not in self.product_list:
            self.product_list.append(self.product_name)
            print(f"Produkt {self.product_name} został dodady do magazynu.")
        else:
            print("Produkt jest już w magazynie")

    def remove_product(self):
        self.product_name = input("Podaj nazwę produktu który chcesz usunąć: ")
        if self.product_name in self.product_list:
            self.product_list.remove(self.product_name)
            print(f"Z magazynu usunięto {self.product_name}!")
        else:
            print("Wskazanego produktu nie ma na stane magazynu.")


warehouse = Warehouse(['mleko', 'woda', 'jajka'])

while True:
    print("Wprowadź 1 aby wyśiwetlić stan magazynu.")
    print("Wprowadź 2 aby dodać produkt.")
    print("Wprowadź 3 aby usunąc produkt.")
    print("Wprowadź 4 aby zakończyć")
    user_choice = int(input(">>> "))
    if user_choice == 1:
        warehouse.display_available_products()
    elif user_choice == 2:
        warehouse.add_product()
    elif user_choice == 3:
        warehouse.remove_product()
    elif user_choice == 4:
        sys.exit()
