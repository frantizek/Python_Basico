# Create a python function to check if a given string is a palindrome.

def only_alpha_characters(frase: str) -> str:
    """
    Funcion que utiliza una comprension de lista para obtener solo caracteres alfabeticos de una frase.

    Args:
        frase: La frase a procesar.

    Returns:
        str: La frase con solo caracteres alfabeticos.
    """
    return "".join(letra for letra in frase if letra.isalpha())


def reemplaza_letras_acentuadas(frase: str) -> str:
    frase = frase.lower()
    vocales = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
    for acentuada, sin_acento in vocales.items():
        frase = frase.replace(acentuada, sin_acento)
    return frase


def is_palindrome(evaluate_this_string: str) -> bool:
    if len(evaluate_this_string.replace(" ", "").lower()) > 0:
        new_reversed_string = (reemplaza_letras_acentuadas(only_alpha_characters(evaluate_this_string)))
        new_reversed_string = new_reversed_string.lower()[::-1]
        if new_reversed_string == only_alpha_characters(reemplaza_letras_acentuadas(evaluate_this_string.replace(" ", "").lower())):
            return True
    return False


def main() -> None:
    print(is_palindrome("Anna"))
    print(is_palindrome("Ateo poco poeta"))
    print(is_palindrome("arriba la birra"))
    print(is_palindrome(
        "Allí por la tropa portado, traído a ese paraje de maniobras, una tipa como capitán usar boina me dejara, pese a odiar toda tropa por tal ropilla"))


if __name__ == '__main__':
    main()
