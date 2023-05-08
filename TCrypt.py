# Importing Reqired Modules 
import tkinter
import tcrypt_GUI_functions
#import pyperclip
#-----------------------------------------------------------------------------------------------------------------
# Checking if a required directory is present if not , creating it. 
tcrypt_GUI_functions.create_directory()
#-----------------------------------------------------------------------------------------------------------------
# Functions created to use as command in GUI buttons.
# Get text from input textbox and encrypting. (Function as command for encrypt button in GUI)
def get_text_encrypted():
        textinput = textbox_input.get('1.0','end-1c')
        text_encrypt = tcrypt_GUI_functions.encrypt_txt(textinput)
        textbox_output.config(state='normal')
        textbox_output.delete('1.0','end')
        textbox_output.insert(tkinter.INSERT,text_encrypt)
        textbox_output.config(state='disable')
        titlemsg_o.config(text = ' Encrypted Text is : ')
# Get text from output textbox and decrypting. (Function as command for decrypt button in GUI)
def get_text_decrypted():
        textinput = textbox_input.get('1.0','end-1c')
        text_decrypt = tcrypt_GUI_functions.decrypt_txt(textinput)
        textbox_output.config(state='normal')
        textbox_output.delete('1.0','end')
        textbox_output.insert(tkinter.INSERT,text_decrypt)
        textbox_output.config(state='disable')
        titlemsg_o.config(text = ' Decrypted Text is : ')
# Function to copy text from output textbox to clipboard. (Function as command for copy button in GUI)
def copy_textbox():
        textoutput = textbox_output.get('1.0','end-1c')
       # pyperclip.copy(textoutput)
# Function to cut text from output textbox to clipboard. (Function as command for cut button in GUI)
def cut_textbox():
        textoutput = textbox_output.get('1.0','end-1c')
       # pyperclip.copy(textoutput)
        textbox_output.config(state='normal')
        textbox_output.delete('1.0','end')
        textbox_output.config(state='disable')
        titlemsg_o.config(text = ' Output : ')
        textoutput = ''
# Function to reset program. (Function as command for reset button in GUI)
def reset_textbox():
        textbox_output.config(state='normal')
        textbox_output.delete('1.0','end')
        textbox_output.config(state='disable')
        textbox_input.delete('1.0','end')
        titlemsg_o.config(text = ' Output : ')
# Function to clear program. (Function as command for clear button in GUI)
def clear_textbox():
        textbox_output.config(state='normal')
        textbox_output.delete('1.0','end')
        textbox_output.config(state='disable')
        titlemsg_o.config(text = ' Output : ')
#-----------------------------------------------------------------------------------------------------------------
# Standard GUI For Main Screen :
root = tkinter.Tk()
root.geometry('400x550')
root.title('TCrypt - Encryption/Decryption Program')
root.config(bg = 'black')
root.minsize(400,550)
root.maxsize(400,550)
#-----------------------------------------------------------------------------------------------------------------
# Icon for title bar in GUI  
#tcrypt_mainicon = tkinter.PhotoImage(file=r'TCrypt_Data\TCrypt_window_icon.png')
#root.iconphoto(True,tcrypt_mainicon )
#-----------------------------------------------------------------------------------------------------------------
# MENU BAR 
# Creating Menu Bar in main screen
menubar = tkinter.Menu(root)
root.config(menu = menubar)

#Creating Logs menu in Menu Bar
log_menu = tkinter.Menu(menubar, tearoff = 'off')
menubar.add_cascade(label='Logs', menu = log_menu)
#Creating View Logs & Clear Logs options in Log Menu.
log_menu.add_command(label='View Logs',command= lambda : tcrypt_GUI_functions.open_log())
log_menu.add_command(label='Clear Logs',command= lambda : tcrypt_GUI_functions.clear_logs())
        
# Creating Info menu in Menu Bar
info_menu = tkinter.Menu(menubar, tearoff = 'off')
menubar.add_cascade(label='Info', menu = info_menu)
#Creating Help , Credits & Licience Options in info menu
info_menu.add_command(label='License', command= lambda : tcrypt_GUI_functions.open_license())
info_menu.add_separator()
info_menu.add_command(label='Help',command= lambda : tcrypt_GUI_functions.open_help())
#-----------------------------------------------------------------------------------------------------------------
# Creating Header on main screen
main_header = tkinter.Label(text = ('-'*40)+'TCrypt'+('-'*40),bg='white',fg='black')
main_header.pack(pady=5)
#-----------------------------------------------------------------------------------------------------------------
# Creating a text  on main screen to show  over input screen
titlemsg_i = tkinter.Label(text = ' Input : ',bg='black',fg='white',font=('bold'))
titlemsg_i.pack()
#-----------------------------------------------------------------------------------------------------------------
# Creating a Text Box to take user input - 
textbox_input= tkinter.Text(root, height = 5 , width = 40)
textbox_input.pack(pady=15)
#-----------------------------------------------------------------------------------------------------------------
# Creating Frame for placing Encrypt & Decrypt Button
button_encrypt_decrypt_frame = tkinter.Frame(root,bg='black')
button_encrypt_decrypt_frame.pack()
#-----------------------------------------------------------------------------------------------------------------
# Creating a seperator on main screen between input and output area
seperator = tkinter.Label(text ='-'*80,bg='black',fg='white',font=('bold'))
seperator.pack()
#-----------------------------------------------------------------------------------------------------------------
# Creating a text  on main screen to show  over input screen 
titlemsg_o = tkinter.Label(text = ' Output : ',bg='black',fg='white',font=('bold'))
titlemsg_o.pack()
#-----------------------------------------------------------------------------------------------------------------
# Creating a Text Box to provide output after Encryption/Decryption
textbox_output = tkinter.Text(root, height = 5 , width = 40)
textbox_output.pack(pady=15)
textbox_output.config(state='disabled')
#-----------------------------------------------------------------------------------------------------------------
# Creating Frame for placing Options Button
button_option_frame = tkinter.Frame(root,bg='black')
button_option_frame.pack(pady=10)
#-----------------------------------------------------------------------------------------------------------------
# Creating Encrypt Button 
button_encrypt = tkinter.Button(button_encrypt_decrypt_frame,text = 'Encrypt Text', height = 2 , width = 12, command =  lambda :get_text_encrypted(),bg='white')
button_encrypt.grid(row = 0 , column = 0 , pady = 15 , padx = 0)
# Creating decrypt  Button 
button_decrypt = tkinter.Button(button_encrypt_decrypt_frame,text = 'Decrypt Text', height = 2 , width = 12 ,command =  lambda : get_text_decrypted(),bg='white')
button_decrypt.grid(row = 0 , column = 1 , pady = 15 , padx = 20)
#-----------------------------------------------------------------------------------------------------------------
# Creating Copy Button 
button_copy = tkinter.Button(button_option_frame,text = 'Copy Text', height = 2 , width = 10, bg='white',command = lambda : copy_textbox())
button_copy.grid(row = 0 , column = 0, pady = 5 , padx = 8)
# Creating Cut Button
button_cut = tkinter.Button(button_option_frame,text = 'Cut Text', height = 2 , width = 10,bg='white',command = lambda : cut_textbox())
button_cut.grid(row = 0 , column = 1, pady =5 , padx = 8)
# Creating Clear Button 
button_clear = tkinter.Button(button_option_frame,text = 'Clear Text', height = 2 , width = 10,bg='white', command = lambda :clear_textbox())
button_clear.grid(row = 1 , column = 0,pady =5,padx = 8)
# Creating Reset Button 
button_reset = tkinter.Button(button_option_frame,text = 'Reset', height = 2 , width = 10,bg='white', command = lambda : reset_textbox())
button_reset.grid(row = 1 , column = 1, pady =5 ,padx = 8)
#-----------------------------------------------------------------------------------------------------------------
# Creating footer on main screen
main_footer = tkinter.Label(text ='-'*80,bg='white',fg='black')
main_footer.pack(pady=3)
#-----------------------------------------------------------------------------------------------------------------
root.mainloop()
#-----------------------------------------------------------------------------------------------------------------
'''
-------------------------------------------------------------------------------------------------------------------
email - rahulkandwal19@outlook.com | github - rahulkandwal19 
instagram -  @rahulkandwal19 | twitter - @rahulkandwal19
-------------------------------------------------------------------------------------------------------------------
'''
