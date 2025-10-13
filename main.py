# Write a function that ask a user for his name, age and location.
# Return a statement printed using f string mentioning his name, age and location. 
# push to github and share the github link with a new commit message

def personal_details(name,age,location):
    message = f"My name is {name}, I am {age} years old and I live in {location}"
    print(message)

name = input("What is your name? ")
age = int(input("what is your age? "))
location = input("what is your location? ")
personal_details(name, age, location)