from mcityoswrapper import McityOSRail
from mcityoswrapper import McityOSIntersections

#print(McityOSRail.get_railcrossings())
print(McityOSIntersections.get_intersection(1))

print(McityOSRail.trigger_railcrossing(1))
