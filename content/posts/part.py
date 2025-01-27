import os
import re

# Define the weight ranges for each part
part_ranges = {
    "Part 1": (1, 12),
    "Part 2": (13, 19),
    "Part 3": (20, 26),
    "Part 4": (27, 33),
    "Part 5": (34, 40),
    "Part 6": (41, 47),
    "Part 7": (48, 54),
    "Part 8": (55, 61),
    "Part 9": (62, 73)
    # Add more parts as needed
}

def get_part_value(weight):
    """Determine the part value based on the weight ranges."""
    for part, (min_weight, max_weight) in part_ranges.items():
        if min_weight <= weight <= max_weight:
            return part.split()[-1]  # Extract the number from "Part X"
    return "0"  # Default if no range matches

def insert_part_line(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process each line to find "weight =" and insert "part = x"
    i = 0
    while i < len(lines):
        if "weight =" in lines[i]:
            # Extract the number after "weight ="
            match = re.search(r"weight\s*=\s*(\d+)", lines[i])
            if match:
                weight = int(match.group(1))  # Convert the extracted number to an integer
                part_value = get_part_value(weight)  # Get the corresponding part value
                new_line = f"part = {part_value}\n"  # Create the new line
                lines.insert(i + 1, new_line)  # Insert the new line after "weight ="
                i += 1  # Skip the newly inserted line to avoid infinite loops
        i += 1

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

def process_directory(directory_path):
    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            print(f"Processing file: {filename}")
            insert_part_line(file_path)

# Example usage
current_directory = os.getcwd()  # Get the current working directory
process_directory(current_directory)