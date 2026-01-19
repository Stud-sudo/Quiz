from questions import question_1, question_2,question_3,question_4,question_5
from options import option_1, option_2, option_3, option_4, option_5
import argparse
import sys


"""
HOLTON COLLEGE QUIZ - MODULE IMPORTS
1. Load quiz questions and options from local data files.
2. Utilize 'argparse' to provide a professional Command Line Interface (CLI).
"""


def welcoming():

    return f"""

    Welcome to the Holton College Quiz!
    
    Please answer the questions with letters given (1, 2,3 or 4) of your choice.

    if you need help, type: python3 quiz.py --help
    """






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
            "question": question_2,
            "options": option_2,
            "answer": "2"
        },
        {
            "question": question_3,
            "options": option_3,
            "answer": "1"
        },
        {
            "question": question_3,
            "options": option_4,
            "answer": "3"
        },
        {
            "question": question_5,
            "options": option_5,
            "answer": "4"
        }
    ]




"""
This function is for later purpose only

"""

def running_quiz():
    print(welcoming())
    score:int = 0
    questions = get_questions()

    for question in questions:
        print(question["question"])
        for options in question["options"]:
            print(options)
        user_input = input("Select your anwer from (1-4) and press q to quit:")

    
        if user_input == question["answer"]:#
            print("✅ Correct!")
            score += 1
        elif user_input == 'q':
            sys.exit()
        else:
             print(f"❌ Wrong!")



    print(f"Final Score: You scored {score} out of {len(questions)}")
    print("Thanks for taking the quiz!")





if __name__ == "__main__":
    help_description = "An interactive command-line quiz program for Holton College."
    
    parser = argparse.ArgumentParser(description=help_description)

    args = parser.parse_args()

    running_quiz()