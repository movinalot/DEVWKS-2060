"""
ex_01.py

Purpose:
    UCS Manager connect and query example
Author:
    John McDonough (jomcdono@cisco.com) github: (@movinalot)
    Cisco Systems, Inc.
"""

# Create a Login HANDLE and Login
from ucsmsdk.ucshandle import UcsHandle
HANDLE = UcsHandle("198.18.133.91", "admin", "password")
HANDLE.login()

# Print HANDLE 'cookie' attribute
print("cookie: " + HANDLE.cookie)

# Query compute blades and print number of objects returned
# Queries are executed with a HANDLE member method
BLADES = HANDLE.query_classid("ComputeBlade")
print("Number of blades found: " + str(len(BLADES)))

# Iterate over blades list displaying attributes from each object
for blade in BLADES:
    print(blade.dn, blade.serial, blade.model)

# Turn on UCS XML API view to dump XML that is sent and recieved
HANDLE.set_dump_xml()
BLADES = HANDLE.query_classid("ComputeBlade")
HANDLE.unset_dump_xml()

# Logout
HANDLE.logout()
