import os

def create_file(file_name):
    try:
        with open(file_name,'x') as f:
            print(f"{file_name} is created successfully!!")
    except FileExistsError:
        print(f"{file_name} already exists!!")
    except Exception as E:
        print(f"An error occured!!:{E}")

def view_files():
    files = os.listdir()
    if not files:
        print("No files available!")
    else:
        print("Files in directory:")
        for i in files:
            print(i)

def del_file(file_name):
    try:
        os.remove(file_name)
        print(f"{file_name} deleted successfullly")
    except FileNotFoundError:
        print(f"{file_name}not found!!")
    except Exception as E:
        print(f"An error occured!!:{E}")

def read_files(file_name):
    try:
        with open(file_name,"r") as F:
         content =  F.read()
         print(f"following is the {file_name}\n{content}")
    except FileNotFoundError:
        print("File not found!!")
    except Exception as E:
        print(f"An error occured!!:{E}")

def edit_files(file_name):
    try:
        with open(file_name,"a") as F:
            append = input("Enter the things you want to add:: ")
            F.write(append + "\n")
            print(f"{append} has been added to {file_name}")

    except FileNotFoundError:
        print(f"{file_name}not found!!")
    except Exception as E:
        print(f"An error occured!!:{E}")
    

def main():
    while True:
        print("\nFILE MANAGEMENT APP")
        print("1.Create file")
        print("2.View available files")
        print("3.Delete files")
        print("4.Read the content of file")
        print("5.Edit the content of file")
        print("6.Exit")
        choice = input("Enter your choice(1-6): ")
        if choice == '1':
            file_name = input("Enter the file name: ")
            create_file(file_name)
        elif choice == '2':
            view_files()
        elif choice == '3':
            file_name = input("Enter the filename you want to delete: ")
            del_file(file_name)
        elif choice == '4':
            file_name = input("Enter the filename you want to read: ")
            read_files(file_name)
        elif choice == '5':
            file_name = input("Enter the filename you want to edit: ")
            edit_files(file_name)
        elif choice == '6':
            print("App closed!!!")
            break
        else:
            print("Invalid Input!!")  

main()