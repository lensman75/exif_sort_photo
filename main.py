import tkinter as tk
from tkinter import filedialog
import glob
import os
# import exifread
import time
import datetime as dt
from time import gmtime, strftime
import errno
import shutil
import image
import exifread
import PIL
from PIL import Image
from PIL.ExifTags import TAGS

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
# file_path = filedialog.askopenfilenames()
# format = '%Y-%m-%d'
# TODO: rename variables and remove unnecessary lines.
for files in glob.glob(os.path.join(file_path, '*.jpg')):
    dirname, filename = os.path.split(files)
    print(filename)
    print(dirname)
    current_path = "%s" % files
    print(current_path)

    def get_exif(filename):
        ret = {}
        i = Image.open(current_path)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        return ret

    try:
        ddd = get_exif(filename)
    except AttributeError:
        print('skipped')
    print(type(ddd))
    dddd = ddd["DateTimeOriginal"]
    print(dddd[0:10])
    cutddd = dddd[0:10]
    ddddd = cutddd.replace(":", "-")
    print(ddddd)
    # for files in glob.glob(file_path):
    #     print (type(files))
    # tags = exifread.process_file(files)
    # print(tags)
    # print ("created : %s" % time.ctime(os.path.getctime(files)))
    # full_date = time.gmtime(os.path.getctime(files))
    # year_need=str(full_date.tm_year)
    # month_need=str(full_date.tm_mon).zfill(2)
    # day_need=str(full_date.tm_mday).zfill(2)
    # correct_date = "%s-%s-%s" % (year_need, month_need, day_need)
    # print(correct_date)
    # print (file_path)
    new_folder_path = "%s/%s" % (file_path, ddddd)
    print (new_folder_path)
    try:
        os.mkdir(new_folder_path)
    except OSError as e:
        if e.errno == errno.EEXIST:
            print('')
    new_file_path = "%s/%s" % (new_folder_path, filename)
    print(new_file_path)
    shutil.move(current_path, new_file_path)
    # ffff = dt.datetime.utcfromtimestamp(fff).strftime("%Y/%m/%d %H:%M")
    # print(ffff)
    # d = dt.datetime.strptime(full_date, format)
    # print(d)
print("Finished.")