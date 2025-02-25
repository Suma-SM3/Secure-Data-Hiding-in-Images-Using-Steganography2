# Secure-Data-Hiding-in-Images-Using-Steganography2
1. Installation
    Prerequisites:
     Ensure you have Python installed on your system. You can download it from here.
    
    Install Required Libraries:
     Run the following command to install the necessary dependencies:
          pip install opencv-python

2. Usage
   Encryption (Hiding a Message in an Image) :
     I. Place the image you want to use in the project folder.
    II. Open a terminal or command prompt and run the script:
         python encrypt.py
   III. Enter the secret message when prompted.
    IV. Set a password for encryption.
     V. The encrypted image will be saved as encryptedImage.png in the project folder.
    VI. A file named password.txt will be generated, storing the password for decryption.

  Decryption (Retrieving the Hidden Message) :
   I. Ensure that the encryptedImage.png and password.txt files exist in the project folder.
  II. Open a terminal or command prompt and run:
       python decrypt.py
 III. Enter the correct password.
  IV. If the password matches, the hidden message will be displayed. If incorrect, access will be denied.
