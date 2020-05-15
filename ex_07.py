"""
ex_07.py

Purpose:
    UCS Manager Compare and Sync
Author:
    John McDonough (jomcdono@cisco.com) github: (@movinalot)
    Cisco Systems, Inc.
"""

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils import comparesyncmo

# Login to a SOURCE UCS and a TARGET UCS
SOURCE_UCS = UcsHandle("10.10.20.40", "admin", "password")
TARGET_UCS = UcsHandle("10.10.20.50", "admin", "password")
SOURCE_UCS.login()
TARGET_UCS.login()

# Query the SOURCE UCS VLANS and the TARGET UCS VLANS
SOURCE_UCS_VLANS = SOURCE_UCS.query_classid("fabricVlan")
TARGET_UCS_VLANS = TARGET_UCS.query_classid("fabricVlan")

# Compare the TARGET VLANS with the SOURCE VLANS
DIFFERENCE_VLANS = comparesyncmo.compare_ucs_mo(TARGET_UCS_VLANS, SOURCE_UCS_VLANS)

# Display the difference
comparesyncmo.write_mo_diff(DIFFERENCE_VLANS)

# Sync - apply the difference to the TARGET_UCS, remove from the
# TARGET_UCS any objects that are not present on the SOURCE_UCS
# This action is not done through the HANDLE, the commit() is implicit
comparesyncmo.sync_ucs_mo(TARGET_UCS, DIFFERENCE_VLANS, delete_not_present=True)

# Logout
SOURCE_UCS.logout()
TARGET_UCS.logout()
