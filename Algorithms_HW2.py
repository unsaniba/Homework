def reverse_integer(n: int):
    num_str = str(n)

    if num_str[0] == '-':
        reversed_str = '-' + num_str[:0:-1]
    else:
        reversed_str = num_str[::-1]

    reversed_num = int(reversed_str)

    return reversed_num


n = -189
reversed_result = reverse_integer(n)
print(f"The reversed integer is: {reversed_result}")


def reverse_words(sentence: str):
    # Split the sentence into individual words using the .split() method
    words = sentence.split()

    # Create an empty list to store the reversed versions of words
    reversed_words = []

    # Iterate through each word in the list of words
    for word in words:
        # Reverse each word using string slicing with a step of -1
        reversed_word = word[::-1]

        # Append the reversed word to the list of reversed words
        reversed_words.append(reversed_word)

    # Join (.join) the reversed words back together into a single string, separated by spaces
    reversed_sentence = " ".join(reversed_words)

    # Return the final reversed sentence
    return reversed_sentence


sentence1 = "Hello World"
result1 = reverse_words(sentence1)
print(f"Original: {sentence1}\nReversed: {result1}")

sentence2 = "mistertwister"
result2 = reverse_words(sentence2)
print(f"Original: {sentence2}\nReversed: {result2}")


def repeat_digits(s: str):
    result = ""  # Initialize an empty string to store the result

    for char in s:  # Iterate through each character in the input string
        # Convert the character to an integer
        current_num = int(char)

        # Repeat the character based on its integer value
        repeated_char = char * current_num

        # Append the repeated character to the result string
        result += repeated_char

    return result  # Return the final result string


string1 = "312"
result1 = repeat_digits(string1)
print(f"Original: {string1}\nRepeated: {result1}")

string2 = "102"
result2 = repeat_digits(string2)
print(f"Original: {string2}\nRepeated: {result2}")


def shortcut(s: str):
    result = ""  # Initialize an empty string to store the result

    for char in s:  # Iterate through each character in the input string
        # Check if the character is NOT a vowel (using the NOT operator)
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            # If not a vowel, add the character to the result string
            result += char

    return result  # Return the final result string


string1 = "hello"
result1 = shortcut(string1)
print(f"Original: {string1}\nShortcut: {result1}")

string2 = "goodbye"
result2 = shortcut(string2)
print(f"Original: {string2}\nShortcut: {result2}")


