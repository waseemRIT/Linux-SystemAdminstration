#!/usr/bin/python3
# STUDENT: WASEEM QAFFAF
# STUDENT ID: whq8052
# DATE 2/12/2022
import re

from geoip import geolite2
import requests
import re


def get_location(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    return response.get("country_name")


s = r"(%s)" % ("\.".join(['(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'] * 4))
patt = re.compile(s)
fn = "syslog.log"
s = open(fn).read()
i = 0
ip_list = []

while True:
    m = patt.search(s, i)
    if m:
        ip_list.append(m.group(1))
        i = m.end() + 1
    else:
        break

ips_set = set(ip_list)  # removes duplicates

for unique_ip in ips_set:
    counter = 0
    for ip in ip_list:
        if ip == unique_ip:
            counter += 1
    if counter >= 10:
        # print(f"{unique_ip} is repeated {counter} times")
        pass
    counter = 0
print(get_location("162.135.10.255"))


def main():
    # os.system("clear")
    pass


if __name__ == '__main__':
    main()
