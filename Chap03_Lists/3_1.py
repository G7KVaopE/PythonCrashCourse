

names = ['bob', 'mary', 'jack']

message = "My friends name is " + names[0].title()

print(names[-2].title())

print(message)

names[0] = 'sam'

print(names)

names.append('joe')

print(names)

names.insert(2,'sally')

print(names)

del names[1]

print(names)

popped_names = names.pop()
print(names)
print(popped_names)
names.remove('jack')
print(names)
