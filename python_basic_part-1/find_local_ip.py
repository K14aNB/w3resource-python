"""
Task
----
Write a python program to find local IP addresses using Python's stdlib.
"""

from socket import gethostname, gethostbyname_ex

hostname = gethostname()

ip_addrs = gethostbyname_ex(hostname)[2]

filtered_ip_addrs = [ip for ip in ip_addrs if not ip.startswith("127.")]

print(filtered_ip_addrs)
