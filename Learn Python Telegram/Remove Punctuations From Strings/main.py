# Python Program 
# Remove Punctuations From a String in Python 

# Taking user-input
''' 
sentence = input("Please enter your sentence: ")

punctuations = "!¡?¿.,;:()[]{}<>'/*+-=#%&|" # List of punctuations  
new_string = '' # Empty string for storing sentence without punctuations 
for i in sentence: 
    if i not in punctuations: 
        new_string +=i 
# iterating in sentence and check if character is not in punctuations then adding to new_string 
print(new_string) 
'''


def remove_punctuations(str_to_clean: str) -> str:
    PUNCTUATIONS = ",.;'<>:!¡?¿@#$%^&*()_+=-{}[]"
    new_str = ""
    for char in str_to_clean:
        if char not in PUNCTUATIONS:
            new_str += char
    return new_str


def remove_punctuations_list_comprehension(str_to_clean: str) -> str:
    PUNCTUATIONS = set(",.;'<>:!¡?¿@#$%^&*()_+=-{}[]")  # Using a set for faster lookup
    return ''.join(char for char in str_to_clean if char not in PUNCTUATIONS)


def main() -> None:
    test_cases = [
        "First, Test!",
        "a,b.c;d'e<f>g:h!i¡j?k¿l",
        "alpha ,betha .coco ;d'e<f>g:h!i¡j?k¿l",
        "",
        "   ",
    ]
    
    for test in test_cases:
        print(remove_punctuations(test))
        print(remove_punctuations_list_comprehension(test))


if __name__ == '__main__':
    main()
