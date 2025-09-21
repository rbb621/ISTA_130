def double_str(word):
    
    new_string = ""
    for i in range(len(word)):
        new_string += word[i] * 2
        
    return new_string
        
def triple_str(word):
    new_str = ""
    
    for i in range(len(word)):
        new_str += word[i] * 3
        
    return new_str

def quad_str(text):
    es = "" 
    
    for i in range(len(text)):
        es += text[i] * 4
    return es

def main():
    print(double_str('HeroOfTime'))
    print(triple_str("Rent-a-Girlfriend"))
    print(quad_str("Giggity Goo"))

    
if __name__ == '__main__':
    main()