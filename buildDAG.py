# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
#!/usr/local/bin/python



# please use following code to run the python file.
# cat subcatstest.txt | python #.py
import sys
import re
parent=[]
child=[]
for line in sys.stdin:
    words=line.split(",")
    pattern = re.compile(r'[,\.\?\"\!:;\)\(]')
    apostrophe = re.compile(r'[\'\\]')
    pad = words[1].replace('_',' ')
    pad0=re.sub(pattern,"",re.sub(apostrophe,"",pad))
    parent.append(pad0.upper())
    if words[2].find('\\n') == -1:
        child.append(re.sub(pattern,"",re.sub(apostrophe,"",words[2])))
    else:
        current = words[2].split('\\n')
        child.append(re.sub(pattern,"",re.sub(apostrophe,"",current[-1])))
print(parent)
