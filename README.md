# file-finder
A utility to recursively search a directory for all instances of files matching a search string.

I made this utility to help with locating a group of files that contain a certain extension (.nex). 

I had multiple terrabytes of storage that I had to search, and I was curious if a CPP application would outperform 
python, given that the time limiting factor was likely opening/closing the files rather than the actual iteration of folders. 

This application outperformed python by less than 3s, which was not surprising. 

The python version can be found at the top level of this repository.
It contains routines for parallel processing, which weren't used in the benchmark. 
