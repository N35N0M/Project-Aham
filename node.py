## Representation of a node (road intersection on a map)
class Node():
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    # How to check if two nodes are equal
    def __eq__(self, other):
        if self.latitude == other.latitude and self.longitude == other.longitude:
            return True
        else:
            return False

    ## How to print Node instance to console
    def __repr__(self):
        theString = "NODEDATA\n" + "Latitude:\t" + str(self.latitude) +  "\t\tLongitude:\t" + str(self.longitude) + "\n\n"
        return theString

    ## Default hashing for Node in order to make it hashable
    def __hash__(self):
        return hash(repr(self))