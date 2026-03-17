name = "HARSH"
friends = "Rohan"
another_friend = "lovish"
apple ='He said, Hi harry Iam Goood "I want to eat an apple'''
print("Hello, " + name)
#print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])# throw an error
print("lets use a for loop\n")
for character in apple:
    print(character)
#string slicing
names = "harry,shubham"
print(names[0:5])
#indexing starts from 0 and move till the number - 1
fruit = "Mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4])
#Similarly
print(fruit[:4])
print(fruit[0: len(fruit)  - 3])
#python take print(fruit[0:-3]) as print(fruit[0:len(fruit)  - 3])
print(fruit[0:-3])
print(fruit[-3:-1])
nm = "harry"
print(nm[-4:-2])
#ar