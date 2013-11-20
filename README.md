Filter Images
=============

This script filters the images inside a folder and checks for dimensions. This is helpful, if you run an automated download script and want to get rid of small images.

### Requirements
This script is based on python, obviously you need that (python-2.7 works). You also need the following python packages:

    PIL (python imaging library)

### Options
Inside the file, there are some options you should have a look at:

* **`minDim`**: a tuple for (width, height)
* **`useExactDim`**: *True*: match the `minDim` exactly, *False*: use `minDim` as a lower limit
* **`useAR`**: Should we match to the aspect ratio from `minDim`?
* **`imagePath`**: Path to the images. Remember the trailing /
* **`moveImproper`**: Move images not matching the criteria instead of deleting them.
* **`improperPath`**: If the above is true, move the improper images.

### Example use-case
I run an [IFTTT recipe](https://ifttt.com/recipes/129664) that downloads pictures posted in the subreddit [/r/EarthPorn](http://www.reddit.com/r/EarthPorn) into a Dropbox folder (thanks [@senfi](https://github.com/senfi)!). Because I want to use these pictures as wallpaper/screensaver images, I have to get rid of all those that are to small.
The IFTTT script runs instantly, so I put this line in my crontab to run the script every 30 minutes:

    30/2 *  *   *   *   andre    python /Users/andre/Development/git/filter-wallpapers/filter.py
