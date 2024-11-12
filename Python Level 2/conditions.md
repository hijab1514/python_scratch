In Python, conditions are used to perform different actions based on whether a condition is true or false. Here’s a quick look at basic conditional statements with examples.

### 1. **if Statement**
The `if` statement runs a block of code only if the condition is true.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

**Output**:
```
x is greater than 5
```

### 2. **if-else Statement**
The `if-else` statement provides an alternative path if the condition is false.

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

**Output**:
```
x is not greater than 5
```

### 3. **if-elif-else Statement**
The `if-elif-else` structure allows multiple conditions to be checked in sequence.

```python
x = 8
if x > 10:
    print("x is greater than 10")
elif x == 8:
    print("x is equal to 8")
else:
    print("x is less than 10")
```

**Output**:
```
x is equal to 8
```

### 4. **Nested if Statements**
You can nest `if` statements within each other.

```python
x = 20
if x > 10:
    print("

Here are three examples for each type of conditional statement in Python.

---

### **if Statement Examples**

1. **Check if a number is positive**
   ```python
   num = 7
   if num > 0:
       print("The number is positive")
   ```

   **Output**:
   ```
   The number is positive
   ```

2. **Check if a string contains a specific character**
   ```python
   text = "Hello, world!"
   if "H" in text:
       print("The text contains 'H'")
   ```

   **Output**:
   ```
   The text contains 'H'
   ```

3. **Check if a list is empty**
   ```python
   my_list = []
   if not my_list:
       print("The list is empty")
   ```

   **Output**:
   ```
   The list is empty
   ```

---

### **if-else Statement Examples**

1. **Check if a number is even or odd**
   ```python
   num = 4
   if num % 2 == 0:
       print("The number is even")
   else:
       print("The number is odd")
   ```

   **Output**:
   ```
   The number is even
   ```

2. **Check if a user is an adult**
   ```python
   age = 15
   if age >= 18:
       print("You are an adult")
   else:
       print("You are not an adult")
   ```

   **Output**:
   ```
   You are not an adult
   ```

3. **Check if a password is correct**
   ```python
   password = "password123"
   if password == "password123":
       print("Access granted")
   else:
       print("Access denied")
   ```

   **Output**:
   ```
   Access granted
   ```

---

### **if-elif-else Statement Examples**

1. **Grade assignment**
   ```python
   score = 85
   if score >= 90:
       print("Grade: A")
   elif score >= 80:
       print("Grade: B")
   elif score >= 70:
       print("Grade: C")
   else:
       print("Grade: F")
   ```

   **Output**:
   ```
   Grade: B
   ```

2. **Determine the time of day**
   ```python
   hour = 14
   if hour < 12:
       print("Good morning!")
   elif 12 <= hour < 18:
       print("Good afternoon!")
   else:
       print("Good evening!")
   ```

   **Output**:
   ```
   Good afternoon!
   ```

3. **Check age range**
   ```python
   age = 65
   if age < 18:
       print("You are a minor")
   elif 18 <= age < 60:
       print("You are an adult")
   else:
       print("You are a senior citizen")
   ```

   **Output**:
   ```
   You are a senior citizen
   ```

--- 

These examples show how to use different conditional structures in Python to perform actions based on conditions.
