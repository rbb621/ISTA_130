import random
def random_color_string():
    color_string = "#"
    letters = "0123456789ABCDEF"
    
    for i in range(6):
        random_letter = letters[random.randrange(16)]
        color_string = color_string + random_letter
        
    return color_string
 

def main():
    print(random_color_string())
    
if __name__ == "__main__":
    main()