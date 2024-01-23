from PIL import Image
import os

def create_gif(source_folder, output_file, duration):
    frames = []

    # Sort files based on numeric value assuming file format like 'image_1.png', 'image_2.png', etc.
    files = sorted(os.listdir(source_folder), key=lambda x: int(x.split('_')[-1].split('.')[0]))

    # Loop through all sorted files in the source folder
    for file_name in files:
        if file_name.endswith('.png'):
            file_path = os.path.join(source_folder, file_name)
            try:
                img = Image.open(file_path)
                frames.append(img)
            except IOError:
                print(f"Could not open file: {file_path}")

    # Save frames as a gif
    if frames:
        frames[0].save(output_file, format='GIF', append_images=frames[1:], save_all=True, duration=duration, loop=0)
        print("GIF created successfully.")
    else:
        print("No frames to create GIF.")

# Define parameters
source_folder = '../photoset'
output_file = '../output.gif'
frame_duration = 200  # Duration for each frame in milliseconds

# Create the GIF
create_gif(source_folder, output_file, frame_duration)
