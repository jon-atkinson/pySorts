# pySorts
<<<<<<< Updated upstream
Simple collection of sorts, testing and comparison CLI for comparing the implementations of many commonly used and some slightly unusual simple sorting algorithms. Algorithm implementations available only in python and C for the moment. 
=======
Simple collection of sorts, testing and comparison CLI for comparing the
implementations of many commonly used and some more complex sorting algorithms.
Algorithm implementations available only in python and C for the moment. 

## Requirements
pySorts has been tested on Debian and Windows 10, it's likely able to run wherever
python, pip, numpy and matplotlib are supported (most modern python3 envs).

To use pySorts, you'll need git and a compatible python3 and pip3 installed.

Support for the C algorithm impelementations requires an up to date cSorts.so.
A bash script for library compilation is included (pySorts/src/c/buildCLib.sh)
if you would like to rebuild ```cSorts.so``` but an up-to-date version should
exist in ```src/c``` already.
>>>>>>> Stashed changes

## Getting Set Up
To use pySorts just clone this repo into a local directory.
```
git clone git@github.com:jon-atkinson/pySorts.git
```

You'll also need some version of python3 and a compatible pip tool installed on your system. 

Ctypes is used to call C algorithms from python, it requires an up to date cSorts.so. A bash script for library compilation is included (pysorts/src/c/buildCLib.sh) but an up to date compilation of cSorts.so should exist in the correct position already (caveat, different system architectures will require recompiling). 

<<<<<<< Updated upstream
## Running pySorts from the terminal
Use the ```./cli``` script to run the CLI from a bash terminal in the projects root directory.
=======
### Running pySorts from the terminal
After building, run the following command to run the CLI interface.
```
pySortsCli
```
>>>>>>> Stashed changes

I recommend starting with the command ```algo -p -o``` and then hitting enter for all other default options (shown below). 
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/182abf9b-fd3e-4c00-8138-5afca3c9d1be)

You can compare multiple algorithms using ```algo```, compare the performance of one algorithm on different input types with ```sorting```, or plot the response of some combination of algorithms using ```plot```. See ```h``` command for more information.

Use the ```clear``` command to reset the terminal view and the ```q``` command to exit.

<<<<<<< Updated upstream
## Running pySorts using a GUI
Use the ```./app``` script to run the GUI from a bash terminal in the projects root directory. Pick an option from the buttons on the splash page, then set the comparison you want using the widgets and hit plot. Everything's single threaded at the moment so more complex/larger sorts may take a longer time depending on your hardware. 
=======
### Running pySorts using a GUI
After building, run the following command to open the GUI interface.
```
pySortsApp
```
Pick an option from the buttons on the front page, then set the comparison you
want using the widgets and hit plot.
Everything's single threaded at the moment so more complex/larger sorts may take
a longer time depending on your hardware. 
>>>>>>> Stashed changes
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/53b573f1-0dd4-473b-af1e-d657c7afad60)


### Example flow for comparing algorithms
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/0d299c11-b2a7-44e2-a53e-17e7d107ae88)
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/d3da567a-01d2-41e8-90c4-237db82ee2c6)
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/f0a75c7e-43d5-4541-9eec-97b5a61ee682)


### Example flow for comparing input types
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/0678efe8-74ff-477e-b414-36fb68688869)
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/77686944-72e6-43f4-bb27-51458256777c)
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/5903eb09-026e-4800-8164-5d61538d5b69)


Happy Sorting!
