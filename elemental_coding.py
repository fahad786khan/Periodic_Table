import pygame
import sys
import math



#Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 1200, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Periodic Combinator - Periodic Table")

#Define colors
BACKGROUND = (44, 44,47)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 100)
ELEMENT_FONT_COLOR = (82, 87, 93)


#Pastel colors for elements groups
ALKALI_METALS = (255, 204 ,204)
ALKALINE_EARTH_METALS = (255, 229, 204)
TRANSITION_METALS = (255, 255, 204)
POST_TRANSITION_METALS = (229, 255, 204)
METALLOIDS = (204, 255, 204)
NONMETALS = (204, 255, 229)
HALOGENS = (204, 229, 255)
NOBEL_GASES = (229, 204, 255)
LANTHANIDES = (255, 204, 229)
ACTINIDES = (255, 229, 204)


#SET UP FONTS
#Default font for general text , size 29
font = pygame.font.Font(None, 29)
# Larger font for headings or emphasized tezt
large_font = pygame.font.Font(None, 36)
#Bold font for emphasis, size 33
bold_font = pygame.font.Font(None, 33)
bold_font.set_bold(True) #Set this font to  bold

element_font = pygame.font.Font\
    ("C:/Users/Micro/Desktop/Periodic_Table/JetBrainsMonoNerdFontPropo-Medium.ttf", 28)

#Font for popups, Size 46
popup_font = pygame.font.Font(None, 46)

#Element cell size
CELL_SIZE = 53 #Size of each element cell in pixels
GRID_PADDING = 4 #Paddinf between cells in pixels
TABLE_OFFSET_X = 80 #Horizontal offset for the entire periodic table

# Define elements 
ELEMENTS = {
    'H' : {'name' : 'Hydrogen' , 'color' : NONMETALS,'atomic_number' : 1, 'mass' : 1.008,'electron_config' : '1s1' , 'shells' : [1]},
    'He' : {'name' : 'Helium', 'color' : NOBEL_GASES,'atomic_number' : 2, 'mass' : 4.003,'electron_config': '1s2', 'shells' : [2]},
    'Li': {'name': 'Lithium', 'color': ALKALI_METALS, 'atomic_number': 3, 'mass': 6.94, 'electron_config': '1s2 2s1', 'shells': [2]},
    'Be': {'name': 'Beryllium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 4, 'mass': 9.0122, 'electron_config': '1s2 2s2', 'shells': [2]},
    'B': {'name': 'Boron', 'color': METALLOIDS, 'atomic_number': 5, 'mass': 10.81, 'electron_config': '1s2 2s2 2p1', 'shells': [2]},
    'C': {'name': 'Carbon', 'color': NONMETALS, 'atomic_number': 6, 'mass': 12.011, 'electron_config': '1s2 2s2 2p2', 'shells': [2]},
    'N': {'name': 'Nitrogen', 'color': NONMETALS, 'atomic_number': 7, 'mass': 14.007, 'electron_config': '1s2 2s2 2p3', 'shells': [2]},
    'O': {'name': 'Oxygen', 'color': NONMETALS, 'atomic_number': 8, 'mass': 15.999, 'electron_config': '1s2 2s2 2p4', 'shells': [2]},
    'F': {'name': 'Fluorine', 'color': HALOGENS, 'atomic_number': 9, 'mass': 18.998, 'electron_config': '1s2 2s2 2p5', 'shells': [2]},
    'Ne': {'name': 'Neon', 'color': NOBEL_GASES, 'atomic_number': 10, 'mass': 20.180, 'electron_config': '1s2 2s2 2p6', 'shells': [2]},
    'Na': {'name': 'Sodium', 'color': ALKALI_METALS, 'atomic_number': 11, 'mass': 22.990, 'electron_config': '1s2 2s2 2p6 3s1', 'shells': [3]},
    'Mg': {'name': 'Magnesium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 12, 'mass': 24.305, 'electron_config': '1s2 2s2 2p6 3s2', 'shells': [3]},
    'Al': {'name': 'Aluminium', 'color': POST_TRANSITION_METALS, 'atomic_number': 13, 'mass': 26.982, 'electron_config': '1s2 2s2 2p6 3s2 3p1', 'shells': [3]},
    'Si': {'name': 'Silicon', 'color': METALLOIDS, 'atomic_number': 14, 'mass': 28.085, 'electron_config': '1s2 2s2 2p6 3s2 3p2', 'shells': [3]},
    'P': {'name': 'Phosphorus', 'color': NONMETALS, 'atomic_number': 15, 'mass': 30.974, 'electron_config': '1s2 2s2 2p6 3s2 3p3', 'shells': [3]},
    'S': {'name': 'Sulfur', 'color': NONMETALS, 'atomic_number': 16, 'mass': 32.06, 'electron_config': '1s2 2s2 2p6 3s2 3p4', 'shells': [3]},
    'Cl': {'name': 'Chlorine', 'color': HALOGENS, 'atomic_number': 17, 'mass': 35.45, 'electron_config': '1s2 2s2 2p6 3s2 3p5', 'shells': [3]},
    'Ar': {'name': 'Argon', 'color': NOBEL_GASES, 'atomic_number': 18, 'mass': 39.948, 'electron_config': '1s2 2s2 2p6 3s2 3p6', 'shells': [3]},
    'K': {'name': 'Potassium', 'color': ALKALI_METALS, 'atomic_number': 19, 'mass': 39.098, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s1', 'shells': [4]},
    'Ca': {'name': 'Calcium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 20, 'mass': 40.078, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2', 'shells': [4]},
    'Sc': {'name': 'Scandium', 'color': TRANSITION_METALS, 'atomic_number': 21, 'mass': 44.956, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d1 4s2', 'shells': [4]},
    'Ti': {'name': 'Titanium', 'color': TRANSITION_METALS, 'atomic_number': 22, 'mass': 47.867, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d2 4s2', 'shells': [4]},
    'V': {'name': 'Vanadium', 'color': TRANSITION_METALS, 'atomic_number': 23, 'mass': 50.942, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d3 4s2', 'shells': [4]},
    'Cr': {'name': 'Chromium', 'color': TRANSITION_METALS, 'atomic_number': 24, 'mass': 51.941, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d5 4s1', 'shells': [4]},
    'Mn': {'name': 'Manganese', 'color': TRANSITION_METALS, 'atomic_number': 25, 'mass': 54.938, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d5 4s2', 'shells': [4]},
    'Fe': {'name': 'Iron', 'color': TRANSITION_METALS, 'atomic_number': 26, 'mass': 55.845, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d6 4s2', 'shells': [4]},
    'Co': {'name': 'Cobalt', 'color': TRANSITION_METALS, 'atomic_number': 27, 'mass': 58.933, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d7 4s2', 'shells': [4]},
    'Ni': {'name': 'Nickel', 'color': TRANSITION_METALS, 'atomic_number': 28, 'mass': 58.693, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d8 4s2', 'shells': [4]},
    'Cu': {'name': 'Copper', 'color': TRANSITION_METALS, 'atomic_number': 29, 'mass': 63.546, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s1', 'shells': [4]},
    'Zn': {'name': 'Zinc', 'color': TRANSITION_METALS, 'atomic_number': 30, 'mass': 65.38, 'electron_config': '1s2 2s2 2p6 3s2 3p6 3d10 4s2', 'shells': [4]},
    'Ga': {'name': 'Gallium', 'color': POST_TRANSITION_METALS, 'atomic_number': 31, 'mass': 69.723, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p1', 'shells': [4]},
    'Ge': {'name': 'Germanium', 'color': METALLOIDS, 'atomic_number': 32, 'mass': 72.63, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p2', 'shells': [4]},
    'As': {'name': 'Arsenic', 'color': METALLOIDS, 'atomic_number': 33, 'mass': 74.922, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p3', 'shells': [4]},
    'Se': {'name': 'Selenium', 'color': NONMETALS, 'atomic_number': 34, 'mass': 78.971, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p4', 'shells': [4]},
    'Br': {'name': 'Bromine', 'color': HALOGENS, 'atomic_number': 35, 'mass': 79.904, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p5', 'shells': [4]},
    'Kr': {'name': 'Krypton', 'color': NOBEL_GASES, 'atomic_number': 36, 'mass': 83.798, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6', 'shells': [4]},
    'Rb': {'name': 'Rubidium', 'color': ALKALI_METALS, 'atomic_number': 37, 'mass': 85.468, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s1', 'shells': [5]},
    'Sr': {'name': 'Strontium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 38, 'mass': 87.62, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2', 'shells': [5]},
    'Y': {'name': 'Yttrium', 'color': TRANSITION_METALS, 'atomic_number': 39, 'mass': 88.906, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2', 'shells': [5]},
    'Zr': {'name': 'Zirconium', 'color': TRANSITION_METALS, 'atomic_number': 40, 'mass': 91.224, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d2', 'shells': [5]},
    'Nb': {'name': 'Niobium', 'color': TRANSITION_METALS, 'atomic_number': 41, 'mass': 92.906, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d4', 'shells': [5]},
    'Mo': {'name': 'Molybdenum', 'color': TRANSITION_METALS, 'atomic_number': 42, 'mass': 95.95, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d5', 'shells': [5]},
    'Tc': {'name': 'Technetium', 'color': TRANSITION_METALS, 'atomic_number': 43, 'mass': 98, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d7', 'shells': [5]},
    'Ru': {'name': 'Ruthenium', 'color': TRANSITION_METALS, 'atomic_number': 44, 'mass': 101.07, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d7', 'shells': [5]},
    'Rh': {'name': 'Rhodium', 'color': TRANSITION_METALS, 'atomic_number': 45, 'mass': 102.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d8', 'shells': [5]},
    'Pd': {'name': 'Palladium', 'color': TRANSITION_METALS, 'atomic_number': 46, 'mass': 106.42, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10', 'shells': [5]},
    'Ag': {'name': 'Silver', 'color': TRANSITION_METALS, 'atomic_number': 47, 'mass': 107.87, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10', 'shells': [5]},
    'Cd': {'name': 'Cadmium', 'color': TRANSITION_METALS, 'atomic_number': 48, 'mass': 112.41, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10', 'shells': [5]},
    'In': {'name': 'Indium', 'color': POST_TRANSITION_METALS, 'atomic_number': 49, 'mass': 114.82, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10 5p1', 'shells': [5]},
    'Sn': {'name': 'Tin', 'color': POST_TRANSITION_METALS, 'atomic_number': 50, 'mass': 118.71, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10 5p2', 'shells': [5]},
    'Sb': {'name': 'Antimony', 'color': METALLOIDS, 'atomic_number': 51, 'mass': 121.76, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10 5p3', 'shells': [5]},
    'Te': {'name': 'Tellurium', 'color': METALLOIDS, 'atomic_number': 52, 'mass': 127.60, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10 5p4', 'shells': [5]},
    'I': {'name': 'Iodine', 'color': HALOGENS, 'atomic_number': 53, 'mass': 126.90, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10 5p5', 'shells': [5]},
    'Xe': {'name': 'Xenon', 'color': NOBEL_GASES, 'atomic_number': 54, 'mass': 131.29, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10 5p6', 'shells': [5]},
    'Cs': {'name': 'Cesium', 'color': ALKALI_METALS, 'atomic_number': 55, 'mass': 132.91, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10 6s1', 'shells': [6]},
    'Ba': {'name': 'Barium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 56, 'mass': 137.33, 'electron_config': '1s2 2s2 2p6 3s2 3p6 4s2 4p6 5s2 5d10 6s2', 'shells': [6]},
    'La': {'name': 'Lanthanum', 'color': LANTHANIDES, 'atomic_number': 57, 'mass': 138.91, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1', 'shells': [6]},
    'Ce': {'name': 'Cerium', 'color': LANTHANIDES, 'atomic_number': 58, 'mass': 140.12, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Pr': {'name': 'Praseodymium', 'color': LANTHANIDES, 'atomic_number': 59, 'mass': 140.91, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Nd': {'name': 'Neodymium', 'color': LANTHANIDES, 'atomic_number': 60, 'mass': 144.24, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Pm': {'name': 'Promethium', 'color': LANTHANIDES, 'atomic_number': 61, 'mass': 145, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Sm': {'name': 'Samarium', 'color': LANTHANIDES, 'atomic_number': 62, 'mass': 150.36, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Eu': {'name': 'Europium', 'color': LANTHANIDES, 'atomic_number': 63, 'mass': 151.96, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Gd': {'name': 'Gadolinium', 'color': LANTHANIDES, 'atomic_number': 64, 'mass': 157.25, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Tb': {'name': 'Terbium', 'color': LANTHANIDES, 'atomic_number': 65, 'mass': 158.93, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Dy': {'name': 'Dysprosium', 'color': LANTHANIDES, 'atomic_number': 66, 'mass': 162.50, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Ho': {'name': 'Holmium', 'color': LANTHANIDES, 'atomic_number': 67, 'mass': 164.93, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Er': {'name': 'Erbium', 'color': LANTHANIDES, 'atomic_number': 68, 'mass': 167.26, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Tm': {'name': 'Thulium', 'color': LANTHANIDES, 'atomic_number': 69, 'mass': 168.93, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Yb': {'name': 'Ytterbium', 'color': LANTHANIDES, 'atomic_number': 70, 'mass': 173.04, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Lu': {'name': 'Lutetium', 'color': LANTHANIDES, 'atomic_number': 71, 'mass': 174.97, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d1 6s2', 'shells': [6]},
    'Hf': {'name': 'Hafnium', 'color': TRANSITION_METALS, 'atomic_number': 72, 'mass': 178.49, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d2 6s2', 'shells': [6]},
    'Ta': {'name': 'Tantalum', 'color': TRANSITION_METALS, 'atomic_number': 73, 'mass': 180.95, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d3 6s2', 'shells': [6]},
    'W': {'name': 'Tungsten', 'color': TRANSITION_METALS, 'atomic_number': 74, 'mass': 183.84, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d4 6s2', 'shells': [6]},
    'Re': {'name': 'Rhenium', 'color': TRANSITION_METALS, 'atomic_number': 75, 'mass': 186.21, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d5 6s2', 'shells': [6]},
    'Os': {'name': 'Osmium', 'color': TRANSITION_METALS, 'atomic_number': 76, 'mass': 190.23, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d6 6s2', 'shells': [6]},
    'Ir': {'name': 'Iridium', 'color': TRANSITION_METALS, 'atomic_number': 77, 'mass': 192.22, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d7 6s2', 'shells': [6]},
    'Pt': {'name': 'Platinum', 'color': TRANSITION_METALS, 'atomic_number': 78, 'mass': 195.08, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d8 6s2', 'shells': [6]},
    'Au': {'name': 'Gold', 'color': TRANSITION_METALS, 'atomic_number': 79, 'mass': 196.97, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s1', 'shells': [6]},
    'Hg': {'name': 'Mercury', 'color': TRANSITION_METALS, 'atomic_number': 80, 'mass': 200.59, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2', 'shells': [6]},
    'Tl': {'name': 'Thallium', 'color': POST_TRANSITION_METALS, 'atomic_number': 81, 'mass': 204.38, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p1', 'shells': [6]},
    'Pb': {'name': 'Lead', 'color': POST_TRANSITION_METALS, 'atomic_number': 82, 'mass': 207.2, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p2', 'shells': [6]},
    'Bi': {'name': 'Bismuth', 'color': POST_TRANSITION_METALS, 'atomic_number': 83, 'mass': 208.98, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p3', 'shells': [6]},
    'Po': {'name': 'Polonium', 'color': METALLOIDS, 'atomic_number': 84, 'mass': 209, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p4', 'shells': [6]},
    'At': {'name': 'Astatine', 'color': HALOGENS, 'atomic_number': 85, 'mass': 210, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p5', 'shells': [6]},
    'Rn': {'name': 'Radon', 'color': NOBEL_GASES, 'atomic_number': 86, 'mass': 222, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6', 'shells': [6]},
    'Fr': {'name': 'Francium', 'color': ALKALI_METALS, 'atomic_number': 87, 'mass': 223, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s1', 'shells': [7]},
    'Ra': {'name': 'Radium', 'color': ALKALINE_EARTH_METALS, 'atomic_number': 88, 'mass': 226, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2', 'shells': [7]},
    'Ac': {'name': 'Actinium', 'color': ACTINIDES, 'atomic_number': 89, 'mass': 227, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2', 'shells': [7]},
    'Th': {'name': 'Thorium', 'color': ACTINIDES, 'atomic_number': 90, 'mass': 232.04, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p1', 'shells': [7]},
    'Pa': {'name': 'Protactinium', 'color': ACTINIDES, 'atomic_number': 91, 'mass': 231.04, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p2', 'shells': [7]},
    'U': {'name': 'Uranium', 'color': ACTINIDES, 'atomic_number': 92, 'mass': 238.03, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p3', 'shells': [7]},
    'Np': {'name': 'Neptunium', 'color': ACTINIDES, 'atomic_number': 93, 'mass': 237.05, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p4', 'shells': [7]},
    'Pu': {'name': 'Plutonium', 'color': ACTINIDES, 'atomic_number': 94, 'mass': 244, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p5', 'shells': [7]},
    'Am': {'name': 'Americium', 'color': ACTINIDES, 'atomic_number': 95, 'mass': 243, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p6', 'shells': [7]},
    'Cm': {'name': 'Curium', 'color': ACTINIDES, 'atomic_number': 96, 'mass': 247, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p7', 'shells': [7]},
    'Bk': {'name': 'Berkelium', 'color': ACTINIDES, 'atomic_number': 97, 'mass': 247, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p8', 'shells': [7]},
    'Cf': {'name': 'Californium', 'color': ACTINIDES, 'atomic_number': 98, 'mass': 251, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p9', 'shells': [7]},
    'Es': {'name': 'Einsteinium', 'color': ACTINIDES, 'atomic_number': 99, 'mass': 252, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p10', 'shells': [7]},
    'Fm': {'name': 'Fermium', 'color': ACTINIDES, 'atomic_number': 100, 'mass': 257, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p11', 'shells': [7]},
    'Md': {'name': 'Mendelevium', 'color': ACTINIDES, 'atomic_number': 101, 'mass': 258, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p12', 'shells': [7]},
    'No': {'name': 'Nobelium', 'color': ACTINIDES, 'atomic_number': 102, 'mass': 259, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p13', 'shells': [7]},
    'Lr': {'name': 'Lawrencium', 'color': ACTINIDES, 'atomic_number': 103, 'mass': 262, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Rf': {'name': 'Rutherfordium', 'color': TRANSITION_METALS, 'atomic_number': 104, 'mass': 267, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Db': {'name': 'Dubnium', 'color': TRANSITION_METALS, 'atomic_number': 105, 'mass': 270, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Sg': {'name': 'Seaborgium', 'color': TRANSITION_METALS, 'atomic_number': 106, 'mass': 271, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Bh': {'name': 'Bohrium', 'color': TRANSITION_METALS, 'atomic_number': 107, 'mass': 270, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Hs': {'name': 'Hassium', 'color': TRANSITION_METALS, 'atomic_number': 108, 'mass': 277, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Mt': {'name': 'Meitnerium', 'color': TRANSITION_METALS, 'atomic_number': 109, 'mass': 278, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Ds': {'name': 'Darmstadtium', 'color': TRANSITION_METALS, 'atomic_number': 110, 'mass': 281, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Rg': {'name': 'Roentgenium', 'color': TRANSITION_METALS, 'atomic_number': 111, 'mass': 282, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Cn': {'name': 'Copernicium', 'color': TRANSITION_METALS, 'atomic_number': 112, 'mass': 285, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p14', 'shells': [7]},
    'Nh': {'name': 'Nihonium', 'color': POST_TRANSITION_METALS, 'atomic_number': 113, 'mass': 286, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p15', 'shells': [7]},
    'Fl': {'name': 'Flerovium', 'color': POST_TRANSITION_METALS, 'atomic_number': 114, 'mass': 289, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p16', 'shells': [7]},
    'Mc': {'name': 'Moscovium', 'color': POST_TRANSITION_METALS, 'atomic_number': 115, 'mass': 288, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p17', 'shells': [7]},
    'Lv': {'name': 'Livermorium', 'color': POST_TRANSITION_METALS, 'atomic_number': 116, 'mass': 293, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p18', 'shells': [7]},
    'Ts': {'name': 'Tennessine', 'color': HALOGENS, 'atomic_number': 117, 'mass': 294, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p19', 'shells': [7]},
    'Og': {'name': 'Oganesson', 'color': NOBEL_GASES, 'atomic_number': 118, 'mass': 294, 'electron_config': '1s2 2s2 2p6 3s2 3s2 3p6 4s2 4p6 5s2 5d10 6s2 6p6 7s2 7p20', 'shells': [7]},
}

            #Continue with the rest of elements

#Define compounds
COMPOUNDS = {
    'H2O': {'elements': ['H', 'H', 'O'], 'name': 'Water', 'uses': 'Essential for life, solvent', 'properties': 'Colorless, odorless liquid'},
    'CO2': {'elements': ['C', 'O', 'O'], 'name': 'Carbon Dioxide', 'uses': 'Carbonated drinks, plant photosynthesis', 'properties': 'Colorless gas, soluble in water'},
    'NaCl': {'elements': ['Na', 'Cl'], 'name': 'Sodium Chloride', 'uses': 'Table salt, food preservation', 'properties': 'White crystalline solid, soluble in water'},
    'NH3': {'elements': ['N', 'H', 'H', 'H'], 'name': 'Ammonia', 'uses': 'Fertilizers, cleaning products', 'properties': 'Colorless gas, pungent odor'},
    'C6H12O6': {'elements': ['C', 'C', 'C', 'C', 'C', 'C', 'O', 'O', 'O', 'O', 'O', 'O'], 'name': 'Glucose', 'uses': 'Energy source in cells', 'properties': 'White crystalline solid, soluble in water'},
    'C2H5OH': {'elements': ['C', 'C', 'O', 'H', 'H', 'H', 'H', 'H'], 'name': 'Ethanol', 'uses': 'Alcoholic beverages, antiseptic', 'properties': 'Colorless liquid, flammable'},
    'C8H18': {'elements': ['C'] * 8 + ['H'] * 18, 'name': 'Octane', 'uses': 'Fuel, gasoline', 'properties': 'Colorless liquid, flammable'},
    'C6H5COOH': {'elements': ['C', 'C', 'C', 'C', 'C', 'C', 'O', 'O', 'H'], 'name': 'Benzoic Acid', 'uses': 'Preservative, antifungal', 'properties': 'White crystalline solid, slightly soluble in water'},
    'C5H5N': {'elements': ['C', 'C', 'C', 'C', 'C', 'N', 'H', 'H', 'H', 'H', 'H'], 'name': 'Pyridine', 'uses': 'Solvent, chemical synthesis', 'properties': 'Colorless liquid, has a distinctive odor'},
    'SiO2': {'elements': ['Si', 'O', 'O'], 'name': 'Silicon Dioxide', 'uses': 'Glass, ceramics', 'properties': 'Colorless solid, insoluble in water'},
    'KNO3': {'elements': ['K', 'N', 'O', 'O', 'O'], 'name': 'Potassium Nitrate', 'uses': 'Fertilizer, food preservation', 'properties': 'White crystalline solid, soluble in water'},
    'LiOH': {'elements': ['Li', 'O', 'H'], 'name': 'Lithium Hydroxide', 'uses': 'Batteries, CO2 scrubbers', 'properties': 'White solid, hygroscopic'},
    'C4H8': {'elements': ['C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H'], 'name': 'Butene', 'uses': 'Fuel, chemical synthesis', 'properties': 'Colorless gas, flammable'},
    'C3H4': {'elements': ['C', 'C', 'C', 'H', 'H', 'H', 'H'], 'name': 'Propylene', 'uses': 'Plastic manufacturing', 'properties': 'Colorless gas, flammable'},
    'H2C2O4': {'elements': ['H', 'H', 'C', 'C', 'O', 'O', 'O', 'O'], 'name': 'Oxalic Acid', 'uses': 'Cleaning agents, rust removal', 'properties': 'Colorless solid, soluble in water'},
    'C12H26': {'elements': ['C'] * 12 + ['H'] * 26, 'name': 'Dodecane', 'uses': 'Solvent, fuel', 'properties': 'Colorless liquid, flammable'},
    'FeCl3': {'elements': ['Fe', 'Cl', 'Cl', 'Cl'], 'name': 'Iron(III) Chloride', 'uses': 'Water treatment, etching agent', 'properties': 'Brown solid, soluble in water'},
    'C8H10': {'elements': ['C'] * 8 + ['H'] * 10, 'name': 'Styrene', 'uses': 'Plastic manufacturing, insulation', 'properties': 'Colorless liquid, flammable'},
    'C2H4Cl2': {'elements': ['C', 'C', 'H', 'H', 'Cl', 'Cl'], 'name': 'Ethylene Dichloride', 'uses': 'Solvent, chemical intermediate', 'properties': 'Colorless liquid, toxic'},
    'H2C6H5O7': {'elements': ['H', 'H', 'C', 'C', 'C', 'C', 'C', 'C', 'O', 'O', 'O', 'O', 'O'], 'name': 'Citric Acid', 'uses': 'Food additive, flavoring', 'properties': 'White crystalline solid, soluble in water'},
    'C6H6': {'elements': ['C'] * 6 + ['H'] * 6, 'name': 'Benzene', 'uses': 'Solvent, chemical feedstock', 'properties': 'Colorless liquid, flammable, carcinogenic'},
    'C3H8O': {'elements': ['C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'O'], 'name': 'Isopropyl Alcohol', 'uses': 'Disinfectant, solvent', 'properties': 'Colorless liquid, flammable'},
    'C3H4O3': {'elements': ['C', 'C', 'C', 'H', 'H', 'O', 'O'], 'name': 'Lactic Acid', 'uses': 'Food additive, workout supplement', 'properties': 'Colorless liquid, slightly soluble in water'},
    'C3H7NO2': {'elements': ['C', 'C', 'C', 'H', 'H', 'N', 'O', 'O'], 'name': 'Alanine', 'uses': 'Amino acid, dietary supplement', 'properties': 'White crystalline solid, soluble in water'},
    'C4H6O3': {'elements': ['C', 'C', 'C', 'C', 'H', 'H', 'O', 'O', 'O'], 'name': 'Fumaric Acid', 'uses': 'Food additive, chemical intermediate', 'properties': 'White crystalline solid, soluble in water'},
#Continue with the rest of the compounds
}

#Define the layout of the periodic table
PERIODIC_TABLE_LAYOUT = [
    ['H',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  'He'],
    ['Li',  'Be',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  'B',  'C',  'N',  'O',  'F',  'Ne'],
    ['Na',  'Mg',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  'Al',  'Si',  'P',  'S',  'Cl',  ' Ar'],
    ['K',  'Ca',  'Sc',  'Ti',  'V',  'Cr',  'Mn',  'Fe',  'Co',  'Ni',  'Cu',  'Zn',  'Ga',  'Ge',  'As',  'Se',  'Br',  'Kr'],
    ['Rb',  'Sr',  'Y',  'Zr',  'Nb',  'Mo',  'Tc',  'Ru',  'Rh',  'Pd',  'Ag',  'Cd',  'In',  'Sn',  'Sb',  'Te',  'I',  'Xe'],
    ['Cs',  'Ba',  'La',  'Hf',  'Ta',  'W',  'Re',  'Os',  'Ir',  'Pt',  'Au',  'Hg',  'Tl',  'Pb',  'Bi',  'Po',  'At',  'Rn'],
    ['Fr',  'Ra',  'Ac',  'Rf',  'Db',  'Sg',  'Bh',  'Hs',  'Mt',  'Ds',  'Rg',  'Cn',  'Nh',  'Fl',  'Mc',  'Lv',  'Ts',  'Og'],  
    [' ',  ' ',  '*',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' '],
    [' ',  ' ',  '#',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' ',  ' '],
    [' ', ' ', '*La',  'Ce',  'Pr',  'Nd',  'Pm',  'Sm',  'Eu',  'Gd',  'Tb',  'Dy',  'Ho',  'Er',  'Tm',  'Yb',  'Lu',  ' '],
    [' ', ' ', '#Ac',  'Th',  'Pa',  'U',  'Np',  'Pu',  'Am',  'Cm',  'Bk',  'Cf',  'Es',  'Fm',  'Md',  'No',  'Lr',  ' '],
]

def draw_element(element, x, y, angle=0):
    # If angle is 0 (no rotation)
    if angle == 0:
        #Check if the element exists and is in the ELEMENTS dictionary
        if element and element in ELEMENTS:
            #Create a rectangle for the element
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            #Draw the element's background color
            pygame.draw.rect(screen, ELEMENTS[element]['color'], rect)
            #Draw a black borer around the element
            pygame.draw.rect(screen, BLACK, rect, 1)

            #REnder the element's symbol
            symbol = element_font.render(element, True,ELEMENT_FONT_COLOR)
            #Center the symbol in the element's rectangle
            symbol_rect = symbol.get_rect(center=\
                                                             (x + CELL_SIZE // 2, y + CELL_SIZE // 2))
            #Draw the symbol on the screen
            screen.blit(symbol, symbol_rect)

def draw_periodic_table():
    #Iterate through each row in the PERIODIC_TABLE_LAYOUT
    for row, elements in enumerate(PERIODIC_TABLE_LAYOUT):
        #iterate through each element in the row
        for col, element in enumerate(elements):
            #Calculate the x position of the element
            x = col * (CELL_SIZE + GRID_PADDING) + GRID_PADDING + TABLE_OFFSET_X
            #Calculate the y position of the element
            y = row * (CELL_SIZE + GRID_PADDING) + GRID_PADDING
            #Draw the element at the calculate position
            draw_element(element, x , y)

def draw_electron_shells(element, x, y, width, height):
    #Get the electron shell configuration for the element
    shells = ELEMENTS[element]['shells']
    #Calculate the center of the drawing area
    center_x, center_y = x + width // 2, y + height // 2
    #Iterate through each shell
    for i, electrons in enumerate(shells):
        #Calculate the radius for this shell
        radius = (i + 1) * (min(width, height)) // (2 * len(shells))
        #Draw the shell circle
        pygame.draw.circle(screen, WHITE, (center_x, center_y, radius, 1))
        #Calculate the angle step between electrons
        angle_step = 360 / electrons
        #Draw each electron in the shell
        for j in range(electrons):
            #Calculate the angle for this electron
            angle = math.radians(j * angle_step)
            #calculate the x position of the electron
            ex = center_x + int(radius * math.cos(angle))
            # Calculate the y position of the electron
            ey = center_y + int(radius * math.sin(angle))
            #Draw the electron
            pygame.draw.circle(screen, WHITE, (ex, ey), 2)


def create_tooltip(element):
    #Get the information for the given lement from the LELEMENTS dictionary
    info = ELEMENTS[element]
    #Create the tooltip text, which is just the name of the element
    tooltip_text = f"{info['name']}"
    #Render the tooltip text as a surface
    #Text color is (44, 44, 47) (#2c2c2f), background is (229, 229, 229)
    tooltip = font.render(tooltip_text, True, (44, 44, 47), (229, 229, 229))
    #Render the tooltip surface
    return tooltip

def draw_tooltip(screen, tooltip, pos):
    #Draw the tooltip on the screen
    #Position is offset by 15 pixels right and down from the cursor position
    screen.blit(tooltip, (pos[0] + 15, pos[1] + 15))


def show_element_info(element):
    #Get the information for the given element from the ELEMENTS dictionary
    info = ELEMENTS[element]
    #Create a list of formatted strings with element information
    lines = [
        f"Name : {info['name']}",
        f"Atomic Number: {info['atomic_number']}",
        f"Mass: {info['mass']}",
        f"Electron Config: {info['electron-config']}"
    ]
    #Return the list of information lines
    return lines


def show_compound_info(compound):
    #Get the information for compound from the COMPOUNDS dictionary
    info = COMPOUNDS[compound]
    #Create a list of formatted strings with compound information
    lines = [
        f"Name: {info['name']}",
        f"Formation: {compound}",
        f"Uses: {info['uses']}",
        f"Properties: {info['properties']}"
    ]
    #Return the list of information lines
    return lines


def check_compund(elements):
    #Sort the input elements to ensure consistent ordering
    elements.sort()
    #Iterate through all known compounds
    for compound, data in COMPOUNDS.items():
        #Compare the sorted input elements with the sorted elements of each compound
        if elements == sorted(data['elements']):
            #If a match is found, return the compound formula and name
            return compound, data['name']
    #If no match is found, return None for both compound and name
    return None, None

def show_popup(message, color):
    #Render the popup message with th specified color
    popup = popup_font.render(message, Trun, color)
    #Create a rectangle for the popup,
    #centered horizontally and 260 pixels from the bottom
    popup_rect = popup.get_rect(center=(WIDTH // 2, HEIGHT - 260))
    #Draw the popup on the screen
    screen.blit(popup, popup_rect)
    #Update the display to show the popup
    pygame.display.flip()
    #Wait for 1.5 seconds (1500 milliseconds)
    pygame.time.wait(1500)

def get_element_at_pos(pos):
    #Unpack the x and y coordinates from the input position
    x, y = pos
    #Calculate the column, accounting for the table offset
    col = (x - TABLE_OFFSET_X)  // (CELL_SIZE + GRID_PADDING)
    #Calculate the row
    row = y // (CELL_SIZE + GRID_PADDING)
    #Check if the calculated row and column are within the periodic table layout
    if 0 <= row < len(PERIODIC_TABLE_LAYOUT)\
        and 0 <=col < len(PERIODIC_TABLE_LAYOUT[0]):
          #return the element at the calculated positin in the periodic table layout
          return PERIODIC_TABLE_LAYOUT[row][col]
    #Return None if the position is outside the periodic table
    return None

def main():
    #Create a clock object to control the game's frame rate
    clock = pygame.time.Clock()

    #Flag to indicate if an element is being dragged
    dragging = False

    #Store the currently dragged element
    dragged_element = None

    #List to store elements in the merge area
    merge_area = [ ]

    #Define rectangles for various UI elements
    merge_area_rect = pygame.Rect(180, 100, WIDTH - 200, HEIGHT - 150) #merge area
    electron_shell_rect = pygame.Rect(180, 100, WIDTH - 200, HEIGHT - 260)
    #Electron shell visualization
    merge_button = pygame.Rect(180, 30, WIDTH - 200, HEIGHT - 40) #Merge button

    #List to store information about selected elements or compounds
    info_area = [ ]

    #Store the element currently being hovered over
    hover_element = None

    #Store the tooltip to be displayed
    tooltip = None


    while True:
        #Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Exit the game if the window is closed
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if merge_button.collidepoint(event.pos):
                    #Check if a compound can be formed from elements in the merge area
                    compound, name = check_compound(merge_area)
                    if compound:
                        #Show a popup with the created compound
                        show_popup(f"Created {name}  ({compound})",  WHITE)
                        #Display information about the compound
                        info_area = show_compound_info(compound)
                    else:
                        #Show a popup if no compound can be formed
                        show_popup("No compound formed", RED)
                    #Clear the merge area 
                    merge_area = [ ]
                else:
                    #Check if an element_at_pos(event.pos)
                    if element and element in  ELEMENTS:
                        #Start dragging the element
                        dragging = True
                        dragged_element = element
                        #Display informatin about the clicked element
                        info_area = show_element_info(element)
            elif event.type == pygame.MOUSEBUTTONUP:
                if dragging:
                    dragging = False
                    if merge_area_rect.collidepoint(event.pos) and dragged_element:
                        #Add the dragged element to the merge area if release there
                        merge_area.append(dragged_element)
                    else:
                        #Show a popup with the element name if released elsewhere
                        show_popup(f"{ELEMENTS[dragged_element]['name']}", WHITE)
                #reset the dragged element
                dragged_element = None

#Fill the screen with the background color
screen.fill(BACKGROUND)
#Draw the periodic table
draw_periodic_table()

#Draw the merge area 
pygame.draw.rect(screen,WHITE, merge_area_rect, 2)
for i, elem in enumerate(merge_area):
    #Draw elements in the merge area
    draw_element(elem, merge_area_rect.x + 10 + i * 40,merge_area_rect.y + 10)


#Draw the electron shell visualization area
pygame.draw.rect(screen, WHITE, electron_shell_rect, 2)
if merge_area:
    #Draw electron shells for the last element in the merge area
    draw_electron_shells(merge_area[-1], \
        electron_shell_rect.x,electron_shell_rect.y,
        electron_shell_rect.width, \
        electron_shell_rect.height)

#Draw the merge button
pygame.draw.rect(screen, WHITE, merge_button)
merge_text = font.render("Merge", True, BLACK)
screen.blit(merge_text, (merge_button.x + 70, merge_button.y + 8))

#Draw information area
info_rect = pygame.Rect(10, HEIGHT - 150, 300, 140)
for i, line in enumerate(info_area):
    #Render each line of information as white text
    info_text = font.render(line, True, WHITE)
    #Display the text in the information area
    screen.blit(info_text, (info_rect.x, info_rect.y + i*30))

#handle tooltips
mouse_pos = pygame.mouse.get_pos()
#Get the element at the current mouse position
hover_element = get_element_at_pos(mouse_pos)
if hover_element and hover_element in ELEMENTS:
    #Create a tooltip for the hovered element
    tooltip = create_tooltip(hover_element)
else:
    #Create the tooltip if not hovering over an element
    tooltip = None

if tooltip:
    #Draw the tooltip if not hovering over an element
    draw_tooltip(screen, tooltip, mouse_pos)

#Draw dragged element
if dragging and dragged_element:
    #Get the current mouse position
    x, y = pygame.mouse.get_pos()
    #Draw the dragged element at the mouse position
    draw_element(dragged_element, x - \
                            CELL_SIZE // 2,y  - CELL_SIZE //2)


#Update the display
pygame.display.flip()
#Control the frame rate
clock.tick(60)

if __name__ == "__main__":
    #Run the main function if this script is executed directly
    main()