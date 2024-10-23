from colorama import Fore

def generate_sql_from_excel(wb):
    sheetnames = wb.sheetnames
    selected_sheet = input(Fore.LIGHTBLUE_EX + "→" + Fore.WHITE + " | Select a sheet name from the above list: ")

    if selected_sheet in sheetnames:
        ws = wb[selected_sheet]
        sql_lines = []

        create_table_choice = input(Fore.LIGHTBLUE_EX + "→" + Fore.WHITE + " | Do you want to create a new table in the database? (yes/no): ").strip().lower()
        
        if create_table_choice == 'yes':
            table_name = input(Fore.LIGHTBLUE_EX + "→" + Fore.WHITE + " | Enter the name for the SQL table: ")
            sql_lines.append(f"CREATE TABLE `{table_name}` (\n  ") 
        else:
            table_name = input(Fore.LIGHTBLUE_EX + "→" + Fore.WHITE + " | Enter the name of the existing table to insert data: ")

        columns = [cell.value for cell in ws[1]] 
        print(Fore.LIGHTBLUE_EX + "Available columns: " + Fore.WHITE + ", ".join(columns))

        choice = input(Fore.LIGHTBLUE_EX + "→" + Fore.WHITE + " | Do you want to select specific columns to transfer? (yes/no): ").strip().lower()

        selected_columns = []
        if choice == 'yes':
            selected_columns_input = input(Fore.LIGHTBLUE_EX + "→" + Fore.WHITE + " | Enter the columns you want to include (comma-separated): ")
            selected_columns = [col.strip() for col in selected_columns_input.split(",") if col.strip() in columns]
            if not selected_columns:
                print(Fore.RED + '✘' + Fore.WHITE + " | No valid columns selected. Exiting...")
                return
        else:
            selected_columns = columns

        rename_choice = input(Fore.LIGHTBLUE_EX + "→" + Fore.WHITE + " | Do you want to rename any columns? (yes/no): ").strip().lower()

        new_column_names = {}
        if rename_choice == 'yes':
            for col in selected_columns:
                new_name = input(Fore.LIGHTBLUE_EX + f"→ {Fore.WHITE} | Enter new name for column '{col}' (or press Enter to keep the same): ")
                new_column_names[col] = new_name if new_name else col
        else:
            new_column_names = {col: col for col in selected_columns}

        column_definitions = [f"`{new_column_names[col]}` TEXT" for col in selected_columns]
        
        if create_table_choice == 'yes':
            sql_lines[0] += ',\n  '.join(column_definitions) + "\n);\n"
        
        for row in ws.iter_rows(min_row=2, values_only=True): 
            values = []
            for col in selected_columns:
                value = row[columns.index(col)]
                if value is None:
                    values.append('NULL')
                else:
                    escaped_value = str(value).replace("'", "''")
                    values.append(f"'{escaped_value}'")
                    
            sql_line = f"INSERT INTO `{table_name}` ({', '.join(new_column_names[col] for col in selected_columns)}) VALUES ({', '.join(values)});"
            sql_lines.append(sql_line)

        sql_filename = table_name + '.sql'
        with open(sql_filename, 'w') as sql_file:
            sql_file.write('\n'.join(sql_lines))

        print(Fore.GREEN + '✔' + Fore.WHITE + f" | SQL file '{sql_filename}' has been created successfully!")
    else:
        print(Fore.RED + '✘' + Fore.WHITE + " | The selected sheet does not exist.")