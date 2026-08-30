# --- 1. Importing Built-in Python Modules ---
import math
import random
import os

# Math module usage
print("Square root of 25:", math.sqrt(25))
print("Pi value:", math.pi)

# Random module usage (essential for data shuffling and train/test splits)
random.seed(42)  # Setting seed ensures reproducible results
dataset = [10, 20, 30, 40, 50]
random.shuffle(dataset)
print("Shuffled Dataset:", dataset)

# OS module usage (used for file path operations)
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)

# --- 2. Importing Specific Functions from Modules ---
from math import ceil, floor

print("Ceil of 4.2:", ceil(4.2))     # Rounds up -> 5
print("Floor of 4.8:", floor(4.8))   # Rounds down -> 4

# --- 3. Importing Your Custom Module ---
import ml_helpers as ml

raw_scores = [12, 45, 67, 89, 34, 100]

# Using functions from your custom module
mean_score = ml.calculate_mean(raw_scores)
scaled_scores = ml.min_max_scale(raw_scores)

print("\n--- Custom Module Metrics ---")
print("Mean Score:", round(mean_score, 2))
print("Scaled Scores:", [round(s, 2) for s in scaled_scores])
print("Random Seed from Helper:", ml.DEFAULT_RANDOM_SEED)