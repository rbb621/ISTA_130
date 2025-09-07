import math

def angle(x1, y1, z1, x2, y2, z2):
    
    
    
    dot_product = x1 * x2 + y1 * y2 + z1 * z2
    length_u = math.sqrt(x1**2 + y1**2 + z1**2)
    length_v = math.sqrt(x2**2 + y2**2 + z2**2)
    angle = math.acos(dot_product / length_u / length_v)
    return angle * 180 / math.pi

print(angle(1, 0, 0, 1, 0, 1))


