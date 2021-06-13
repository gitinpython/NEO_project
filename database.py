"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""

class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        #ELABORATE
        #:param NEO_des: Dictionary of all "designations" as keys & their corresponding "neos" as values to map neos with their corresponding designations(additional data structure to facilitate NEO-Close approach linking)
        #:param NEO_names: Dictionary of all "neo names" as keys & their corresponding "neos" as values to map neos with their corresponding names(additional data structure to facilitate NEO-Close approach linking)
        self._neos = neos
        self._approaches = approaches
        self.NEO_des = dict((neo.designation,neo) for neo in self._neos)
        self.NEO_names = dict((neo.name,neo) for neo in self._neos)
        
    ###GOOD TO HAVE BUT NOT MANDATORY : If you want to print all NEOs having the same name, follow/enable below code to build the self.NEO_names; else keep it disabled###
            #  self.NEO_names = dict()
             # for neo in self._neos:
               #    if neo.name not in self.NEO_names:
                #       self.NEO_names[neo.name]=list()
                 #  self.NEO_names[neo.name].append(neo)
    ###GOOD TO HAVE BUT NOT MANDATORY : If you want to print all NEOs having the same name, follow/enable above code to build the self.NEO_names; else keep it disabled### 
     
    #ELABORATE : Linking close approach with their corresponding NEO's if their designation is the same
        for cad in self._approaches:
            if cad._designation in self.NEO_des.keys():
                cad.neo=self.NEO_des[cad._designation]
                self.NEO_des[cad._designation].approaches.append(cad)
        

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        #ELABORATE : if designation argument passed by user belongs to the dictionary mapping of neo-designation, return the corresponding NEO specific to that designation, else return None
        if(designation in self.NEO_des.keys()):
            return self.NEO_des[designation]
        else:
            return None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        #ELABORATE : if name argument passed by user belongs to the dictionary mapping of neo-name, return the corresponding NEO specific to that name, else return None

        if(name in self.NEO_names.keys()):
            return self.NEO_names[name]           
        else:
            return None
        
    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        
        for approach in self._approaches:
            output=[f(approach) for f in filters]   #ELABORATE:output consists of a list of closed approaches which are filtered by the :param filters
            if(len(output) > 1): #ELABORATE:if output is a collection of more than 1 filter functions , then return approach only if it matches/satisfies all the filter functions 
                if(all(output)): 
                    yield approach
            elif(len(output)==1): #ELABORATE:if output contains only one filter function, then return approach if it matches/satisfies this filter function 
                if(output[0]):
                    yield approach
            else:   #ELABORATE:if output is empty or doesnt match any filter criteria, then return all closed approaches by default 
                yield approach
