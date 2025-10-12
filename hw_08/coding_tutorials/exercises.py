# 🧩 Level 1 — Warm-Up (Simple Slicing & Access)

# ✅ Goal: Get comfortable with indexing and slicing.

# 1️⃣ Write a function first_two(string) that returns the first two characters.
# 👉 Example: "hello" → "he"

# 2️⃣ Write a function last_char(string) that returns only the last character.
# 👉 "Mewtwo" → "o"

# 3️⃣ Write a function middle_char(string) that returns the middle character (assume the length is odd).
# 👉 "Pikachu" → "k"

# 4️⃣ Write a function skip_three(string) that returns every third character.
# 👉 "Naruto" → "nu"


def first_two(string):
    return string[:2]

def last_char(string):
    return string[5:]

def middle_char_odd(string):
    middle = len(string) // 2
    return string[middle]

def middle_char_even(string):
    middle = len(string) // 2
    
    if middle % 2 != 0:
        string[middle]
    else:
        return string[middle -1: middle + 1]
    
def skip_three(string):
    return string[::3]


# 🧠 Level 2 — Traversal & Building Strings

# ✅ Goal: Use loops and conditionals.

# 5️⃣ Write a function replace_spaces(string) that returns the string with all spaces replaced by underscores _.
# 👉 "Genshin Impact" → "Genshin_Impact"

# 6️⃣ Write a function count_vowels(string) that counts how many vowels are in the string.
# 👉 "Zelda" → 2

# 7️⃣ Write a function double_letters(string) that returns a new string with every letter repeated twice.
# 👉 "Go" → "GGoo"

# 8️⃣ Write a function remove_vowels(string) that removes all vowels (like you just practiced).
# 👉 "Stellar Blade" → "Stllr Bld"



def replace_spaces(string):
    return string.replace(' ', "_")

# TIP
# Instead use return string.replace(' ', '_')


def count_vowels(string):
    num_vowels = 0
    vowels = 'aeiouAEIOU'
    for char in string:
        if char in vowels:
           num_vowels = num_vowels + 1
    return num_vowels        
    



def double_letters(string):
    new_str = ""
    for i in string:
        new_str += i * 2
    return new_str

    # Instead of new_str = new_str + i * 2
    # Do new_str += i * 2


def remove_vowels(string):
    new_str = ''
    vowels = 'aeiouAEIOU'
    
    for char in string:
        if char not in vowels:
            new_str += char            
    return new_str

def main():
    # Level 1
    print(first_two('hello'))
    print(last_char('Mewtwo'))
    print(middle_char_odd('Pikachu'))
    print(middle_char_even('Ashes'))
    print(skip_three('Naruto'))
    
    # Level 2
    print(replace_spaces('Genshin Impact'))
    print(count_vowels('Zelda'))
    print(double_letters('Go'))
    print(remove_vowels('Stellar Blade'))
    
    # Level 3
    
if __name__ == '__main__':
    main()