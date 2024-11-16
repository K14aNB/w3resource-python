"""
Task
----
Write a python program to print a URL's content to console.
"""

from http.client import HTTPConnection
from requests import get

# Method 1

conn = HTTPConnection("google.com")

conn.request("GET", "/")

result = conn.getresponse()

print(result.read())


# Method 2

data = get("https://www.google.com")

print(data.text)
