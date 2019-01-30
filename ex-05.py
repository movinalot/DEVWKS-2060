"""
  ex-05.py
"""

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

fabric_lan_cloud = handle.query_classid("FabricLanCloud")
vlan = FabricVlan(parent_mo_or_dn=fabric_lan_cloud[0],
    name="vlan100",
    id="100")

handle.add_mo(vlan)
handle.commit()
handle.logout()