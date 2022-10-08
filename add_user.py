#!/usr/bin/python3

# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
import csv
import subprocess

users = []
failed_users = []
users_to_skip = []


def create_user(EmployeeID, lastName, firstName, Office, Phone, Department, group):
    # creating the initial unique
    unique_user = str(firstName[0]) + lastName
    # check if adding extra digit beside user is required, if yes it will check how much to add and return required user
    username = is_unique_user(unique_user)
    if group == "office":
        subprocess.run(f"useradd -m /home/{Department.lower()} -s csh -G {group} -p password -K PASS_MAX_DAYS=0 {username}",
                       stdout=subprocess.PIPE)
    else:
        subprocess.run(f"useradd -m /home/{Department.lower()} -G {group} -p password -K PASS_MAX_DAYS=0 {username}",
                       stdout=subprocess.PIPE)


def initializing_data():
    with open(r'linux_users.csv', 'r') as users:  # opening the file
        reader = csv.reader(users)
        next(reader)  # skipping first row

        for i, row in enumerate(reader, start=1):
            if '' in row[:7]:
                failed_users.append(f"user in line {i}, couldn't be added due to missing information")
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
    unique_que = []
    for i in range(len(users) - 1):
        if unique_user in users[i]:
            unique_que.append(unique_user)

    if len(unique_user) == 0:  # means first time getting the user, appends to users
        users.append(unique_user)
        return unique_user
    elif len(unique_que) == 1:  # means user already exist so add 1
        users.append(unique_user)
        return unique_user + "1"
    else: # here user already have a number so easy to increament
        users.append(unique_user)
        last_seen = unique_que.pop()[-1]
        return unique_user + str(int(last_seen) + 1)


def main():
    # initializing_data()
    # print("----------------")
    # notify_missing_users()
    x = [1, 2, 3, 4, 5]

    print(len(x))


if __name__ == '__main__':
    main()
