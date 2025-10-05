# Let's suppose I have 10 plants. 
x = "length"
print(x)

# My plant is 5 cm tall
x = 5
print(x)

# My plant grew 3 cm
x1 = x + 3

# My plant grew another 6 cm
x2 = x1 + 6

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
a1 = a + 2
b1 = b + 2
c1 = c + 1
d1 = d + 2
e1 = e + 9
f1 = f + 3
g1 = g + 6
h1 = h + 5
i1 = i + 7

# Second measuremnent
b2 = b1 + 1
c2 = c1 + 2
d2 = d1 + 1
e2 = e1 + 1
f2 = f1 + 1
g2 = g1 + 0.5
h2 = h1 + 11

# Third measurement
a2 = a1 + 3
h3 = h2 + 2
g2 = g + 4

myPlants = [a2, b2, c2, d2, h3, ]
mean = sum(myPlants) / len(myPlants)