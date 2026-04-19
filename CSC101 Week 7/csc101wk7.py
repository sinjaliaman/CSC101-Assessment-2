# Store the file name in a variable
filename = 'csc101wk7.txt'

# Step 1: Open the file in read mode ("r")
file = open(filename, 'r')

# Step 2: Read the entire contents of the file as one string
contents = file.read()

# Step 3: Close the file (good practice)
file.close()

# Step 4: Display the file name
print("File name:", filename)

# Step 5: Display the contents of the file
print("\nFile contents:")
print(contents)

# Step 6: Display the total number of characters in the file
print("\nTotal characters:", len(contents))
