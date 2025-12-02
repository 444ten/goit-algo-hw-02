from collections import deque

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()

    chars = deque(cleaned)
    while len(chars) > 1:
        left = chars.popleft()
        right = chars.pop()

        if left != right:
            return False

    return True


if __name__ == "__main__":
    user_input = input("Enter a string to check for palindrome: ")

    if is_palindrome(user_input):
        print("The string IS a palindrome.")
    else:
        print("The string is NOT a palindrome.")
