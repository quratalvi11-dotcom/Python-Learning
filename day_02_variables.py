#  1. Variables & ML Naming Conventions 
# Storing basic dataset metrics
age = 26              #int: Feature (e.g., patient age)
first_name = "Qurat"  #str: Text Identifier
height = 5.4          #float: Feature(e.g., height in feet)
is_student = True     #bool: Target Indicator/Flag

# Printing variables
print("Name:", first_name )
print("Age:", age, "|Height:", height)

# Multiple assignments in one line (commonly used for model parameters)
learning_rate, epochs, accuracy = 0.01, 100, 95.5
print("Model Accuracy:", accuracy, "%")

# 2. Built-in Functions for Data Inspection
sample_data = "Machine Learning"

# len(): Checks length of string, list, array, etc.
print("Length of string:", len(sample_data))

# type(): Checks the data type
print("Data Type:", type(learning_rate))

# int(), float(), str(): Type Conversion (Casting)
num_str = "100"
converted_num = int(num_str)
print("Converted type:", type(converted_num))

# input(): Accepts input from user (returns string)
user_name = input("Enter your name: ")
print("Welcome to Day 2,", user_name)



