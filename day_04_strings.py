# --- 1. String Creation & Multiline Strings ---
single_quote = 'Machine Learning'
double_quote = "Data Science"
multiline_doc = """This is a multiline string.
Useful for dataset descriptions or model docstrings."""

# --- 2. Indexing and Slicing ---
# Indexing starts at 0. Negative indices count from the end.
text = "Deep Learning"
print("First character:", text[0])       # 'D'
print("Last character:", text[-1])       # 'g'

# Slicing: [start:stop:step] (stop index is excluded)
print("Substring (0-4):", text[0:4])     # 'Deep'
print("Substring (5 to end):", text[5:])  # 'Learning'
print("Reversed string:", text[::-1])    # 'gninraeL peeD'

# --- 3. String Methods (Crucial for Data Cleaning) ---
raw_text = "  python for machine learning  "

print("Stripped whitespace:", raw_text.strip())       # Removes outer spaces
print("Uppercase:", raw_text.upper())                 # Converts to uppercase
print("Title case:", raw_text.title())                # Capitalizes words
print("Replace text:", raw_text.replace("python", "Py")) 

# Check contents
print("Starts with space?", raw_text.startswith(" ")) # True
print("Contains 'learning'?", "learning" in raw_text)  # True

# Splitting and Joining
csv_row = "age,salary,purchased"
columns = csv_row.split(",")                          # Splits into a list
print("Split columns:", columns)

joined_text = " - ".join(columns)                     # Joins list into string
print("Joined string:", joined_text)

# --- 4. String Formatting (f-strings) ---
model_name = "RandomForest"
accuracy = 0.94582

# f-strings allow embedding variables directly with formatting control
formatted_message = f"Model: {model_name} | Accuracy: {accuracy:.2%}"
print(formatted_message)                              # Outputs: Model: RandomForest | Accuracy: 94.58%