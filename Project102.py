import os
import shutil

from_dir = 'C:\christina-dev\python\infolder'
to_dir = "C:\christina-dev\python\outfolder"


listoffiles = os.listdir(from_dir)
print(listoffiles)

for file in listoffiles:
    filename, extension = os.path.splitext(file)
    if extension == ' ':
        continue
    if extension in [".txt", ".doc", '.docx', '.pdf']:
        path1 = from_dir + '/' + file
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file
        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)
       