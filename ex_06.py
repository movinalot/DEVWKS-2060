"""
ex_06.py

Purpose:
    UCS Manager Multiple VLAN creation example as a transaction
Author:
    John McDonough (jomcdono@cisco.com) github: (@movinalot)
    Cisco Systems, Inc.
"""

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

# Create a Login Handle and Login
HANDLE = UcsHandle("198.18.133.91", "admin", "password")
HANDLE.login()

VLANS = ['200', '300', '400', '500']

# Iterate over the VLANS list instantiating a vlan_mo and adding
# the vlan_mo to the HANDLE. The UCS Python SDK is transactional
# by default.
for vlan in VLANS:
    vlan_mo = FabricVlan(
        parent_mo_or_dn="fabric/lan",
        name="vlan" + vlan,
        id=vlan
        )

    # Add the current instantiated vlan_mo Object to the HANDLE
    # This action does not overwrite previous vlan_mo ojects in
    # the uncommited HANDLE
    HANDLE.add_mo(vlan_mo)

# Commit the HANDLE to add the VLANS to UCS Manager
HANDLE.commit()

# Logout
HANDLE.logout()
