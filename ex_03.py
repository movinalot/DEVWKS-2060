"""
ex_03.py

Purpose:
    UCS Manager query return types example
Author:
    John McDonough (jomcdono@cisco.com) github: (@movinalot)
    Cisco Systems, Inc.
"""

# Create a Login HANDLE and Login
from ucsmsdk.ucshandle import UcsHandle
HANDLE = UcsHandle("10.10.20.40", "admin", "password")
HANDLE.login()

# List of Objects Returned
BLADES = HANDLE.query_classid("ComputeBlade")
print(BLADES)

# Single Object Returned
BLADE_BY_DN = HANDLE.query_dn("sys/chassis-1/blade-1")
print(BLADE_BY_DN)

# Dictionary of Object Lists Returned Key is the ClassId
BLADES_AND_CHASSIS = HANDLE.query_classids(
    "ComputeBlade",
    "EquipmentChassis"
    )
print(BLADES_AND_CHASSIS)

# Access each returned Class Objects by the ClassId
print(BLADES_AND_CHASSIS['EquipmentChassis'])
for chassis in BLADES_AND_CHASSIS['EquipmentChassis']:
    print(chassis.dn, chassis.model)

print(BLADES_AND_CHASSIS['ComputeBlade'])
for blade in BLADES_AND_CHASSIS['ComputeBlade']:
    print(blade.dn, blade.model)

# Dictionary of dn as the key and objects as the value
BLADES_AND_CHASSIS = HANDLE.query_dns(
    "sys/chassis-1/blade-1",
    "sys/chassis-2"
    )

print(BLADES_AND_CHASSIS)
print(
    BLADES_AND_CHASSIS['sys/chassis-2'].dn,
    BLADES_AND_CHASSIS['sys/chassis-2'].model
    )
print(
    BLADES_AND_CHASSIS['sys/chassis-1/blade-1'].dn,
    BLADES_AND_CHASSIS['sys/chassis-1/blade-1'].model
    )

# Logout
HANDLE.logout()
