def three_copies(my_list, data):
    my_list.extend([data]*3)
message=input("Enter a message to copy: ")
my_list = []
print(f"list before", my_list)
three_copies(my_list,message)
print("List after", my_list)