# create a to_do list for an individual and his various task or activities
My_to_do = []

while True:
    user_input = input("""1 to create,
2 to read,
3 to update,
4 to delete
5 to quit.
""")

    if user_input == "1":
        My_to_do_1 = str(input("Enter a task: "))
        My_to_do.append(My_to_do_1)
        print( My_to_do_1)

    elif user_input == "2":
        print("To-Do List:")
        for index, task in enumerate(My_to_do):
            print(f"{index}. {task}")

    elif user_input == "3":
        print("To-Do List:")
        for index, task in enumerate(My_to_do):
            print(f"{index}. {task}")

        index_of_item = int(input("Enter the index of the task to update: "))
        if 1 <= index_of_item <= len(My_to_do):
            name_of_item = input("Enter the new task name: ")
            My_to_do[index_of_item - 1] = name_of_item
            print("Task updated.")
        else:
            print("Invalid index.")

    elif user_input == "4":
        print("To-Do List:")
        for index, task in enumerate(My_to_do):
            print(f"{index}. {task}")

        index_of_item = int(input("Enter the index of the task to delete: "))
        if 1 <= index_of_item < len(My_to_do):
            removed_task = My_to_do.pop(index_of_item - 1)
            print(removed_task)
        else:
            print("Invalid index.")

    elif user_input == "5":
        break

    else:
        print("Invalid input. Please try again.")


