#!/usr/bin/python3
# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
# DATE 2/12/2022
import re

from geoip import geolite2
import os

myAuthlog = open('syslog.log', 'r')  # open the syslog.log for reading

ips_list = []

for line in myAuthlog:
    x = re.search("(\d{1,3}\.){3}\d{1,3}", line)
    if x:
        ips_list.append(x.group())

print(ips_list)



def main():
    # os.system("clear")
    pass


if __name__ == '__main__':
    main()
