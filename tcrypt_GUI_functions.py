# Importing Required Modules
import os
import tkinter
import tcrypt_encryption_decryption
import webbrowser
from datetime import datetime
# -----------------------------------------------------------------------------------------------------------------
# Function to check for required directory and creating if not present .
def create_directory():
    list_of_dir =  os.listdir()
    tcrypt_dir_is_avaliable= False
    # Transversing LIst of avaviable directory and checking if required directory is present .
    for i in list_of_dir :
        if i == 'TCrypt_UserFiles':
            tcrypt_dir_is_avaliable = True
    # Creating the directory if not present .
    if tcrypt_dir_is_avaliable == False :
        os.mkdir('TCrypt_UserFiles')
# -----------------------------------------------------------------------------------------------------------------
# Creating new window to show past logs to user .
def open_log():
        log_view_window = tkinter.Tk()
        log_view_window.title('TCrypt - User Logs')
        log_view_window.geometry('1200x400')
        log_view_window.minsize(500,400)
        log_view_window.maxsize(500,400)
        heading = tkinter.Label(log_view_window,text = ('-'*42)+' TCrypt - User Logs '+('-'*42) ,bg='black',fg='white')
        heading.pack()
        textbox_log = tkinter.Text(log_view_window)
        textbox_log.pack()
        textbox_log.config(state='normal')
        log_data = get_logs()
        # Inserting into Data into Text Box Using Loop
        for i in log_data:
            textbox_log.insert(tkinter.INSERT,i)
        textbox_log.config(state='disable')
# -----------------------------------------------------------------------------------------------------------------
# Log management Functions .
# Function to get log data (Function is used in  open_logs() to get log data) .
def get_logs():
        logfile = open(r'TCrypt_UserFiles\Tcrypt_logs','r',encoding="utf-8")
        list_log_lines = logfile.readlines()
        logfile.close
        return list_log_lines
# Function to save Logs into secondry memory as (.txt file) . (Function is used in encrypt_text() & decrypt_text()  to get log data)
def save_logs(text_i,text_o,e_o_d):
        logfile = open(r'TCrypt_UserFiles\Tcrypt_logs','a',encoding="utf-8")
        # Getting System time  .
        date_time = str(datetime.now())
        # Creating a line to save in log (Input text = text_i & Output text = text_o)
        log_line = ('['+ (date_time) +'] \n'+'[' +  (text_i) + ']\n'+'[' +(e_o_d) +'] \n' + '[' +  (text_o) + ']','\n')
        # Saving data in log file
        logfile.writelines(log_line)
        logfile.writelines(('_'*60)+'\n')
        logfile.close
# Function to Clear Log file . (Function used as commmand in clear logs in  logs menu)
def clear_logs ():
        logfile = open(r'TCrypt_UserFiles\Tcrypt_logs','w',encoding="utf-8")
        logfile.write('')
        logfile.close
# -----------------------------------------------------------------------------------------------------------------
# Function to create a new window to show license info (Function used as commmand in License in info menu) . 
def open_license():
        license_view_window = tkinter.Tk()
        license_view_window.title('TCrypt - License')
        license_view_window.geometry('800x410')
        license_view_window.minsize(700,410)
        license_view_window.maxsize(700,410)
        heading = tkinter.Label(license_view_window,text =('-'*62)+' TCrypt License '+('-'*62),bg='black',fg='white')
        heading.pack()
        textbox_license = tkinter.Text(license_view_window)
        textbox_license.pack(pady=1)
        # Opening License.txt and reterving Text (Data)
        textbox_license.config(state='normal')        
        licensefile = open(r'TCrypt_Data\TCrypt_License.txt','r',encoding="utf-8")
        data_license = licensefile.readlines()
        licensefile.close
        # Showing License in TEXT BOX
        for i in data_license:
            textbox_license.insert(tkinter.INSERT,i)
        textbox_license.config(state='disable')
# -----------------------------------------------------------------------------------------------------------------
# Creating a new help window .
def open_help():
        webbrowser.open_new(r'TCrypt_Data\tycrypt_help.pdf')
# -----------------------------------------------------------------------------------------------------------------
# Bridge Function between GUI and Encryption Function in tcrypt_encryption_decryption module .
def encrypt_txt(text):
        encrypted_txt = tcrypt_encryption_decryption.text_encrypt(text)
        # Saving Operation History in logs 
        #save_logs(text,encrypted_txt,'Encryption')
        return encrypted_txt
# -----------------------------------------------------------------------------------------------------------------
# Bridge Function between GUI and decryption Function in tcrypt_encryption_decryption module .
def decrypt_txt(text):
        decrypted_txt = tcrypt_encryption_decryption.text_decrypt(text)
        # Saving Operation History in logs 
        #save_logs(text,decrypted_txt ,'Decryption')
        return decrypted_txt
# -----------------------------------------------------------------------------------------------------------------
'''
-------------------------------------------------------------------------------------------------------------------
email - rahulkandwal19@outlook.com | github - rahulkandwal19 
instagram -  @rahulkandwal19 | twitter - @rahulkandwal19
-------------------------------------------------------------------------------------------------------------------
'''






