def movie_cost():
    total = 0
    renting_movies = int(input("How many movies do you want?: "))
    for i in range(1, renting_movies + 1):
        total += 2
        print("After renting", i, "movies, total is: $", total)
    return total


def bacteria(minutes, generations):    
    total_bacteria = 0    

    for i in range(1, generations, + 1):
        time_passed = minutes * i
        bacteria_count = 2 ** i
        total_bacteria += bacteria_count
        print("after", time_passed, "minutes: ", bacteria_count, "bacteria, (total:)", total_bacteria)

    
def staircase_word(word, num_row):
    for i in range(num_row - 1):
        print(word * (i + 1))
    print(word * num_row)

def coin_collector():
    total = 0
    number_of_days = int(input("Enter number of days: "))
    
    for i in range(1, number_of_days + 1):
        total += i 
        print("Day ", str(i), ":", total, "coin")
    return total
    
    
def multiplication_table(grid_size):
    for i in range(1, grid_size + 1): 
        for j in range(1, grid_size + 1):  
            product = i * j
            print(f"{product:4}", end="")  
        print()


def savings_tracker(daily_amount, days):
    total = 0
    for i in range(1, days + 1):
        total += daily_amount
        print(f"Day {i}: ${daily_amount} saved (Total: ${total})")
    return total
    

def main():
    final_cost = movie_cost()
    print("Final cost of the movies are $", final_cost)
    
    bacteria(20, 5)
    staircase_word("Hi", 5)
    coin_collector()
    multiplication_table(5)
    savings_tracker(5, 5)
    


if __name__ == '__main__':
    main()
    