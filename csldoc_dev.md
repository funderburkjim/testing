

## Development environment Sanskrit Lexicon Documentation

These notes assume a Windows 10 computer with Gitbash and python3.4 or later.
It also assumes a previous version of the csldoc repository at Github.
These instructions describe a complete installation of development environment for csldoc on
local computer.

### initialize csldoc from github

```
git clone git@github.com:sanskrit-lexicon/csldoc.git
cd csldoc
```

### python requirements for sphinx
sphinx version 1.8.1 requirements:Python >=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*
I have python 2.7 and Python3.7 on local windows 10 computer.
Cologne website has python3.4.
On local computer, 'python3' is the command to run python3.7.   ('python' is command to run python2.7)
We must use python3.


### setup virtual environment with sphinx on local computer 

Be sure that 'csldoc' is the current directory.  We are going to create subdirectories *virtualenv-16.0.0* and *myenv* within
csldoc;  Note these are in .gitignore, so they are not tracked by git.
```
# 1. retrieve zipped version of virtualenv
# csldoc is current directory
curl -O https://files.pythonhosted.org/packages/33/bc/fa0b5347139cd9564f0d44ebd2b147ac97c36b2403943dbee8a25fd74012/virtualenv-16.0.0.tar.gz
# 2. unpack the compressed file into directory virtualenv-16.0.0
tar xvfz virtualenv-16.0.0.tar.gz
# creates directory virtualenv-16.0.0
#3. Make a directory to contain a new virtual environment:
# use python3
python3 virtualenv-16.0.0/virtualenv.py myenv
# 4. activate the *myenv* virtual environment.  
source myenv/Scripts/activate
# When myenv is activated, the 'python' command refers to python3.7
 which python
#>>> /C/ejf/pdfs/TM2013/0docs/csldev/myenv/Scripts/python
# note that this is python version 3.7, presumably since i used 'python3'
# in creating the virtual environment.
python --version
#>>> Python 3.7.0
# also check that 'pip' is also the one in 'myenv'
 which pip
#>>> /C/ejf/pdfs/TM2013/0docs/csldev/myenv/Scripts/pip
#5. install sphinx
pip install sphinx
#6. Deactivate virtual environment
deactivate
#7. note on size:  myenv is 74MB
```

### quick commands for virtualenv
```
# in csldoc directory
#1. Activate the 'myenv' virtual environment, so sphinx will be available
source myenv/Scripts/activate
#2. Deactivate the 'myenv' viritual environment when you are done working with sphinx.
deactivate
```


* initalizing test sphinx document
# besure myenv is activated
sphinx-quickstart

a) Separate source/build directories
 named 'source' and 'build'
* make copyright blank
in source/conf.py, change 
copyright = '2018, Jim Funderburk'
to 
copyright = ''
This copyright seems to show on all pages.
When blank, there is still a copyright to Sphinx and alabaster.
Guess we'll have to leave these.

* making html
sphinx-build -b html source build

The 'build' directory is constructed or updated.
We'll want to do some modification of this when uploading to 
Cologne.  Details later under 'Cologne upload'
* images folder 
For conceptual simplicity, it seems better to relocate the scanned 
images of the front matter of the dictionary.
For ease of reference in the restructured text files, the images directory
should be within the *source* directory
cd source
mkdir images
* current location of front matter scans
For dictionary X, the images are in folder
source/dictionaries/prefaces/Xpref/images

For each image, the page referencing image number NN is XprefNN.rst.
In this file, the sphinx image directive is
.. image:: images/IMGFILENAME_X_NN
We need to:
a) move source/dictionaries/prefaces/Xpref/images/IMGFILENAME_X_NN to
        source/images/IMGFILENAME_X_NN
  -- I assume that as X ranges over all dictionaries and NN over all
     the possibilities, then there all the IMGFILENAME_X_NN are distinct.
     This assumption needs to be checked before moving all these
     files into one directory.
* imgchk
  python move_images.py imgchk
  There are 34 dictionary codes
  acc, ae, ap90, ben  have no images folder
  There are 468 total file names found in images folders for the other 30
  dictionaries.
  There are no dupicates among these file names (i.e., each filename 
   occurs in the images folder of precisely one dictionary).
* copyimg 
python move_images.py copyimg
Copy images for all dictionaries. 
The source images are in directories for each dictionary code X
  ../sphinx/cslv1/dictionaries/prefaces/Xpref/images'
The target images are in 'images' directory.
* copy and alter XprefNN files
python move_images.py prefnn
* Cologne upload
* THE END
* image sizes
size of git repository with just bhs: 17 mb
images 20mb  (just bhs - 30 files -- only 15 are used)

After build,
  size of build directory: 3.8 mb
  size of .git directory : 17.8mb
