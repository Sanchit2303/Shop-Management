import pickle
import os


# Helper function to open files in binary mode
def open_file(filename, mode):
    try:
        return open(filename, mode)
    except FileNotFoundError:
        print(f"{filename} not found.")
        return None


# --- Processor Functions ---
def add_rec():
    f = open_file('processor.dat', 'ab')
    if not f:
        return
    done = 'no'
    while done == 'no':
        d = {}
        d['PCPname'] = input('Enter name of your processor company: ')
        d['Pname'] = input('Enter your processor\'s name: ')
        d['Pcode'] = input('Enter your processor\'s code: ')
        d['Palpha'] = input('Enter your processor\'s alphabet: ').upper()
        d['Pcores'] = int(input('Enter the cores for the processor: '))
        d['Pgen'] = int(input('Enter your processor\'s generation: '))
        d['Pprice'] = int(input('Enter price for the processor: '))
        d['Pqty'] = int(input('Enter the quantity of processor: '))
        d['PWarranty'] = int(input('Enter the warranty period of the purchased processor: '))
        pickle.dump(d, f)
        done = input('Done adding data (yes/no): ').strip().lower()
    f.close()


def view_record_Processor():
    f = open_file('processor.dat', 'rb')
    if not f:
        return
    try:
        while True:
            d = pickle.load(f)
            print(f"Company Name: {d['PCPname']}")
            print(f"Processor name: {d['Pname']}")
            print(f"Processor code: {d['Pcode']}")
            print(f"Processor cores: {d['Pcores']}")
            print(f"Processor alphabet: {d['Palpha']}")
            print(f"Processor Gen: {d['Pgen']}")
            print(f"Processor Price: {d['Pprice']}")
            print(f"Processor quantity: {d['Pqty']}")
            print(f"Processor warranty: {d['PWarranty']}")
    except EOFError:
        pass
    f.close()


def find_processor_rec():
    f = open_file('processor.dat', 'rb')
    if not f:
        return
    name = input('Enter the processor name to search: ')
    alpha = input('Enter the alphabet of processor to find: ').upper()
    cores = int(input('Enter the number of cores for selected processor: '))
    gen = int(input('Enter the generation for the processor: '))
    found = False
    try:
        while True:
            r = pickle.load(f)
            if r['Pname'] == name and r['Pcores'] == cores and r['Palpha'] == alpha and r['Pgen'] == gen:
                found = True
                print(f"Processor details:\nCompany: {r['PCPname']}\nName: {r['Pname']}\nCode: {r['Pcode']}")
                print(f"Alpha: {r['Palpha']}\nGen: {r['Pgen']}\nPrice: {r['Pprice']}\nQuantity: {r['Pqty']}")
                break
    except EOFError:
        pass
    if not found:
        print('Invalid info entered')
    f.close()


def del_processor_rec():
    f = open_file('processor.dat', 'rb')
    n = open_file('newp.dat', 'ab')
    if not f or not n:
        return
    name = input('Enter the name of processor whose data is to be deleted: ')
    gen = int(input('Enter the gen of the processor: '))
    p_core = int(input('Enter the cores for the processor: '))
    alpha = input('Enter the alphabet of the processor to be deleted: ').upper()
    try:
        while True:
            d = pickle.load(f)
            if not (d['Pgen'] == gen and d['Pname'] == name and d['Pcores'] == p_core and d['Palpha'] == alpha):
                pickle.dump(d, n)
    except EOFError:
        pass
    f.close()
    n.close()
    os.remove('processor.dat')
    os.rename('newp.dat', 'processor.dat')


# --- Customer Functions ---
def add_costumer():
    fC = open_file('Costumer.dat', 'ab')
    if not fC:
        return
    more = 'no'
    while more == 'no':
        c = {}
        c['Cnme'] = input('Enter the customer\'s name: ')
        c['CAno'] = int(input('Enter the Aadhar number of the customer: '))
        c['CMob'] = int(input('Enter mobile number of the customer: '))
        c['CSpecial'] = int(input('Enter the customer\'s special card number: '))
        c['CAdd'] = input('Enter the customer\'s address: ')
        c['CGen'] = input('Enter the customer\'s gender: ')
        pickle.dump(c, fC)
        more = input('Done adding data (yes/no): ').strip().lower()
    fC.close()


def view_costumer_rec():
    f = open_file('Costumer.dat', 'rb')
    if not f:
        return
    try:
        while True:
            r = pickle.load(f)
            print(f"Customer's name: {r['Cnme']}")
            print(f"Customer's Aadhar no: {r['CAno']}")
            print(f"Customer's mobile no: {r['CMob']}")
            print(f"Customer's special code: {r['CSpecial']}")
            print(f"Customer's address: {r['CAdd']}")
            print(f"Customer's gender: {r['CGen']}")
    except EOFError:
        pass
    f.close()


def del_costumer_rec():
    f = open_file('Costumer.dat', 'rb')
    n = open_file('newc.dat', 'wb')
    if not f or not n:
        return
    name = input('Enter the customer\'s name: ')
    scode = int(input('Enter the special code of the customer: '))
    try:
        while True:
            c = pickle.load(f)
            if not (c['Cnme'] == name and c['CSpecial'] == scode):
                pickle.dump(c, n)
    except EOFError:
        pass
    f.close()
    n.close()
    os.remove('Costumer.dat')
    os.rename('newc.dat', 'Costumer.dat')


# --- Admin Functions ---
def admin_login():
    admin_username = "admin"
    admin_password = "admin123"
    print("\nAdmin Login:")
    username = input("Username: ")
    password = input("Password: ")
    return username == admin_username and password == admin_password


def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Processor")
        print("2. View Processor Records")
        print("3. Search Processor")
        print("4. Delete Processor Record")
        print("5. Add Customer")
        print("6. View Customer Records")
        print("7. Delete Customer Record")
        print("8. Exit Admin Menu")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print('\nRecord Added,\n')
            add_rec()
        elif choice == 2:
            view_record_Processor()
        elif choice == 3:
            print('\nAvailable Processors,\n')
            find_processor_rec()
        elif choice == 4:
            print('\nRecord deleted,\n')
            del_processor_rec()
        elif choice == 5:
            print('\nCostumer Aded,\n')
            add_costumer()
        elif choice == 6:
            print('\nAvailabe costumers are,\n')
            view_costumer_rec()
        elif choice == 7:
            print('\nCostumer Record Deleated,\n' )
            del_costumer_rec()
        elif choice == 8:
            break
        else:
            print("Invalid choice!!!, Try again.")


# --- Customer Functions ---
def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. View all Processor Records")
        print("2. Search for a Processor")
        print("3. View Your Customer Records")
        print("4. Exit Customer Menu")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print('\nAvailable Procesors,\n')
            view_record_Processor()
        elif choice == 2:
            print('\nMost Matched Processor,\n')
            find_processor_rec()
        elif choice == 3:
            print('\nYour record,\n')
            view_costumer_rec()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Try again.")


# --- Main Function to Test the Code ---
def main():
    while True:
        print("\nMenu:")
        print("1. Admin Menu")
        print("2. Customer Menu")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            if admin_login():
                admin_menu()
            else:
                print("Invalid admin credentials.")
        elif choice == 2:
            customer_menu()
        elif choice == 0:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
