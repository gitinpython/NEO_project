"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # Write the results to a CSV file, following the specification in the instructions.
   
    final_list=[] #ELABORATE:create a list of dictionaries where every dictionary belongs to a result(aka close approach 's object) containing all essential fieldnames as keys with their corresponding values
    for elem in results:
        elem_dict=elem.serialize()
        elem_dict.update(elem.neo.serialize())
        final_list.append(elem_dict)
    with open(filename,'w') as outfile:
        writer=csv.DictWriter(outfile,fieldnames)
        writer.writeheader()
        for f in final_list:  #ELABORATE:Here, f is a dictionary that represents details of every close approach object & is written to the csv file
            writer.writerow(f)
        
 
def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # Write the results to a JSON file, following the specification in the instructions.
    final_list=[] #ELABORATE:create a list of dictionaries where every dictionary belongs to a result(aka close approach 's object) containing all essential fieldnames as keys with their corresponding values
    for elem in results:
        elem_dict=elem.serialize()
        elem_dict['neo']=elem.neo.serialize() #ELABORATE:json file should have a key named "neo" that is a dictionary of all essential details of a NEO object having a well-defined close approach
        final_list.append(elem_dict)
    with open(filename,'w') as outfile:
         json.dump(final_list,outfile) 
         
