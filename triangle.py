''' module for triangle '''

def area(x,y,z):
    s=(x+y+z)/2
    ar=s*(s-x)*(s-y)*(s-z)
    return ar**0.5
def perimeter(x,y,z):
    return x+y+z
