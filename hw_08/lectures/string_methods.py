
#1. captialize()
word = "super mario world"

print(word.capitalize())


#2. casefold()

word = "sTaR fOx"
word_2 = "StAr FoX"

print(word.casefold())
print(word_2.casefold())

#3. center()

word = 'Trump'
print(word.center(20, '!')) 

#4. count()

story = '''92% percent of Republicans believe in God. Only 60% of Democrats do. That's the real divide in America.
           One side believes life is sacred because it’s God-given. The other has forgotten who gives life at all. 
           When you erase God, you erase truth, purpose, and the very meaning of freedom. This isn’t just politics anymore. 
           It’s a spiritual fight for the soul of America. '''
           
print(story.count('God'))


#5. encode()

figure_head = 'Elon Musk'
print(figure_head.encode(encoding='UTF-8', errors='strict'))


#6. endswith()

pokemon = 'Pikachu'

# make sure it matches the exact letter
print(pokemon.endswith('u'))

# capitals don't match with lowercase
print(pokemon.endswith('U'))

# or statement
print(pokemon.endswith(('e','u')))


#7 find()
text: str = 'Remember to comment and subscribe!'
position: int = text.find('comment')
print(position)
print(text[position:])

#8 isdigit()

number = '1140'

print("1140 is" + str(number.isdigit()))