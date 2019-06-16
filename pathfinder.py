from PIL import Image

def get_elevations(filename):
    with open(filename) as file:
        elevation_array = [line.split() for line in file]
        get_elevations_tidy= [[int(e) for e in row] for row in elevation_array]
        list_of_maxes = [max(row) for row in get_elevations_tidy]
        print(list_of_maxes)
        list_of_mins = [min(row) for row in get_elevations_tidy]
        print(list_of_mins)
    


get_elevations("elevation_small.txt")

def draw_box():
    map = Image.new('RGBA', (600, 600))
    for x in range(600):
        for y in range(600):
             map.putpixel((x, y), (210, 210, 210))
    map.save('MyMap.png')

draw_box()