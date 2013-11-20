#!/usr/bin/python
# -*- coding: utf-8

#
#  Filter wallpapers by size/ratio
# ----------------------------------
#
# With this IFTTT recipe you can automatically download images posted to a
# specific subreddit on reddit.com. Unfortunately, this also includes small
# images or those out of your required aspect ratio.
# This small tool loops through all the images and deletes/moves the ones with
# the wrong aspect ratio and/or those too small.

# Configuration Array
# Note for the paths: use trailing slash (/)!
_conf = {
    'minDim': (1920, 1200), # (width, height)
    'useExactDim': False,   # True: exact dimensions, False: minDim is lower limit
    'useAR': False,         # use the aspect ratio from the minimum dimensions
    'imagePath': '/Users/andre/Dropbox/IFTTT/reddit/EarthPorn/',
    'moveImproper': False,  # True moves, False deletes immediately
    'improperPath': '/Users/andre/Dropbox/IFTTT/reddit/EarthPorn/improper/',
}

# import stuff
import os               # file handling
import re               # regular expression
from PIL import Image   # handling images


def handleImproper(file):
    if _conf['moveImproper']:
        if not os.path.exists(_conf['improperPath']):
            os.makedirs(_conf['improperPath'], 0755)
        os.rename(_conf['imagePath'] + file, _conf['improperPath'] + file)
        print "move   {0}".format(file)
    else:
        os.remove(_conf['imagePath'] + file)
        print "delete {0}".format(file)


# the main function, obviously
def main():
    for filename in os.listdir(_conf['imagePath']):
        filepath = _conf['imagePath'] + filename
        if os.path.isdir(filepath):
            continue
        if re.match("\.jpg$", filename) is not None:
            continue

        image = Image.open(filepath)

        # check for minimum/exact dimensions
        if _conf['useExactDim']:
            if image.size[0] != _conf['minDim'][0] or image.size[1] != _conf['minDim'][1]:
                # print "delete (wrongDim) {0}".format(filename)
                handleImproper(filename)
                print
        else:
            if image.size[0] < _conf['minDim'][0] or image.size[1] < _conf['minDim'][1]:
                # print "delete (minDim)   {0}".format(filename)
                handleImproper(filename)
                continue

        # check for exact aspect ratio
        if _conf['useAR']:
            AR_req = float(_conf['minDim'][0]) / float(_conf['minDim'][1])
            AR_img = float(image.size[0]) / float(image.size[1])
            if AR_req != AR_img:
                # print "delete (wrongAR)  {0}".format(filename)
                handleImproper(filename)
                continue

        print "keep   {0}".format(filename)


if __name__ == '__main__':
    main()
