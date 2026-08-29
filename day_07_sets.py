# --- 1. Creating Sets & Uniqueness ---
# Sets automatically eliminate duplicate entries
raw_user_ids = [101, 102, 103, 101, 104, 102, 105]
unique_user_ids = set(raw_user_ids)

print("Original List with Duplicates:", raw_user_ids)
print("Unique Set:", unique_user_ids)  # Duplicates removed automatically

# --- 2. Adding and Removing Elements ---
categories = {"cat", "dog", "bird"}

categories.add("fish")        # Add single element
categories.update(["lion", "tiger"])  # Add multiple elements

categories.remove("dog")     # Removes element (raises Error if not found)
categories.discard("monkey") # Safely removes element (no error if missing)

print("Updated Categories:", categories)

# --- 3. Set Operations (Crucial for Data Preprocessing) ---
train_ids = {101, 102, 103, 104, 105}
test_ids = {104, 105, 106, 107}

# Union (|): Combine all unique IDs from both sets
all_ids = train_ids | test_ids
# or: train_ids.union(test_ids)
print("All Unique IDs:", all_ids)

# Intersection (&): Find overlapping IDs (data leakage check!)
overlapping_ids = train_ids & test_ids
# or: train_ids.intersection(test_ids)
print("Overlapping (Leaked) IDs:", overlapping_ids)

# Difference (-): Elements in train but NOT in test
train_only = train_ids - test_ids
# or: train_ids.difference(test_ids)
print("Train-only IDs:", train_only)

# Symmetric Difference (^): Elements in train OR test, but NOT both
exclusive_ids = train_ids ^ test_ids
# or: train_ids.symmetric_difference(test_ids)
print("Exclusive IDs:", exclusive_ids)

# --- 4. Membership Testing ---
print(101 in train_ids)  # Extremely fast evaluation: True