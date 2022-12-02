#!/usr/bin/python3
# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
# DATE 2/12/2022

# Importing required libraries
import requests  # used to get the location of the IP address
import re  # used to extract the IP addresses
import os  # used to clear the screen
from datetime import date  # used to get today's date


def date_of_day():
    """
    Function to get the date of the day
    Using the date library
    """

    today = date.today()  # Extracting today's date
    print(f'Attacker Report: {today.strftime("%B %d, %Y")}\n')  # Formatting Today's Date Output


def getLocation(ip_address):
    """
    Function to request the Location of the IP address
    From the ipapi website
    """
    # response stores json values that include information about the IP ADDRESS
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    return response.get("country_code")  # extracting the country code from the Json Values


def main():
    # clear screen
    os.system("clear")

    # Print Today's Date
    date_of_day()

    # Printing Headers
    print("COUNT\t\tIP ADDRESS\t\tCOUNTRY")

    ip_list = []  # List to store the IP address

    # The regex IP  address format
    regex_format = r"(%s)" % ("\.".join(['(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'] * 4))
    pattern = re.compile(regex_format)  # pattern of the regex
    file_name = "syslog.log"  # file name
    opened_file = open(file_name).read()  # opening the file
    i = 0  # index

    while True:  # Extracting the IP addresses and adding them to the ips list
        m = pattern.search(opened_file, i)
        if m:
            ip_list.append(m.group(1))
            i = m.end() + 1
        else:
            break

    ips_set = set(ip_list)  # removes duplicates

    ip_dict = dict()  # dictionary to add the ip address in

    for unique_ip in ips_set:  # used to count the number of occurrences for each ip and store them in the dictionary
        counter = 0
        for ip in ip_list:
            if ip == unique_ip:
                counter += 1
        if counter >= 10:
            ip_dict[unique_ip] = counter

    # used to sort the counters by values
    ip_dict = dict(sorted(ip_dict.items(), key=lambda item: item[1]))

    # loop to print the table of ip count and location
    for ip, count in ip_dict.items():
        print(f"{count:5} {' ':5} {ip:20} {getLocation(ip):15}")


if __name__ == '__main__':
    # Calling the Main Function
    main()
