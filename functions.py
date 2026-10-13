FILEPATH = "./todos.txt"


# Custom Functions in Python
def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do contents of that file."""
    # Open the file
    with open(filepath, "r") as file:
        # Read the file
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """Write a content inside the text file"""
    # open() designed to interact with files like txt files. "w" means write, "r" means read
    with open(filepath, "w") as file:
        # writelines() append a string of list to the file
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hielo")
