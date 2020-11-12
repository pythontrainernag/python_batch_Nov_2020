"""Condition? based on condition either we will execute/skip few lines 
condition? If use either boolean directly or relational operator between any similiar 3>2 --> true
 8 -----> internally 8 will be converted as boolean 
Any statement which gives outcome as a boolean can be condition
"""

"""
oust1
oust2
oust3
oust4
if condition:
  st1
  st2
  |
  |
  stn
oust5
\
\
oustn
"""

"""
oust1
oust2
oust3
oust4
if condition:
  st1
    st2 #invalid syntax
  |
  |
  stn
oust5
\
\
oustn
"""


"""
oust1
oust2
oust3
oust4
if condition1:
  st1
  st2
  |
  |
  stn
oust5
oust6
oust7
if condition2:
    st1
    st2
    |
    |
    stn
oust8
\
\
oustn
"""