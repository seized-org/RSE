from cryptography.fernet import Fernet # Using cryptography package.
from datetime import date
import base64
time = date.today()
startyesno = input("Would You Like to Encrypt a Message? yes/no: ")
if startyesno >= 'yes':
    message = input("[+] Please Type the Message to Encrypt: ") # Need user intercation in order to have a msg to encrypt.
    with open("SSE-DataStoring.siracrypt", "wb") as key: # Opens the data storing file
        gen_key = Fernet.generate_key()
        key.write(gen_key) # Writes the fernet key

    with open("SSE-DataStoring.siracrypt", "rb") as f:
        first_line_read = f.readline()
        fernetkey = Fernet(first_line_read)    
        msg_encrypt = fernetkey.encrypt(message.encode())
        print(time.strftime("%d/%m/%Y"),"[+] Your Decryption Key is:", first_line_read) # Prints The generated key so it can be store it yourself, everywhere
        print(time.strftime("%d/%m/%Y"), "[+] Your New Message is: ", msg_encrypt) # Prints the encrypted message

    with open("SSE-DataStoring.siracrypt", "wb") as f: # Opening an existing file to store the fernet key for later use
        f.write(first_line_read) # Writes the first line / fernet key on the file
        print(time.strftime("%d/%m/%Y"),"[+] Saving Fernet Key In SSE_DataStoring.txt...")
if startyesno >= 'no':

    # Prints a notification that the program stored your ferent key in SSE_DataStoring.txt
    # It does that so you will be able to remember the key and also to use that key for futher msg's
    # IN ORDER TO DECRYPT MESSAGES, PLEASE PUT THE MESSAGES IN InsertEncryptedMessagesToHereInOrderToDecryptThem.siracrypt AND FERNET KEYS IN InsertKeysToHERE.siracrypt BEFORE TRYING TO DECRYPT MESSAGES!
    # AFTER DECRYPTING THE MESSAGE YOU WANTED TO DECRYPT, YOU'LL BE ABLE TO SEE THE DECRYPTED MESSAGE INSIDE InsertEncryptedMessagesToHereInOrderToDecryptThem.siracrypt FILE!
#yesandno = input("[+] Would You Like to Decrypt a Message? ")
#if yesandno >= "yes":
    #with open("InsertKeysToHERE.siracrypt", "rb") as fileskey:
        #key = fileskey.readline()
        #f1 = Fernet(key)
#try:
        #return fernet1.decrypt(data).decode()
    #except InvalidToken:
        #None

    yesandno = input("[+] Would You Like to Decrypt a Message? yes/no: ")
if yesandno >= "yes":
    with open("InsertEncryptedMessagesToHereInOrderToDecryptThem.siracrypt", 'rb') as enc: # Reads file
        encryptedd = enc.read() # Will read the file once executing variable
    with open("InsertKeysToHERE.siracrypt", 'rb') as keysfile:
        key = keysfile.readline()
        #key = input("[+] Type the Fernet Key to Decrypt: ") # Asks user for the fernet key that came with the encrypted file
        f = Fernet(key) # Setting a new variable for Fernet and specifying the fernet key
        decrypting = f.decrypt(encryptedd) # Decrypting file using fernet key
        with open("InsertEncryptedMessagesToHereInOrderToDecryptThem.siracrypt", 'wb') as dec:
            dec.write(decrypting) # Writing the decrypted strings in the file


#if yes_no >= "yes":
    #key = input("[+] Type the Fernet Key: ")
    #f = Fernet(key)
    #token = input("[+] Type the Message To Decrypt: ")
    #f.decrypt(token)
    #print("[+] Your Decrypted Message is: ", dec)
yesno = input("[+] Would You Like to Encrypt a File? yes/no: ") # User Intercation if the user would like to encrypt a file
if yesno >= "yes": # If user types "yes" it will move further:
    key = Fernet.generate_key() # Generating a new fernet key and storing it on the short term memory
    fileencrypt = input("[+] Please Specify the Path to the File to Encrypt: ") # User intercation, if the user wanted to encrypt a file, now the user needs to specify the file path
    with open("SSE-DataStoring.siracrypt", 'wb') as keyinfile: # Opening the Data file as keyinfile
        keyinfile.write(key) # Writing key inside the Data file
        f = Fernet(key) # Sets "f" as the new variable of Fernet(key)
        with open(fileencrypt, "rb") as file: # Reading the file we want to encrypt
            org = file.read() # Original file is a variable of file.read()
            encrypted = f.encrypt(org) # Fernet encrypts the Original file we want to encrypt
            with open(fileencrypt, "wb") as encrypted_file: # Writing original file
                encrypted_file.write(encrypted) # Writing the new encryption so the file we encrypt is now encrypted
                print(time.strftime("%d/%m/%Y"),"[+] Your Encrypted File is: ", fileencrypt) # Letting user know the file is encrypted
                print(time.strftime("%d/%m/%Y"),"[+] Your Decryption Key is: ", key) # Printing the fernet key in order to decrypt the file
if yesno >= "no": # If the user types no we will be moving to the decryption part
    print(time.strftime("%d/%m/%Y"),"Waiting for System Intercation..") # Sets a very short delay again..

    yes_nos = input("[+] Would You Like to Decrypt a File? yes/no: ") # # User intercation
if yes_nos >= "yes": # If user types yes, it will move further...
    fileencrypted = input("[+] Please Specify the Path to the Encrypted File: ") # Asks file to decrypt
    with open(fileencrypted, 'rb') as enc: # Reads file
        encryptedd = enc.read() # Will read the file once executing variable
    with open("InsertKeysToHERE.siracrypt", 'rb') as keysfile: # INSERT YOUR FERNET KEY BEFORE EXECUING THE DECRYPTION PART
        key = keysfile.readline() # Reads first line of the file( the file with the key! )
        #key = input("[+] Type the Fernet Key to Decrypt: ") # Asks user for the fernet key that came with the encrypted file
        f = Fernet(key) # Setting a new variable for Fernet and specifying the fernet key
        decrypting = f.decrypt(encryptedd) # Decrypting file using fernet key
        with open(fileencrypted, 'wb') as dec: #
            dec.write(decrypting) # Writing the decrypted strings in the file
        print(time.strftime("%d/%m/%Y"),"[+] File Decrypted With Code 0.")
            
else:  # If user didn't want to decrypt a file he will be send to line 74
    print(time.strftime("%d/%m/%Y"),"[-] Exiting Program...") # Prints that the application is closing
    
    
    
    
    







    
    
