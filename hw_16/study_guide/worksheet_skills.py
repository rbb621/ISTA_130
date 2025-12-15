def get_class(units):
    '''
    This only works because of the
    returns!!!  For instance, wouldn't
    work if we were printing.  Why not?
    '''
    if units < 30:
        return 'Freshman'
    if units < 60:
        return 'Sophomore'
    if units < 90:
        return 'Junior'
    return 'Senior'
    
print('Should be "Sophomore":', get_class(59))
print('*' * 25 + '\n')
    
def get_class_safely(units):
    if units < 30:
        return 'Freshman'
    elif units < 60:
        return 'Sophomore'
    elif units < 90:
        return 'Junior'
    else:
        return 'Senior'
    
def uppers(string):
    result = ''
    for ch in string:
        if ch.isupper():
            result += ch
    return result
    
print('Should be ROCKET:', uppers('RabcOCdefKETxyz'))
print('*' * 25 + '\n')
    
def add_lists(l1, l2):
    result = []
    for i in range(len(l1)):
        result.append(l1[i] + l2[i])
    return result
    
l1 = ['abc', 77, True]
l2 = ['def', 77, False]
print('Should be ["abcdef", 154, 1]:', add_lists(l1, l2))
print('*' * 25 + '\n')
    
def add_lists2(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]

print('Should be ["abcdef", 154, 1]:', add_lists(l1, l2))
print('*' * 25 + '\n')
    
import random
die1 = 5
die2 = 5
while die1 == die2:
    print('die1:', die1)
    print('die2:', die2)
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
print('die1:', die1)
print('die2:', die2)
print('*' * 25 + '\n')

die1 = 5
die2 = 5
while True:
    print('die1:', die1)
    print('die2:', die2)
    if die1 != die2:
        break
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
print('*' * 25 + '\n')

astring = " I heart Rocket !!!"
print('$'.join(astring.split()))
print(astring[3:8])
print(astring[::2])
print(astring.upper().split('T'))
print('*' * 25 + '\n')


def letter_dict(fname):
    result = {}
    for line in open(fname):
        line = line.split()
        for i in range(len(line)):
            line[i] = line[i].lower()
        for word in line:
            if word[0] in result:
                if word not in result[word[0]]:
                    result[word[0]].append(word)
                # else do nothing
            else:
                result[word[0]] = [word]
    return result
    
"""
Should be:
{
"i": ["i", "is"],
"h": ["heart", "he"],
"r": ["rocket.", "really,", "really", "radical."]
}
"""
print(letter_dict('rocket.txt'))
print('*' * 25 + '\n')
    
class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
      
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * self.width + 2 * self.height
        
    def __repr__(self):
        result = 'Width: ' + str(self.width) + '\n'
        result += 'Height: ' + str(self.height) + '\n'
        result += 'Area: ' + str(self.area()) + '\n'
        result += 'Perimeter: ' + str(self.perimeter()) + '\n'
        return result
    
r = Rectangle(30, 40)    
print(r)
    
    