from questions import * 
from options import option_1, option_2, option_3, option_4, option_5

"""
 

calling others functions from other python files



"""


def welcoming():

    return f""" Welcome!

    Console-Based Quiz Application
    
    Please answer the questions with letters given (1, 2,3 or 4) of your choice.
    """


print(welcoming())




def get_questions():
    """
    Return a list of questions
    each questions is stored in a dictonary    
    """

    return [
        {
            "question": question_1,
            "options": option_1,
            "answer": "3"
        },
        {
            "question": quesiton_2,
            "options": option_2,
            "answer": "2"
        },
        {
            "question": quesiton_3,
            "options": option_3,
            "answer": "1"
        },
        {
            "question": quesiton_4,
            "options": option_4,
            "answer": "3"
        },
        {
            "question": quesiton_5,
            "options": option_5,
            "answer": "4"
        }
    ]




"""
This function is for later purpose only

"""

# def run_quiz():
#     score:int = 0
#     questions = get_questions()

#     for question in questions:
#         print(question["question"])
#         for options in question["options"]:
#             print(options)
#         user_input = input("Select your anwer from (1-4):")

#         if user_input == question["answer"]:
#             score += 1



#     print(f"You scored {score} out of {len(questions)}")
#     print("Thanks for taking the quiz!")


# run_quiz()
