# Function to extract coordinates from a PDBQT file
def extract_coordinates(pdbqt_file):
    x_coords = []
    y_coords = []
    z_coords = []

    with open(pdbqt_file, 'r') as f:
        for line in f:
            # PDBQT lines that start with 'ATOM' or 'HETATM' contain the coordinates
            if line.startswith('ATOM') or line.startswith('HETATM'):
                # Extract the x, y, z coordinates from the line
                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                
                # Append the coordinates to respective lists
                x_coords.append(x)
                y_coords.append(y)
                z_coords.append(z)
    
    return x_coords, y_coords, z_coords

# Function to calculate the center and box size
def calculate_box_and_center(pdbqt_file, padding=6):
    x_coords, y_coords, z_coords = extract_coordinates(pdbqt_file)
    
    # Calculate min, max, and center coordinates for x, y, z
    x_min = min(x_coords)
    x_max = max(x_coords)
    x_center = (x_max + x_min) / 2
    x_box = x_max - x_min + padding

    y_min = min(y_coords)
    y_max = max(y_coords)
    y_center = (y_max + y_min) / 2
    y_box = y_max - y_min + padding

    z_min = min(z_coords)
    z_max = max(z_coords)
    z_center = (z_max + z_min) / 2
    z_box = z_max - z_min + padding

    # Return the results
    return {
        "x_center": x_center,
        "x_box": x_box,
        "y_center": y_center,
        "y_box": y_box,
        "z_center": z_center,
        "z_box": z_box
    }

# Example usage with your pdbqt file
pdbqt_file = 'camao_fad_gromacs.pdbqt'
result = calculate_box_and_center(pdbqt_file)

# Print the returned result
print(result)
