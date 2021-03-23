# Python Data types and Operators
### Data Types
* Strings
* Numbers Integers > floats, longs
* Boolean (True or False)
* None (Python's Null equivalent)

### Arithmetic Operators
* `+` addition
* `-` subtraction
* `*` multiplication
* `/` division
* `%` modulus - gives the remainder of 2 numbers
  
### Comparison Operators
  * `>` greater than 
  * `<` less than
  * `>=` greater than equal to
  * `==` equal to
  * `!=` not equal to
    
## Strings and Casting
Strings in single and double quotes.
```python
single_quotes = 'single quotes \'WoW\' moment'
double_quotes = "double quotes 'WoW'"
```

Python indexing
```python
greeting = "hello world!"

# Indexing in Python starts from 0
h e l l o   w o r l d  !
0 1 2 3 4 5 6 7 8 9 10 11

# Reverse indexing starts with -1
 h   e   l   l  o     w  o  r  l  d  !
-12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(greeting[0]) # outputs "h"
print(greeting[-1]) # outputs "!"
```

String slicing
```python
greeting = "hello world!"
print(len(greeting)) # number of characters in the string
print(greeting[0:5]) # outputs "hello"
print(greeting[6:11]) # outputs "world"
print(greeting[-6:]) # outputs "world!"
```

Concatenation and type casting
```python
first_name = "William"
last_name = "King"
wage = 18.5

# Outputs "William King 18.5"
print(first_name + " " + last_name + " " + str(wage))

# outputs 18. Converts into an int and rounds down.
print(int(wage))
```

String formatting with f
```python
# Outputs "My name is William King and I earn £18.5."
print(f"My name is {first_name} {last_name} and I earn £{wage}.")
```

## String methods
Boolean methods for strings.
```python
greeting = "Hello world!"
print(greeting.isalpha()) # checks if the variable holds letters
print(greeting.islower()) # checks if the variable is in lower case
print(greeting.endswith("!")) # checks if it ends with a "!"
print(greeting.startswith("H")) # checks if it starts with a "H"
```

`strip()` method
```python
white_space = "lots of space at the end          "
print(len(white_space))
print(len(white_space.strip())) # .strip() removes white space
```

`count()` method
```python
# counts number of times the string is mentioned
example_text = "here's SOME text with lots of text"
print(example_text.count("text")) # outputs 2
```

`upper()`, `lower()` and `capitalize()` methods
```python
example_text.upper() # all letters to upper case
example_text.lower() # all letters to lower case
example_text.capitalize() # capitalises the first letter
```

`replace()` method
```python
example_text = "here's SOME text with lots of text"

# replaces "with" with ","
print(example_text.replace("with", ","))

# Outputs "here's SOME text , lots of text"
print(example_text)
```