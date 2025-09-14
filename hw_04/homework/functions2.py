import math

def print_word(num, word):

    for i in range(num):
        print(i + 1,'-->', word)
        

'''
The function has two parameters. The first is an integer giving 
the number of minutes it takes for a bacterium to split into 
two new bacteria. 

The second is an integer giving the number of bacterial 
generations to include in the output. 

#

Assume you always begin with a
single bacterium in the dish and every bacterium 
always splits into exactly two bacteria at the end of each time period.
'''

def bacteria(minutes, bacterial):
    
    for i in range(bacterial):
        i += 1
        time_went_by = minutes * i
        bacteria = 2 ** i
        print('after', time_went_by, 'minutes: ', bacteria, 'bacteria')
        


def convert_to_copper(gp,sp, cp):
    total_copper = (gp * 10 * 5) + (sp * 5) + (cp)
    print(gp, 'gp,', sp, 'sp,', cp, 'cp converted to copper is:', total_copper, 'cp')


def convert_from_copper(copper):
    gold_remainder = copper // 50
    remainder = copper % 50
    silver_remainder = remainder // 5
    copper_remainder = remainder % 5
    
    print(copper, 'copper pieces is:', gold_remainder, 'gp,', silver_remainder, 'sp,', copper_remainder, 'cp')
    

def repeat_word(word, row, column):
    for i in range(row):
        print(word * column)
        
def text_triangle(row):
    for i in range(row -1):
        print('X' * (i + 1))
    print('X' * (row))
    

def surface_area_of_cylinder(radius, height):

    height_float = float(height)
    radius_float = float(radius)

    sa = (2 * math.pi * radius_float * height_float) + (2 * math.pi * radius_float**2)


    print('The surface area of a cylinder with radius', radius_float, 'and height', height_float, 'is', sa)
    


def tree_height(distance, length):
    
    height = math.sqrt(length ** 2 - distance ** 2)
    print("Kite string:", length)
    print("Distance:", distance)
    print("Height:", height)

print(tree_height(300, 500))