# Write a function called mileage that takes an integer, which represents the
# number of trips a driver has taken in his/her car during the previous week. 
# In a loop, get the mileage for each trip from the user (use the input function), keeping track
# of the total. At the end, print out the total distance the user drove in the past week.


def mileage(num_trips):

    total_distance = 0
    for i in range(1, num_trips + 1):
        distance = input("How many miles did you drive for trip #" + str(i) + ": ")
        total_distance = total_distance + int(distance)
    print("The total distance the person drove was " + str(total_distance))
    return None
        


def main():
    mileage(4)
    
if __name__ == '__main__':
    main()