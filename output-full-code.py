import os

# Set the root directory path
root_directory = r"c:\codedir"

# Set the output file path
output_file = r"c:\outputfiledir.txt"

# Open the output file in write mode
with open(output_file, "w", encoding="utf-8") as file:
    # Write the legend header
    file.write("Legend:\n")
    
    # Initialize a counter for the file number
    file_number = 1
    
    # Iterate over each file in the directory and its subdirectories
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            # Check if the file has a .py extension
            if filename.endswith(".py"):
                # Get the full file path
                file_path = os.path.join(root, filename)
                
                # Write the file number and file name to the legend
                file.write(f"{file_number}. {filename}\n")
                
                # Increment the file number
                file_number += 1
    
    # Add a separator between the legend and file details
    file.write("\n" + "-" * 50 + "\n\n")
    
    # Reset the file number counter
    file_number = 1
    
    # Iterate over each file in the directory and its subdirectories
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            # Check if the file has a .py extension
            if filename.endswith(".py"):
                # Get the full file path
                file_path = os.path.join(root, filename)
                
                # Write the file number to the output file
                file.write(f"{file_number}. File: {filename}\n")
                
                # Write the file location to the output file
                file.write(f"   Location: {file_path}\n")
                
                # Open the .py file and read its contents
                with open(file_path, "r", encoding="utf-8") as py_file:
                    code = py_file.read()
                
                # Write the code to the output file
                file.write(f"   Code:\n{code}\n")
                
                # Add a separator between files
                file.write("\n" + "-" * 50 + "\n\n")
                
                # Increment the file number
                file_number += 1

print("File parsing completed. Output saved to", output_file)
