from colorama import init, Fore
from modules.filehandler import load_file
from modules.sql_converter import generate_sql_from_excel

init(autoreset=True)

def main():
    file_path = str(input(Fore.LIGHTBLUE_EX + "→" + Fore.WHITE + " | Enter the path to your EXCEL file: "))
    wb = load_file(file_path)
    if wb:
        generate_sql_from_excel(wb)

if __name__ == "__main__":
    main()