"""
ex_04.py

Purpose:
    UCS Manager metadata example
Author:
    John McDonough (jomcdono@cisco.com) github: (@movinalot)
    Cisco Systems, Inc.
"""

from ucsmsdk.ucscoreutils import get_meta_info

# Create a Login Handle and Login
from ucsmsdk.ucshandle import UcsHandle
HANDLE = UcsHandle("10.10.20.40", "admin", "password")
HANDLE.login()

# What is in the HANDLE
vars(HANDLE)

# What capabilities does the HANDLE have
dir(UcsHandle)

# How can the capabilties of the HANDLE be used
help(UcsHandle)

# Meta data variations for containment hierarcy and object properties
print("\nMetadata: include_prop=False, show_tree=True")
print(get_meta_info(class_id="FabricVlan", include_prop=False, show_tree=True))

print("\nMetadata: include_prop=True, show_tree=False")
print(get_meta_info(class_id="FabricVlan", include_prop=True, show_tree=False))

# Query Metadata information, include_prop and show_tree are True by default
META = get_meta_info(class_id="FabricVlan")

# Drill into the "id" attribute
print("\nMetadata: vars")
print(vars(META.props['id']))
print("\nMetadata: id atttribute")
print(META.props['id'])

# The "id" restriction object and "range_val" attribute
print("FabricVlan:id - range_val: ", META.props['id'].restriction.range_val)

# The "name" restriction object and "pattern" attribute
print("FabricVlan:name - pattern: ", META.props['name'].restriction.pattern)

# The "sharing" restriction object and "value_set" attribute
print("FabricVlan:sharing - value_set: ", META.props['sharing'].restriction.value_set)

# Logout
HANDLE.logout()
