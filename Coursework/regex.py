			# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:18:13 2019

@author: zahmed
"""

'''
Identifiers
\d any number
\D anything but a number
\s space
\S not a space
\w any character
\W anything but a character
.  any character but \n
\b white space around words
\. full stop

Modifiers
{m,n} range of m to n
? match 0 or 1 
* match 0 or more
+ match 1 or more 
$ match end of the string
^ match start of the string
| or
[] range or variance
{x} expecting x amount

White Space Characters

\n new line
\s space
\t tab
\e escape
\f from feed
\r return

Dont Forget

. * ^ $ + [] () {} | \ are all special characters

Attributes

group() return string matched by the re
start() return the starting position of the match
end()   return the end position of the match
span()  return a tuple containing the (start,end) position of the match
    
'''

import re
import numpy as np
file=open('CV_Zeeshan_Ahmed_2018.txt', 'r')
lines=file.readlines()
lines_str=str(lines)
lines_clean=lines_str.strip('\n')

term=re.compile('NIST')
x=term.findall(lines_str) 
#print(x.group())