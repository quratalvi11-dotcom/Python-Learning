# --- 1. Creating and Accessing Tuples ---
# Representing an image tensor shape: (height, width, channels)
image_shape = (224, 224, 3)
model_hyperparams = ("adam", 0.001, 32)

print("Image Height:", image_shape[0])
print("Image Channels:", image_shape[-1])

# --- 2. Tuples are Immutable ---
# Uncommenting the line below will throw a TypeError:
# image_shape[0] = 512  # Tuples cannot be modified after creation!

# --- 3. Tuple Unpacking (Crucial for ML Function Returns) ---
# Machine learning functions often return multiple values as a tuple
def get_dataset_split():
    # Returns (X_train, X_test, y_train, y_test)
    return [1, 2, 3], [4], [0, 1, 1], [0]

# Unpacking the tuple directly into variables
X_train, X_test, y_train, y_test = get_dataset_split()
print("Training Features:", X_train)
print("Testing Features:", X_test)

# --- 4. Useful Tuple Methods ---
numbers = (1, 2, 2, 3, 4, 2, 5)

print("Count of '2':", numbers.count(2))  # Counts occurrences
print("Index of '3':", numbers.index(3))  # Finds first index of value

# --- 5. Converting Between Lists and Tuples ---
# Convert tuple to list to modify it, then back to tuple
shape_list = list(image_shape)
shape_list[0] = 512
image_shape_updated = tuple(shape_list)

print("Updated Image Shape:", image_shape_updated)