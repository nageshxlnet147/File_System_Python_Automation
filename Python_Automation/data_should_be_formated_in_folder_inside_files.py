import os
import shutil
source_path = '/home/Python_Automation'         # Parent path


dt = {
    'language':['Python.py', 'C.c', 'Java.java', 'Go.go'],
    'Laptop' : ['LG.lg', 'Samsung.sg', 'Asus.as','Lenovo.le','Dell.dl', 'HP.h'],
    'Cost':['ONE.txt','TWO.txt','THREE.txt','FOUR.txt']
}
try:
    folder_rename_count = 1
    for i, j in dt.items():
        if i != False:
            folder_assigning = folder_rename_count
            df = str(folder_assigning)+'_'+ i   # Adding the number of folders to be counted in front
            f = os.path.join(source_path, df)    # join the source path and keys
            os.makedirs(f, exist_ok = True)     # Creating the f paths
            file_rename_count = 1
            for k in j:
                assigning = file_rename_count
                p = os.path.join(source_path,  k)   # Join the source path and value k
                if os.path.exists(p):
                    new_file_name = str(assigning) + '_' + k    # Adding the number of files to be counted in front
                    new_file_name_path = os.path.join(source_path,  new_file_name)  #join the source path and new_file_name
                    os.rename(p, new_file_name_path)    # Rename the old path to new path
                    shutil.move(new_file_name_path, f)  # moving the new path data to destination path 
                    print('copied')
                    file_rename_count += 1  # Increasing the rename files count
        folder_rename_count += 1    # Increasing the rename folder count
except Exception as e:
    print(e)
