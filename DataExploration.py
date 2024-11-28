import pandas as pd  # Import the pandas library for DataFrame operations

# Create a DataFrame with fruit data, indexed by city names
data = {"Apples": [102, 500, 250, 73], "Grapes": [50, 150, 95, 45]}  
df = pd.DataFrame(data, index=["Mumbai", "Pune", "Nagpur", "Nashik"])  

print(df[['Grapes']])  # Select and display the column 'Grapes' as a DataFrame

# Add a new column 'Banana', calculated by adding 150 to 'Grapes'
df["Banana"] = df["Grapes"] + 150  

# Add more columns with calculations based on existing columns
df["pear"] = df["Grapes"] + 15  
df["straberry"] = df["pear"] + 50  
df["oranges"] = df["Grapes"] + 10  
df["kiwi"] = df["straberry"] + 120  
df["mangoes"] = df["kiwi"] + 100  

# Example of row selection using loc and iloc
# Select row by index position (e.g., 3 for Nashik)
# print(df.iloc[[3]])  

# Select row by label name (e.g., 'Nagpur')
# print(df.loc[["Nagpur"]])  

# Select a range of rows using iloc
# print(df.iloc[0:2])  

# Select a range of rows using loc by label name
# print(df.loc["Pune":"Nagpur"])  

# Create a DataFrame for student marks
students_marks = {
    "Name": ["Vipul", "Yash", "Harsh", "Harshal", "Sakshi", "Sid"],  
    "OS": [95, 60, 45, 75.5, 15, 46],  
    "DBMS": [96, 63, 25.6, 84, 65, 84]  
}
df1 = pd.DataFrame(students_marks)  # Create DataFrame with students' data

# Adding a new row using concatenation
data3 = {"Name": "Venom", "OS": 70, "DBMS": 89}  # Define a new row
df3 = pd.DataFrame(data3, index=[0])  # Create a DataFrame for the new row

data4 = {"Name": "Deadpool", "OS": 90, "DBMS": 39}  # Define another new row
df4 = pd.DataFrame(data4, index=[0])  # Create a DataFrame for this new row

# Concatenate the new rows into the existing DataFrame
df1 = pd.concat([df1, df4, df3])  

# Calculate and add a new column for average marks
df1["Avg_marks"] = (df1["OS"] + df1["DBMS"]) / 2  

# Display statistical exploration of the DataFrame
# print(df1.head(4))  # Display the first 4 rows
# print(df1.tail())   # Display the last 5 rows
# print(df1.dtypes)   # Display the data types of columns
# print(df1.empty)    # Check if the DataFrame is empty
# print(df1.ndim)     # Display the number of dimensions of the DataFrame
# print(df1.shape)    # Display the shape (rows, columns) of the DataFrame
# print(df1.size)     # Display the total number of elements in the DataFrame
# print(df1.values)   # Display the values as a NumPy array
# print(df1.describe())  # Display a statistical summary of the DataFrame
# print(df1.T)        # Display the transpose of the DataFrame
# print(df1.sum(1))   # Calculate the sum of values along rows
# print(df1.mean(1))  # Calculate the mean of values along rows
# print(df1.median(1))  # Calculate the median of values along rows
print(df1.mode(1))    # Calculate the mode along rows
