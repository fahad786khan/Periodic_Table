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
    ("your/path/.ttf", 28)

#Font for popups, Size 46
popup_font = pygame.font.Font(None, 46)

#Element cell size
CELL_SIZE = 53 #Size of each element cell in pixels
GRID_PADDING = 4 #Paddinf between cells in pixels
TABLE_OFFSET_X = 80 #Horizontal offset for the entire periodic table

# Define elements 
ELEMENTS = {
    'H' : {'name' : 'Hydrogen' , 'color' : NONMETALS,\
        'atomic_number' : 1, 'mass' : 1.008, \
            'electron_config' : '1s1' , 'shells' : [1]},
    'He' : {'name' : 'Helium', 'color' : NOBEL_GASES,\
        'atomic_number' : 2, 'mass' : 4.003,\
            'electron_config': '1s2', 'shells' : [2]},
}

            #Continue with the rest of elements

#Define compounds
COMPOUNDS = {
    'H2O' : {'elements' : ['H', 'H', 'O'],\
        'name': 'Water','user':\
            'Essential for life, solvent',\
                'properties': 'Colorless, odorless liquid'},
    'CO2' : {'elements' : ['C', 'O', 'O'],\
        'name': 'Carbon Dioxide' , 'uses' : \
            'Carbonated drinks, plant photosynthesis' ,\
                'properties': 'colorless gas , solubke in water'
    },
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
    merge_area_rect = pygame.Rect\
    (WIDTH - 200, HEIGHT - 150, 180, 100) #merge area
    electron_shell_rect = pygame.Rect\
    (WIDTH - 200, HEIGHT - 260, 180, 100)
    #Electron shell visualization
    merge_button = pygame.Rect
    (WIDTH - 200, HEIGHT - 40, 180, 30) #Merge button

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
                        info_arera = show_element_info(element)
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
    draw_element(elem, merge_area_rect.x + 10 + i*40,\
                            merge_area_rect.y + 10)

#Draw the electron shell visualization area
pygame.draw.rect(screen, WHITE, electron_shell_rect, 2)
if merge_area:
    #Draw electron shells for the last element in the merge area
    draw_electron_shells(merge_area[-1], \
        electron_shell_rect.x,electron_shell_rect.y,
        electron_shell_rect.width, \
            electron_shell_rect.height)

#Draw the merge button
pygame.draaw.rect(screen, WHITE, merge_button)
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