#!/usr/bin/python3


import os
import sys
import time
from collections import defaultdict
from geoip import geolite2
# clear the screen
os.system('clear')

# current time
now = time.strftime("%c") # %c is the format for the current time

print("Attacker Report - ", now)
failed= defaultdict(int) # create a dictionary to store the failed login attempts
with open('syslog.log', 'r') as f: # open the syslog file
    data=f.readlines() # read the file
    # print(data)
    for line in data: # loop through the file
        line=line.strip() # remove the newline character
        if 'Failed password for root from'  in line:
            # if the line contains the string 'Failed password for root from
            # #store the IP address if it is not already in the dictionary else increment the count
            ip=line.split(' ')[10] # split the line and get the IP address
            # print(ip)
            failed[ip]+=1 # increment the count
        elif 'Failed password for invalid user' in line: # if the line contains the string 'Failed password for invalid user'
            # print(line)
            ip=line.split('from')[1].split('port')[0].strip() # split the line and get the IP address
            # print(ip)
            failed[ip]+=1
# keep only attackers with more than 10 failed attempts
failed={k:v for k,v in failed.items() if v>=10}
failed=sorted(failed.items(), key=lambda x: x[1]) # sort the dictionary by the value
print("COUNT\t\t\tIP ADDRESS\t\tCOUNTRY")
for i in failed:
    country=geolite2.lookup(i[0]) # get the country of the IP address
    if country is not None:
        if len(i[0]) < 8: # if the IP address is less than 8 characters
            print(str(i[1]) + "\t\t\t" + i[0] + "\t\t\t" + country.country) # print the count, IP address and country
        elif len(i[0]) < 16: # if the IP address is less than 16 characters
            print(str(i[1]) + "\t\t\t" + i[0] + "\t\t" + country.country) # print the count, IP address and country