'''
In-class examples and solutions to worksheet.
'''

def add_elements(list1, list2):
    '''
    This function takes two list arguments (corresponding
    parameters are list1 and list2) and returns a 
    new list. Each element in the new list is the sum of 
    the elements at the same position in the arguments.  
    Assume the lists are the same length.
    '''
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

def underscored(string):
    result = ''
    for ch in string:
        if ch.isupper():
            result += '_' + ch.lower()
        else:
            result += ch
    return result
    
def underscored2(camel_str):
    '''
    This function takes a string argument (parameter name is
    camel_str) in camelCase ('aStringThatLooksLikeThis'), and 
    returns the string converted into python's convention for 
    variables ('a_string_that_looks_like_this'). 
    '''
    i = 0
    while i < len(camel_str):
        if camel_str[i].isupper():
            camel_str = camel_str.replace(camel_str[i], '_' +
                        camel_str[i].lower())
        i += 1
    return camel_str

def split(string, delim):
    '''
    This function takes a string and a character and
    returns a list of the words in the string delimited
    by the character.
    '''
    result = []
    while delim in string:
        pos = string.find(delim)
        result.append(string[:pos])
        string = string[pos + 1:]
    result.append(string)
    return result
    
def join(lst, sep):
    '''
    This function takes a list of strings and a string
    separator and returns a string consisting of the
    strings in the list separated by the separator.
    '''
    if not lst:
        return ''
    result = ''
    for i in range(len(lst) - 1):
        result += lst[i] + sep
    return result + lst[-1]
    
def main():
    lst = ['Arizona', 'California', 'New Mexico']
    print(lst)
    lst.append('Utah')
    print(lst)
    lst.insert(0, 'Oregon')
    print(lst)
    for i in range(len(lst)):
        lst[i] = lst[i].upper()
    print(lst)
    i = 0
    while i < len(lst):
        lst[i] = lst[i].lower()
        i += 1
    print(lst)
    lst.pop(0)
    print(lst) 
    lst.pop()
    print(lst)

    ''' Test the functions. '''
    list1 = ["Quail", True, 13]
    list2 = [" eaten by coyote", 24.5, 42]
    print(add_elements(list1, list2))
    print('-' * 25)
    print(underscored("camelStringExample"))
    print(underscored2("camelStringExample"))
    print('-' * 25)
    print(split('I heart Rocket!', ' '))
    print(split('I heart Rocket!', 'e'))
    print(join(['I', 'heart', 'Rocket!'], ' '))
    print(join(['I', 'heart', 'Rocket!'], '--'))
    
if __name__ == "__main__":
    main()