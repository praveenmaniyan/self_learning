import os

#DIR = "C:\\Users\\v-manipr.FAREAST\\Documents\\personal\\acc_training\\udacity\\ML\\dataset\\data\\train"
DIR = "C:\\Users\\v-manipr.FAREAST\\Documents\\personal\\acc_training\\udacity\\ML\\dataset\\data\\validation"

path, dirs, files = next(os.walk(DIR))
#print(dirs)
print("species_name,count")
for each_dir in dirs:
    path1, dirs1, files1 = next(os.walk(os.path.join(DIR,each_dir)))
    file_count = len(files1)
    print("%s,%d" % (each_dir,file_count))