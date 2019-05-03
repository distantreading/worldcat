

# Imports and parameters

import yaml 
import getmetadata 
#import gethtmlworldcat

configfile = "config.yaml"


def main(configfile): 
    with open(configfile, 'r') as configfile:
        config = yaml.load(configfile)
    getmetadata.main(config["xmlpath"])
    

main(configfile)
