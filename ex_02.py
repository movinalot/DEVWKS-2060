"""
ex_02.py

Purpose:
    UCS Manager query filter example
Author:
    John McDonough (jomcdono@cisco.com) github: (@movinalot)
    Cisco Systems, Inc.
"""

from ucsmsdk.ucshandle import UcsHandle

def show_ucs_object_attributes(ucs_objects, attributes):
    """
      Iterate over objects list displaying attributes from each object
      This function could be used for any object not just computeBlade
    """
    print("  Query results")
    for ucs_object in ucs_objects:
        display_str = ""
        for attribute in attributes:
            display_str += (
                "    " +
                attribute + ": " +
                getattr(ucs_object, attribute) +
                " "
                )
        print(display_str)


# Create a Login HANDLE and Login
HANDLE = UcsHandle("10.10.20.40", "admin", "password")
HANDLE.login()

# Attributes of the UCS Object to display
ATTRS = ["dn", "model", "serial"]

# Query Filters and descriptions
Q_FILTERS = [
    {
        'filter_exp': '(model,"UCSB-[a-zA-Z0-9]*-M4[-a-zA-Z0-9]*", type="re")',
        'filter_des': '"model matches UCSB-[a-zA-Z0-9]*-M4[-a-zA-Z0-9]*"'
    },
    {
        'filter_exp': '(model,"UCSB-B200-M4", type="eq")',
        'filter_des': '"model equals UCSB-B200-M4"'
    },
    {
        'filter_exp': '(model,"UCSB-B200-M4", type="ne")',
        'filter_des': '"model not equal UCSB-B200-M4"'
    },
    {
        'filter_exp': '(model,"ucsB-B200-m4", flag="I")',
        'filter_des': '"model matches ucsB-B200-m4 case insensitive"'
    }
]

# Iterate over the Q_FILTERS dictionary and display the results
for q_filter in Q_FILTERS:
    blades = HANDLE.query_classid(
        "ComputeBlade", filter_str=q_filter['filter_exp']
        )
    print('\nUCS Query for ' + q_filter['filter_des'])
    print("  Number of blades found: " + str(len(blades)))

    if blades:
        show_ucs_object_attributes(blades, ATTRS)

# Logout
HANDLE.logout()
