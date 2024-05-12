# Implement a program that checks if a given string is a palindrome.

def isPalindrome(str1: str, str2: str) -> bool:
    """Receives two strings then compares them and return if they are a Palindrome

    :param str1: str - first string to compare
    :param str2: str - second string to compare
    :return: Boolean
    """
    return str1 == str2[::-1] and str2 == str1[::-1]


def main():
    print(isPalindrome("racecar", "racecar"))


if __name__ == '__main__':
    main()
