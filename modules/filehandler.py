import os
from openpyxl import load_workbook
from colorama import Fore

def load_file(path):
    wb = None 

    if(path.endswith(('.xls', '.xlsx'))):
        if(os.path.exists(path)):
            if(os.path.isfile(path)):
                try: 
                    wb = load_workbook(path)
                    print(Fore.GREEN + '✔' + Fore.WHITE + " | The file has been successfully uploaded!")
                    print(Fore.LIGHTBLUE_EX + '→' + Fore.WHITE + ' | Found workbooks on file: ' + ", ".join(map(str, wb.sheetnames)))
                except Exception as e:
                    print(Fore.RED + '✘' + Fore.WHITE + " | An error occurred when uploading file: " + Fore.RED + f"{e}")
            else:
                print(Fore.RED + '✘' + Fore.WHITE + " | The path entered is not a file!")
        else:
            print(Fore.RED + '✘' + Fore.WHITE + " | The entered path is invalid!")
    else:
        print(Fore.RED + '✘' + Fore.WHITE + " | This file format " + Fore.RED + "is not supported" + Fore.WHITE + "!" + Fore.WHITE + " Use " + Fore.GREEN + ".xls " + Fore.WHITE + "or " + Fore.GREEN + ".xlsx" + Fore.WHITE + ".")

    return wb