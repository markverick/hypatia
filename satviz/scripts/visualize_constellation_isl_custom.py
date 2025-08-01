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

# from astropy import units as u
# from poliastro.bodies import Earth
# from poliastro.twobody import Orbit
# from astropy.time import Time
# from extractor import CZMLExtractor
import math
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


# General files needed to generate visualizations; Do not change for different simulations
topFile = "../static_html/top.html"
bottomFile = "../static_html/bottom.html"

# Output directory for creating visualization html files
OUT_DIR = "../viz_output/"
# JSON_NAME  = NAME+"_5shell.json"
# OUT_JSON_FILE = OUT_DIR + JSON_NAME
OUT_HTML_FILE = OUT_DIR + NAME + ".html"

# START = Time(EPOCH, scale="tdb")
# END = START + (10*60) * u.second
# sample_points = 10
# extractor = CZMLExtractor(START, END, sample_points)


def generate_satellite_trajectories():
    """
    Generates and adds satellite orbits to visualization.
    :return: viz_string
    """
    viz_string = ""
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
        # sat_objs = sat_objs[:22 * 36]
        filtered_node = [5, 16, 27, 38, 49, 60, 71, 82, 93, 104, 115, 126, 137, 148, 159, 170, 181, 192, 203, 214, 225, 236, 247, 258, 269, 280, 291, 302, 313, 324, 335, 346, 357, 368, 379, 390, 401, 412, 423, 434, 445, 456, 467, 478, 489, 500, 511, 522, 533, 544, 555, 566, 577, 588, 599, 610, 621, 632, 643, 654, 665, 676, 687, 698, 709, 720, 731, 742, 753, 764, 775, 786, 797, 808, 819, 830, 841, 852, 863, 874, 885, 896, 907, 918, 929, 940, 951, 962, 973, 984, 995, 1006, 1017, 1028, 1039, 1050, 1061, 1072, 1083, 1094, 1105, 1116, 1127, 1138, 1149, 1160, 1171, 1182, 1193, 1204, 1215, 1226, 1237, 1248, 1259, 1270, 1281, 1292, 1303, 1314, 1325, 1336, 1347, 1358, 1369, 1380, 1391, 1402, 1413, 1424, 1435, 1446, 1457, 1468, 1479, 1490, 1501, 1512, 1523, 1534, 1545, 1556, 1567, 1578]
        
        for j in range(len(sat_objs)):
            sat_objs[j]["sat_obj"].compute(EPOCH)
            if j not in filtered_node:
                continue
            viz_string += "var redSphere = viewer.entities.add({name : '', position: Cesium.Cartesian3.fromDegrees(" \
                          + str(math.degrees(sat_objs[j]["sat_obj"].sublong)) + ", " \
                          + str(math.degrees(sat_objs[j]["sat_obj"].sublat)) + ", " + str(
                sat_objs[j]["alt_km"] * 1000) + "), " \
                          + "ellipsoid : {radii : new Cesium.Cartesian3(30000.0, 30000.0, 30000.0), " \
                          + "material : Cesium.Color.BLACK.withAlpha(1),}});\n"
        grid_links = util.find_grid_links(sat_objs, NUM_ORBS[i], NUM_SATS_PER_ORB[i])
        for key in grid_links:
            sat1 = grid_links[key]["sat1"]
            sat2 = grid_links[key]["sat2"]
            if (grid_links[key]["dist"] > 1 and grid_links[key]["dist"] < 21):
                continue
            color = COLOR[0] if grid_links[key]["inter_orbit"] else COLOR[1] 
            viz_string += "viewer.entities.add({name : '', polyline: { positions: Cesium.Cartesian3.fromDegreesArrayHeights([" \
                          + str(math.degrees(sat_objs[sat1]["sat_obj"].sublong)) + "," \
                          + str(math.degrees(sat_objs[sat1]["sat_obj"].sublat)) + "," \
                          + str(sat_objs[sat1]["alt_km"] * 1000) + "," \
                          + str(math.degrees(sat_objs[sat2]["sat_obj"].sublong)) + "," \
                          + str(math.degrees(sat_objs[sat2]["sat_obj"].sublat)) + "," \
                          + str(sat_objs[sat2]["alt_km"] * 1000) + "]), " \
                          + "width: 1, arcType: Cesium.ArcType.NONE, " \
                          + "material: new Cesium.PolylineOutlineMaterialProperty({ " \
                          + "color: Cesium.Color.fromCssColorString(\'"+color+"\').withAlpha(0.3), outlineWidth: 0, outlineColor: Cesium.Color.BLACK})}});"
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