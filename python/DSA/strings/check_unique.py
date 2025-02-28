def has_unique_characters(s: str) -> bool:
    char_set = set()  # Set to store unique characters

    for char in s:
        if char in char_set:  # Check if character is already in the set
            return False
        char_set.add(char)  # Add character to the set

    return True  # All characters are unique

# Test cases
print(has_unique_characters("abcdef"))  # Output: True
print(has_unique_characters("abcdeaf"))  # Output: False
print(has_unique_characters(""))  # Output: True
print(has_unique_characters("a"))  # Output: True
print(has_unique_characters("abcd"))  # Output: True
print(has_unique_characters("hello"))  # Output: False
