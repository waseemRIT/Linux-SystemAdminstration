#!/usr/bin/python3

# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
# DATE 09/10/2022
import csv
import subprocess
import os

users = []
failed_users = []


def create_user(EmployeeID, lastName, firstName, office, phone, Department, group):
    # creating the initial unique
    unique_user = str(firstName[0]) + lastName
    # check if adding extra digit beside user is required, if yes it will check how much to add and return required user
    username = is_unique_user(unique_user)
    if group == "office":
        subprocess.run(
            f'useradd -m /home/{Department.lower()} -s csh -g {group} -p password -K PASS_MAX_DAYS=0 -c "{office},{phone}" "{username}"',
            stdout=subprocess.PIPE)
    else:
        subprocess.run(
            f'useradd -m /home/{Department.lower()} -g {group} -p password -K PASS_MAX_DAYS=0 -c "{office},{phone}" "{username}"',
            stdout=subprocess.PIPE)


def initializing_data():
    with open(r'linux_users.csv', 'r') as users:  # opening the file
        reader = csv.reader(users)
        next(reader)  # skipping first row

        for i, row in enumerate(reader, start=1):
            if '' in row[:7]:
                failed_users.append(f"user in line {i} with ID {row[0]}, couldn't be added due to missing information")
                continue
            # EXTRACTING USERS DATA
            EmployeeID = row[0]
            LastName = row[1]
            FirstName = row[2]
            Office = row[3]
            Phone = row[4]
            Department = row[5]
            Group = row[6]
            # print(EmployeeID, LastName, FirstName, Office, Phone, Department, Group)
            # PASSING DATA TO THE ADDING USER FUNCTION TO ADD THEM!
            create_user(EmployeeID, LastName, FirstName, Office, Phone, Department, Group)


def notify_missing_users():
    for i in failed_users:
        print(i)


def is_unique_user(unique_user):
    counter = 0  # check how many times user was repeated
    users.append(unique_user)
    for i in users:
        if unique_user in i:
            counter += 1

    if counter == 1:
        return unique_user
    else:
        return unique_user + str(counter - 1)


def main():
    # os.system("clear")  # CLEAR ALL PAST OUTPUTS
    # initializing_data()
    # print("----------------")
    # notify_missing_users()
    pass


if __name__ == '__main__':
    main()
