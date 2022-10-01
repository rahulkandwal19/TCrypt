# Functions to peform encryption & decryption of passed string
#------------------------------------------------------------------------------------------------------------------------------------------------------
# Function to Encrypt Text 
def text_encrypt(Text):
    msg_encrypt = Text
    decrypt_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    encrypt_string = '∮₩⊥∥∞¾Ɣƕ‰Þ¡§¶∫∱ωΓΔΞξρσγδζηθι∰κλμνετ�¼υφβα∯ΣΦΨΩ~`฿Ϣֆ½ƱƷǢǷɄͶЖЉЮѪ'
    #Using loop to convert passed string into encrypted form character by character.
    for character in decrypt_string :
          new_character = encrypt_string[decrypt_string.index(character)]
          msg_encrypt = msg_encrypt.replace(character,new_character)
    # Returning Encrypted Text 
    return msg_encrypt
#------------------------------------------------------------------------------------------------------------------------------------------------------
# Function to Decrypt Text 
def text_decrypt(Text):
    msg_decrypt = Text
    decrypt_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    encrypt_string = '∮₩⊥∥∞¾Ɣƕ‰Þ¡§¶∫∱ωΓΔΞξρσγδζηθι∰κλμνετ�¼υφβα∯ΣΦΨΩ~`฿Ϣֆ½ƱƷǢǷɄͶЖЉЮѪ'
    # Using loop to convert passed string into decrypted form character by character.
    for character in  encrypt_string :
          new_character = decrypt_string [encrypt_string.index(character)]
          msg_decrypt = msg_decrypt.replace(character,new_character)
    # Returning Decrypted Text 
    return msg_decrypt
#------------------------------------------------------------------------------------------------------------------------------------------------------
'''
-------------------------------------------------------------------------------------------------------------------
email - rahulkandwal19@outlook.com | github - rahulkandwal19 
instagram -  @rahulkandwal19 | twitter - @rahulkandwal19
-------------------------------------------------------------------------------------------------------------------
'''
