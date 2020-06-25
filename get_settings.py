# This  script will apply all settings, which are chosen in config.yaml
# It includes: the language, based on that the xml-folder, the csv-file, the language-parameter for the worldcat-url, the write-file, which stores the
# html-pages, and the htmlpages parameter
# the data is stored in a dictionary, that will be used in the run_worldcat.py (and the dependent scripts)
import os
from os.path import join

def get_lang(lang, d): # input: empty dictionary, the chosen language; new key "lang", value is the chosen language  
    
    d["lang"] = lang
    
    return lang, d
    
    
def get_xml_folder(d, basedir, level): # input: dictionary, xml_path, level (both parameters from config.yaml); gets to the chosen language and the chosen level
    
    #print(level)
    if not os.path.isdir(basedir):   # checking the xmlpath
        print("Wrong path. No XML-TEI files can be found. Please adjust the basedir variable in the config file!")
    xml_folder = basedir + "/ELTeC-{}/{}/*.xml".format(d["lang"], level)
    d["xml_path"] = xml_folder
    
    return d, xml_folder

def get_csv_file(d): # input: dictionary; returns csv_file with language extention
    
    csv_file = d["lang"] + "_" + "metadata.csv"
    d["csv_file"] = csv_file
    
    return d

def match_langs(lang, d, chosen_dict, chosen_key):
    
    if lang in [*chosen_dict]:    
        for key, value in chosen_dict.items():
        
            if lang == key:
                val = value
                break
        d[chosen_key] = val
    else:
        print("choose valid lang")
        
    return d

def get_write_file(d, write_file): # for creating or using a sub-file for each language, where html-pages will be stored
    
    new_write_file = join(write_file, d["lang"])
    #print("new write file", new_write_file)
    
    d["write_file"] = new_write_file
    #print(new_write_file)
    return new_write_file, d

def get_html_file(d, htmlpages): # will be used to get the right html pages, based on the htmlpages-parameter of the config.yaml
    
    html_folder, ext = htmlpages.split("/")
    html_folder = join(html_folder, d["lang"], ext)
    #print("html_folder", html_folder)
    #print("ext", ext)
    d["html_folder"] = html_folder

    return html_folder, d

def get_wdir_file(d, wdir):
    
    d["wdir"] = wdir
    
    return d

def get_results_file(d, results):
    
    d["results"] = results
    
    return d

def main(lang, basedir, level, wdir, results):
    print("--getsettings")
    d_keys = ["lang", "xml_path", "csv_file", "lang_worldcat", "lang_hit", "write_file", "html_folder"]
    d = {key: None for key in d_keys}
    
    worldcat_lang = {"fra": "fre", "eng":"eng", "ita":"ita", "deu":"ger", "por":"por", "spa":"spa", "srp":"srp", "gre":"gre", "ukr":"ukr","slv":"slv", "rom":"rum", "nor":"nor", "cze":"cze", "lit":"lit", "pol":"pol", "frch":"fre", "gsw": "ger"} # dictionary contains ELTeC-language abbreviations as keys, worldcat-language codes as values 
    hit_lang = {"fra":"French", "eng":"English", "ita":"Italian" , "deu":"German", "por":"Portuguese", "spa":"Spanish", "srp":"Serbian", "gre":"Greek, Modern[1453-]", "ukr":"Ukranian", "slv":"Slovenian", "rom":"Romanian", "nor":"Norwegian", "cze":"Czech", "lit":"Lithuanian", "pol":"Polish", "frch": "French", "gsw":"German"} # dictionary contains ELTeC-language abbreviations as keys, worldcat-language category as values
    
    write_file = join(wdir, "html")
    htmlpages = join(wdir, "html/*.html")
    
    lang, d = get_lang(lang, d)
    d, xml_folder = get_xml_folder(d, basedir, level)
    d = get_csv_file(d)
    d = match_langs(lang, d, worldcat_lang, "lang_worldcat")
    d = match_langs(lang, d, hit_lang, "lang_hit")
    d = get_wdir_file(d, wdir)
    new_write_file, d = get_write_file(d, write_file)
    html_folder, d = get_html_file(d, htmlpages)
    d = get_results_file(d, results)
    print(d)
    return d
