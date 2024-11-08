#Mohamed Boudabbous
#300376202
from math import sqrt
def surface_triangle (ca,cb,cd):
    p=ca+cb+cd
    s=sqrt(p*(p-2*ca)*(p-2*cb)*(p-2*cd))/4
    print ("la surface du triangle est",s)
surface_triangle (3,4,5)
surface_triangle (7,8,9)
surface_triangle (10,11,13)
    
