filename = "ricky_berliant.pdf"

# This prints the first four characters. The way I like to think of this is beginning to 4 characters!
until_four = filename[:4]
print("until_four:", until_four)
# rick

# This prints everything except the first four characters. The way I like to think of this is the fourth character to the end!
four_until = filename[4:]
print("four_until:", four_until)
# y_berliant.pdf

# The prints index 1 to index 4. Index 1 is inclusive; that is, index 1 is included in the result! Index 4 is exclusive; that is, index 4 is NOT included in the result!
one_to_four = filename[1:4]
print("one_to_four:", one_to_four)
# ick

# This prints nothing! Python slicing only works if the beginning is smaller than the end.
one_to_four = filename[4:1]
print("one_to_four:", one_to_four)
# prints nothing

# This prints everything EXCEPT the last four characters. 
subtract_four = filename[:-4]
print("subtract_four:", subtract_four)
# ricky_berliant

# This prints JUST the last four characters. 
negative_four = filename[-4:]
print("negative_four:", negative_four)
# .pdf

# Play around with this! If you ever get lost, you can return to this and see what happens when you change things around!
# Try changing filename = 
# Try changing the numbers!

