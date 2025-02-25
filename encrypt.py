import cv2
import os

# Define paths
IMAGE_PATH = r"C:\Users\admin\Desktop\Steganography_Project\img.png" 
OUTPUT_IMAGE = r"C:\Users\admin\Desktop\Steganography_Project\encryptedImage.png"  # Use PNG to prevent compression issues
PASSWORD_FILE = r"C:\Users\admin\Desktop\Steganography_Project\password.txt"

def encrypt_message(image_path, message, password, output_image):
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Image not found at {image_path}")
        return

    d = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = d[char]
        z = (z + 1) % 3  # Cycle through BGR channels
        if z == 0:  
            m += 1
            if m >= img.shape[1]:  # Move to the next row if needed
                m = 0
                n += 1

    cv2.imwrite(output_image, img)  # Save as PNG to avoid compression issues

    # Store the password in a file
    with open(PASSWORD_FILE, "w") as file:
        file.write(password)

    print(f"Encryption Successful! Encrypted image saved at {output_image}")

if __name__ == "__main__":
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    encrypt_message(IMAGE_PATH, message, password, OUTPUT_IMAGE)
