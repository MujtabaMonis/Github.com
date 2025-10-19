import pandas as pd

# Read the CSV file
df = pd.read_csv("student data.csv")

# Function to determine grade based on percentage
def get_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

# Apply the function to create a new column
df["Grade"] = df["Percentage"].apply(get_grade)

# Write the updated data to a new CSV file
df.to_csv("student_data_with_grades.csv", index=False)

print("✅ New file created: student_data_with_grades.csv")
