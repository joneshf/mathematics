from mathematics import Vector

u = Vector(1, 4, 6)
v = Vector(2, 3, 5)
w = Vector(1, 2)
print u + v
print w + w
print u - v
print u * 5
print 5 * u
print u.dot(u)
print u.dot(v)
print u.cross(u)
print u.cross(v)
print u.mag()
print u[2]