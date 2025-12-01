'''
Name: Ricky Berliant
Section Leader: Sungjoon Shin
Date: 12/10/2025
Class: ISTA 130
Homework: Classes Discussion
'''

class DatingProfile:
    # __init__ function
    def __init__(self, name, age, looking_for, interests):
        self.name = name
        self.age = age
        self.looking_for = looking_for
        self.interests = interests
        return None
    
    # __repr__ function
    def __repr__(self):
        output = '-----' + self.name +  '----- \n'
        output += 'Age: ' + str(self.age) + '\n'
        output += 'Looking for: ' + self.looking_for + '\n'
        interests_str = ', '.join(self.interests)
        output += 'Interests: ' + interests_str + '\n'
        
        return output

    # Match Me With Function
    def match_me_with(self, other_profiles):
        
        # Match levels score from 0-3:
        # 0 = Not a good match
        # 1 = Possible Match
        # 2 = Good Match
        # 3 = Great Match
        score = 0
        
        # Match rating score
        match_rating = ["Not a good match", "Possible match", "Good match", "Great match"]
        
        # Age Difference
        if abs(self.age - other_profiles.age) <= 10:
            score += 1
            print('Both are withing the' + abs(self.age - other_profiles.age) + 'age difference')
        else:
            print(abs(self.age - other_profiles.age) + ' is too big of an age gap.')
            
        # Looking for
        if self.looking_for == other_profiles.looking_for:
            score += 1
            print('They both are looking for', self.looking_for)
        else:
            print('Both have different prioritites')

        # Interests
        if self.interests == other_profiles.interests:
            score += 1
            print('Both', self.name, 'and', other_profiles.name, 'have', self.interests, 'in common!')
        else:
            print('There is nothing in common between', self.name, 'and', other_profiles.name)
            

        return match_rating[score]
            
        
        
    
def main():
    ricky_profile = DatingProfile('Ricky', 37, 'Loyal and supportive', ['Video games', 'Anime', 'Hiking'])
    print("--- Profile Display Test: Ricky ---")
    print(ricky_profile) 
    
    # 2. Test case from the instructions: Jeanine vs Bob
    
    # Jeanine's Profile
    jeanine_profile = DatingProfile('Jeanine', 26, 'Short term dating', ['Skiing', 'Board games', 'Hiking'])
    print(jeanine_profile)
    
    # Bob's profile
    bob_profile = DatingProfile('Bob', 57, 'Long term dating', ['TV', 'Stamp collecting', 'Hiking'])
    print(bob_profile)
    
    print("\n--- Match Test 1: Jeanine vs Bob ---")
    match_jeanine_bob = jeanine_profile.match_me_with(bob_profile)
    print("\nResult:", match_jeanine_bob)
    
    print("\n--- Match Test 1: Ricky vs Sally ---")
    sally = DatingProfile('Sally', 35, 'Loyal and supportive', ['Guitar', 'Reading', 'Video Games'])

    match_ricky_sally = ricky_profile.match_me_with(sally)
    print("\n Result:", match_ricky_sally)


if __name__ == '__main__':
    main()
