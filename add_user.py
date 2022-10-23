#!/usr/bin/python3

# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
# DATE 09/10/2022
import csv  # used to read the users csv file, and get user data
import subprocess  # used to run the linux commands: group creation, user creation, password change
import os  # used to run linux command to clear the screen when running the program

users = []  # used to check duplicate users


def create_user(EmployeeID, lastName, firstName, office, phone, Department, group):
    """
    Function to create a unique user in Linux
    """
    # creating the initial unique
    unique_user = str(firstName[0]) + lastName
    unique_user = remove_special_char(unique_user)
    # check if adding extra digit beside user is required, if yes it will check how much to add and return required user
    username = is_unique_user(unique_user)
    if group == "office":  # check's such that it would add the csh shell to user
        group_command = ["sudo", "groupadd", "-f", f"office"]
        group_maker = subprocess.run(group_command, stdout=subprocess.PIPE)  # create group
        if group_maker.returncode == 0:
            user_command = ["sudo", "useradd", "-u", f"{EmployeeID}", "-m", "-d",
                            f"/home/{Department.lower()}/{username}", "-g",
                            "office", "-s", "/usr/csh", "-c", f'"{firstName} {lastName}, {office},{phone}"', "-p",
                            "password", f"{username}"]
            # create user if group got created
            user_maker = subprocess.run(
                user_command,
                stdout=subprocess.PIPE)
            if user_maker.returncode == 0:
                print("DEFAULT PASSWORD IS password")
                password_command = ["sudo", "passwd", "-e", f"{username}"]
                # expire the user's password
                passwd_expire = subprocess.run(password_command, stdout=subprocess.PIPE)
                if passwd_expire.returncode == 0:
                    print(f"User {EmployeeID} successfully created!")
    elif group == '' or group == 'unlisted':
        default_user_group_command = ["sudo", "useradd", "-u", f"{EmployeeID}", "-m", "-d",
                                      f"/home/{Department.lower()}/{username}", "-c",
                                      f'"{firstName} {lastName}, {office},{phone}"', "-p", "password", f"{username}"]
        # Create user with default group
        user_maker = subprocess.run(
            default_user_group_command,
            stdout=subprocess.PIPE)
        if user_maker.returncode == 0:
            print("DEFAULT PASSWORD IS password")
            password_command = ["sudo", "passwd", "-e", f"{username}"]
            # expire the user's password
            passwd_expire = subprocess.run(password_command, stdout=subprocess.PIPE)
            if passwd_expire.returncode == 0:
                print(f"User {EmployeeID} successfully created!")
    else:
        group_command = ["sudo", "groupadd", "-f", f"{group}"]
        group_maker = subprocess.run(group_command, stdout=subprocess.PIPE)  # create group
        if group_maker.returncode == 0:
            user_command = ["sudo", "useradd", "-u", f"{EmployeeID}", "-m", "-d",
                            f"/home/{Department.lower()}/{username}", "-g",
                            f"{group}", "-c", f'"{firstName} {lastName}, {office},{phone}"', "-p", "password",
                            f"{username}"]
            # create user if group got created
            user_maker = subprocess.run(
                user_command,
                stdout=subprocess.PIPE)
            if user_maker.returncode == 0:
                password_command = ["sudo", "passwd", "-e", f"{username}"]
                print("DEFAULT PASSWORD IS password")
                # expire the user's password
                passwd_expire = subprocess.run(password_command, stdout=subprocess.PIPE)
                if passwd_expire.returncode == 0:
                    print(f"User {EmployeeID} successfully created!")


def getData_createUser():
    """
    Function to get data from csv file,
    Check for missing cells
    Check if Group is missing
    Passes Data to create_user()
    """
    with open(r'linux_users.csv', 'r') as users:  # opening the file
        reader = csv.reader(users)  # Initializing the reading from CSV format
        next(reader)  # skipping first row -> the labels row

        for i, row in enumerate(reader, start=1):  # looping through the rows in the csv file
            # print(row)
            if '' in row[:6]:  # check if any of ID to Department cells are missing
                print(f"user in line {i}, User account was not added due to missing "
                      f"information!")  # to notify the users of missing data
                continue  # If anything is missing skip the user
            elif '' == row[6] or is_group_not_valid(groupName=group):  # check if user is missing a group or invalid
                # notify user the group is missing or group is invalid
                print("Group is Missing or Invalid, Default Group Will Be Used!")
                row[6] = "default" # setting group to default -> if groups is missing, or if group is invalid
            # EXTRACTING USERS DATA
            employee_id = row[0]
            last_name = row[1]
            first_name = row[2]
            office = row[3]
            phone = row[4]
            department = row[5]
            group = row[6]
            if is_name_not_valid(last_name, last_name):
                print(f'user in line {i}, User Account has invalid name!')
                continue
            # PASSING DATA TO THE ADDING USER FUNCTION TO ADD THEM!
            create_user(employee_id, last_name, first_name, office, phone, department, group)


def is_group_not_valid(groupName: str):
    for char in groupName:  # check each char in the group name if a number exist then return True
        if char.isnumeric():
            return True


def is_name_not_valid(firstname: str, lastname: str):
    """
        check if the name fields are letters and not numbers
        If the name includes numbers then it's invalid
        If name is Invalid
            return True
    """
    for char in firstname:  # check each char in the first name if a number exist then return True
        if char.isnumeric():
            return True
    for char in lastname:
        if char.isnumeric():  # check each char in the last name if a number exist then return True
            return True


def remove_special_char(name: str):
    """
       returns a string with no special characters
    """
    # Looping over the name and removing all special chars
    new_str = "".join(char for char in name if char.isalpha())
    return new_str


def is_unique_user(unique_user):
    """
    Function to check uniqueness of the username
    """
    counter = 0  # check how many times user was repeated
    users.append(unique_user)
    for i in users:  # checks if there is an occurrence of the user
        if unique_user in i:
            counter += 1

    if counter == 1:
        # if no occurrence return as is
        return unique_user
    else:
        # if there is an occurrence calculation was made and correct number will be added
        return unique_user + str(counter - 1)


def main():
    getData_createUser()  # Function to create the users
    print("----------------")


if __name__ == '__main__':
    # Clear Screen
    os.system("clear")  # CLEAR ALL PAST OUTPUTS
    # run the program
    main()
