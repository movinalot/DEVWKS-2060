"""
  ex-07.py
"""

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils import comparesyncmo
source_ucs=UcsHandle("198.18.133.91", "admin", "password")
target_ucs=UcsHandle("198.18.134.249", "admin", "password")
source_ucs.login()
target_ucs.login() 

source_ucs_vlans=source_ucs.query_classid("fabricVlan") 
target_ucs_vlans=target_ucs.query_classid("fabricVlan")

difference_vlans=comparesyncmo.compare_ucs_mo(target_ucs_vlans, source_ucs_vlans)

# print the difference to the console
comparesyncmo.write_mo_diff(difference_vlans)

comparesyncmo.sync_ucs_mo(target_ucs, difference_vlans, delete_not_present=True)

source_ucs.logout()
target_ucs.logout()
