#!/usr/bin/python3
# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
# DATE 2/12/2022
import re

from geoip import geolite2
import os
import ipaddress

myAuthlog = open('syslog.log', 'r')  # open the syslog.log for reading

ips_list = []
# with open("syslog.log") as f:
#    data = f.read()
#
# address_ipv4 = re.findall(r"\b(\d{1,3}\.){3}\d{1,3}\b", data)
#
# print(address_ipv4)


for line in myAuthlog:  # loop to extract the IP address
    x = re.search("((\d\d?|[01]\d\d|2([0-4]\d|5[0-5]))\.){3}(\d\d?|[01]\d\d|2([0-4]\d|5[0-5]))", line)
    if x:
        ips_list.append(x.group())

ips_set = set(ips_list)  # removes duplicates

for unique_ip in ips_set:
    counter = 0
    for ip in ips_list:
        if ip == unique_ip:
            counter += 1
    if counter >= 10:
        print(f"{unique_ip} is repeated {counter} times")


def main():
    # os.system("clear")
    pass


if __name__ == '__main__':
    main()
