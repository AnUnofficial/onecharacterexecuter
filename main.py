from os import listdir
from sys import exit
fs = []
for i in listdir("."):
 match i.endswith("."):
  case True:
   fs.append(i)
for j in fs:
 c = open(j, "r").read().replace("\n", "")
 for k in c:
  match k:
   case _:
    exit