#!/usr/bin/env python3

"""
Script for creating a table with the number of publications per year for each novel in the collection.

Input: html files from worldcat downloaded by gethtmlsworldcat.py.
Output: csv-file
"""

from bs4 import BeautifulSoup as bs
import glob
import os
from os.path import join
import re
import pandas as pd
import logging

# === Parameters ===

#dir=""
#htmlpages = join(dir, "html", "*.html")


# === Functions ===

def read_html(file):
    """
    Parsing with Beautiful Soup, see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    
    input: html file
    output: parsed html
    
    """
    with open(file, "r", encoding="utf8") as infile:
        html = infile.read()
        html = bs(html, "html.parser")
        return html


def get_id(file):
    """
    input: file
    output: filename (in this case the id of the novel)
    """
    base = os.path.basename(file)                   
    id = str(os.path.splitext(base)[0])
    #id = id.split("_html")[0]
    id = id.split("_html(.*?)")[0]
    print(id)
    return id


def test_search_result(html, id):
    """
    Prints warning if there are no search results in worldcat and writes warning into log file.
    The warning contains the id and the search strings of the title and the author.
    
    input: html file
    output: log file
    """
    text = "No results match your search"
    try:
        errors = html.find('div', {'class' : 'error-results'}).get_text()
        errors = errors.strip()
        search_string = re.search("ti:(.*?)au:(.*?)\'", errors).group()
        title = re.sub(" au:(.*?)\'", "", search_string)                   # extracts search string for the title
        title = re.sub("ti:", "", title)
        author = re.search("au:(.*?)\'", search_string).group()            # extracts search string for the author
        author = re.sub("au:", "", author)
        author = re.sub("\'", "", author)
        if errors.startswith(text):
            print(id + ": No search result in worldcat! Please check the spelling of author and title (see log file)!")
            logging.warning(id + ": No search result in worldcat! Search strings: title: '" + title + "', author: '" + author + "'")
    except:
        pass



def fill_publicationlist(html, id, publist):
    """
    
    Extracts the year of every publication and adds it to a list.
    If there isn't mentioned a year or the extracted number hasn't got a value between 1840 an 2019, the year will be set to 0 in order to contribute to the total number of publications.
    
    input: html file (search result for a specific novel in worldcat), id, list (empty or already filled with publication years from first pages of the search result)
    output: list with publication years of one novel
    
    """
 
    list = html.find_all('span', {'class' : 'itemPublisher'})       # search for <span class="itemPublisher">
    for element in list:
        element = str(element)
        try:
            element = re.search("[0-9]+", element).group()          # filters the year from the result string
        except:
            print(id + ": No publication year found!")
            logging.warning(id + ": No publication year found!")
            element = 0                                             # if the year isn't mentioned, the year 0 is set
        element = int(element)
        if element not in range(1840, 2020):                        # if the publication year isn't a number between 1840 and 2020
            element = 0
        publist.append(element)                                     # adding the year to the list
    return publist
    

def create_dictionary():
    """
    Returns a dictionary with keys from 1840 to 2019, each value is an empty dictionary.
    """
    keys = [0]
    for x in range(1840,2020):                        # creates a list with keys from 1840 to 2019 and 0 (for cases where there is no mentioned publication year)
        keys.append(x)
    
    pubdict = {key: {} for key in keys}               # creates a dictionary with the keys from the list and sets empty dictionaries as values
    #print(pubdict)
    return pubdict


def fill_dictionary(pubdict, publist, id):
    """
    Writes the information from the publication list into the dictionary.
    
    input: dictionary with years from 1840 to 1940 as keys and empty dictionaries as values; list with publication years; id of the novel
    output: dictionary in which every year (1840 to 2019) is related to another dictionary containing the novel id (keys) and the number of publications in the specific year (values)
    """
    
    for x in range(1840,2020):                 # adding a new dictionary entry to each key (year): id of the novel (key) and "0" (number of publications; value)
        d = pubdict[x]
        d[id] = 0
        
    d = pubdict[0]                             # adding the dictionary for the year "0" (cases where there is no mentioned year)
    d[id] = 0
    
    for year in publist:                           # for each year in the list the corresponding number of publications is increased by 1
       pubdict[year][id] = pubdict[year][id] + 1     
    
    return pubdict
    

def create_dataframe(pubdict):
    """
    Changes the dictionary into a dataframe using pandas, see: https://pandas.pydata.org/.
    
    input: dictionary
    output: dataframe
    """
    dataframe = pd.DataFrame.from_dict(pubdict, orient='index')
    return dataframe


def add_sum(dataframe):
    """
    Adds the total number of publications of each novel.
    """
    dataframe.loc['Total']= dataframe.sum()


def save_csv(dataframe):
    """
    Saves the dataframe as csv file.
    """
    dataframe.to_csv('reprint_counts.csv')
     
                
# === Coordinating function ===

def main(htmlpages):
    """
    Coordinates the creation of the publication table.
    """
    print("--createpublicationtable")
    logging.basicConfig(filename='createpublicationtable.log',level=logging.WARNING, format='%(asctime)s %(message)s')
    publdict = create_dictionary()
    publist = []
    id_prev = ""
    
    for file in glob.glob(htmlpages):
        html = read_html(file)
        id = get_id(file)
        test_search_result(html, id)
        if id == id_prev:                                            # html file contains second, third, ... page of the search result
            publist = fill_publicationlist(html, id, publist)        # existing publist is appended
        else:                                                        # html contains the first page of the search result
            publist = []                                             # a new publist is created
            publist = fill_publicationlist(html, id, publist)
        fill_dictionary(publdict, publist, id)
        id_prev = id
    
    dataframe = create_dataframe(publdict)
    add_sum(dataframe)
    save_csv(dataframe)
        
        
#main(dir, htmlpages)
