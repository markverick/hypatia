# MIT License
#
# Copyright (c) 2020 Debopam Bhattacherjee
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from astropy import units as u
# from poliastro.bodies import Earth
# from poliastro.twobody import Orbit
from astropy.time import Time
# from extractor import CZMLExtractor
import math
import csv
import matplotlib.pyplot as plt
try:
    from . import util
except (ImportError, SystemError):
    import util

# Generate static visualizations for entire constellation (multiple shells).

EARTH_RADIUS = 6378135.0 # WGS72 value; taken from https://geographiclib.sourceforge.io/html/NET/NETGeographicLib_8h_source.html

# CONSTELLATION GENERATION GENERAL CONSTANTS
ECCENTRICITY = 0.0000001  # Circular orbits are zero, but pyephem does not permit 0, so lowest possible value
ARG_OF_PERIGEE_DEGREE = 0.0
PHASE_DIFF = True
EPOCH = "2000-01-01 00:00:00"

# Shell wise color codes
# COLOR = [[255, 0, 0, 200], [32, 128, 46, 200], [0, 0, 255, 200], [245, 66, 242, 200], [245, 126, 66, 200]]
COLOR = ['CRIMSON', 'FORESTGREEN', 'DODGERBLUE', 'PERU', 'BLUEVIOLET', 'DARKMAGENTA']
COLOR = ['#1f77b4', '#ff7f0e']
# CONSTELLATION SPECIFIC PARAMETERS


# STARLINK
NAME = "Starlink"

SHELL_CNTR = 1

MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
ALTITUDE_M = [None]*SHELL_CNTR
NUM_ORBS = [None]*SHELL_CNTR
NUM_SATS_PER_ORB = [None]*SHELL_CNTR
INCLINATION_DEGREE = [None]*SHELL_CNTR
BASE_ID = [None]*SHELL_CNTR
ORB_WISE_IDS = [None]*SHELL_CNTR

MEAN_MOTION_REV_PER_DAY[0] = 15.19  # Altitude ~550000 km
ALTITUDE_M[0] = 550000  # Altitude ~550000 km
NUM_ORBS[0] = 72
NUM_SATS_PER_ORB[0] = 22
INCLINATION_DEGREE[0] = 53
BASE_ID[0] = 0
ORB_WISE_IDS[0] = []

# MEAN_MOTION_REV_PER_DAY[1] = 13.4  # Altitude ~1110 km
# ALTITUDE_M[1] = 1110000  # Altitude ~1110 km
# NUM_ORBS[1] = 32
# NUM_SATS_PER_ORB[1] = 50
# INCLINATION_DEGREE[1] = 53.8
# BASE_ID[1] = 1584
# ORB_WISE_IDS[1] = []

# MEAN_MOTION_REV_PER_DAY[2] = 13.35  # Altitude ~1130 km
# ALTITUDE_M[2] = 1130000  # Altitude ~1130 km
# NUM_ORBS[2] = 8
# NUM_SATS_PER_ORB[2] = 50
# INCLINATION_DEGREE[2] = 74
# BASE_ID[2] = 3184
# ORB_WISE_IDS[2] = []

# MEAN_MOTION_REV_PER_DAY[3] = 12.97  # Altitude ~1275 km
# ALTITUDE_M[3] = 1275000  # Altitude ~1275 km
# NUM_ORBS[3] = 5
# NUM_SATS_PER_ORB[3] = 75
# INCLINATION_DEGREE[3] = 81
# BASE_ID[3] = 3584
# ORB_WISE_IDS[3] = []

# MEAN_MOTION_REV_PER_DAY[4] = 12.84  # Altitude ~1325 km
# ALTITUDE_M[4] = 1325000  # Altitude ~1325 km
# NUM_ORBS[4] = 6
# NUM_SATS_PER_ORB[4] = 75
# INCLINATION_DEGREE[4] = 70
# BASE_ID[4] = 3959
# ORB_WISE_IDS[4] = []


"""
# TELESAT
NAME = "Telesat"
SHELL_CNTR = 2

MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
ALTITUDE_M = [None]*SHELL_CNTR
NUM_ORBS = [None]*SHELL_CNTR
NUM_SATS_PER_ORB = [None]*SHELL_CNTR
INCLINATION_DEGREE = [None]*SHELL_CNTR
BASE_ID = [None]*SHELL_CNTR
ORB_WISE_IDS = [None]*SHELL_CNTR

MEAN_MOTION_REV_PER_DAY[0] = 13.66  # Altitude ~1015 km
ALTITUDE_M[0] = 1015000  # Altitude ~1015 km
NUM_ORBS[0] = 27
NUM_SATS_PER_ORB[0] = 13
INCLINATION_DEGREE[0] = 98.98
BASE_ID[0] = 0
ORB_WISE_IDS[0] = []

MEAN_MOTION_REV_PER_DAY[1] = 12.84  # Altitude ~1325 km
ALTITUDE_M[1] = 1325000  # Altitude ~1325 km
NUM_ORBS[1] = 40
NUM_SATS_PER_ORB[1] = 33
INCLINATION_DEGREE[1] = 50.88
BASE_ID[1] = 351
ORB_WISE_IDS[1] = []
"""

"""
# KUIPER
NAME = "kuiper"
################################################################
# The below constants are taken from Kuiper's FCC filing as below:
# [1]: https://www.itu.int/ITU-R/space/asreceived/Publication/DisplayPublication/8716
################################################################

SHELL_CNTR = 3

MEAN_MOTION_REV_PER_DAY = [None]*SHELL_CNTR
ALTITUDE_M = [None]*SHELL_CNTR
NUM_ORBS = [None]*SHELL_CNTR
NUM_SATS_PER_ORB = [None]*SHELL_CNTR
INCLINATION_DEGREE = [None]*SHELL_CNTR
BASE_ID = [None]*SHELL_CNTR
ORB_WISE_IDS = [None]*SHELL_CNTR

MEAN_MOTION_REV_PER_DAY[0] = 14.80  # Altitude ~630 km
ALTITUDE_M[0] = 630000  # Altitude ~630 km
NUM_ORBS[0] = 34
NUM_SATS_PER_ORB[0] = 34
INCLINATION_DEGREE[0] = 51.9
BASE_ID[0] = 0
ORB_WISE_IDS[0] = []

MEAN_MOTION_REV_PER_DAY[1] = 14.86  # Altitude ~610 km
ALTITUDE_M[1] = 610000  # Altitude ~610 km
NUM_ORBS[1] = 36
NUM_SATS_PER_ORB[1] = 36
INCLINATION_DEGREE[1] = 42
BASE_ID[1] = 1156
ORB_WISE_IDS[1] = []

MEAN_MOTION_REV_PER_DAY[2] = 14.93  # Altitude ~590 km
ALTITUDE_M[2] = 590000  # Altitude ~590 km
NUM_ORBS[2] = 28
NUM_SATS_PER_ORB[2] = 28
INCLINATION_DEGREE[2] = 33
BASE_ID[2] = 2452
ORB_WISE_IDS[2] = []
"""

def generate_link_mapping(N=72, M=22):
    mapping = {}  # (node1, node2) -> (node1, link_id)

    def node_id(orbit, sat):
        return (orbit % N) * M + (sat % M)

    for orbit in range(N):
        for sat in range(M):
            node = node_id(orbit, sat)
            link_id = 1

            # East (same orbit, sat+1)
            neighbor = node_id(orbit, sat + 1)
            mapping[(node, neighbor)] = (node, link_id)
            link_id += 1

            # South (orbit+1, same sat)
            neighbor = node_id(orbit + 1, sat)
            mapping[(node, neighbor)] = (node, link_id)
            link_id += 1

            # West (same orbit, sat-1)
            neighbor = node_id(orbit, sat - 1)
            mapping[(node, neighbor)] = (node, link_id)
            link_id += 1

            # North (orbit-1, same sat)
            neighbor = node_id(orbit - 1, sat)
            mapping[(node, neighbor)] = (node, link_id)
            link_id += 1

    return mapping
# General files needed to generate visualizations; Do not change for different simulations
topFile = "../static_html/top.html"
bottomFile = "../static_html/bottom.html"

# Output directory for creating visualization html files
OUT_DIR = "../viz_output/"
# JSON_NAME  = NAME+"_5shell.json"
# OUT_JSON_FILE = OUT_DIR + JSON_NAME
OUT_HTML_FILE = OUT_DIR + NAME + ".html"

START = Time(EPOCH, scale="tdb")
END = START + (10*60) * u.second
# sample_points = 10
# extractor = CZMLExtractor(START, END, sample_points)

def read_per_node_summary(file_path="per_node_summary.csv"):
    node_dict = {}
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            node_id = int(row['node_id'])
            node_dict[node_id] = {
                'packet_count': int(row['packet_count']),
                'traffic_size_mb': float(row['traffic_size_mb']),
                'orbit': int(row['orbit']),
                'sat_id': int(row['sat_id'])
            }
    return node_dict

def read_per_link_summary(file_path="per_link_summary.csv"):
    link_dict = {}
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sat_id = int(row['link_id'].split('-')[0])
            link_id = int(row['link_id'].split('-')[1])
            link_dict[(sat_id, link_id)] = {
                'packet_count': int(row['packet_count']),
                'traffic_size_mb': float(row['traffic_size_mb']),
            }
    return link_dict

def traffic_to_hex_color(traffic_values):
    min_traffic = min(traffic_values.values())
    max_traffic = max(traffic_values.values())
    color_map = {}
    cmap = plt.get_cmap('viridis')
    for node_id, traffic in traffic_values.items():
        # Normalize traffic value to 0–1
        norm = (traffic - min_traffic) / (max_traffic - min_traffic) if max_traffic > min_traffic else 0.5
        rgba = cmap(norm)
        # Convert RGBA (0–1 floats) to hex string
        r, g, b, _ = [int(255 * x) for x in rgba]
        color_map[node_id] = f'#{r:02x}{g:02x}{b:02x}'
    print(f"Per-node ranges: {min_traffic} - {max_traffic}")
    return color_map

def traffic_to_hex_color_link(traffic_values):
    min_traffic = min(traffic_values.values())
    max_traffic = max(traffic_values.values())
    color_map = {}

    # Use a different colormap than viridis (e.g., 'plasma')
    cmap = plt.get_cmap('plasma')

    for link_id, traffic in traffic_values.items():
        # Normalize traffic value to 0–1
        norm = (traffic - min_traffic) / (max_traffic - min_traffic) if max_traffic > min_traffic else 0.5
        rgba = cmap(norm)
        # Convert RGBA (0–1 floats) to hex string
        r, g, b, _ = [int(255 * x) for x in rgba]
        color_map[link_id] = f'#{r:02x}{g:02x}{b:02x}'
        # print(traffic, f'#{r:02x}{g:02x}{b:02x}')
    print(f"Per-link ranges: {min_traffic} - {max_traffic}")
    return color_map

def generate_satellite_trajectories():
    """
    Generates and adds satellite orbits to visualization.
    :return: viz_string
    """
    viz_string = ""

    # print(colors_links)
    for i in range(0, SHELL_CNTR):
        sat_objs = util.generate_sat_obj_list(
            NUM_ORBS[i],
            NUM_SATS_PER_ORB[i],
            EPOCH,
            PHASE_DIFF,
            INCLINATION_DEGREE[i],
            ECCENTRICITY,
            ARG_OF_PERIGEE_DEGREE,
            MEAN_MOTION_REV_PER_DAY[i],
            ALTITUDE_M[i]
        )
        # colors[node_summary[key]['traffic_size_mb']]
        sat_objs = sat_objs[:22 * 12]
        node_summary = read_per_node_summary()
        link_summary = read_per_link_summary()
        traffic_values = {node_id: data['traffic_size_mb'] for node_id, data in node_summary.items()}
        traffic_values_link = {link_id: data['traffic_size_mb'] for link_id, data in link_summary.items()}
        colors = traffic_to_hex_color(traffic_values)
        colors_links = traffic_to_hex_color_link(traffic_values_link)

        for j in range(len(sat_objs)):
            sat_objs[j]["sat_obj"].compute(EPOCH)
            viz_string += "var redSphere = viewer.entities.add({name : '', position: Cesium.Cartesian3.fromDegrees(" \
                          + str(math.degrees(sat_objs[j]["sat_obj"].sublong)) + ", " \
                          + str(math.degrees(sat_objs[j]["sat_obj"].sublat)) + ", " + str(
                sat_objs[j]["alt_km"] * 1000) + "), " \
                          + "ellipsoid : {radii : new Cesium.Cartesian3(30000.0, 30000.0, 30000.0), " \
                          + "material : Cesium.Color.fromCssColorString(\'"+colors[j]+"\'),}});\n"
        grid_links = util.find_grid_links(sat_objs, NUM_ORBS[i], NUM_SATS_PER_ORB[i])
        link_mapping = generate_link_mapping()
        for key in grid_links:
            sat1 = grid_links[key]["sat1"]
            sat2 = grid_links[key]["sat2"]
            if (sat2 < 0):
                continue
            if (grid_links[key]["dist"] > 1 and grid_links[key]["dist"] < 21):
                continue
            color = COLOR[0] if grid_links[key]["inter_orbit"] else COLOR[1]
            link_id = link_mapping[(sat1, sat2)]
            # print(link_id
            viz_string += "viewer.entities.add({name : '', polyline: { positions: Cesium.Cartesian3.fromDegreesArrayHeights([" \
                          + str(math.degrees(sat_objs[sat1]["sat_obj"].sublong)) + "," \
                          + str(math.degrees(sat_objs[sat1]["sat_obj"].sublat)) + "," \
                          + str(sat_objs[sat1]["alt_km"] * 1000) + "," \
                          + str(math.degrees(sat_objs[sat2]["sat_obj"].sublong)) + "," \
                          + str(math.degrees(sat_objs[sat2]["sat_obj"].sublat)) + "," \
                          + str(sat_objs[sat2]["alt_km"] * 1000) + "]), " \
                          + "width: 1, arcType: Cesium.ArcType.NONE, " \
                          + "material: new Cesium.PolylineOutlineMaterialProperty({ " \
                          + "color: Cesium.Color.fromCssColorString(\'"+colors_links[link_id]+"\').withAlpha(1), outlineWidth: 0, outlineColor: Cesium.Color.BLACK})}});"
    return viz_string


def write_viz_files():
    """
    Writes JSON and TML files to the output folder
    :return: None
    """
    with open("cesium-token", "r") as f:
        token = f.read().strip()
    writer_html = open(OUT_HTML_FILE, 'w')
    with open(topFile, 'r') as fi:
        original = fi.read()
        writer_html.write(original.replace("<CESIUM_ACCESS_TOKEN>", token))
    writer_html.write(viz_string)
    with open(bottomFile, 'r') as fb:
        writer_html.write(fb.read())
    writer_html.close()


viz_string = generate_satellite_trajectories()
write_viz_files()