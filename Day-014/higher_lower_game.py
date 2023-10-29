import art, os, random
import game_data

# Choosing random person from game_data
def random_person():
    return game_data.data[random.randint(0, len(game_data.data)-1)]
         
# Printing chosen person's data
def printing_data(person):
    return f"Compare: {person['name']}, {person['description']} from {person['country']}."

def user_answer():
    answer=input("Who has more followers? 'A' or 'B': ").lower()
    if answer not in ["a", "b"]:
        print("Provide proper answer - 'A' or 'B'!")
        return user_answer()
    return answer

def check_if_people_are_the_same(comparedPeople):
    while comparedPeople[0]==comparedPeople[1]:
        comparedPeople[1]=random_person()  

def user_answer_validate(comparedPeople, answer):
    if comparedPeople[0]['follower_count']>comparedPeople[1]['follower_count']:
        correctAnswer="a"
    else:
        correctAnswer="b"
    
    if correctAnswer==answer:
        return True
    else:
        return False

def higher_lower():
    points=0
    shouldContinue=True
    comparedPeople=[random_person(), random_person()]

    check_if_people_are_the_same(comparedPeople)   

    while shouldContinue:
        os.system("clear")
        if comparedPeople[0]["follower_count"]<comparedPeople[1]["follower_count"]:
            comparedPeople[0]=comparedPeople[1]
            comparedPeople[1]=random_person()
            check_if_people_are_the_same(comparedPeople)    
        else:
            comparedPeople[1]=random_person()
            check_if_people_are_the_same(comparedPeople)    

        print(art.logo)
        if points>0:
            print(f"You have {points} points.")

        print(f"Compare A: {printing_data(comparedPeople[0])}")
        print(art.vs)
        print(f"Versus B:  {printing_data(comparedPeople[1])}")
        
        if user_answer_validate(comparedPeople, user_answer()):
            points+=1
        else:
            print(f"You're wrong. Final score is {points}")
            shouldContinue=False

higher_lower()