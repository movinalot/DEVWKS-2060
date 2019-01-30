"""
  ex-02.py
"""

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