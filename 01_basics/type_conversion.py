# ---------------------------
# Implicit Type Conversion
# ---------------------------
# Python automatically converts smaller types to larger types
# to prevent data loss during operations.

x = 5       # int
y = 2.5     # float

z = x + y   # int + float → float
print("Implicit Type Conversion:")
print("x (int):", x)
print("y (float):", y)
print("z (x + y):", z, type(z))  # z becomes float
print()

# ---------------------------
# Explicit Type Conversion (Casting)
# ---------------------------

# int() - converts to integer
a = 3.9
b = int(a)  # decimal part truncated
print("Explicit Type Conversion:")
print("Original a (float):", a)
print("Converted to int:", b)

# float() - converts to float
c = 7
d = float(c)
print("Original c (int):", c)
print("Converted to float:", d)

# str() - converts to string
e = 100
f = str(e)
print("Original e (int):", e)
print("Converted to string:", f, type(f))

# bool() - converts to boolean
g = 0
h = bool(g)  # 0 is False, non-zero is True
print("Original g (int):", g)
print("Converted to boolean:", h)
