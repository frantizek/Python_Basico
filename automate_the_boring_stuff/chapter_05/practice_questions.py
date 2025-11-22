#!/usr/bin/env python3
"""
practice_questions.py
A script to test knowledge of assertions, logging, and debugging.
The user answers questions, and the script grades their responses.
"""

def question_1():
    """Question 1: Assertion for integer less than 10."""
    print("\n1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.")
    user_answer = input("Your answer (e.g., 'assert spam > 10, \"Error message\"'): ").strip()
    # Correct answer logic would go here (omitted to avoid spoilers)
    return check_answer_1(user_answer)

def question_2():
    """Question 2: Assertion for case-insensitive string equality."""
    print("\n2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different.")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here
    return check_answer_2(user_answer)

def question_3():
    """Question 3: Assertion that always triggers."""
    print("\n3. Write an assert statement that always triggers an AssertionError.")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here
    return check_answer_3(user_answer)

def question_4():
    """Question 4: Lines needed to call logging.debug()."""
    print("\n4. What two lines must your program have to be able to call logging.debug()?")
    print("   (Separate the two lines with a semicolon ;)")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here
    return check_answer_4(user_answer)

def question_5():
    """Question 5: Lines needed to log to programLog.txt."""
    print("\n5. What two lines must your program have to make logging.debug() send a logging message to a file named programLog.txt?")
    print("   (Separate the two lines with a semicolon ;)")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here
    return check_answer_5(user_answer)

def question_6():
    """Question 6: Five logging levels."""
    print("\n6. What are the five logging levels?")
    print("   (Separate the levels with commas ,)")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here
    return check_answer_6(user_answer)

def question_7():
    """Question 7: Disable all logging messages."""
    print("\n7. What line of code can you add to disable all logging messages in your program?")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here
    return check_answer_7(user_answer)

def question_8():
    """Question 8: Why is logging better than print()?"""
    print("\n8. Why is using logging messages better than using print() to display the same message?")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here (accept any reasonable explanation)
    return check_answer_8(user_answer)

def question_9():
    """Question 9: Differences between Step Over, Step In, and Step Out."""
    print("\n9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here (accept any reasonable explanation)
    return check_answer_9(user_answer)

def question_10():
    """Question 10: When does the debugger stop after Continue?"""
    print("\n10. After you click Continue, when will the debugger stop?")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here
    return check_answer_10(user_answer)

def question_11():
    """Question 11: What is a breakpoint?"""
    print("\n11. What is a breakpoint?")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here (accept any reasonable explanation)
    return check_answer_11(user_answer)

def question_12():
    """Question 12: How to set a breakpoint in Mu?"""
    print("\n12. How do you set a breakpoint on a line of code in Mu?")
    user_answer = input("Your answer: ").strip()
    # Correct answer logic would go here (accept any reasonable explanation)
    return check_answer_12(user_answer)

# Placeholder functions for answer checking (to be implemented)
def check_answer_1(answer): return answer == "assert spam >= 10, 'spam must be at least 10'"  # Example
def check_answer_2(answer): return False  # Implement logic
def check_answer_3(answer): return False  # Implement logic
def check_answer_4(answer): return False  # Implement logic
def check_answer_5(answer): return False  # Implement logic
def check_answer_6(answer): return False  # Implement logic
def check_answer_7(answer): return False  # Implement logic
def check_answer_8(answer): return False  # Implement logic
def check_answer_9(answer): return False  # Implement logic
def check_answer_10(answer): return False  # Implement logic
def check_answer_11(answer): return False  # Implement logic
def check_answer_12(answer): return False  # Implement logic

def main():
    """Runs the practice questions and grades the user's answers."""
    print("=== Practice Questions: Assertions, Logging, and Debugging ===")
    print("Answer each question. Your score will be displayed at the end.\n")

    questions = [
        question_1, question_2, question_3, question_4, question_5,
        question_6, question_7, question_8, question_9, question_10,
        question_11, question_12
    ]

    score = 0
    for question in questions:
        if question():
            score += 1

    print(f"\nYour score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
