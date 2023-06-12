import os
import shutil

# Paths to the Images and Poses folders
images_folder = 'D:\AI-ML\Datasets\pokemonImagesTypes\images\PokedexImages'
poses_folder = 'D:\AI-ML\Datasets\pokemonImagesTypes\images\PokemonData'

# Iterate through each file in the Images folder
for filename in os.listdir(images_folder):
    # Get the file name without the extension
    name_without_extension, _ = os.path.splitext(filename)
    name_without_extension = name_without_extension.capitalize()
    # Construct the source path (file to be moved)
    source_path = os.path.join(images_folder, filename)
    
    # Construct the destination directory
    dest_dir = os.path.join(poses_folder, name_without_extension)
    
    # Check if the destination directory exists
    if os.path.exists(dest_dir):
        # Construct the full destination path
        dest_path = os.path.join(dest_dir, filename)
        # Move the file to the destination directory
        shutil.move(source_path, dest_path)
    else:
        print(f"Directory not found: {dest_dir}")
        print(f"Making Directory: {dest_dir}")

        # Make the destination directory
        os.mkdir(dest_dir)
        # Construct the full destination path
        dest_path = os.path.join(dest_dir, filename)
        # Move the file to the destination directory
        shutil.move(source_path, dest_path)