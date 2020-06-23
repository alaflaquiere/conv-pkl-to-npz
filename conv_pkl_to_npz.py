import os, sys
import numpy as np
import _pickle as cpickle
from fnmatch import fnmatch


def get_matching_files(folder, template):
    filenames = []
    for root, dirs, files in os.walk(folder, topdown=True):
        for file in files:
            filename = os.path.join(root, file)
            if fnmatch(file, template):
                filenames.append(filename)
                print(filename)
    return filenames


def check_dict_equality(dict1, dict2):
    for key in dict1:
        if key not in dict2:
            print("ERROR: incorrect save")
            return False
        if not np.all(dict2[key] == dict1[key]):
            print("ERROR: incorrect save")
            return False
    for key in dict2:
        if key not in dict1:
            print("ERROR: incorrect save")
            return False
        if not np.all(dict1[key] == dict2[key]):
            print("ERROR: incorrect save")
            return False
    return True


def convert(filename_pkl):
    filename_npz = os.path.splitext(filename_pkl)[0] + ".npz"
    print("converting [{}] -> [{}]".format(filename_pkl, filename_npz))
    with open(filename_pkl, "rb") as f:
        data_pkl = cpickle.load(f)
    # save as npz file
    np.savez_compressed(filename_npz, **data_pkl)
    # check the data is correctly saved
    with np.load(filename_npz) as npzfile:
        data_npz = dict(zip(npzfile.files, [npzfile[x] for x in npzfile.files]))

    if check_dict_equality(data_pkl, data_npz):
        os.remove(filename_pkl)


if __name__ == "__main__":
    """
    Converts a dictionary saved as pkl file to a npz file.
    
    Arguments:
        1. folder to convert (including subfolders)
        2. template to match the files against (ex: dataset*.pkl) 
    """

    folder = sys.argv[1]
    template = sys.argv[2]

    names = get_matching_files(folder=folder, template=template)

    ans = input("Proceed with the conversion of these files? [y/n] > ")
    if ans.lower() not in ["y", "yes"]:
        sys.exit()

    for name in names:
        convert(name)
