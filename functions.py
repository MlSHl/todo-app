# Functions for the main.py


def get_todos(filepath='todos.txt'):
    """ Opens file todos.txt, reads it,
    returns contents of the file
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath='todos.txt'):
    """ Opens file, writes todos_local into it"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)
