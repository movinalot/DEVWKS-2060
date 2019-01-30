"""
  ex-03.py
"""

# List of Objects Returned
blades = handle.query_classid("ComputeBlade")

# Single Object Returned
blade_by_dn = handle.query_dn("sys/chassis-1/blade-2")
print blade_by_dn

# Dictionary of Object Lists Returned
blades_and_chassis = handle.query_classids("ComputeBlade","EquipmentChassis")
print blades_and_chassis

print blades_and_chassis['ComputeBlade']
for blade in blades_and_chassis['ComputeBlade']:
    print blade.dn

# Dictionary of Objects Returned
blade_and_chassis = handle.query_dns("sys/chassis-1/blade-1","sys/chassis-2")
print blade_and_chassis
print blade_and_chassis['sys/chassis-3/blade-1'].dn