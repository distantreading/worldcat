# worldcat

Guidelines for using the "worldcat" scripts


## Purpose

The worldcat-scripts take the XML files of an ELTeC collection as input and queries the WorldCat catalogue in order to retrieve the reprint data for each novel contained in the collection, for the period 1840 to 2019. The result are a CSV file with the reprint counts for each year and each novel, as well as a CSV file that provides a summary of the reprints counts. This is research software intended for a very specific purpose, so please don't expect any bells and whistles. 

## Requirements

The scripts are written in Python 3 so you need Python 3 on your computer. The scripts have been tested with Python 3.6. 

In addition, you need to have the following packages installed: pandas, Beautifulsoup, requests, yaml or pyyaml, numpy and transliterate. 

Finally, you need the contents of the "worldcat" repository (https://github.com/distantreading/worldcat) as well as the contents of the ELTeC collection of your choice (see: https://github.com/COST-ELTeC).

## Folders and files

The "worldcat repository" contains all required scripts. You can save it anywhere on your computer.

You can also save your chosen ELTec repository in a folder of your choice. The path to the top-level folder of the intended repository has to be assigned to the variable "basedir" in the configration file ("config.yaml"). 
The repository should be named ELTeC-(chosen language), e.g. ELTeC-fra.

The Working Directory (wdir) is the path where the Worldcat-Scripts are stored and where the downloaded html-pages will be stored in a new folder named "html", these are the search result for the request in Worldcat.
In addition the script adds the folders "csv-files" and "logfiles". If you wish to choose another directory other than your working directory, you can specify it in the variable "results". 

The folder "csv-files" contains:
* xxx_metadata.csv: contains xmlid, title and author name for each novel in the collection
* xxx_reprint_counts.csv: number of reprints of each novel between 1840 and 2019
* xxx_summary.csv: contains for each novel total number of reprints, number of reprints in target period and canonicity status

The folder "logfiles" contains:
* xxx_publicationtable.log: log file that documents problems while reading out the reprints from worldcat


## Setting the parameters 

All parameters are set in the configuration file called "config.yaml". You find explanations there for each parameter. Please make sure to save the settings before running the scripts.

## Running the scripts 


The easiest way of running the script is to do so using the Terminal. 

1. Navigate to the folder containing the "run_worldcat.py" script.
2. Type "python3 run_worldcat.py" and hit return. 


## Contact 

If you run into issues, such as getting incomprehensible error messages or obtaining obviously erroneous results, please get in touch with Christof Schöch, <schoech@uni-trier.de>. 

## Attribution and Licence

The scripts have been developed by Anne Klee and Johanna Konstanciak at the University of Trier, Germany, in 2019-2020. 

The scripts are published with a Creative Commons Attribution 4.0 International licence: https://creativecommons.org/licenses/by/4.0/. 



