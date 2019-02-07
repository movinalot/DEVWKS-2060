"""
ex_08.py

Purpose:
    UCS Manager Python SDK code generation from GUI XML capture
Author:
    John McDonough (jomcdono@cisco.com) github: (@movinalot)
    Cisco Systems, Inc.
"""

from ucsmsdk.utils.converttopython import convert_to_ucs_python

# Windows
convert_to_ucs_python(xml=True, literal_path='C:\\Users\\demouser\\Downloads\\vlan_ops_xmlReq.log')

# Linux
convert_to_ucs_python(xml=True, literal_path='/Users/demouser/Downloads/vlan_ops_xmlReq.log')
