import getpass
import time
import requests


print("Welcome to myser!")
print("This is a simple file management system where you can create, read, update, and delete files and folders.")
print("Please set a password to protect your files and folders. You will need this password to delete files and modify them.")
print("version 0.2.1")
print("-------------------------------")

diskaF = {"file.txt": "hello, world!"}
# read password without echoing it to the console
password = getpass.getpass("Set a password to delete files and modify them:")
confirm_password = getpass.getpass("Confirm the password:")
while password != confirm_password:
    print("Passwords do not match. Please try again.")
    password = getpass.getpass("Set a password to delete files and modify them:")
    confirm_password = getpass.getpass("Confirm the password:")
print(f'successfully set the password to delete the files and modify them. Please keep it safe!')
def read_file(filename):
    if filename in diskaF:
        return diskaF[filename]
    else:
        return "File not found."
while True:
    ask = input("What file do you want to read? (type '#help' for help):")
    if ask == "#exit":
        break
    if ask == "#help":
        print("Commands:")
        print("#help - Show this help message")
        print("#exit - Exit the program")        
        print("#list - List available files")
        print("#add - Add a new file")
        print("#delete - Delete a file (requires password)")
        print("#password - Change the password (requires current password)")
        print("#folderadd - Add a new folder")
        print("#folderdelete - Delete a folder")  
        print("#addtofolder - Add a file to a folder")
        print("#pointer - Create a pointer to a file or folder")
        print("#disk - Show the contents of the disk")
        print("Note: Folders are denoted with a '@' at the start of their name, and pointers will show the content of the file or folder they point to.")
        continue
    if ask == "#list":
        print("Available files:", ", ".join(diskaF.keys()))
        continue
    if ask == "#add":
        filename = input("Enter the name of the file to add: ")
        content = input("Enter the content of the file: ")
        diskaF[filename] = content
        print(f'File {filename} added/edited successfully.')
        continue
    if ask == "#delete":
        password_input = input("Enter the password to delete files: ")
        if password_input == password:
            filename = input("Enter the name of the file to delete: ")
            if filename in diskaF:
                del diskaF[filename]
                print(f"File '{filename}' deleted successfully.")
            else:
                print("File not found.")
        else:
            print("Incorrect password.")
        continue
    if ask == "#password":
        password_input = input("Enter the current password to change it: ")
        if password_input == password:
            password = getpass.getpass("Enter the new password:")
            print("Password changed successfully.")
        else:
            print("Incorrect password.")
        continue  
    if ask == "#folderadd":
        foldername = input("Enter the name of the folder to add: ")
        foldername = "@" + foldername
        if foldername in diskaF:
            print("Folder already exists.")
        else:
            diskaF[foldername] = []
            print(f'Folder {foldername} added successfully.')
        continue
    if ask == "#folderdelete":
        password_input = getpass.getpass("Enter the password to delete folders:")
        if password_input == password:
            foldername = input("Enter the name of the folder to delete:")
            foldername = "@" + foldername
            if foldername in diskaF:            
                del diskaF[foldername]
        continue
    if ask == "#addtofolder":
        foldername = input("Enter the name of the folder to add the file to:")
        foldername = "@" + foldername
        if foldername in diskaF:
            filename = input("Enter the name of the file to add to the folder:")
            if filename in diskaF:
                diskaF[foldername].append(filename)
                print(f'File {filename} added to folder {foldername} successfully.')
            else:
                content = input("File not found. Enter the content of the new file to create and add to the folder:")
                diskaF[filename] = content
                diskaF[foldername].append(filename)
                print(f'File {filename} created and added to folder {foldername} successfully.')
        else:        
            print("Folder not found.")
        continue
    if ask == "#pointer":
        pointername = input("Enter the name of the pointer to create:")
        targetname = input("Enter the name of the file or folder to point to:")
        if targetname in diskaF:
            diskaF[pointername] = diskaF[targetname]
            print(f'Pointer {pointername} created successfully, pointing to {targetname}.')
            print("remember that if you delete/edit the target file, the pointer will not be deleted.")
        else:
            print("Target file or folder not found.")
        continue
    if ask == "#disk":
        print("Disk contents:")
        for name, content in diskaF.items():
            if isinstance(content, list):
                print(f"{name}/ (folder) - contains: {', '.join(content)}")
            else:
                print(f"{name} (file) - content: {content}")
        continue
    if ask == "#request":
        print("this command is not implemented yet, but it will be used to request files from other users in the future.")
    if ask == "#requestweb":
        page = input("Enter the URL of the web page to request:")
        print(requests.get(page))
    if ask.startswith("#"):
        print("Unknown command. Type '#help' for a list of commands.")
        continue
    if ask in diskaF:
        print(read_file(ask))
    else:        
        print("File not found.")
print("\nExiting the program please wait...")
time.sleep(1)
print("\nGoodbye!\n")
