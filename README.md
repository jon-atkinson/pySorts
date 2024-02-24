# pySorts
Simple collection of sorts, testing and comparison CLI for comparing the implementations of many commonly used and some slightly unusual simple sorting algorithms. Algorithm implementations available only in python and C for the moment. 

## Getting Set Up
To use pySorts just clone this repo into a local directory.
```
git clone git@github.com:jon-atkinson/pySorts.git
```

You'll also need some version of python3 and a compatible pip tool installed on your system. 

Ctypes is used to call C algorithms from python, it requires an up to date cSorts.so. A bash script for library compilation is included (pysorts/src/c/buildCLib.sh) but an up to date compilation of cSorts.so should exist in the correct position already (caveat, different system architectures will require recompiling). 

## Running pySorts from the terminal
Use the ```./cli``` script to run the CLI from a bash terminal in the projects root directory.

I recommend starting with the command ```algo -p -o``` and then hitting enter for all other default options. You can compare multiple algorithms using ```algo```, compare the performance of one algorithm on different input types with ```sorting```, or plot the response of some combination of algorithms using ```plot```. See ```h``` command for more information. 

Use the ```q``` command to exit.

## Running pySorts using a GUI
Use the ```./app``` script to run the CLI from a bash terminal in the projects root directory. Pick an option from the buttons on the splash page, then set the comparison you want using the widgets and hit plot. Everything's single threaded at the moment so more complex/larger sorts may take a longer time depending on your hardware. 

Happy Sorting!
