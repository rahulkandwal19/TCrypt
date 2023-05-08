#-------------------------------------------------------------------------
# Python Program to Encrypt & Decrypt String.
#-------------------------------------------------------------------------
decrypt_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
encrypt_string = '∮₩⊥∥∞¾Ɣƕ‰Þ¡§¶∫∱ωΓΔΞξρσγδζηθι∰κλμνετ�¼υφβα∯ΣΦΨΩ~`฿Ϣֆ½ƱƷǢǷɄͶЖЉЮѪ'
#-------------------------------------------------------------------------
def encrypt(string,decrypt_string,encrypt_string):
	encrypted_text = string 
	for character in decrypt_string : 
		char_index = decrypt_string.index(character)
		newcharacter = encrypt_string[char_index]
		
		encrypt_text = encrypt_text.replace(character,newcharacter)
	
	return encrypt_text
#-------------------------------------------------------------------------



