import os

# Specify the root directory path
root_directory = 'D:\AI-ML\Datasets\pokemonImagesTypes\images\PokemonData'

# Iterate through each child directory in the root directory
for child_directory in os.listdir(root_directory):
    child_directory_path = os.path.join(root_directory, child_directory)

    # Check if it's a directory
    if os.path.isdir(child_directory_path):
        
        # Iterate through each file in the child directory
        for index, filename in enumerate(os.listdir(child_directory_path)):
            # Construct the old and new file paths
            old_file_path = os.path.join(child_directory_path, filename)
            new_file_name = f"{child_directory}_{index}{os.path.splitext(filename)[1]}"
            new_file_path = os.path.join(child_directory_path, new_file_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)

            print(f"Renamed: {old_file_path} -> {new_file_path}")
