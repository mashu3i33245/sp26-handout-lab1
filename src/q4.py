"""
Please implement this stub function to match the documentation.
As always, make sure to implement tests in the tests directory.
"""

from typing import Optional


def most_common_letter(s: str) -> Optional[str]:
    """Finds the most common letter in a given string.
    
    Parameters
    ----------
    s : str
        The input string
    
    Returns
    -------
    Optional[str]
        The most common letter in the string. If there is a tie, return the 
        letter that comes first alphabetically.
        Ignore case -- 'a' is equal to 'A'. Non-letter characters should be ignored.
        If there are no letters in the string, return None.
    """
     # Count letter frequencies (case-insensitive)
    letter_counts = {}
    
    for char in s:
        if char.isalpha():
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1
    
    # If no letters found, return None
    if not letter_counts:
        return None
    
    # Find the most common letter
    # In case of tie, return the one that comes first alphabetically
    max_count = max(letter_counts.values())
    most_common_letters = [letter for letter, count in letter_counts.items() if count == max_count]
    
    return min(most_common_letters)
