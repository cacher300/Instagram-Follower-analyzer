# Define the filenames for the text files containing names
file2 = "1.txt"
file1 = "2.txt"

# Read names from the first text file into a set
with open(file1, "r", encoding="utf-8") as f1:
    list1 = [line.strip() for line in f1]

# Read names from the second text file into a set
with open(file2, "r", encoding="utf-8") as f2:
    list2 = [line.strip() for line in f2]

# Convert both lists to sets for efficient membership testing
set1 = set(list1)
set2 = set(list2)

# Find names in list1 that are not in list2
names_not_in_list2 = set1 - set2

# Print the result
print("Names in", file1, "that don't appear in", file2 + ":")
for name in names_not_in_list2:
    print(name)



