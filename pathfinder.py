from PIL import Image

def get_elevations(filename):
    with open(filename) as file:
        elevation_array = [line.split() for line in file]
        get_elevations_tidy= [[int(e) for e in row] for row in elevation_array]
        list_of_maxes = [max(row) for row in get_elevations_tidy]
        max_number = max(list_of_maxes)
        list_of_mins = [min(row) for row in get_elevations_tidy]
        min_number = min(list_of_mins)

        scaled_elevations = []
        for row in get_elevations_tidy:
            scaled_row = []
        for elevation in row:
            scaled_elevation = 255 * ((elevation - min_number)/(max_number - min_number))
            scaled_row.append(scaled_elevation)
            scaled_elevations.append(scaled_row)
        print(scaled_elevations)
        return scaled_elevations

get_elevations("elevation_small.txt")

def draw_box():
    map = Image.new('RGBA', (600, 600))
    for x in range(600):
        for y in range(600):
             map.putpixel((x, y), (210, 210, 210))
    map.save('MyMap.png')

draw_box()