# pySorts
Simple collection of sorts, testing and comparison CLI for comparing the implementations of many commonly used simple sorting algorithms implemented in python. 

Ctypes used to call C implementations of all sorting algorithms, bash script for library compilation included but an up to date compilation of cSorts.so should exist in the correct position already. C functions require slightly different input array types to function correctly, the functions included in gen_data_sets.py take a language string param that takes care of this. All functions written in the current package should implement this correctly. 

Unittest implemented for functioning components.

Not really feasible for actual use, more to see how python and C implementation of different data structures and memory allocation changes the performance of each of the implemented sorts. 

Frontend interface for visualisation is in the works - long way down the road for this though (also working off ssh so this is a PITA to work on rn). 

Leaning towards using seaborn plotting for it's customisable and generally better looking and more developed UI.
