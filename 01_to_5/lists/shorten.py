Max_length=3

def pop(list):
    while len(list) > Max_length:
     remove_item=list.pop()
     print(remove_item)
def main():
   list=[1,2,3,4,5,6,7,8,9,0]
   pop(list)
main()
