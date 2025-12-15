def sum_num(filename):
    fp1 = (filename, 'r')
    # new_filename = filename[:-4] + '_summed.csv'
    # outfile = open(new_filename, 'w')
    
    sum_dict = {}
    line_num = 1
    for line in fp1:
        current_line = line.strip().split(',')
        total = 0
        for el in current_line:
            total += float(el)
        # outfile.write(str(total) + '\n')
            
        sum_dict[line_num] = total
        total += 1
    fp1.close()
    # outfile.close()
    return sum_dict
        



def main():
    print(sum_num('testing_sum.txt'))
    

if __name__ == '__main__':
    main()