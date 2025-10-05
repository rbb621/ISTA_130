# Let's suppose I have 10 plants. 
x = "length"
print(x)

# My plant is 5 cm tall
x = 5
print(x)

# My plant grew 3 cm
x = x + 3

# My plant grew another 6 cm
x = x + 6

# I have 9 other plants
a = 4
b = 7
c = 1
d = 9
e = 3
f = 1 
g = 4
h = 2
i = 1

# First measurement
a = a + 2
b = b + 2
c = c + 1
d = d + 2
e = e + 9
f = f + 3
g = g + 6
h = h + 5
i = i + 7

# Second measuremnent
b = b + 1
c = c + 2
d = d + 1
e = e + 1
f = f + 1
g = g + 0.5
h = h + 11

# Third measurement
a = a + 3
h = h + 2

myPlants = [a, b, c, d, e, f, g, h, i, x]
mean = sum(myPlants) / len(myPlants)