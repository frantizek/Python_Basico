# Create a program that takes a sentence as input and counts the number of words in it.

def only_alpha_characters(frase: str):
    """
    Funcion que utiliza una comprension de lista para obtener solo caracteres alfabeticos y espacios de una frase.

    Args:
        frase: La frase a procesar.

    Returns:
        str: La frase con solo caracteres alfabeticos y espacios.
    """
    punctuation = "!\"#$%&'*+,./:;<=>?@[\]^_`{|}~"
    return "".join(char for char in frase if char not in punctuation)


def words_in_this_phrase(phrase: str) -> int:
    if phrase == " " or phrase == "":
        return 0
    return len(only_alpha_characters(phrase.strip()).split(" "))


def main() -> None:
    print(words_in_this_phrase(""))
    print(words_in_this_phrase(" "))
    print(words_in_this_phrase("      "))
    print(words_in_this_phrase("shut up, and take my money..."))
    print(words_in_this_phrase("Parangatirimicuaro"))
    print(words_in_this_phrase("bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla"))


if __name__ == '__main__':
    main()
