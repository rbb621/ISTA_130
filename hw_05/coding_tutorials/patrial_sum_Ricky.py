# Write a function called partial_sum that takes an integer n and returns the
# following partial sum:


def partial_sum(n):
    part_sum = 0
    for i in range(n):
        current_sum = 1 / (2 ** i)
        part_sum += current_sum
        
    return part_sum
    


def main():
    
    max_expoonent = 4
    print("New partial sum of the exponent of " + str(max_expoonent) + " is " + str(partial_sum(4)))
    
if __name__ == '__main__':
    main()