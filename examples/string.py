from string_stack.string import String, AdvancedString

string_1 = String('test12345')
print(string_1.length)  # 9

string_2 = String('q')
print(string_2.length)  # 1

string_3 = String('')
print(string_3.length)  # 0

string_1.clear()
print(string_1.length)  # 0

try:
    string_error = String(123)
except AssertionError as e:
    print(e)  # String constructor takes only literal


advanced_string_1 = AdvancedString('Hello there!')
print(advanced_string_1.get_chars())  # ['H', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'e', 'r', 'e', '!']
print(advanced_string_1.get_chars(offset=0, limit=0))  # []
print(advanced_string_1.get_chars(offset=100, limit=100))  # []
print(advanced_string_1.get_chars(offset=2, limit=5))  # ['l', 'l', 'o']
print(advanced_string_1.get_chars(offset=5, limit=10))  # [' ', 't', 'h', 'e', 'r']

advanced_string_1.clear()
print(advanced_string_1.get_chars())  # []
