# Conditional Statements
### 1. Problem: **FizzBuzz Custom**

#Problem Statement:
# Write a function `fizzBuzzCustom(n, x, y)` that takes three integers: `n`, `x`, and `y`. For each number from 1 to `n`, return:
# - `"Fizz"` if the number is divisible by `x`,
# - `"Buzz"` if the number is divisible by `y`,
# - `"FizzBuzz"` if the number is divisible by both `x` and `y`,
# - Otherwise, return the number itself.



# Example 1
# Input: n = 15, x = 3, y = 5
# Output: [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

# Example 2
# Input: n = 10, x = 2, y = 4
# Output: [1, "Fizz", 3, "FizzBuzz", 5, "Fizz", 7, "FizzBuzz", 9, "Fizz"]




### 2. Problem: **Triangle Type**

#Problem Statement:
# Write a function `triangleType(a, b, c)` that takes the lengths of three sides of a triangle `a`, `b`, and `c`. Determine the type of triangle:
# - Return `"Equilateral"` if all sides are equal,
# - Return `"Isosceles"` if exactly two sides are equal,
# - Return `"Scalene"` if all sides are different,
# - If the sides do not form a valid triangle, return `"Not a triangle"`.



# Example 1
# Input: a = 3, b = 3, c = 3
# Output: "Equilateral"

# Example 2
# Input: a = 5, b = 5, c = 8
# Output: "Isosceles"

# Example 3
# Input: a = 2, b = 3, c = 5
# Output: "Not a triangle"




### 3. Problem: **Character Case Identifier**

#Problem Statement:
# Write a function `identifyCase(char)` that takes a single character `char` and returns:
# - `"Uppercase"` if the character is an uppercase letter,
# - `"Lowercase"` if the character is a lowercase letter,
# - `"Digit"` if the character is a digit (0-9),
# - `"Special Character"` if it’s any other character.



# Example 1
# Input: char = 'A'
# Output: "Uppercase"

# Example 2
# Input: char = 'g'
# Output: "Lowercase"

# Example 3
# Input: char = '#'
# Output: "Special Character"




### 4. Problem: **Month Days**

#Problem Statement:
# Write a function `daysInMonth(month, year)` that takes an integer `month` (1-12) and an integer `year`, and returns the number of days in that month. Remember that February has 29 days in a leap year.


# Example 1
# Input: month = 2, year = 2020
# Output: 29

# Example 2
# Input: month = 4, year = 2021
# Output: 30

# Example 3
# Input: month = 2, year = 1900
# Output: 28




### 5. Problem: **Password Strength Checker**

#Problem Statement:
# Write a function `passwordStrength(password)` that takes a string `password` as input and returns the password strength:
# - Return `"Weak"` if the password is less than 6 characters long,
# - Return `"Moderate"` if the password is at least 6 characters and contains either only letters or only numbers,
# - Return `"Strong"` if the password is at least 6 characters and contains both letters and numbers.


# Example 1
# Input: password = "12345"
# Output: "Weak"

# Example 2
# Input: password = "abcdef"
# Output: "Moderate"

# Example 3
# Input: password = "abc123"
# Output: "Strong"

