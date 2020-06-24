#!/usr/bin/env python3

"""
Script for creating a minimal metadata table of a collection of novels.
The table contains the novel id, title and name of the author.

Input: xml files (novels)
Output: metadata as csv-file
"""


from bs4 import BeautifulSoup as bs
import os
from os.path import join
import glob
import re
import pandas as pd

from transliterate import translit, get_available_language_codes

# === Functions ===

def read_xml(file):
    """
    Parsing with Beautiful Soup, see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    
    input: xml file
    output: parsed xml
    
    """
    with open(file, "r", encoding="utf8") as infile: 
        xml = infile.read()
        #xml = bs(xml, "xml")
        return xml


def get_id(file):
    """
    Extracts the xml:id from the xml file.
    """
    try:
        id = re.search("xml:id=\"(.*?)\"", file).group()
        id = re.search("\"(.*?)\"", id).group()
        id = re.sub("\"", "", id)
    except AttributeError:
        id = re.search("xml:id=\s\"(.*?)\"", file).group()
        id = re.search("\"(.*?)\"", id).group()
        id = re.sub("\"", "", id)

    return id


def get_title(xml, lang):
    """
    Extracts the title from the teiHeader.
    """
    title = xml.find("title").get_text()
    
    if lang == "srp":
        #print(get_available_language_codes())
        title = translit(title, "sr", reversed=True)
    elif lang == "ukr":
        title = translit(title, "uk", reversed = True)
    #elif lang == "gre":
    #    title = translit(title, "el", reversed = True)
    print(title)
    return title


def get_author(xml, lang):
    """
    Extracts the author name from the teiHeader.
    """
    author = xml.find("author").get_text()
    author = re.sub('\((.*?)\)', "", author)
    
    if lang== "srp":
        author = translit(author, "sr", reversed=True)
    elif lang == "ukr":
        author = translit(author, "uk", reversed=True)
    #elif lang == "gre":
    #    author = translit(author, "el", reversed=True)
    return author


def append_dict(dict, id, basename, title, author):
    """
    Adds metadata to the dictionary.
    """
    dict[id] = [basename, title, author]
    return dict


def save_csv(dict, settings_dict, results):
    """
    Turns the dictionary into a dataframe.
    Saves the dataframe to a csv file.
    """
    csvpath = join(results, "csv-files")
    if not os.path.exists(csvpath):
        os.makedirs(csvpath)
    dataframe = pd.DataFrame.from_dict(dict, orient="index")
    dataframe.to_csv(join(csvpath,'{}_metadata.csv'.format(settings_dict["lang"])), index_label="xmlid", header = ["basename", "title", "au-name"], sep="\t", encoding="utf-8-sig")
    
    
# === Coordinating function ===

def main(settings_dict):
    """
    Coordinates the creation of the metadata table.
    """
    print("--getmetadata")
    dict = {}
    
    xmlfolder = settings_dict["xml_path"]
    lang = settings_dict["lang"]
    results = settings_dict["results"]
    for file in glob.glob(xmlfolder):
        xml = read_xml(file)
        basename,ext = os.path.basename(file).split(".")
        id = get_id(xml)
        print(id)
        xml = bs(xml, "xml")
        title = get_title(xml, lang)
        author = get_author(xml, lang)
        append_dict(dict, id, basename, title, author)
        save_csv(dict, settings_dict, results)
