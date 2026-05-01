def find_uppercase_position(S):
    # Iterate over each character in the string
    for index, char in enumerate(S):
        # Check if the character is an uppercase letter
        if char.isupper():
            # Return the 1-based index of the uppercase letter
            return index + 1

# Example usage
if __name__ == "__main__":
    import sys
    input = sys.stdin.read().strip()
    print(find_uppercase_position(input))
