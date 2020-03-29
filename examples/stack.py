from string_stack.string import String, AdvancedString
from string_stack.stack import Stack

string_1 = String('test12345')
string_2 = String('q')
string_3 = String('')

advanced_string_1 = AdvancedString('Hello there!')
advanced_string_2 = AdvancedString('Goodbye!')


stack = Stack()

stack.put(string_1)
print(stack.get())  # string_1

stack.put(string_2)
print(stack.get())  # string_2

print(stack.get_all())  # two elements in stack (string_1, string_2)

stack.delete()
print(stack.get())  # string_1
print(stack.get_all())  # one element (string_1)

stack.put(advanced_string_1)
stack.put(advanced_string_2)
stack.put(string_3)

for elem in stack.get_all():  # (string_1, advanced_string_1, advanced_string_2, string_3)
    print(elem.length)  # (9, 12, 8, 0)

for elem in stack.get_all():  # (string_1, advanced_string_1, advanced_string_2, string_3)
    elem.clear()
    print(elem.length)  # (0, 0, 0, 0)


print(stack.is_empty())  # False
for _ in range(len(stack.get_all())):  # 4
    stack.delete()

print(stack.is_empty())  # True
