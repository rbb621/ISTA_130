def word_length(word, char):
    if len(word) > char:
        print('Longer than', char, 'characters:', word)
    elif len(word) == char:
        print('Exactly', char, 'characters:', word)
    else:
        print('Shorter than', char, 'characters:', word)
        

def stop_light(color, seconds):
    
    #green
    if color == 'green':
        if seconds > 60:
            return 'yellow'
        else:
            return 'green'
    
    #yellow
    if color == 'yellow':
        if seconds > 5:
            return 'red'
        else:
            return 'yellow'
    
    #red
    if color == 'red':
        if seconds > 55:
            return 'green'
        else:
            return 'red'

def is_normal_blood_pressure(sbp, dbp):
    if sbp < 120 and dbp < 80:
        return True
    else:
        return False
    

def doctor():
    systolic_reading = input('Enter your systolic reading: ')
    diastolic_reading = input('Enter your diastolic reading: ')
    
    if int(systolic_reading) < 120 and int(diastolic_reading) < 80:
        print('Your blood pressure is normal.') 
    else:
        print('Your blood pressure is high.')
        

def pants_size(size):
    # 34 inches or larger should return large. 
    # Measurements that are 30 #inches or larger, 
    # but not large enough to be in the large category, 
    # should return medium.
    # Anything smaller should return small
    
    if size >= 34:
        return 'large'
    elif size >= 30:
        return 'medium'
    else:
        return 'small' 
    

def pants_fitter():
    name = input("Enter your name: ")
    print('Greetings', name, 'welcome to Pants-R-Us')
    waist_size = int(input('Enter your waist size in inches: '))
    amnt_pants = int(input('How many pairs of pants would you like: '))
    fashion_choice = input('Would you like regular or fancy pants? ')
    

    if fashion_choice == 'regular':
        regular_pants = 40
        total = regular_pants * amnt_pants 
    
    if fashion_choice == 'fancy':
        fashion_pants = 100
        total = fashion_pants * amnt_pants 

    # Size of pants
    if waist_size >= 34:
        size = 'large'
    elif waist_size >= 30:
        size = 'medium'
    else:
        size = 'small' 
        
    print(amnt_pants, 'pairs of', size, fashion_choice, 'pants: $', total)


def digdug(num):
    for i in range(3, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, ': digdug')
        elif i % 3 == 0:
            print(i, ': dig')
        elif i % 5 == 0:
            print(i, ': dug')

            

def beef_type(percent_lean):
    if percent_lean < 78:
        return 'Hamburger'
    if percent_lean >= 78 and percent_lean < 85:
        return 'Chuck'
    if percent_lean >= 85 and percent_lean < 90:
        return 'Round'
    if percent_lean >= 90 and percent_lean <= 95:
        return 'Sirloin'
    else:
        return 'Unknown'
    

def species_height(species, inches):
    
    # Species Average height
    if species == "Human":
        average = 67
    elif species == "Klingon":
        average = 71
    
    # Average Scale
    if inches > average:
        print("Above Average")
    elif inches < average:
        print("Below Average")
    else:
        print("Average")
            


def sooner_date(month_num_01, day_num_01, month_num_02, day_num_02):
    

    # comparing months
    if month_num_01 < month_num_02:
        print(month_num_01,"/",day_num_01)
    elif month_num_01 > month_num_02:
        print(month_num_02,"/",day_num_02)

    # Same Month
    elif month_num_01 == month_num_02:
    # comparing days
        if day_num_01 < day_num_02:
            print(month_num_01,"/",day_num_01)
        
        elif day_num_02 < day_num_01:
            print(month_num_02,"/",day_num_02)
            
        if day_num_02 == day_num_01:
            print(month_num_01, "/", day_num_01)
            
    else:
        print(month_num_01,"/",day_num_01)