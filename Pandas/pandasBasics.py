from operator import index

import pandas as pd

# -------------------------------
# 1. Creating DataFrames
# -------------------------------

# From dictionary

data = {
    "Name": ["Aparna", "Richa", "Mrunal", "Amruta", "Shital","Laxmi","Sameer"],
    "Age": [23,23,24,25,26,26,NaN],
    "City": ["Pune","Mumbai","Nashik","Delhi","Chennai", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)
print("Initial data")
print(df, '\n')

# -------------------------------
# 2. Reading & Writing CSV Files
# -------------------------------

# Save to CSV
df.to_csv("people.csv", index = False)

#Read from CSV
df_csv = pd.read_csv("people.csv")
print("Read from CSV:")
print(df_csv, "\n")


# -------------------------------
# 3. Reading & Writing JSON Files
# -------------------------------

df.to_json("people.json")
df_json = pd.read_json("people.json")
print("Read fron json")
print(df_json, '\n')

# -------------------------------
# 4. Selecting Columns
# -------------------------------

print("Select one column (Name):")
print(df["Name"], "\n")


print("Select multiple columns (Name, City):")
print(df[["Name", "City"]], "\n")

# -------------------------------
# 5. Selecting Rows
# -------------------------------

print("Select first 2 rows:")
print(df.head(2), '\n')

print("Select row by index (loc):")
print(df.loc[2], '\n')

print("Select row by position (iloc):")
print(df.iloc[2], '\n')

#example showing index and positions are different
datax = pd.DataFrame({
    "empName": ["Karan", "Arjun"],
    "empPost": ["Sr.Developer", "Jr.Developer"]
}, index = [101, 102])

print(datax, "\n")

print("select row by index: ")
print(datax.loc[101], "\n")

print("select row by position: ")
print(datax.iloc[1], "\n")

# -------------------------------
# 6. Filtering Data
# -------------------------------

print("People older than 25:")
print(df[df["Age"] > 23], "\n")

print("People from Mumbai:")
print(df[df["City"] == "Mumbai"], "\n")

# -------------------------------
# 7. Adding New Column
# -------------------------------

df["Age+5"] = df["Age"] + 5
print("New Column added:")
print(df, "\n")

# -------------------------------
# 8. Updating Values
# -------------------------------

df.loc[3, "Name"] = "Yuvi"
print("Updated Name from Amruta to Yuvi:")
print(df.loc[3])

# -------------------------------
# 9. Deleting Columns & Rows
# -------------------------------

df2 = df.drop(columns = "Age+5") #delete column
print("After deleting column Age+5:")
print(df2, "\n")

df3 = df.drop(index=2)
print("After deleting row 2:")
print(df3, "\n")

# -------------------------------
# 10. Sorting
# -------------------------------

print("Sorted by Age:")
print(df.sort_values("Age"), "\n")

print("Sorted by Name descending:")
print(df.sort_values("Name", ascending=False), "\n")

# -------------------------------
# 11. GroupBy
# -------------------------------
group_data = df.groupby("City")["Age"].mean()
print("Average age per city (GroupBy):")
print(group_data, "\n")

# -------------------------------
# 12. Missing data
# -------------------------------
print("Check values are NULL / missing")
df1 = df.isnull()
print(df1, "\n")

print("Drop missing data row")
df2 = df.dropna()
print(df2, "\n")

print("Replaces all missing values with Unknown (or any value you give)")
df3= df.fillna("Unknown")
print(df3, "\n")

print("Replaces missing values in numeric columns with the average (mean) of that column.")
df4 = df.fillna(df["Age"].mean())
print(df4, "\n")

# -------------------------------
# 13. Basic Statistics
# -------------------------------
print("Statistics Summary:")
print(df.describe())
