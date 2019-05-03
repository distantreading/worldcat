# Guidelines for using the "worldcat" scripts


## Purpose

The worldcat.py scripts take the XML files of an ELTeC collection as input and query Worldcat in order to retrieve the reprint data for each novel contained in the collection, for the period 1840 to 2019. The result is a CSV file with the reprint counts for each year and each novel.

## Requirements

The scripts are written in Python3 so you need Python 3 on your computer. The scripts have been tested with Python 3.6. 

In addition, you need to have the following packages installed: pandas, Beautifulsoup, requests, yaml. 

Finally, you need the contents of the "worldcat" repository as well as the contents of the ELTeC collection of your choice somewhere on your computer.

## Setting the parameters 

All parameters are set in the configuration file called "config.yaml". You find explanations there for each parameter. 

## Running the scripts 

The easiest way of running the script is to do so using the Terminal. 

1. Navigate to the folder containing the "run_worldcat.py" script.
2. Type "python3 run_worldcat.py" and hit return. 

## Contact 

If you run into issues, such as getting incomprehensible error messages or obtaining obviously erroneous results, please get in touch with Christof Schöch, <schoech@uni-trier.de>. 

## Attribution and Licence

The scripts have been developed by Anne Klee and Johanna Konstanciak at the University of Trier, Germany. 

The scripts are published with a Creative Commons Attribution 4.0 International licence: https://creativecommons.org/licenses/by/4.0/. 



