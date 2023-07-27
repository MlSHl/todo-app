# TodoList command line program!
import functions
import time

print(time.strftime("Today's date is %b %d %Y, %H:%M:%S"))
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos()

            todos[int(number) - 1] = input("Changed todo: ") + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            complete = int(user_action[9:])

            index = complete - 1

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"todo {todo_to_remove} has been removed from the list")
        except IndexError:
            print("There is no item with that number")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")
print('Bye!')
