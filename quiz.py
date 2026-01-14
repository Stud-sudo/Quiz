

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
            "question": "What is the capital of France?",
            "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
            "answer": "3"
        },
        {
            "question": "Which language is mainly used for web structure?",
            "options": ["1. Python", "2. HTML", "3. Java", "4. C++"],
            "answer": "2"
        },
        {
            "question": "What does CPU stand for?",
            "options": [
                "1. Central Processing Unit",
                "2. Computer Personal Unit",
                "3. Central Performance Utility",
                "4. Control Processing Unit"
            ],
            "answer": "1"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["1. //", "2. <!-- -->", "3. #", "4. /* */"],
            "answer": "3"
        },
        {
            "question": "Which company manages Python?",
            "options": [
                "1. Microsoft",
                "2. Google",
                "3. Apple",
                "4. Python Software Foundation"
            ],
            "answer": "4"
        }
    ]


def get_user_answer():
    
    while True:
        answer = input("Enter your answer from 1:4 :")
        if answer in ["1","2","3","4"]:
            return answer
        print("Not right, try again")


def run_quiz():
    questions = get_questions()

    for question in questions:
        print(question["question"])
        for options in question["options"]:
            print(options)


run_quiz()
