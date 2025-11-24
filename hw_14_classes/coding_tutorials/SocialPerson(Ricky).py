'''
Name: Ricky Berliant
Date: 12/4/2025
Class: ISTA 130
Section Leader: Sungjoon Shin
'''


class SocialPerson:
    '''
    1. Define the __init__ method. This method will have 3 parameters. As with all
    instance methods, the first parameter will be self. The second represents the person's
    name. Assign this parameter to an instance variable called my_name (don't forget to
    include self. to tell Python that this is an instance variable). The last argument will
    be a dictionary that has the names of friends as keys and the time the person has known
    them as values. Assign this parameter to an instance variable called friends.
    '''
    
    def __init__(self, person_name, list_of_friends):
        
        self.person_name = person_name
        self.list_of_friends = list_of_friends
        return None
    
    '''
    2. Define the __repr__ method. self is the only parameter in this method definition.
    This method should return a string with first line "Friends of " followed the
    contents of my_name, a line with 20 asterisks, and each of the keys in self.friends,
    one per line, indented two spaces.
    '''
    def __repr__(self):
        output = 'Friends of ' + self.person_name + '\n'
        output += '*' * 20 + '\n'
        for friend in self.list_of_friends:
            output += "" + friend + '\n'
        return output
        
    '''
    3. Write a method called new_year. new_year has only one parameter, self, and
    increments the value associated with each key in self.friends.
    '''
    
    def new_year(self):
        for friend in self.list_of_friends:
            self.list_of_friends[friend] += 1
            

    '''
    4. Write a method called add_friend. add_friend has three parameters, self,
    friend, and time. friend is another instance of SocialPerson. This method   
    adds the name of friend to self.friends as a key, with associated value time.
    '''
    def add_friend(self, friend, time):
        self.list_of_friends[friend.person_name] = time
        

    '''
    5. Write a method called unfriend. unfriend has two parameters, self and sp. sp
    is another instance of SocialPerson. This method pops the name of sp from
    self.friends.
    '''
     
    def unfriend(self, sp):
        self.list_of_friends.pop(sp.person_name)


#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    ricky_dict_of_friends = {'Jimmy': 39, 'Andy': 31, 'Tommy': 42, 'Max': 35, 'Bobby': 37, 'Mike':35}
    ricky = SocialPerson('Ricky', ricky_dict_of_friends)

    max_dict_of_friends = {'Derek': 35, 'Saman': 34, 'Jake':35, 'Jacob':35, 'Sasha': 33, 'Alex': 39}
    max = SocialPerson('Max', max_dict_of_friends)
    
    andy_dict_of_friend = {'Jared': 30, 'Peter': 29, 'Kulty': 26, 'Chad': 38, 'Luc': 31, 'John': 33}
    andy = SocialPerson('Andy', andy_dict_of_friend)
    
    print(andy)
    print(andy.list_of_friends)
    


    print(ricky)
    print(ricky.list_of_friends)
    
    print(max)
    print(max.list_of_friends)
    
    #ricky.new_year()
    #print(ricky.friends)
    #print(dict_of_friends)

    # print()
    # ricky.add_friend(max, 35)
    # print(ricky)
    # print(ricky.list_of_friends)

    # ricky.unfriend(max)
    # print(ricky)
    # print(ricky.list_of_friends)
    # print(max)

    
if __name__ == '__main__':
    main()