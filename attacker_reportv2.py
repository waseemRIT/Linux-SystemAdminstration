#!/usr/bin/python3

import os
from datetime import date
import re
from geoip import geolite2

os.system("clear")

today_date_format = date.today()

print("Attacker Report: {}\n".format(today_date_format.strftime("%B %d, %Y")))

print("COUNT\t\tIP ADDRESS\t\tCOUNTRY")

list_of_ips = []  # List to store the IP address

# The regex IP  address format
regex_format = r"(%s)" % ("\.".join(['(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'] * 4))
pattern = re.compile(regex_format)
f_name = "syslog.log"
opened_file = open(f_name).read()
i = 0

while True:
    m = pattern.search(opened_file, i)
    if m:
        list_of_ips.append(m.group(1))
        i = m.end() + 1
    else:
        break

ip_dict = dict()

for ip in list_of_ips:  # to count occurrence of each ip
    if ip in ip_dict.keys():
        ip_dict[ip] += 1
    else:
        ip_dict[ip] = 1
# print(ip_dict)
ip_dict_ten_and_more = dict()

for ip, count in ip_dict.items(): # store ip occurrence of 10+ times
    if count >= 10:
        ip_dict_ten_and_more[ip] = count

# print(ip_dict_ten_and_more)

sorted_ip_count = {}
sorted_keys = sorted(ip_dict_ten_and_more, key=ip_dict_ten_and_more.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_ip_count[w] = ip_dict_ten_and_more[w]

for addr, count in sorted_ip_count.items():
    # print(f"{count:<10}\t{addr:<10}\t{geolite2.lookup(ip):}")
    print(f"{count:<10}\t{addr:<10}")







