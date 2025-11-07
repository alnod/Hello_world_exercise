# Write a function that ask a user for his name, age and location.
# Return a statement printed using f string mentioning his name, age and location. 
# push to github and share the github link with a new commit message


def personal_details(name,age,location):
    message = f"My name is {name}, I am {age} years old and I live in {location}"
    print(message)

name = input("What is your name? ")
age = (input("what is your age? "))
location = input("what is your location? ")
personal_details(name, age, location)




# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del it_companies
del A
del B
ageset = set(age)
print(len(ageset))
print(len(age))
print()


rows = 8
cols = 8

for i in range(rows):
    for j in range(cols):
        print('#', end=' ' )
    print(i)
print()
     
for i in range(11):
    print(f"{i} x {i} = {i * i}")
   
    
     
    