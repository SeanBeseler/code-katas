import json
import math
from graph_paths import Graph
with open('path.json') as path_file:
    path = json.load(path_file)
#json file can be found at https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-using-python


def calculate_distance(point1, point2):  #pragma no cover
    """
    Calculates the distance from point1 to point2. Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """
    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])
    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934


def get_path(c1, c2, path=path):
    """gets the shortest path between two cities"""
    chart = Graph()
    location = {}
    for city in path:
        try:
            location[city['city']]
        except KeyError:
            location[city['city']] = city['lat_lon']
    for city in path:
        for dest in city['destination_cities']:
            try:
                chart.add_edge(city['city'], dest, calculate_distance(city['lat_lon'], location[dest]))
            except KeyError:
                pass
    return chart.bellman_ford(c1, c2)
