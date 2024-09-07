# pySorts
Simple collection of sorts, testing and comparison CLI for comparing the
implementations of many commonly used and some more complex sorting algorithms.
Algorithm implementations available only in python and C for the moment. 

## Requirements
To use pySorts, you'll need git and a compatible python3 and pip3 installed.

Ctypes is used to call C algorithm implementations from python, it requires an up
to date cSorts.so. A bash script for library compilation is included
(pySorts/src/c/buildCLib.sh) if you would like to rebuild ```cSorts.so``` but an
up to date version should exist in that directory already.

## Getting Set Up
To use pySorts just clone this repo into a local directory.
```
git clone https://github.com/jon-atkinson/pySorts.git
```

Then run the following command from the pySorts directory to build the package.
```
pip install .
```


## Running

### Running pySorts from the terminal
After building, run the command ```pySortsCli``` to run the CLI interface.

I recommend starting with the command ```algo -p -o``` and then hitting enter for all other default options (shown below). 
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/182abf9b-fd3e-4c00-8138-5afca3c9d1be)

You can compare multiple algorithms using ```algo```, compare the performance of one algorithm on different input types with ```sorting```, or plot the response of some combination of algorithms using ```plot```. See ```h``` command for more information.

Use the ```clear``` command to reset the terminal view and the ```q``` command to exit.

### Running pySorts using a GUI
After building, run the command ```pySortsApp``` to open the GUI interface.
Pick an option from the buttons on the front page, then set the comparison you
want using the widgets and hit plot.
Everything's single threaded at the moment so more complex/larger sorts may take
a longer time depending on your hardware. 
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/53b573f1-0dd4-473b-af1e-d657c7afad60)

#### Example flow for comparing algorithms
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/0d299c11-b2a7-44e2-a53e-17e7d107ae88)
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/d3da567a-01d2-41e8-90c4-237db82ee2c6)
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/f0a75c7e-43d5-4541-9eec-97b5a61ee682)

#### Example flow for comparing input types
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/0678efe8-74ff-477e-b414-36fb68688869)
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/77686944-72e6-43f4-bb27-51458256777c)
![image](https://github.com/jon-atkinson/pySorts/assets/95665780/5903eb09-026e-4800-8164-5d61538d5b69)

Happy Sorting!
