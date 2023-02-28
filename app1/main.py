print("Enter a to-do:")

Getting user Input
user_prompt = "Enter a todo:"
text = input(user_prompt)
print(text)

Storing User Input:
user_prompt = "enter a todo:"
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)
todos = [todo1, todo2, todo3]
print(todos)

we will be building a program which checks the title of a book and gives us the length of that title.
text = input("Enter the Book Name: ")
length = len(text)
print("The length of the book is ", length)
