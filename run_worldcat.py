

# Imports and parameters

import yaml 
import getmetadata 
import gethtmlworldcat
import createpublicationtable
import get_settings
import create_summary

configfile = "config.yaml"


def main(configfile): 
    with open(configfile, 'r') as configfile:
        config = yaml.safe_load(configfile)
    settings_dict = get_settings.main(config["lang"], config["xmlpath"], config["level"], config["csv_file"], config["write_file"], config["htmlpages"])
    getmetadata.main(settings_dict)
    gethtmlworldcat.main(settings_dict, config["plain_suchstring"])
    createpublicationtable.main(settings_dict)
    create_summary.main(settings_dict)
    

main(configfile)
