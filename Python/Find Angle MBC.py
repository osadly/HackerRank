import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
ab=int(input())
bc=int(input())

#print(ab,bc)

angl = (math.atan(ab/bc)) * (180/math.pi) 

angl = int(round(angl))

print("{}\u00b0".format(angl))

#print("{}\u00bo".format(angl))

#print()