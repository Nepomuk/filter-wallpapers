Filter Images
=============

This script filters the images inside a folder and checks for dimensions. This is helpful, if you run an automated download script and want to get rid of small images.

#### Example use-case
I run an [IFTTT recipe](https://ifttt.com/recipes/129664) that downloads pictures posted in the subreddit [/r/EarthPorn](http://www.reddit.com/r/EarthPorn) into a Dropbox folder (thanks [@senfi](https://github.com/senfi)!). Because I want to use these pictures as wallpaper/screensaver images, I have to get rid of all those that are to small.

Run the script
--------------

### Requirements
This script is based on python, obviously you need that (python-2.7 works). You also need the following python packages:

    PIL (python imaging library)

### Options in the file
Inside the file, there are some options you should have a look at:

* **`minDim`**: a tuple for (width, height)
* **`useExactDim`**: *True*: match the `minDim` exactly, *False*: use `minDim` as a lower limit.
* **`useAR`**: Should we match to the aspect ratio from `minDim`?
* **`imagePath`**: Path to the images. Remember the trailing /
* **`moveImproper`**: Move images not matching the criteria instead of deleting them.
* **`improperPath`**: If the above is true, move the improper images.

### Automatically run the script on OS X
First, have a look at the .plist file. You should take a look at the `ProgramArguments` flag. Inside, the path to the python excecutable and the script has to be adapted to your system. After this, you can add the launch job:

    launchctl load filter.plist

The job should run now every 15 minutes. If you want to check, if launchctrl accepted your job, run this. The output should be similar.

    $ launchctl list com.andre.python.filter-wallpaper
    {
      "Label" = "com.andre.python.filter-wallpaper";
      "LimitLoadToSessionType" = "Aqua";
      "OnDemand" = true;
      "LastExitStatus" = 0;
      "TimeOut" = 30;
      "ProgramArguments" = (
        "/usr/local/bin/python";
        "/Users/andre/Development/filter-wallpapers/filter.py";
      );
    };

If you want to run the script once with launchctrl, use the `start` option:

    $ launchctl start com.andre.python.filter-wallpaper
