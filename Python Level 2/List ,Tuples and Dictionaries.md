Here's a quick breakdown of lists, tuples, and dictionaries in Python, with examples:

### 1. Lists
A list is an ordered, mutable collection in Python, meaning elements can be added, removed, or modified. Lists are defined with square brackets `[]`.

#### Examples:

**Creating a List:**
```python
my_list = [1, 2, 3, "hello", True]
```
```

my_list = [1,2,3]
my_list1 = [1,"python",5, "a"]
my_list2 = ["a","b","c"]
combined_list = [my_list, my_list1, my_list2]
print(combined_list)
```

**Extend Method:**
The `extend()` method adds elements from another list to the end of the current list.
```python
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)  # Result: [1, 2, 3, 4, 5]
```

```
my_list = [1,2,3]
my_list1 = [1,"python",5, "a"]
my_list2 = ["a","b","c"]
my_list.extend(my_list2)
my_list
```


**Adding to a List:**
Use `append()` to add a single item or `extend()` to add multiple items.
```python
my_list.append(6)  # Adds 6 to the end of my_list
my_list.extend([7, 8])  # Adds 7 and 8 to the end of my_list
```

**Sorting a List:**
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # Result: [1, 1, 3, 4, 5]
```

**A None List:**
A list with `None` values.
```python
sorted_list = alpha_list.sort()
sorted_list
print(sorted_list)
```

**Slicing a List:**
Slicing allows selecting specific parts of a list.
```python
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]  # Result: [2, 3, 4]
```

---

### 2. Tuples
A tuple is an ordered, immutable collection. Elements cannot be changed once a tuple is created. Tuples are defined with parentheses `()`.
Tuples , smiliar to list but you create them with parentheses instead of square brackets


**Example:**
```python
my_tuple = (1, 2, 3, "hello", False)
```
```
my_tuple=(1,2,3,4,5)
my_tuple[0:3]
```
---

### 3. Dictionaries
A dictionary is a collection of key-value pairs. It is unordered, mutable, and defined using curly braces `{}`.

#### Examples:

**Creating a Dictionary:**
```python
my_dict = {"name": "Alice", "age": 25, "is_student": True}
```

**Adding True and False Values:**
```python
my_dict["is_graduated"] = False
my_dict["is_employed"] = True
```

**Checking All Keys and Values:**
Use `.keys()` and `.values()` methods to get all keys and values.
```python
keys = my_dict.keys()        # Result: dict_keys(['name', 'age', 'is_student', 'is_graduated', 'is_employed'])
values = my_dict.values()    # Result: dict_values(['Alice', 25, True, False, True])
```
