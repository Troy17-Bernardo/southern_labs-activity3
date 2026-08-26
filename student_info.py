name = input("Enter Your Name: ")
student_id = input("Enter Your Student_ID: ")
fav_programming_lang = input("Enter Your Favorite Programming Language: ")
current_age = int(input("Enter Your Current Age: "))


print(f"Name : {name} - Data Type:{type(name)}\n")
print(f"Student_ID: {student_id} - Data Type:{type(student_id)}\n")
print(f"Favorite Language :(fav_language) - Data Type:{type(fav_language)}\n")
print(f"Current Age: (current_age) - Data Type:{type(current_age)}\n")

age_next_year = current_age +1
total_modules = 7
total_modules_completed = total_modules -2

print(f"Next Year, You will Be {age_next_year} Years Old. \n")
print(f"Total Coarse Modules Completed: {total_modules_completed} Out Of {total_modules}\n")

