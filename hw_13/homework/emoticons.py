# PART 2



#======================================================================
#               LOAD TWITTER DICTS FROM FILE FUNCTION
#======================================================================


#PSEUDOCODE
#Step 1: Create a load_twitter_dicts_from_file function
#Step 2: Parameter #1: File name (twitter_emoticons.dat)
#Step 3: Parameter #2: emoticons to ids (empty dictionary)
#Step 4: Parameter #2: ids to emoticons (empty dictionary)
#Step 5: Use a for loop to target line by line
#Step 6: Remove the quotes from the first key value by using .replace()
#Step 7: Split the columns into parts
#Step 8: Append IDs/emoticons to existing lists
#Step 9: DO NOT RETURN

def load_twitter_dicts_from_file(fileName, emoticons_to_ids, ids_to_emoticons):
    file = open(fileName, 'r')
    
    for line in file:
        current_line = line.strip()
        parts = current_line.split()
        
        emoticon = parts[0].replace('"', '')
        user_id = parts[2].replace('"', '')
        
        if emoticon not in emoticons_to_ids:
            emoticons_to_ids[emoticon] = []
        emoticons_to_ids[emoticon].append(user_id)
        
        if user_id not in ids_to_emoticons:
            ids_to_emoticons[user_id] = []
        ids_to_emoticons[user_id].append(emoticon)
    
    file.close()
    


#======================================================================
#                      FIND MOST COMMON FUNCTION
#======================================================================


#PSEUDOCODE
#Step 1: Create a find_most_common function
#Step 2: Parameter #1: single dictionary 
#Step 3: Keyname = string, value = string
#Step 4: Use the get() method to find longest list
#Step 5: Use an count variable initializer to set it to 0
#Step 6: Use a for loop to read line by line
#Step 7: Split the parts to target specific values
#Step 8: For each specific emoticon, use the count to target
#Step 9: print it out with print(single_dict, 'occurs', count, 'times')
#Step 10: Left Justify emoticon by 21
#Step 11: Right Justify number by 9
#Step 12: Return longest list


def find_most_common(single_dict):
    longest_key = ""
    count = 0
    
    for key, value_list in single_dict.items():
        if len(value_list) > count:
            count = len(value_list)
            longest_key = key
    print(longest_key.ljust(21) + 'occurs' + str(count).rjust(9), 'times')
    
    return longest_key



#======================================================================
#                         MAIN FUNCTION
#======================================================================

#PSEUDOCODE
#Step 1: Create two empty dictionaries (emoticons_to_ids and ids_to_emoticons)
#Step 2: Call load_twitter_dicts_from_file to pass file and two dicts
#Step 3: Set the count variable initalizer to count the emoticons to 0
#Step 4: Use a for loop to read line by line
#Step 5: Count the amount of icons from the part[0]
#Step 6: Print("Emoticons:", num_of_emoticons) from found in data file within the for loop
#Step 7: Call find_most_common(emoticons_to_ids) from the empty dictionary
#Step 8: Use the if statement if len(emoticons_to_ids) to determine what icon 
#        appears the most. Then Pop() most common emoticon
#Step 9: Do this 5 times over

def main():
    emoticons_to_ids = {}
    ids_to_emoticons = {}
    
    load_twitter_dicts_from_file('twitter_emoticons.dat', emoticons_to_ids, ids_to_emoticons)
    
    print("Emoticons: " + str(len(emoticons_to_ids)))
    print("UserIDs:   " + str(len(ids_to_emoticons)))
    
    # Print top 5 most common emoticons
    for i in range(5):
        most_common = find_most_common(emoticons_to_ids)
        emoticons_to_ids.pop(most_common)



if __name__ == '__main__':
    main()