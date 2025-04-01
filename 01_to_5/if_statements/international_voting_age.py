user_age_in_Peturksbouipo:int=16
user_age_in_Stanlau:int=25
user_age_in_Mayengua:int=48

def voting():
    user_age=int(input("How old are you? "))


    if user_age >= user_age_in_Peturksbouipo:
       print("You can vote in Peturksbouipo")
    else:
       print("You can not vote in Peturksbouipo ")


    if user_age >= user_age_in_Stanlau:
      print("You can vote in Stanlau ")
    else:
      print("You can not vote in Stanlau ")



    if user_age >= user_age_in_Mayengua:
      print("You can vote in Mayengua")
    else:
      print("You can not vote in Mayengua ")
voting()