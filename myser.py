import getpass
import time

print("Welcome to myser!")
print("This is a simple file management system where you can create, read, update, and delete files and folders.")
print("Please set a password to protect your files and folders. You will need this password to delete files and modify them.")
print("version v0.2.2-alpha")
print("date: 2026-apr-06")
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
        print("#request - Request a file from another user (not implemented yet)")
        print("#requestweb - Request a web page (not implemented yet)")
        print("#newuser - Create a new user (not implemented yet nor in the code yet)")
        print("#deleteuser - Delete a user (not implemented yet nor in the code yet)")
        print("#listusers - List users (not implemented yet nor in the code yet)")
        print("#version - Show the version and changelog")
        print("#credits - Show the credits for this program")
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
        print("this command is not implemented yet, but it will be used to request to the web in the future.")
    if ask == "#newuser":
        print("this command is not implemented yet, but it will be used to create new users in the future.")
    if ask == "#deleteuser":
        print("this command is not implemented yet, but it will be used to delete users in the future.")
    if ask == "#listusers":
        print("this command is not implemented yet, but it will be used to list users in the future.")
    if ask == "#version":
        print("myser version v0.2.1-alpha (2026-04-06):")
        print("- Added the ability to create pointers to files and folders.")
        print("- Added the ability to show the contents of the disk with the '#disk' command.")
        print("- Added the '#request' command to request files from other users (not implemented yet).")
        print("- Added the '#requestweb' command to request web pages (not implemented yet).")
        print("- Added the '#newuser', '#deleteuser', and '#listusers' commands to manage users (not implemented yet).")
        print("- Improved the user interface and added more helpful messages.")
        print("- Fixed some bugs and improved the overall stability of the program.")
        continue
    if ask == "#credits":
        print("myser was created by Daniel, with contributions from the open-source community.")
        print("Thank you to everyone who has contributed to the development of myser!")
        continue
    if ask == "#":
        print("did you forget to type the command after the '#'? Type '#help' for a list of commands.")
        continue
    if ask == "":
        print("you didn't type anything. Type '#help' for a list of commands.")
        continue
    if ask != ask.lower():
        print("commands are case-sensitive. Type '#help' for a list of commands.")
        continue
    if ask == "#viewhidden":
        password_input = input("Enter the password to view hidden files:")
        if password_input == password:
            filename = input("Enter the name of the hidden file to view:")
            if filename in diskaF:      
                print(read_file(filename))
            else:
                print("File not found.")
        else:
            print("Incorrect password.")
        continue
    if ask == "#deletehidden":
        password_input = input("Enter the password to delete hidden files:")
        if password_input == password:
            filename = input("Enter the name of the hidden file to delete:")
            if filename in diskaF:
                del diskaF[filename]
                print(f"Hidden file '{filename}' deleted successfully.")
            else:
                print("File not found.")
        else:
            print("Incorrect password.")
        continue
    if ask == "#edithidden":
        password_input = input("Enter the password to edit hidden files:")
        if password_input == password:
            filename = input("Enter the name of the hidden file to edit:")
            if filename in diskaF:
                content = input("Enter the new content of the hidden file:")
                diskaF[filename] = content
                print(f"Hidden file '{filename}' edited successfully.")
            else:
                print("File not found.")
        else:
            print("Incorrect password.")
        continue
    if ask.startswith("@"):
        print("Unknown list. Type '#help' for a list of commands.")
        continue
    if ask.startswith("#"):
        print("Unknown command. Type '#help' for a list of commands.")
        continue
    print("content of the file:")
    print(read_file(ask))
print("\nExiting the program please wait...")
time.sleep(1)
print("\nGoodbye!\n")
