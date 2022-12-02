#!/usr/bin/python3
import os
import subprocess

# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
# DATE 21/11/2022

# INFORMING USER OF THEIR CURRENT PATH
print("YOU ARE IN:")
print(os.getcwd())
# PATH OF THE HOME DIRECTORY, DEFINED GLOBALLY SINCE IT WILL BE THE SAME FOR ALL
home = os.path.expanduser("~")


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
        name_of_symlink = input("Insert Name of the shortcut/symbolic link:\n--> ")
        # Joins the Shortcut with its full path to the hone directory
        name_of_symlink = os.path.join(home, name_of_symlink)
        # ln -s file_path symlink_name
        # Command to create the Symlink/Shortcut
        os.symlink(file_path, name_of_symlink)
    else:  # NOTIFY USER IN CASE FILE DOESN'T EXIST
        print("User File Does Not Exist!")


def delete_symlink():
    """
    Function to delete a symlink
    User Inputs SYMLINK FILE PATH
    USER WILL BE NOTIFIED IF SYMLINK IS DELETED SUCCESSFULLY
    """
    symlink_to_delete = input("Insert Path to Symlink you want to remove:\n")

    try:
        os.unlink(symlink_to_delete)  # TO UNLINK THE SYMLINK
        print(f"{symlink_to_delete} deleted successfully !")  # DISPLAY TO USER THAT IT IS UNLINKED IS SUCCESSFULLY
    except Exception:  # JUST IN CASE USER GIVES A NON-EXISTENT FILE, NOTIFYING USER
        print(f"{symlink_to_delete} doesn't exist\nPlease Insert A Valid SymLink")


def display_summary():
    """
    Function to Display a Summary of Linked Files
    Displays the number of Linked Files
    Displays the name of the File
    Path of the Link
    """
    counter = 0  # TO KEEP A COUNTER OF THE NUMBER OF FILES
    output = subprocess.Popen(  # To Find the List of Linked Files
        ["sudo", "find", home, "-type", "l"],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )
    stdout, stderr = output.communicate()  # TO GET THE OUTPUT OF THE CODE
    if stdout.splitlines():  # CHECK IF THERE ARE LINKED FILE IN FIRST PLACE
        for line in stdout.splitlines():  # SPLITTING THE LINES SO WE COULD LOOP OVER THEM
            original_path = subprocess.Popen(
                ["readlink", "-f", line],
                stdout=subprocess.PIPE,
                universal_newlines=True
            )
            origin, stderr = original_path.communicate()  # TO GET THE ORIGINAL PATH OF THE LINKED PATH

            fileName = line.split("/")  # TO GET THE NAME OF THE FILE SPLIT INTO A LIST
            # PRINTING LAST INDEX OF LIST SINCE LAST INDEX IS THE NAME OF FILE
            print(f"Linked File Name is: {fileName[-1]}")
            print(f"{fileName[-1]} is linked to {origin}", end="")
            print(f"Path to {fileName[-1]} is:")
            print(line, end="\n\n")  # PRINTS THE FULL PATH TO THE LINKED FILE
            counter += 1  # INCREMENTING THE COUNTER OF LINKED FILES
        print(f"\nTHE NUMBER OF SYMLINKS AVAILABLE IS {counter}")
    else:
        print("There are 0 Linked Files")


def main():
    """
    FUNCTION TO LIST 4 OPTIONS
    1 -> TO GO TO CREATING A SYMLINK FUNCTION
    2 -> TO GO TO DELETING A SYMLINK FUNCTION
    2 -> TO GO TO SUMMARY FUNCTION
    QUIT -> TO EXIT THE PROGRAM
    """
    user_option = input("Please insert one of the following options:\n1 to add a shortcut\n2 to remove a shortcut\n3 "
                        "to get a summary of shortcuts in the home\nquit to stop execution of the program\n--> ")
    user_option.lower()  # incase someone inserts eXit capital litters for the exit option!!
    if user_option == "1":
        # create shortcut/symbolic link Function
        create_symlink()
    elif user_option == "2":
        # delete shortcut/symbolic link Function
        delete_symlink()
    elif user_option == "3":
        # Display summary function
        display_summary()
    elif user_option == "quit":
        # To stop the execution of the program
        exit()
    else:
        print("Please Insert a valid option")


if __name__ == '__main__':
    os.system("clear")  # TO CLEAR THE SCREEN IN THE  BEGGING OF THE PROGRAM
    while True:
        main()
