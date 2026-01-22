import argparse
import sys
import random
import time
import json
import pathlib
import os
from datetime import datetime


def welcoming():
    return """

    Welcome to the Holton College Quiz!

    Please answer the questions with numbers (1, 2, 3 or 4).

    If you need help, type: python3 quiz.py --help
    """


def get_questions():
    return [
        {"question": "8^0", "answer": 1, "options": ["1", "0", "8", "0.5"]},
        {"question": "42 / 7", "answer": 2, "options": ["5", "6", "7", "8"]},
        {"question": "190 + (-30)", "answer": 3, "options": ["220", "60", "160", "70"]},
        {"question": "6^2", "answer": 4, "options": ["22", "12", "16", "36"]},
        {"question": "7 * 7", "answer": 1, "options": ["49", "47", "46", "42"]},
        {"question": "121^(1/2)", "answer": 2, "options": ["10", "11", "12", "13"]},
        {"question": "21 / 3", "answer": 1, "options": ["7", "8", "9", "6"]},
        {"question": "10^3", "answer": 3, "options": ["10", "10000", "1000", "100"]},
        {"question": "11 * 11", "answer": 2, "options": ["111", "121", "130", "120"]},
        {"question": "12^2", "answer": 2, "options": ["141", "144", "151", "120"]},
        {"question": "15 * 5", "answer": 3, "options": ["65", "80", "75", "70"]},
        {"question": "72 / 8", "answer": 4, "options": ["8", "6", "7", "9"]},
        {"question": "16 * 3", "answer": 3, "options": ["46", "44", "48", "42"]},
        {"question": "17 - 19", "answer": 2, "options": ["2", "-2", "0", "1"]},
        {"question": "9^2", "answer": 4, "options": ["17", "11", "18", "81"]},
    ]


def show_score_report(score, total_questions, total_time):
    percentage = (score / total_questions) * 100
    incorrect = total_questions - score

    report = (
        "\nSCORE REPORT\n"
        f"Correct answers:   {score}\n"
        f"Incorrect answers: {incorrect}\n"
        f"Total questions:   {total_questions}\n"
        f"Percentage:        {percentage:.2f}%\n"
        f"Time taken:        {total_time:.2f} seconds\n"
        "\n"
    )

    print(report)
    return report


def save_results_json(score, total_questions, total_time):
    data = {
        "score": score,
        "total_questions": total_questions,
        "percentage": (score / total_questions) * 100,
        "time_taken_seconds": total_time,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    filename = "results.json"

    # Create file if missing
    path = pathlib.Path(filename)
    if not path.exists():
        with open(filename, "w") as f:
            json.dump({"attempts": []}, f, indent=4)

    # Load existing data
    with open(filename, "r") as f:
        existing = json.load(f)

    # Append new attempt
    existing["attempts"].append(data)

    # Save back
    with open(filename, "w") as f:
        json.dump(existing, f, indent=4)


def running_quiz():
    print(welcoming())
    score = 0
    questions = get_questions()
    random.shuffle(questions)

    start_time = time.time()

    for question in questions:
        print(f"Question: {question['question']}")
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        user_input = input("Select your answer (1-4) or press q to quit: ")

        if user_input.lower() == "q":
            sys.exit()

        if not user_input.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if int(user_input) == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Final Score: You scored {score} out of {len(questions)}")

    see_full_report = input("Do you want to see the full report again (yes/no): ").strip().lower()

    if see_full_report in ["yes", "y","Yes","YES"]:
        report = show_score_report(score, len(questions), total_time)

        save_choice = input("Do you want to save the report in a file (yes/no): ").strip().lower()
        if save_choice in ["yes", "y","Yes","YES"]:
            filename = input("Enter your filename: ")
            path_filename = pathlib.Path(filename+".txt")


            if path_filename.exists():
                print("File already exists")
                with open(f"{filename}.txt", "a") as f:
                    f.write(report)
            elif not path_filename.exists():
                with open(f"{filename}.txt", "a") as f:
                    f.write(report)

            save_results_json(score, len(questions), total_time)

    else:
        print("END")

    print("Thanks for taking the quiz!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="An interactive command-line quiz program for Holton College."
    )
    args = parser.parse_args()

    running_quiz()
