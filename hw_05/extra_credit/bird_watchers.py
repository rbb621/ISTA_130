import random

'''
Name: Ricky Berliant
Date: 09/25/2025
Class: ISTA 130
Section Leader: Sungjoon Shin
'''


def bluebird_count(num_bird_watchers):
    total = 0
    for i in range(num_bird_watchers):
        print("---- Obeserver " + str(i + 1) + " ----")
        num_spot_observer = int(input("Enter number spotted by this observer: "))
        print()
        total += num_spot_observer        
    return total

def bluebirds_all_teams():
    regional_total = 0
    num_of_teams = int(input("Enter number of teams: "))
    
    for i in range(1, num_of_teams + 1):
        print("Team", i)
        num_observers = int(input("Enter number of observers for this team: "))
        
    team_total = 0
    for j in range(1, num_observers + 1):
        count = int(input("Enter number of bluebirds spotted by observer " + str(j) + ": "))
        team_total += count
        
    print("Team", i, "total: ", team_total)
    print("Regional Total", team_total)
    return regional_total


def number_of_odds(number):
    count = 0
    for i in range(1, number + 1):
        count += i % 2
    return count

def reverse_str(word): 
    reverse_string = word[::-1]  
    return reverse_string  

def main():
    print(str(bluebird_count(3)))
    bluebirds_all_teams()
    print(str(number_of_odds(6)))
    print(str(number_of_odds(7)))
    print(str(reverse_str('snake')))

if __name__ == "__main__":
    main()
    


