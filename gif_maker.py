from PIL import Image
import os

def create_gif(source_folder, output_file, duration):
    frames = []
    # Loop through all files in the source folder
    for file_name in sorted(os.listdir(source_folder)):
        if file_name.endswith('.png'):
            file_path = os.path.join(source_folder, file_name)
            frames.append(Image.open(file_path))

    # Save frames as a gif
    frames[0].save(output_file, format='GIF', append_images=frames[1:], save_all=True, duration=duration, loop=0)

# Define parameters
source_folder = '../photoset'
output_file = '../output.gif'
frame_duration = 1000  # Duration for each frame in milliseconds

# Create the GIF
create_gif(source_folder, output_file, frame_duration)

print("GIF created successfully.")
