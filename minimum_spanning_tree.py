"""
Program: minimum_spanning_trees.py
Author: Taynor McNally
Date: 23/04/2023
Synopsis:
Using X and Y point List objects to create a Minimum Spanning Tree.
The application has sub programs that calculates the distances between
the X and Y points, and a 256 SHA Hash checksum of one of the Points
List object.
Libraries:
MatplotLib
Networkx
Math
Hashlib
"""

# required to plot the graph of the MST
import matplotlib.pyplot as plt

# required to calculate the MST used library instead of calculating the MST manually
# would have considered Primm's algorithm, find the unit that suggested using
# already created libraries and reference this
import networkx as nx

# required to calculate the distance between two point
import math

# to create the hash 256 SHA value
from hashlib import sha256


# The first sub program for performing the 256 SHA hash function
class HashFunction:
    """The Class object contains the program objects to create a 256 SHA hash from a string object."""

    def __init__(self):
        """
        The attributes of the HashingFunction class initialised values to blank strings, for the List
        and 256 SHA Hash value output.
        """
        # These attributes are needed to convert a simple data structure to a string object, and hold the value
        # of the 256 SHA Hash.

        # This object will store the values of the List data structure, after converting it to a string object. This
        # value has been initialised to a blank string, to ensure the data type is correct.
        self.converted_list_to_string = ''

        # This object will store the value of the 256 SHA hash, after extracting the contents from the
        # list_of_values parameter. This value has been initialised to a blank string,
        # to ensure the data type is correct.
        self.hash_value = ''

    def __str__(self):
        """String representation of the HashFunction objects"""

        return f'hash value: {self.hash_value}, list object: {self.converted_list_to_string}'

    # convert the values in the list_of_values parameter to a string ready for the 256 SHA hashing
    def convert_list_to_string(self, list_of_values_parameter):
        """Extract the list_of_values content parameter, and convert to a string."""
        # Extract and convert the content of the list_of_values list parameter to a string.

        # Copy the list_of_values content to the class variable converted_list_to_string
        self.converted_list_to_string = list_of_values_parameter

        # Take each item in the converted_list_to_string object, using the temporary variable "item". Join the values
        # together as one string, saving the contents in the mutated converted_list_to_string class variable.
        self.converted_list_to_string = ''.join(str(item) for item in list_of_values_parameter)

        return self.converted_list_to_string

    # Take the parameter hash_string and convert to a 256 SHA Hash. The hash_string is the self.converted_list_to_string
    # output. The hash_string is fed into the hashlib sha256 function to create the hash value.
    def hash_the_string(self, hash_string_parameter):
        """Create the hash value from the class variable converted_list_to_string"""
        # Need to set the encode function to use utf-8 when hashing a string value.

        # Perform the hash.
        self.hash_value = sha256(hash_string_parameter.encode('utf-8')).hexdigest()
        return self.hash_value


# The sub program to create coordinates from two Lists of points X and Y. Once the coordinates have been created,
# an algorithm is implemented to calculate each corresponding X and Y coordinate.
class Points:
    """
    The Class object contains the program objects to create X and Y coordinates from Python Lists. Once the
    coordinates have been created, calculate the distance between the respective points of the coordinates object.
    """

    def __init__(self):
        """Initialise the point objects X and Y to empty lists, these lists will be used to build the coordinates."""
        # The X and Y points instantiated as empty lists.
        self.x_points = []
        self.y_points = []

        # Store the value of the calculated distance between points X and Y in the coordinates object, initialised
        # to a Float data type.
        self.distance = 0.0

        # Coordinates are the zipped values of the X and Y points Lists.
        self.coordinates = zip(self.y_points, self.x_points)

        # Empty list to store the calculated distances between the X and Y points from the coordinates object. A loop
        # is performed over the coordinates object, calculating the distance between the points. The results are
        # appended to the list object.
        self.list_of_distances = []

    def __str__(self):
        """String representation of the Point class objects"""

        return f'x point: {self.x_points}, y point : {self.y_points}, coordinates: {self.coordinates}, ' \
               f'individual distance: {self.distance}, list of distances: {self.list_of_distances}'

    # Take the X and Y point lists and zip together, and convert to a Dictionary data structure.
    def zip_coordinates(self, y_point_parameter, x_point_parameter):
        """Zip the X and Y points list objects into the coordinates object, converted to a Dictionary data structure."""
        # Takes the List objects of the X and Y points, zips them together and converts the zip object to a Dictionary.

        # Take the X and Y point_list values from the parameters and load them into the class variables
        # x_point and y_point
        self.x_points = x_point_parameter
        self.y_points = y_point_parameter

        # Zip the X and Y point class variable lists into the class coordinates zip object
        self.coordinates = zip(self.y_points, self.x_points)

        # Convert the class coordinates zip object to a Dictionary
        self.coordinates = dict(self.coordinates)

        return self.coordinates

    # Take the class coordinates object, loop through the object and calculate the distance between each pair.
    def calculate_distance(self, coordinates_parameter):
        """Calculate the distance between each object pair in the class coordinates object."""
        # Takes the converted coordinates Dictionary object and performs a distance operation, between each object pair.

        # Move the coordinates_parameter value to the class coordinates Dictionary object
        self.coordinates = coordinates_parameter

        # x, y are the temporary variables of the x and points concatenated in the coordinates Dcitionary object
        for y, x in self.coordinates.items():
            x = float(x)
            y = float(y)

            # The distance calculation algorithm
            distance_calculation: float = x * x + y * y
            self.distance = math.sqrt(distance_calculation)
            self.list_of_distances.append(self.distance)

        return self.list_of_distances


# The sub program to create a minimum spanning tree using a coordinates Dictionary object created from the Points class.
# The class makes use of the networkx library, the library uses the Kruskal's implementation.
class MinimumSpanningTree(Points):
    """
    The Class object contains the program objects to create a minimum spanning tree, using a coordinates Dictionary
    object of X and Y points. Once the minimum spanning tree has been created, a visualisation using the Matplotlib
    library is available.
    """

    def __init__(self):
        """Initialise the networkx graph objects, and empty X and Y points Lists and the coordinates Dictionary."""
        # The X and Y points and coordinates can be user supplied arguments. The empty networkx Graph objects
        # are required to build the Minimum Spanning Tree and the visualisation.

        self.mst_object = nx.classes.graph.Graph
        self.graph_object = nx.classes.graph.Graph
        self.coordinates = dict()

    def __str__(self):
        """String representation of the MinimumSpanningTree class objects."""

        return f'tree object: {self.mst_object} graph object: {self.graph_object} coordinates: {self.coordinates}'

    # Create an empty Graph object from the networkx library, this will be the base object of the minimum spanning tree.
    def create_minimum_spanning_tree(self):
        """Create an empty networkx minimum spanning tree graph object."""
        # This is the base graph object used to build the minimum spanning tree from the networkx library.

        # This is the empty networkx empty base Graph object.
        self.graph_object = nx.Graph()
        return self.graph_object

    # Add the edges to the minimum spanning tree graph object
    def build_minimum_spanning_tree(self, coordinates_parameter):
        """
        Add edges to the minimum spanning tree networkx Graph object, by looping through the coordinates object.
        Use the coordinates_parameter parameter to input the coordinates' argument."""
        # Add the edges to the base Graph object by looping through the coordinates object fed into the method.
        # These coordinates are X and Y points pairs.

        # move the coordinates_parameter parameter value into the coordinates class object.
        self.coordinates = coordinates_parameter

        # loop through the coordinates Dictionary object and add the edges to the base Graph object.
        for y, x in self.coordinates.items():
            self.graph_object.add_edge(y, x)

        return self.graph_object

    # Return the edges of the minimum spanning tree object.
    def print_minimum_spanning_tree(self, graph_object_parameter):
        """
        Prints the minimum spanning tree content from the networkx implementation. Takes the graph_object_parameter
        argument as input to print the minimum spanning tree.
        """
        # Takes the graph object as input built from the build_minimum_spanning_tree method.

        # Move the graph_object_parameter argument into the class graph_object variable.
        self.graph_object = graph_object_parameter

        # Use networkx function to create the minimum spanning tree object from the input of the Graph object.
        self.mst_object = nx.minimum_spanning_tree(self.graph_object)
        return self.mst_object

    # Produce the visualisation of the minimum spanning tree using default settings.
    def create_minimum_spanning_tree_visual(self, graph_object_parameter, mst_parameter):
        """
        Create the minimum spanning tree visual using the graph_object_parameter and mst_parameter arguments.
        These arguments are the outputs from the build_minimum_spanning_tree and print_minimum_spanning_tree methods.
        """
        # The build_minimum_spanning_tree and print_minimum_spanning_tree methods outputs
        # are input dependency arguments for this method.

        # Move the method parameter arguments in the class variables graph_object and mst_object.
        self.graph_object = graph_object_parameter
        self.mst_object = mst_parameter

        # Kept the official documentation temporary variable names
        pos = nx.spring_layout(self.graph_object)
        nx.draw_networkx_nodes(self.graph_object, pos, node_color="red", node_size=20)
        nx.draw_networkx_edges(self.mst_object, pos, edge_color="blue", width=4)
        plt.axis("off")
        plt.show()
