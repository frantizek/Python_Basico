#!/usr/bin/env python3
"""
feedcat_enhanced.py
Generates a customizable message for feeding a pet.
Demonstrates:
  - User input handling
  - String formatting
  - Basic error handling
  - Modular code structure
"""

def generate_feed_message(sender: str, recipient: str, pet_name: str, pet_type: str, weekend: str) -> str:
    """
    Generates a message asking someone to feed a pet for a specific weekend.

    :param sender: Name of the person sending the message.
    :param recipient: Name of the person receiving the message.
    :param pet_name: Name of the pet.
    :param pet_type: Type of pet (e.g., 'cat', 'dog').
    :param weekend: Description of the weekend (e.g., 'this weekend', 'next weekend').
    :return: Formatted message as a string.
    """
    message = f'''Dear {recipient},
Can you feed {pet_name}'s {pet_type} {weekend}?
Sincerely,
{sender}'''
    return message

def get_user_input(prompt: str) -> str:
    """
    Prompts the user for input and ensures it is not empty.

    :param prompt: The prompt to display to the user.
    :return: The user's input as a string.
    :raises ValueError: If the user enters an empty string.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Error: Input cannot be empty. Please try again.")

def main():
    """Generates and prints a customizable pet-feeding message."""
    print("=== Pet Feeding Message Generator ===")

    # Get user input for message customization
    sender = get_user_input("Enter your name: ")
    recipient = get_user_input("Enter the recipient's name: ")
    pet_name = get_user_input("Enter the pet's name: ")
    pet_type = get_user_input("Enter the type of pet (e.g., cat, dog): ")
    weekend = get_user_input("Enter the weekend description (e.g., 'this weekend'): ")

    # Generate and print the message
    message = generate_feed_message(sender, recipient, pet_name, pet_type, weekend)
    print("\nGenerated Message:\n")
    print(message)

if __name__ == "__main__":
    main()
