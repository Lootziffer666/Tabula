def display_menu():
    """
    Display the main menu options.
    """
    print("=== Main Menu ===")
    print("1. Start")
    print("2. Options")
    print("3. Exit")
    print("Please choose an option:")


def format_output(data):
    """
    Format data for output presentation.
    """
    return f"Formatted data: {data}"


def get_input(prompt):
    """
    Handle user input with a prompt.
    """
    return input(prompt)


def present_output(output):
    """
    Present the output to the user.
    """
    print(output)
