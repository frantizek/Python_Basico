# Given a list of words, count the number of words with more than five characters.

def only_words_with_more_than_five_characters(list_with_words: list[str]) -> int:
    words_with_more_than_five_characters = 0
    list_of_words_with_more_than_five_characters = []
    for word in list_with_words:
        if len(word) > 5:
            words_with_more_than_five_characters += 1
            list_of_words_with_more_than_five_characters.append(word)
    return words_with_more_than_five_characters


def main() -> None:
    print(only_words_with_more_than_five_characters([
    "Liam", "Emma", "Noah", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia",
    "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila",
    "Aria", "Scarlett", "Victoria", "Madison", "Luna", "Grace", "Chloe", "Penelope", "Layla", "Riley",
    "Zoey", "Nora", "Lily", "Eleanor", "Hannah", "Lillian", "Addison", "Aubrey", "Ellie", "Stella",
    "Natalie", "Zoe", "Leah", "Hazel", "Violet", "Aurora", "Savannah", "Audrey", "Brooklyn", "Bella",
    "Claire", "Skylar", "Lucy", "Paisley", "Everly", "Anna", "Caroline", "Nova", "Genesis", "Emilia",
    "Kennedy", "Samantha", "Maya", "Willow", "Kinsley", "Naomi", "Aaliyah", "Elena", "Sarah", "Ariana",
    "Allison", "Gabriella", "Alice", "Madelyn", "Cora", "Ruby", "Eva", "Serenity", "Autumn", "Adeline",
    "Hailey", "Gianna", "Valentina", "Isla", "Eliana", "Quinn", "Nevaeh", "Ivy", "Sadie", "Piper",
    "Lydia", "Alexa", "Josephine", "Emery", "Julia", "Delilah", "Arianna", "Vivian", "Kaylee", "Sophie",
    "Brielle", "Madeline", "Peyton", "Rylee", "Clara", "Hadley", "Melanie", "Mackenzie", "Reagan", "Adalynn",
    "Liliana", "Aubree", "Jade", "Katherine", "Isabelle", "Natalia", "Raelynn", "Maria", "Athena", "Ximena",
    "Arya", "Leilani", "Taylor", "Faith", "Rose", "Kylie", "Alexandra", "Mary", "Margaret", "Lyla",
    "Ashley", "Amaya", "Eliza", "Brianna", "Bailey", "Andrea", "Khloe", "Jasmine", "Melody", "Iris",
    "Isabel", "Norah", "Annabelle", "Valeria", "Emerson", "Adalyn", "Ryleigh", "Eden", "Emersyn", "Anastasia",
    "Kayla", "Alyssa", "Juliana", "Charlie", "Esther", "Ariel", "Cecilia", "Valerie", "Alina", "Molly",
    "Reese", "Aliyah", "Lilly", "Parker", "Finley", "Morgan", "Sydney", "Jordyn", "Eloise", "Trinity",
    "Daisy", "Kimberly", "Lauren", "Genevieve", "Sara", "Arabella", "Harmony", "Elise", "Remi", "Teagan",
    "Alexis", "London", "Sloane", "Lila", "Lola", "Juliet", "Alana", "Malia", "Madison", "Lyric",
    "Camille", "Sienna", "Josie", "Dahlia", "Julianna", "Aliana", "Leila", "Addilyn", "Kaitlyn", "Amara",
    "Adelyn", "Rosalie", "Royal", "Aria", "Jayden", "Lukas", "Milo", "Archer", "Enzo", "Theo",
    "Luca", "Kai", "Liam", "Finn", "Elliot", "Nolan", "Arthur", "Logan", "Ryker", "Alex",
    "Easton", "Oscar", "Julian"
    ]))


if __name__ == '__main__':
    main()
