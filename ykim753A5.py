"""
Aim: to create the texted image into tkinter shapes, and complete the whole picture.
Author: Youmin Kim, ykim753
"""
from tkinter import *

#-------------------------------------------
#-------------------------------------------
# main() function
#-------------------------------------------
def main():
    size = 25
    start_left = size * 2
    start_down = size * 2
    pattern_filename, palette_filename = get_filenames()
    pattern_list = process_file(pattern_filename)
    colours_list = process_file(palette_filename)
    #complete this
    colours_dictionary = create_colour_dictionary(colours_list)
    
    number_of_rows = len(pattern_list)	
    number_of_columns = len(pattern_list[0])
    canvas_width = size * number_of_columns +size * 4
    canvas_height = number_of_rows * size + size * 4
    window = Tk() 
    window.title("A5 by youmin kim") 
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand = True) #Canvas fills the whole window  
    draw_pattern(a_canvas, colours_dictionary, pattern_list, size, start_left, start_down)

def get_filenames():
    name = input("Enter a name: ")
    txtfile = name + ".txt"
    palettefile = name + "_palette.txt"
    bothtuple = (txtfile, palettefile,)
    return bothtuple

def process_file(filename):
    input_file = open(filename, 'r')
    file_contents = input_file.read().split("\n")
    input_file.close()
    return file_contents

def create_colour_dictionary(colours_list):
    colourdict = {}
    for i in range(len(colours_list)):
        assigncolour = colours_list[i]
        symbol = assigncolour[0]
        colour = assigncolour[2:]
        colourdict[symbol] = colour
    return colourdict      

def draw_pattern(a_canvas, colours_dictionary, pattern_list, size, start_x, start_y):     
    y = start_y
    for row in range(len(pattern_list)):
        x = start_x
        eachrow = pattern_list[row]
        for column in range(len(eachrow)):
            symbol = eachrow[column]
            if symbol in colours_dictionary:
                thecolourrr = colours_dictionary[symbol]
                a_canvas.create_rectangle(x, y, (x + size), (y + size), fill=thecolourrr, outline=thecolourrr)
                x += size
        y += size  
 

main()
