import sys
localitation = sys.path
print(localitation)
for i in localitation:
    print(i)
    

import calendar

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
isitleap = calendar.isleap(2036)
print(isitleap)