"""
Program: minimum_spanning_trees_client.py
Author: Taynor McNally
Date: 23/04/2023
Synopsis:
The client implementation of the minimum_spanning_tree.py application.
Libraries:
Colorama
Modules:
HashFunction
Points
MinimumSpanningTree
"""

# Import the minimum_spanning_tree modules
from minimum_spanning_tree import HashFunction
from minimum_spanning_tree import Points
from minimum_spanning_tree import MinimumSpanningTree

# Import colorama to enhance the client output
from colorama import Fore

# y_points for the MST and points calculations
y_points = [20, 93, 72, 35, 54, 95, 25, 37, 29, 72, 65, 66, 49, 43, 35, 61, 97, 66, 64, 22, 83, 69, 19, 21, 69, 40, 35,
            81, 15, 41, 74, 12, 3, 65, 31, 12, 48, 68, 41, 40, 99, 13, 70, 30, 20, 35, 84, 96, 1, 93, 61, 83, 24, 27,
            93, 86, 96, 43, 10, 51, 27, 87, 40, 35, 83, 44, 15, 89, 71, 79, 25, 84, 43, 49, 66, 0, 88, 80, 4, 3, 74, 10,
            41, 45, 75, 34, 41, 44, 50, 99, 41, 37, 26, 6, 94, 94, 76, 48, 32, 42]

# x_points for the MST and points calculations
x_points = [20, 20, 93, 93, 72, 72, 35, 35, 54, 54, 95, 95, 25, 25, 37, 37, 29, 29, 72, 72, 65, 65, 66, 66, 49,
            43, 43, 35, 35, 61, 61, 97, 97, 66, 66, 64, 64, 22, 22, 83, 83, 69, 69, 19, 19, 21, 21, 69, 69, 40, 40,
            35, 35, 81, 81, 15, 15, 41, 41, 74, 74, 12, 12, 3, 3, 65, 65, 31, 31, 12, 12, 48, 48, 68, 68, 41, 41,
            40, 99, 99, 13, 13, 70, 70, 30, 30, 20, 20, 35, 35, 84, 84, 96, 96, 1, 1, 93, 93, 61, 61]


# Create the HashFunction class instance.
def instantiate_hash_object():
    """Instantiate the HashFunction class and set global variables"""
    global hash_function_object
    global string_of_list
    global value_of_hash

    hash_function_object = HashFunction()
    string_of_list = hash_function_object.converted_list_to_string
    value_of_hash = hash_function_object.hash_value

    return hash_function_object, string_of_list, value_of_hash


# Convert a Points List object to a string
def convert_list_to_string(client_list_object):
    """Convert the Points List data structure to a string object"""

    hash_function_object.convert_list_to_string(client_list_object)
    print(Fore.RESET + 'The converted Y Points List to a String object:')
    print(Fore.GREEN + f'{hash_function_object.converted_list_to_string}')

    return string_of_list


# Create a 256 SHA hash checksum of the converted Points List object
def hash_the_string(string_to_hash):
    """Create a 256 SHA has checksum from a string object"""

    hash_function_object.hash_the_string(string_to_hash)
    print(Fore.RESET + 'The 256 SHA Hash checksum value:')
    print(Fore.GREEN + f'{hash_function_object.hash_value}')

    return value_of_hash


# Execute the HashFunction client functions
instantiate_hash_object()
convert_list_to_string(y_points)
hash_the_string(string_of_list)


# Create the Points class instance
def instantiate_points_object():
    """Instantiate the Points class"""

    global points_object

    points_object = Points()

    return points_object


# Create the coordinates object from the inputting the X and Y Points List data structures
def create_coordinates(y_coordinates, x_coordinates):
    """Create X and Y coordinates and convert to Dictionary Data Structure"""
    global calculated_coordinates

    points_object.zip_coordinates(y_coordinates, x_coordinates)
    calculated_coordinates = points_object.coordinates

    return calculated_coordinates


# Calculate the distances using a 0 < cd <= 20 calculation filter
def calculate_coordinates_distance():
    """Calculate the distances between the Points coordinates X and Y"""

    global calculated_distance

    calculated_distance = points_object.calculate_distance(calculated_coordinates)
    for cd in calculated_distance:
        if 0 < cd <= 20:
            print(Fore.RESET + 'Point X and Point Y distances are between 0 and 20:')
            print(Fore.GREEN + f'{points_object.list_of_distances}')


# Execute the Points client functions
instantiate_points_object()
create_coordinates(y_points, x_points)
calculate_coordinates_distance()


# Create the MinimumSpanningTree instance
def instantiate_minimum_search_tree_object():
    """Instantiate the MinimumSpanningTree class"""

    global minimum_spanning_tree_object

    minimum_spanning_tree_object = MinimumSpanningTree()

    return minimum_spanning_tree_object


# Create the Minimum Spanning Tree and graph objects
def create_minimum_spanning_tree():
    """Create the Minimum Spanning Tree objects"""

    global mst_graph_object
    global mst_return_object

    minimum_spanning_tree_object.create_minimum_spanning_tree()

    mst_calculated = minimum_spanning_tree_object.build_minimum_spanning_tree(calculated_coordinates)

    mst_graph_object = minimum_spanning_tree_object.graph_object
    mst_return_object = minimum_spanning_tree_object.print_minimum_spanning_tree(mst_graph_object)
    print(Fore.RESET + 'The Minimum Spanning Tree object:')
    print(Fore.GREEN + f'{minimum_spanning_tree_object.graph_object}')

    return mst_calculated, mst_graph_object, mst_return_object


# Create the Minimum Spanning Tree visualisation uses the networkx library
def create_minimum_spanning_tree_visual():
    """Create the Minimum Spanning Tree visualisation"""

    minimum_spanning_tree_object.create_minimum_spanning_tree_visual(mst_graph_object, mst_return_object)


# Execute the MinimumSpanningTree client
instantiate_minimum_search_tree_object()
create_minimum_spanning_tree()
create_minimum_spanning_tree_visual()
