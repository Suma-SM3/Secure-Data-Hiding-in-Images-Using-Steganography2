import cv2
import os

# Define paths
ENCRYPTED_IMAGE = r"C:\Users\admin\Desktop\Steganography_Project\encryptedImage.png"
PASSWORD_FILE = r"C:\Users\admin\Desktop\Steganography_Project\password.txt"

def decrypt_message(encrypted_image):
    img = cv2.imread(encrypted_image)

    if img is None:
        print(f"Error: Encrypted image not found at {encrypted_image}")
        return

    c = {i: chr(i) for i in range(255)}

    # Check if password file exists
    if not os.path.exists(PASSWORD_FILE):
        print(f"Error: Password file not found at {PASSWORD_FILE}! Run encryption first.")
        return

    password = input("Enter passcode for decryption: ")

    # Read the stored password
    with open(PASSWORD_FILE, "r") as file:
        stored_password = file.read().strip()

    if password == stored_password:
        message = ""
        n, m, z = 0, 0, 0
        while True:
            try:
                char = c[img[n, m, z]]
                if char == "\x00":  # Stop reading when null character is reached
                    break
                message += char
                z = (z + 1) % 3
                if z == 0:  
                    m += 1
                    if m >= img.shape[1]:  # Move to the next row if needed
                        m = 0
                        n += 1
            except:
                break  # Stop if out of bounds

        print("Decryption message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED")

if __name__ == "__main__":
    decrypt_message(ENCRYPTED_IMAGE)
