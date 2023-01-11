# Linux-SystemAdminstration

## Description
This is a collection of scripts that are designed to automate some system administration tasks and make the process more efficient. The bundle includes scripts for creating and deleting symbolic links, adding and deleting users, and generating reports on potential attackers.
Each script can be run individually and they are all written in Python.

## Scripts included in the Bundle:
* attacker_report.py: This file is used to analyze a log file "syslog.log" and extract all the IP addresses that are present in it. The script then uses the IP addresses to get the location of the IP address by calling the IPapi service. It then prints a table of IP count and location.

* attacker_reportv2.py: This file is a modified version of the previous file, it uses 'geoip' library to find the location of the IP addresses. It will read the "syslog.log" file for IP addresses, and it will filter the IP's that appear more than 10 times and print the IP count, IP address and the corresponding country where the IP address is located.

* attacker_reportv3.py: this file is also a modified version of the previous file, it uses the IPapi service to find the location of the IP addresses instead of using the geoip library. It will read the "syslog.log" file for IP addresses, and it will filter the IP's that appear more than 10 times and print the IP count, IP address and the corresponding country code where the IP address is located.

* add_user.py: This script is used to add a new user to the system and assigns them a default password. The script prompts the user for the username and checks if the user already exists. If the user does not exist, it creates the user and assigns them a default password. If the user already exists, it informs the user that the user already exists.

### It makes use of the following python modules:
* csv: used to read the users csv file, and get user data
* subprocess: used to run Linux commands for group creation, user creation, and password change
* os: used to run the Linux command to clear the screen when running the program

### The script takes in the following arguments:

* EmployeeID: a unique identifier for the user
* lastName: the last name of the user
* firstName: the first name of the user
* office: the user's office location
* phone: the user's phone number
* Department: the user's department
* group: the group to which the user belongs (default is "office")

It creates a unique username by combining the first letter of the user's first name and the user's last name, and then checks if the username is already in use. If so, it appends a number to the username until it becomes unique. The user is then added to the specified group. The default shell is set to /usr/csh and the user's password is set to 'password'. The password is also set to expire on the first login. Please note that this script requires sudo privileges to run as it modifies the system's user and group settings.

* sym_link.py: This script allows the user to create and delete symbolic links. The script prompts the user for the file path and name of the symbolic link. If the file exists, it creates the symbolic link in the user's home directory. If the file does not exist, it informs the user that the file does not exist. The script also has a function to display a summary of all linked files including their paths and names.

## How to use
Make sure you have python3 installed.
Clone the repository and navigate to the directory where the scripts are located.
Run the script using the command python3 script_name.py
Follow the prompts to complete the task.
Please note that some scripts may require sudo permissions to run.

## Requirements
* Python3
* geoip
* requests (attacker_reportv3)
## Future Enhancements
* Add more functionalities to the scripts
* Add more robust error handling
* Create a menu-driven interface for running the scripts.
## Contact
For any issues or questions regarding the scripts, please contact the developer at whq8052@rit.edu
