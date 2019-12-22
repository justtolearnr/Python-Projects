import os  # To list all subfolders & files
import shutil

for folderName, subfolders, filenames in os.walk('C:\\xampp'):  # to list folderName, subfolders, filenames
    print('The folder is' + folderName)
    print('The subfolders in' + folderName + 'are : ' + str(subfolders))
    print('The filenames in' + folderName + 'are : ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)

            for file in filenames:
                if file.endswith('.py'):
                    shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))