"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    
    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        
        self.designation = info['designation']   #ELABORATE:Get NEO's designation 
        if(not info['name']):  #ELABORATE:get NEO's name, if its empty string, then default is None 
            self.name=None
        else:
            self.name=info['name']
        if(not info['diameter']):   #ELABORATE:get NEO's diameter, if its not defined/unknown, then default is "nan"
            self.diameter = float('nan')
        else:
            self.diameter=float(info['diameter'])
        if(info['hazardous']=='Y'):  #ELABORATE:get NEO's status for hazardous or not
            self.hazardous=True
        else:
            self.hazardous=False
        
        #ELABORATE: Create an empty initial collection of linked approaches. To be populated later when NEOs are linked o their corresponding closed approaches
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        #ELABORATE: Use self.designation and self.name to build a fullname for this object.
        if(self.name):
            return f"{self.designation} {self.name}"
        else:
            return f"{self.designation}"

    def __str__(self):
        """Return `str(self)`."""
        #ELABORATE: If self.hazardous is True, then return an empty string, but if its false, then return the string "not" so that later it can be used in the output of __str__
        if(self.hazardous): 
            haz = ""
        else:
            haz = "not"
        
        return f"A NearEarthObject {self.fullname!r} has a diameter of {self.diameter:.3f} km & is {haz} potentially hazardous"
        

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")
    
    def serialize(self):  
        """Return a dictionary of all essential keywords of a NEO's object with their corresponding values defined in the class constructor __init__. 
        This dictionary is later used to write into CSV/JSON output file.
        Essential keyword for a NEO object are : name, designation,diameter_km,potentially_hazardous.
        """
        
        neo_dict=dict()
        if(self.name is None):
            neo_dict['name']=''
            
        else:
            neo_dict['name']="{neo_name}".format(neo_name=self.name)
            
        neo_dict['designation']="{des}".format(des=self.designation)
        neo_dict['diameter_km']=self.diameter
        neo_dict['potentially_hazardous']=self.hazardous
        
        return neo_dict

class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
   
    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        
        self._designation = info['designation'] #ELABORATE:get designation of NEO
        if(not info['cd']): #ELABORATE:get unformatted date & time of NEO, if not defined assign none, else convert to datetime format
            self.time = None  
        else:
            self.time=cd_to_datetime(info['cd'])
            
        self.distance = float(info['distance']) #ELABORATE:get NEO's closest distance of approach
        self.velocity = float(info['v_rel'])  #ELABORATE:get NEO's closest approach velocity relative to earth

        #ELABORATE : Create an attribute for the referenced NEO, originally None. It is updated later when NEO's are linked to their corresponding closed approaches
        self.neo=None 

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        
        return f"On {self.time_str!r},  {self.neo.fullname} approaches at a distance of {self.distance:.2f} au & a velocity of {self.velocity:.2f} km/s"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r}, designation={self._designation!r})")
    
    def serialize(self):   
        """Return a dictionary of all essential keywords of a NEO's cloase approach object with their corresponding values defined in the class constructor __init__. 
        This dictionary is later used to write into CSV/JSON output file.
        Essential keyword for a NEO object are : datetime_utc,distance_au,velocity_km_s.
        """
        
        approach_dict=dict()
        approach_dict['datetime_utc']="{date_time}".format(date_time=self.time_str)
        approach_dict['distance_au']=self.distance
        approach_dict['velocity_km_s']=self.velocity
        
        return approach_dict
        
                    
                                                  
