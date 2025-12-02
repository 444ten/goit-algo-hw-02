def check_brackets(expression):
    """
    Check whether brackets in the given expression are balanced (symmetric)
    using a stack. Supports (), [], {}.
    """
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:
                return False

            last_open = stack.pop()
            if last_open != pairs[char]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    user_input = input("Enter an expression with brackets: ")

    if check_brackets(user_input):
        print("Symmetric")
    else:
        print("Not symmetric")
