import os
import time


def main():
    filtertext, operation, main_path = func()
    dirs = []
    files = []
    for root, dir, file in os.walk(main_path):
        for f in file:
            files.append(f)
        for d in dir:
            dirs.append(d)
    # print(files)
    #    user_input= input('please ')
    if operation == "1":
        searchFileSubstring(files, filtertext, main_path)
    elif operation == "2":
        searchFileExtension(files, filtertext, main_path)
    elif operation == "3":
        searchFilesInFolderPrefix(dirs, filtertext, main_path)
    elif operation == "4":
        searchFilesInFolderSuffix(dirs, filtertext, main_path)


def searchFileSubstring(listFile: list, target: str, main_path: str):
    for file in listFile:
        if target in file:
            printDetails(main_path, file)


def searchFileExtension(listFile: list, target: str, main_path: str):
    for file in listFile:
        if str(file).endswith(target):
            printDetails(main_path, file)


def searchFilesInFolderPrefix(listdir: list, target: str, main_path: str):
    for folder in listdir:
        if str(folder).startswith(target):
            path = os.path.join(main_path, folder)
            for root, dir, file in os.walk(path):
                for f in file:
                    folder_path = os.path.join(main_path, folder)
                    printDetails(folder_path, f)


def searchFilesInFolderSuffix(listdir: list, target: str, main_path: str):
    for folder in listdir:
        if str(folder).endswith(target):
            path = os.path.join(main_path, folder)
            for root, dir, file in os.walk(path):
                for f in file:
                    folder_path = os.path.join(main_path, folder)
                    printDetails(folder_path, f)


def printDetails(folderPath: str, fileName: str):
    file_path = os.path.join(folderPath, fileName)
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file_path)
    with open("res.csv", "a") as f:
        data = f"{folderPath},{fileName},{time.ctime(ctime)},{time.ctime(mtime)},{time.ctime(atime)}\n"
        f.write(data)
        f.flush()


message = 'please select one of the following operations:\n' \
          '1) A substring of the file name.' \
          'For example: file names that contain the expression: "XT.ec" or "AcGenral\n' \
          '2) The extension of the file. For example: files with the “.txt” extension\n' \
          '3) Files in folders that start with a certain string. For example: folder name starting with “QHE”.\n' \
          '4) Files in folders that end with a certain string. For example: folder name ends with “GNOFF”'


def func():
    main_path = input("please provide a directory to search:" + "\n")
    while (not os.path.isdir(main_path)):
        print("directoryPlease provide an existing directory!!\n")
        main_path = input("please provide a directory to search:" + "\n")

    operation = input(message + "\n")
    while (operation not in ["1", "2", "3", "4"]):
        print("Please select 1-4!!\n")
        operation = input(message + "\n")
    filter = input("please select a text filter for the files:\n")
    return (filter, operation, main_path)


if __name__ == '__main__':
    with open("res.csv", "w") as f:
        f.write("FolderPath,FileName,CreationDate,ModifiedDate,DateAccessed\n")
        f.flush()
    main()
