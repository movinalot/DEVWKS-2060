"""
  ex-02.py
"""
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91","admin","password")
handle.login()

filter_exp='(model,"UCSB-B200-M4")'
blades = handle.query_classid("ComputeBlade",filter_str=filter_exp)
len(blades)

filter_exp='(model,"UCSB-B200-M4", type="eq")'
blades = handle.query_classid("ComputeBlade",filter_str=filter_exp)
len(blades)

filter_exp='(model,"UCSB-B200-M4", type="ne")'
blades = handle.query_classid("ComputeBlade",filter_str=filter_exp)
len(blades)

filter_exp='(model,"ucsB-B200-m4", flag="I")'
blades = handle.query_classid("ComputeBlade",filter_str=filter_exp)
len(blades)

for blade in blades:
    print blade.dn, blade.model

handle.logout()