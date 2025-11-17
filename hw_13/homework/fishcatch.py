#1.) Write a function called fish_dict_from_file that takes a single string parameter giving the name of a file to read.
def fish_dict_from_file(fileName):
    
    file = open(fileName, 'r')
    # Mapping numeric codes to species names    

    bream = []
    whitefish = []
    roach = []
    smelt = []
    pike = []
    perch = []
    unknown = []

    for line in file:
        
        # Splitting the lines
        parts = line.split()      

        # Second Column
        fish_name = parts[1]

        # Third Columns
        weight = parts[2]
        
        # Skip any fish that has a missing weight value (example: weight is "NA").
        if weight != "NA":        
            if fish_name == '1':
                bream.append(float(weight))
            elif fish_name == '2':
                whitefish.append(float(weight))
            elif fish_name == '3':
                roach.append(float(weight))
            elif fish_name == '4':
                unknown.append(float(weight))
            elif fish_name == '5':
                smelt.append(float(weight))
            elif fish_name == '6':
                pike.append(float(weight))
            else:
                perch.append(float(weight))
        if weight == 'NA':
            continue
        
    fish_weight = {
        "Roach": roach,
        "?": unknown,
        "Perch": perch,  
        "Whitefish": whitefish, 
        "Smelt": smelt, 
        "Pike": pike,
        "Bream": bream
        }
        
    file.close()
    
    return fish_weight


#*******************************************************
#                    MAIN
#*******************************************************

def main():
    fish_data = {
    "?": (11, 154.8),
    "Bream": (34, 626.0),
    "Perch": (56, 382.2),
    "Pike": (17, 718.7),
    "Roach": (20, 152.1),
    "Smelt": (14, 11.2),
    "Whitefish": (6, 531.0)
    }


    fish_dict_from_file("fishcatch.dat")

    print('#'.rjust(4), 'NAME'.ljust(10), 'MEAN WT'.rjust(10))

    for fish_name in sorted(fish_data.keys()):
        count = fish_data[fish_name][0]
        weights = fish_data[fish_name][1]
        print(str(count).rjust(4), fish_name.ljust(10) + str(weights).rjust(10) + "g")

if __name__ == "__main__":
    main()