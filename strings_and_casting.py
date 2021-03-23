# Strings and Casting

# Industry practices
# Single and double quotes

# single_quotes = 'single quotes \'WoW\' moment'
# double_quotes = "double quotes 'WoW'"
# print(single_quotes)
# print(double_quotes)

# String slicing
greeting = "hello world!" # string
# Indexing in Python starts from 0
# h e l l o   w o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

print(len(greeting)) # number of characters in the string
print(greeting[0:5]) # outputs hello (0 to 4)
print(greeting[6:11]) # outputs world

# Reverse indexing starts with -1
#  h   e   l   l  o     w  o  r  l  d  !
# -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(greeting[-6:])

# String metheds
white_space = "lots of space at the end          "
print(len(white_space))
print(len(white_space.strip())) # .strip() removes white space

example_text = "here's SOME text with lots of text"
print(example_text.count("text")) # counts number of times the string is mentioned

# Lower and uppercase
print(example_text)
print(example_text.upper())
print(example_text.lower())
print(example_text.capitalize()) # capitalises the first letter
print(example_text.replace("with", ",")) # replaces "with" with ","