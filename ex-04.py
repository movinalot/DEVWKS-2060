"""
  ex-04.py
"""

vars(handle)
dir(UcsHandle)
help(UcsHandle)

from ucsmsdk.ucscoreutils import get_meta_info
meta = get_meta_info(class_id="FabricVlan")
print meta

meta = get_meta_info(class_id="FabricVlan", include_prop=False, show_tree=False)
print meta

meta = get_meta_info(class_id="FabricVlan", include_prop=False, show_tree=True)
print meta