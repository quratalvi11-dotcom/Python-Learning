# --- 1. Arithmetic Operators (Used for ML formulas/loss functions) ---
a = 15
b = 4

print("Addition:", a + b)           # 19
print("Subtraction:", a - b)        # 11
print("Multiplication:", a * b)     # 60
print("Division:", a / b)           # 3.75
print("Floor Division:", a // b)    # 3 (truncates decimals)
print("Modulus:", a % b)            # 3 (remainder)
print("Exponentiation:", a ** b)    # 50625 (15^4)

# --- 2. Comparison Operators (Returns True or False) ---
y_true = 10
y_pred = 12

print("Equal:", y_true == y_pred)         # False
print("Not Equal:", y_true != y_pred)     # True
print("Greater Than:", y_pred > y_true)    # True
print("Less Than or Equal:", y_pred <= 10) # True

# --- 3. Logical Operators (and, or, not) ---
# Useful for filtering data in datasets
has_high_accuracy = True
has_low_loss = False

print("Both conditions met:", has_high_accuracy and has_low_loss) # False
print("At least one met:", has_high_accuracy or has_low_loss)     # True
print("Negation:", not has_high_accuracy)                          # False

# --- 4. Assignment & Compound Operators ---
epoch_count = 0
epoch_count += 1  # Equivalent to epoch_count = epoch_count + 1
print("Current Epoch:", epoch_count)