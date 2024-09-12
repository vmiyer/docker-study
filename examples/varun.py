def print_V():
    return [
        "*       *",
        " *     * ",
        "  *   *  ",
        "   * *   ",
        "    *    "
    ]

def print_A():
    return [
        "   *    ",
        "  * *   ",
        " *****  ",
        " *   *  ",
        " *   *  "
    ]

def print_R():
    return [
        " ****   ",
        " *   *  ",
        " ****   ",
        " * *    ",
        " *  *   "
    ]

def print_U():
    return [
        "*    *  ",
        "*    *  ",
        "*    *  ",
        "*    *  ",
        " ****   "
    ]

def print_N():
    return [
        "*    *  ",
        "**   *  ",
        "* *  *  ",
        "*  * *  ",
        "*   **  "
    ]

def print_VARUN():
    letters = [print_V(), print_A(), print_R(), print_U(), print_N()]
    for row in range(5):  # Each letter pattern has 5 rows
        print("  ".join(letter[row] for letter in letters))

# Call the function to print VARUN
print_VARUN()
