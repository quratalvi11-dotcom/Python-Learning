# --- 1. Basic List Comprehension Syntax ---
# Syntax: [expression for item in iterable]

# Traditional 'for loop' approach:
squares_loop = []
for x in range(10):
    squares_loop.append(x ** 2)

# Equivalent List Comprehension approach:
squares_comp = [x ** 2 for x in range(10)]
print("Squares (List Comp):", squares_comp)


# --- 2. Filtering Data with Conditions (if) ---
# Syntax: [expression for item in iterable if condition]
# Filtering out low accuracy values / noisy data
scores = [0.45, 0.88, 0.92, 0.31, 0.76, 0.95]

high_accuracy_scores = [score for score in scores if score >= 0.80]
print("High Accuracy Scores (>= 0.80):", high_accuracy_scores)


# --- 3. Conditional Transformations (if-else) ---
# Syntax: [expression_if_true if condition else expression_if_false for item in iterable]
# Labeling predictions as 'Pass' (1) or 'Fail' (0) based on threshold
probabilities = [0.85, 0.42, 0.78, 0.12, 0.91]
binary_predictions = [1 if p >= 0.5 else 0 for p in probabilities]
print("Binary Predictions:", binary_predictions)


# --- 4. Text Data Preprocessing (NLP Application) ---
# Stripping whitespace and lowercasing raw feature text
raw_categories = ["  Cat ", "DOG", "  Bird  ", "FISH  "]
cleaned_categories = [cat.strip().lower() for cat in raw_categories]
print("Cleaned Categories:", cleaned_categories)


# --- 5. Flattening a 2D Matrix (Common in Data Manipulation) ---
# Converting a 2D array/matrix into a 1D vector
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [val for row in matrix for val in row]
print("Flattened Matrix:", flattened_matrix)