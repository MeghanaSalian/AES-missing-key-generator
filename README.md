# AES-missing-key-generator

This python code brute forces the missing bits for AES key (in hexadecimal format) and recover the plaintext. Decryption is done using OpenSSL version *OpenSSL 1.1.1i  8 Dec 2020*

**Input**:

  Document to be decrypted in .aes format
  
**Output**
 
  Plain text
  
 ## Steps to run the code
 

* Install OpenSSL (Version : *OpenSSL 1.1.1i  8 Dec 2020*) for Windows from:
    https://curl.se/windows/dl-7.76.1/openssl-1.1.1k-win64-mingw.zip
 
* In the code, enter the key under the variable 's'. Under cmd variable enter the .aes file to be decrypted.
 
* See to that the .aes file is in same location as that of keygen.py file.
 
* Navigate to the program directory and run `python keygen.py`
