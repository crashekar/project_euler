class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

def area( A, B, C):
    area = (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y))/2.0
    return abs(area)

f = open("triangles.txt", 'r')
d = Point(0.0, 0.0)
number = 0
for value  in f:
    (x1,y1,x2,y2,x3,y3) = value.split(',')
    a = Point(float(x1), float(y1))
    b = Point(float(x2), float(y2))
    c = Point(float(x3), float(y3))
    total = area(a, b, c)
    x1 = area(a,b,d)
    x2 =  area(a,d,c)
    x3 =  area(d,b,c)
    if (x1 + x2 + x3) == total:
        print "contains"
        number = number + 1
    else:
        print "Does not contain"

print number
