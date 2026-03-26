print("Data Redundancy Removal System")

data = input("Enter data separated by commas: ")

data_list = [item.strip() for item in data.split(",")]

unique_data = []
duplicates = []

for item in data_list:
    if item not in unique_data:unique_data.append(item)
else:duplicates.append(item)

print("Unique Data:", unique_data)
print("Removed Duplicates:", duplicates)