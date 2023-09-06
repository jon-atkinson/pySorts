# pySorts
Simple collection of sorts, testing and comparison CLI for comparing the implementations of many commonly used simple sorting algorithms implemented in python. 

Ctypes used to call C implementations of all sorting algorithms, bash script for library compilation included but an up to date comilation of cSorts.so should exist in the correct position already. C functions require slightly different input array types to function correctly, the functions included in gen_data_sets.py take a language string param that takes care of this. All functions written in the current package should implement this correctly. 

Unittest implemented for functioning components.

Not really feasible for actual use, more to see how python implementation of different data structures and memory allocation changes the performance of each of the implemented sorts. 

Also chose to do something the language isn't designed for to hopefully come up against more of the errors and be able to write intuitively python-styled code quicker. 

Possibility to extend/change this repo to run implementations of different sorting algos in different languages against each other over a series of synthetic tests, and have a unified frontend interface for visualisation - long way down the road for this though. 

Leaning towards using seaborn for it's customisable and generally better looking and more developed UI.
