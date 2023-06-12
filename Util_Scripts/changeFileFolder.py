import os
import shutil

# Specify the root directory path
root_directory = 'D:\AI-ML\Datasets\pokemonImagesTypes\images\PokemonData'

# Iterate through each child directory in the root directory
for child_directory in os.listdir(root_directory):
    child_directory_path = os.path.join(root_directory, child_directory)

    # Check if it's a directory
    if os.path.isdir(child_directory_path):
        
        # Iterate through each file in the child directory
        for index, filename in enumerate(os.listdir(child_directory_path)):
            # Move Files to new folder

            file_path = os.path.join(child_directory_path, filename)
            destinationPath = "D:\AI-ML\Datasets\pokemonImagesTypes\images\PrepedImages"
          
            shutil.copy(file_path, destinationPath)
