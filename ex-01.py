"""
  ex-01.py
"""

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91","admin","password")
handle.login()

handle.cookie

blades = handle.query_classid("ComputeBlade")
len(blades)

for blade in blades:
    print blade.dn, blade.serial, blade.model

handle.set_dump_xml()
blades = handle.query_classid("ComputeBlade")
handle.unset_dump_xml()