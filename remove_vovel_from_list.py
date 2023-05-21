# Remove vowels from the given list of strings and return as shown
# 	input: ['apple', 'ball', 'cat', 'dog', 'elephant']
# 	output: ['ppl', 'bll', 'ct', 'dg', 'lphnt']
            # ['pple', 'appl', 'bll', 'ct', 'dg', 'elephnt', 'lphant']

data1 = ['apple', 'ball', 'cat', 'dog', 'elephant']
# v = ['a','i','e','o','u']
# s = []
# for i in data1:
#     for j in v:
#         if j in i:
#             print(i,j)
#             i = i.replace(j,'')
#             print(i)
#     s.append(i)
# print('s',s)
# v = "aeiouAEIOU"
# print([i.replace(j,'') for i in data1 for j in v])


def remove_vowels(strings):
  vowels = "aeiouAEIOU"
  new_strings = []
  for string in strings:
    new_string = ""
    for char in string.lower():
      if char not in vowels:
        new_string += char
    new_strings.append(new_string)
  return new_strings
# new_strings = remove_vowels(data1)
# print(new_strings)

# print([(i=i.replace(j,'')) for i in data1 for j in v])
# a = [''.join(c for c in string.lower() if c not in 'aeiouAEIOU') for string in data1]
# print('a',a)

data1 = ["apple", "ball", "cat", "dog", "elephant"]
v = "aeiouAEIOU"
# s = [i.lower().replace(c, '') for i in data1 for c in v if c not in i]
# s = [''.join([char for char in string if char.lower() not in v]) for string in data1]
# print(s)

print([(i.replace()) for i in data1 for j in v])

