

# Imports and parameters

import yaml 
import getmetadata 
import gethtmlworldcat
configfile = "config.yaml"


def read_config(configfile):
    with open(configfile, 'r') as configfile:
        config = yaml.load(configfile)
    return config


def main(configfile): 
    config = read_config(configfile)
    print(config)
    #getmetadata.main(config["xmlpath"])
    #print(config["csv_file"])
    gethtmlworldcat.main(config["plain_suchstring"], config["csv_file"])
    #createpublicationtable.main()
    

main(configfile)

