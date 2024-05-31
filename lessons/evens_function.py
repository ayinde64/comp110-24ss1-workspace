"""Challenge Question 5-30-24."""

__author__ = "730480705"


def display_evens(even_number: int) -> int:
    """Takes input as integer and prints all even numbers less than or equal to 0."""
    current_number = even_number  
    while current_number >= 0: 
        if current_number % 2 == 0:
            print(current_number)
        current_number -= 1
    return even_number 
