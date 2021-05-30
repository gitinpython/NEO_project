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
    # TODO: Load NEO data from the given CSV file.
    neo_list=[]
    with open(neo_csv_path) as infile:
        read_neo=csv.DictReader(infile)
        for row_neo in read_neo:
            neo_list.append(NearEarthObject(designation=row_neo['pdes'],name=row_neo['name'],diameter=row_neo['diameter'],hazardous=row_neo['pha']))
    return neo_list  #list of NEO objects


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    closeapproach_list=[]
    with open(cad_json_path) as infile:
        ca_load=json.load(infile)
        icd=ca_load['fields'].index('cd')
        idist=ca_load['fields'].index('dist')
        ides=ca_load['fields'].index('des')
        ivrel=ca_load['fields'].index('v_rel')
        for data in ca_load['data']:
            closeapproach_list.append(CloseApproach(cd=data[icd],designation=data[ides],distance=data[idist],v_rel=data[ivrel]))
    return closeapproach_list  #list of CA objects
