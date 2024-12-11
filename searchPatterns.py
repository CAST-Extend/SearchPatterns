import os
import re
import pandas as pd

def remove_java_comments(java_code):
    # Remove single-line comments
    java_code = re.sub(r'\/\/.*', '', java_code)

    # Remove multi-line comments
    java_code = re.sub(r'\/\*[\s\S]*?\*\/', '', java_code)

    return java_code

def search_java_patterns(file_path, patterns):
    result = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        java_code = file.read()
        content = remove_java_comments(java_code)
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                result.append((pattern, matches))
    return result

def search_patterns_in_file(file_path, patterns):
    result = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                result.append((pattern, matches))
    return result

def search_patterns_in_folder(root_folder):
    java_patterns = [
        r'(?i)(@query.*)',
        r'(?i)(@Table.*)',
        r'(?i)\bSELECT\b[\s\S]*?\s\bFROM\b\s+\S+',   
        r'(?i)(\bUPDATE\b\s+\w+\s*?\bSET\b\s+\w+\s*(\bWHERE\s+)?)',   
        r'(?i)(\bDELETE\b\s+?\bFROM\b\s+\w+\s*(\bWHERE\s+)?)',  
        r'(?i)(\bINSERT\b\s+INTO\b\s+\w+(\s*\([^)]*\))?\s*VALUES\s*\([^)]*\)\s*)', 
        r'(?i)\W(call\s.*)',
        r'(?i)crudrepository',
        r'(?i)springframework\.jdbc',
        r'(?i)org\.springframework\.data\.jpa\.repository',
        r'(?i)org\.springframework\.data\.repository\.query',
        r'(?i)org\.springframework\.jdbc\.core',
        r'(?i)org\.springframework\.data\.repository',
        r'(?i)org\.springframework\.jdbc',
        r'(?i)com\.mysql\.cj\.jdbc',
        r'(?i)org\.apache\.ibatis\.\*',
        r'(?i)com\.ibatis\.sqlmap\.\*',
        r'(?i)org\.springframework\.orm\.jpa',
        r'(?i)org\.apache\.spark\.sql\.jdbc',
        r'(?i)org\.mybatis\.dynamic\.sql',
        r'(?i)(import java.sql.*)'
    ]

    xml_js_shell_ctl_ptl_patterns = [
        r'(?i)\bSELECT\b[\s\S]*?\s\bFROM\b\s+\S+',
        r'(?i)(\bUPDATE\b\s+\w+\s*?\bSET\b\s+\w+\s*(\bWHERE\s+)?)',
        r'(?i)(\bINSERT\b\s+INTO\b\s+\w+(\s*\([^)]*\))?\s*VALUES\s*\([^)]*\)\s*)',
        r'(?i)(\bDELETE\b\s+?\bFROM\b\s+\w+\s*(\bWHERE\s+)?)'
    ]

    cbl_cob_pattern = [
        r'(?i)EXEC\sSQL\s*'
    ]

    excel_data = []

    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if filename.endswith(('.java')):
                patterns_found = search_java_patterns(file_path, java_patterns)
                for pattern, matches in patterns_found:
                    excel_data.append((file_path, pattern, matches))

            elif filename.endswith(('.xml', '.js', '.shell', '.ctl', '.pli', '.ts')):
                patterns_found = search_patterns_in_file(file_path, xml_js_shell_ctl_ptl_patterns)
                for pattern, matches in patterns_found:
                    excel_data.append((file_path, pattern, matches))

            elif filename.endswith(('.cbl', '.cob')):
                patterns_found = search_patterns_in_file(file_path, cbl_cob_pattern)
                for pattern, matches in patterns_found:
                    excel_data.append((file_path, pattern, matches))                

    return excel_data

def create_excel_output(excel_data, output_file):
    df = pd.DataFrame(excel_data, columns=['File', 'Pattern', 'Matches'])
    df.to_excel(output_file+"\output.xlsx", index=False)
    print(f'output.xlsx saved to {output_file}')

if __name__ == "__main__":
    root_folder = 'C:\work\servtool_118 search pattern script\src'

while True:
    try:
        #taking source code path as input from the user.
        dirLoc=input(r'Enter the input folder path: ').strip()
        out_put_path = input('\nplease enter the path where you want to store the excel output file : ')
        excel_data = search_patterns_in_folder(dirLoc)
        create_excel_output(excel_data, out_put_path)
        break
    except FileNotFoundError as e:
        print("Incorrect Path!  Please enter the correct path.\n")
    except IndexError as e:
        print("Source code does not exist!  Please copy your source code to - "+ dirLoc +"\n")
    except Exception as e:
        print("Some Exception Occured !\n Please resolve them or contact developers.\n"+str(e))

    

    
    
