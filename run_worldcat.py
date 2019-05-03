

# Imports and parameters

import yaml 
import getmetadata 
import gethtmlworldcat
import createpublicationtable

configfile = "config.yaml"


def main(configfile): 
    with open(configfile, 'r') as configfile:
        config = yaml.load(configfile)
    getmetadata.main(config["xmlpath"])
    gethtmlworldcat.main(config["plain_suchstring"], 
                         config["csv_file"],
                         config["write_file"])
    createpublicationtable.main(config["htmlpages"])
    

main(configfile)
