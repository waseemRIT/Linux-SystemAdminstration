#!/usr/bin/python3
import os
import subprocess


# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
# DATE 21/11/2022

# INFORMING USER OF THEIR CURRENT PATH
print(os.getcwd())
# PATH OF THE HOME DIRECTORY, DEFINED GLOBALLY SINCE IT WILL BE THE SAME FOR ALL
home = os.path.expanduser("~")
# MOVES TO THE HOME DIRECTORY
os.chdir(home)


def create_symlink():
    """
    Function to create a Symbolic link
    Function takes 2 inputs from User
    first input:
        The file that a shortcut would be created for.
            IF the file doesn't exist then
                Returns "User File Does Not Exist!"
    second input:
        The name of the symbolic link that will be in the home directory

    All shortcuts/symbolic links created will be in the Home directory!
    """
    # Ask the user for the Path of the file
    file_path = input("Insert Name/Path of file you want to create a shortcut/Symbolic Link for:\n")
    # checks if the file exists or not
    if os.path.exists(file_path):
        name_of_symlink = input("Insert Name of the shortcut/symbolic link:\n")
        # Joins the Shortcut with its full path to the hone directory
        name_of_symlink = os.path.join(home, name_of_symlink)
        # ln -s file_path symlink_name
        # Command to create the Symlink/Shortcut
        os.symlink(file_path, name_of_symlink)
    else: # NOTIFY USER IN CASE FILE DOESN'T EXIST
        print("User File Does Not Exist!")


def delete_symlink():
    """
    Function to delete a symlink
    User Inputs SYMLINK FILE PATH
    USER WILL BE NOTIFIED IF SYMLINK IS DELETED SUCCESSFULLY
    """
    symlink_to_delete = input("Insert Path to Symlink you want to remove:\n")

    x = subprocess.run(
        ["rm", symlink_to_delete],
        stdout=subprocess.PIPE
    )
    if x.returncode == 0:
        print(f"{symlink_to_delete} deleted successfully !")


def display_summary():
    subprocess.run(
        ["sudo", home, "-type", "l"],
        stdout=subprocess.PIPE
    )
    pass


def main():
    user_option = input("Please insert one of the following options:\n1 to add a shortcut\n2 to remove a shortcut\n3 "
                        "to get a summary of shortcuts in the home\nquite to stop execution of the program\n--> ")
    user_option.lower()  # incase someone inserts eXit capital litters for the exit option!!
    if user_option == "1":
        # create shortcut/symbolic link Function
        pass
    elif user_option == "2":
        # delete shortcut/symbolic link Function
        pass
    elif user_option == "3":
        # Display summary function
        pass
    elif user_option == "quite":
        # To stop the execution of the program
        exit()
    else:
        print("Please Insert a valid option")


if __name__ == '__main__':
    # os.system("clear")
    while True:
        # main()
        pass
