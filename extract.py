"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    
    neo_list=[]
    with open(neo_csv_path) as infile:
        read_neo=csv.DictReader(infile)
        for row_neo in read_neo:
            neo_list.append(NearEarthObject(designation=row_neo['pdes'],name=row_neo['name'],diameter=row_neo['diameter'],hazardous=row_neo['pha']))
    return neo_list  #ELABORATE: list of NEO objects


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    
    closeapproach_list=[]
    with open(cad_json_path) as infile:
        #ELABORATE: 
        #Get the indices of all necessary parameters such as : cd (date & time) , dist (approach distance), des (NEO's designation), v_rel (NEO's relative approach velocity)
        #so that they can be used later to extract the information corresponding to these parameters for every NEO-list element in the JSON dictionary's "data" key
        #(ca_load is a JSON dictionary that contains a key - "data" & a key - "fields" where the former is paired to a value that is a list of lists where every list holds information corresponding to the parameters/elements of another list which is represented as the value of the key "fields" 
        ca_load=json.load(infile)
        icd=ca_load['fields'].index('cd')
        idist=ca_load['fields'].index('dist')
        ides=ca_load['fields'].index('des')
        ivrel=ca_load['fields'].index('v_rel')
        for data in ca_load['data']:
            closeapproach_list.append(CloseApproach(cd=data[icd],designation=data[ides],distance=data[idist],v_rel=data[ivrel]))
    return closeapproach_list  #ELABORATE: list of Close Approach objects
