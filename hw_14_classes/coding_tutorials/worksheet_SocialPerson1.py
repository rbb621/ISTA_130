'''
Author: <your name>
Date: <the date>
Class: ISTA 130
Section Leader: <your section leader>

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment


# put all of your function / class definitions below this line and then delete this comment
class SocialPerson:
    def __init__(self, my_name, friends):
        self.my_name = my_name
        self.friends = friends
        return None
    def __repr__(self):
        output = "Friends of \n"
        output += self.my_name + "\n"
        output += "*"*20 + "\n"
        for current_friend in self.friends:
            output += "  " + current_friend + "\n"
        return output
    def new_year(self):
        for current_friend_name in self.friends:
            self.friends[current_friend_name] += 1
    def add_friend(self, friend, time):
        self.friends[friend.my_name] = time

    def unfriend(self, sp):
        self.friends.pop(sp.my_name)
        

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    dans_dict_of_friends = {'Al':1, 'Sam':5, 'Emily':3}
    dan = SocialPerson('Dan', dans_dict_of_friends)

    bobs_dict_of_friends = {'Al':4, 'Dan':5, 'Jim':10, 'Emily':1}
    bob = SocialPerson('Bob', bobs_dict_of_friends)


    print(dan)
    print(dan.friends)
    #dan.new_year()
    #print(dan.friends)
    #print(dict_of_friends)
    print()
    dan.add_friend(bob, 5)
    print(dan)
    print(dan.friends)

    dan.unfriend(bob)
    print(dan)
    print(dan.friends)

    
if __name__ == '__main__':
    main()
