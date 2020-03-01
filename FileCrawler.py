# files crawler

import os, os.walk
Count = 0
for root, direc,files in os.walk(d):
          Count = Count + len(files)

print(Count)
