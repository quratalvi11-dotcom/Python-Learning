# --- 1. Creating and Accessing Lists ---
# Lists can hold multiple data types
features = ["age", "income", "credit_score", "loan_status"]
scores = [0.85, 0.92, 0.78, 0.88]

print("First feature:", features[0])       # Indexing starts at 0
print("Last feature:", features[-1])       # Negative indexing
print("Subset of features:", features[1:3]) # Slicing [start:stop]

# --- 2. Modifying Lists ---
features[0] = "age_in_years"               # Reassigning an item
print("Updated features:", features)

# --- 3. Essential List Methods for Data Science ---
loss_history = []                          # Empty list to track training loss

# .append(): Adds a single element to the end
loss_history.append(0.54)
loss_history.append(0.32)
loss_history.append(0.18)
print("Loss History:", loss_history)

# .insert(): Adds an element at a specific index
loss_history.insert(0, 0.89)               # Insert initial loss at index 0
print("With Initial Loss:", loss_history)

# .remove() and .pop(): Removing elements
loss_history.remove(0.89)                  # Removes specific value
popped_val = loss_history.pop()            # Removes and returns last item
print("Popped value:", popped_val)
print("Remaining Loss History:", loss_history)

# --- 4. Useful Functions with Numeric Lists ---
epoch_acc = [0.65, 0.72, 0.81, 0.89, 0.94]

print("Total Epochs:", len(epoch_acc))
print("Minimum Accuracy:", min(epoch_acc))
print("Maximum Accuracy:", max(epoch_acc))
print("Sum of Accuracies:", sum(epoch_acc))

# Sorting lists
nums = [42, 12, 89, 7, 23]
nums.sort()                                # Modifies list in-place (ascending)
print("Sorted numbers:", nums)
nums.sort(reverse=True)                    # Descending order
print("Descending numbers:", nums)

# --- 5. Checking Existence ---
print("income" in features)                # Returns True
print("zip_code" in features)              # Returns False