# Linux-SystemAdminstration

The system_administration repository contains a collection of scripts designed to assist with various system administration tasks. The following is a brief overview of each script contained in this repository:

* add_user.py: This script allows for the creation of a new user on a Linux-based system, including setting the user's password and adding them to specific groups.

* attacker_reportv2.py and attacker_reportv3.py: These scripts parse through a log file, in this case a syslog.log file, and looks for IP addresses that occur 10 or more times. The script then sorts the IP addresses by count, and attacker_reportv2.py uses the geoip library to look up the country of origin for each IP address. attacker_reportv3.py uses the requests library to hit the "https://ipapi.co/{addr}/json" to resolve country of origin instead of geoip

* ping_test.py: This script allows for testing of network connectivity to various IP addresses or hostnames. The user can select to test the connectivity of their default gateway, the connectivity of a hard-coded RIT DNS server, or the connectivity of a hostname/IP address of their choice after resolving it.

* sym_link.py: This script allows the user to create or delete symbolic links (symlinks) on a Linux-based system. Symlinks allow for a file or directory to be accessed at multiple locations without having to duplicate the file or directory. User can create symlinks for a file, and delete symlinks if the file no longer required.

* ping_test.py : this script allows the user to check the network connectivity for a specific IP address, and it also provides the options to check the connectivity for the default gateway and RIT DNS server. The script uses the os library to execute ping commands and subprocess library to run shell commands and socket library to resolve DNS.

Please note that these scripts are designed to be run on a Linux-based system and may not work as expected on other operating systems. Additionally, some scripts may require additional libraries to be installed.
