# imports
import os
import sys


# def main
def main():
    for practice in range(2, 16):
        print(f"day{str(practice).zfill(2)}")
        ifExist = os.path.exists(f"day{str(practice).zfill(2)}")
        if not ifExist:
            # Create a new directory because it does not exist
            os.makedirs(f"day{str(practice).zfill(2)}")
            print("The new directory is created!")
        if ifExist:
            # Create a new directory because it does not exist
            os.chdir(f"day{str(practice).zfill(2)}")
            print("cd into directory!")
            # os.makedirs("practice_questions")
            os.chdir("practice_questions")
            for practice_num in range(1, 11):
                with open(f"practice_{str(practice_num).zfill(2)}.py", 'w') as document:
                    pass
            os.chdir("../..")


# main
if __name__ == "__main__":
    main()
