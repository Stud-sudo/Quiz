# Holton College Digital Quiz System - Proof of Concept

This repository contains my Python implementation for the Holton College digital transformation project. It’s a Proof of Concept (PoC) designed to show how the college can move away from paper tests and use a digital math quiz instead.

### Student Details
* **Student Number:** 25165912
* **Module Code:** COM4402
* **Project:** Proof of Concept (PoC) Digital Quiz

### Project Description
This application is a command-line math quiz with 15 different multiple-choice questions. I focused on making it feel like a real tool, so I added:
* **Randomized Questions:** The quiz shuffles the math problems every time you run it so it's never the same twice.
* **Persistent History:** Every attempt is automatically saved into a `results.json` file.
* **Score Reporting:** At the end, you get a full report with your percentage and exactly how many seconds it took you to finish.
* **File Export:** You can choose to save your final results as a `.txt` file with a name of your choice.

### Files in this Repository
* `quiz.py`: The main script with all the quiz logic, timers, and file saving.
* `results.json`: This file is included by default. It stores the history of every quiz attempt (scores, dates, and times).

### Requirements
You just need **Python 3.x** installed. I didn't use any external libraries, so you don't need to install anything extra like `pip`. It just uses standard Python modules like `json` and `random`.

### How to Run and Test
1. **Run the Quiz:** Open your terminal and type `python quiz.py`.
2. **Take the Test:** Follow the prompts. Make sure to answer with numbers 1-4.
3. **Check Persistence:** Once you finish, type 'yes' to see the report and 'yes' to save it. 
4. **Verify:** You can then open `results.json` to see your new attempt logged at the very bottom.
5. **Help Menu:** To see the command-line options, run `python quiz.py --help`.

### Known Issues & Future Fixes
* **Input Validation:** Right now, if you type a letter instead of a number, the program shows an error message but skips to the next question. In a future version, I'd like to make it re-prompt the user for the same question instead of skipping it.
* **File Overwriting:** If you save a `.txt` report with the same name twice, it currently appends the new report to the old one. I'd eventually like to add a feature that asks the user if they want to overwrite the file instead.
