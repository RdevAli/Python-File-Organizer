import os, shutil

path = r"D:\Code\Sorting"

file_names= os.listdir(path)

folder_names = {
    "Documents":[".pdf", ".doc"],
    "Videos":[".mp4",".mov"],
    "Images":[".png",".jpeg",".jpg"]
}
#Create Folders
for folder in folder_names.keys():
    folder_path=os.path.join(path,folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

#Sort into respective folders
for file in file_names:
    file_path=os.path.join(path,file)
    if not os.path.isfile(file_path):
        continue

    for folder, folders in folder_names.items():
        if file.endswith(tuple(folders)):
            destination_folder= os.path.join(path,folder)
            destination_path= os.path.join(destination_folder, file)
            try: 
                shutil.move(file_path, destination_path)
                print(f"Moved:{file} -> {folder}")
            except Exception as e:
                print(f"Error Moving {file}: {e}")