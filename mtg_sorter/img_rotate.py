import os
import glob
from PIL import Image

input_folder = "batch_five/"
output_folder = "images/batch_five/"
angle = 90

def rotate_images_in_folder(input_folder, output_folder, angle):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # Define the image extensions to process
    extensions = ('*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG')

    # Iterate over all files matching the extensions
    for ext in extensions:
        for file_path in glob.glob(os.path.join(input_folder, ext)):
            try:
                # Open the image file
                with Image.open(file_path) as img:
                    # Rotate the image
                    rotated_img = img.rotate(angle, expand=True)

                    # Create the new filename with a suffix and the original extension
                    file_name = os.path.basename(file_path)
                    name, extension = os.path.splitext(file_name)
                    new_file_name = f"{name}_rotated{extension}"
                    full_out_path = os.path.join(output_folder, new_file_name)

                    # Save the rotated image
                    rotated_img.save(full_out_path)
                    print(f"Rotated and saved: {file_name} to {new_file_name}")

            except IOError:
                print(f"Cannot process image file: {file_path}")
rotate_images_in_folder
if __name__ == "__main__":
    # --- Configuration ---
    # Specify your input and output folder paths
    INPUT_DIR = "batch_five/"
    OUTPUT_DIR = "images/batch_five/"
    ROTATION_ANGLE = angle # Angle in degrees clockwise (90, 180, 270 are common)

    rotate_images_in_folder(INPUT_DIR, OUTPUT_DIR, ROTATION_ANGLE)
    print("\nProcessing complete.")
