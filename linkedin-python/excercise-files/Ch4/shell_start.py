#
# Example file for working with filesystem shell methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import os
import shutil
from zipfile import ZipFile
from os import path
from tarfile import TarFile

def main():
    # make a duplicate of an existing file
    if path.exists("sachin.txt"):
        # get the path to the file in current directory
        src = path.realpath("sachin.txt")

        # seperate the path part from the filename
        (head, tail) = path.split(src)
        print ("path: %s", str(head))
        print ("file: %s", str(tail))

        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"
        # now use the shell to make a copy of the file
        shutil.copy(src, dst)

        # copy over the permission, modification times and other info
        shutil.copystat(src, dst)

        # rename the original file
        #os.rename("sachin-test1.txt", "sachin.txt")

        # now put things into a ZIP archive
        #root_dir,tail = path.split(src)
        #shutil.make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("sachin.txt")
            newzip.write("sachin.txt.bak")
            newzip.close()

        # gzip compression
        with TarFile.open("test.tar.gz", "w:gz") as gzip:
            for name in ["sachin.txt", "sachin.txt.bak"]:
                gzip.add(name)
            gzip.close()

        # bzip compression
        with TarFile.open("sachin-test.tar.bz2", "w:bz2") as bzip:
            for name in ["sachin.txt", "sachin.txt.bak"]:
                bzip.add(name)
            bzip.close()

if __name__ == "__main__":
  main()
