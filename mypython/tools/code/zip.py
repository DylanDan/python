# !/usr/bin/python
# -*- coding:utf-8 -*-

import time
import zipfile
import shutil


def generatezip(zipname, filename, arcname):
    destzip = zipfile.ZipFile(zipname, "w")
    destzip.write(filename, arcname)
    destzip.close()


def copyziptodest(source):

    shutil.copy2(source, r"\\Hyper-SZ01\Share\Private\Dylan.Dan\tmp\qoute")


if __name__ == '__main__':

    name = time.strftime("%Y%m%d", time.localtime())
    filename = name+".zip"
    zipfilepullpath = "/"+filename
    arcname = name+".csv"
    sourcefilefullpath = "/"+arcname
    generatezip(zipfilepullpath, sourcefilefullpath, arcname)
    copyziptodest(zipfilepullpath)

