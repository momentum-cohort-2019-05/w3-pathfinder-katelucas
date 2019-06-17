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
    map = Image.new('L', (600, 600))
    for x in range(600):
        for y in range(600):
             map.putpixel((x, y), (210, 210, 210))
    map.save('MyMap.png')

draw_box()

#current issues: 1.plotting to map
                #2.elevations are huge floats
                
#more provided code
class ElevationMap:
    """
    ElevationMap is a class that takes a matrix (list of lists, 2D)
    of integers and can be used to generate an image of those elevations
    like a standard elevation map.
    """

    def __init__(self, elevations):
        self.elevations = elevations

    def elevation_at_coordinate(self, x, y):
        return self.elevations[y][x]

    def min_elevation(self):
        return min([min(row) for row in self.elevations])

    def max_elevation(self):
        return max([max(row) for row in self.elevations])

    def intensity_at_coordinate(self, x, y):
        """Given an x, y coordinate, return the
        intensity level (used for grayscale in image) of
        the elevation at that coordinate.
        """
        elevation = self.elevation_at_coordinate(x, y)
        min_elevation = self.min_elevation()
        max_elevation = self.max_elevation()

        return (elevation - min_elevation) / (max_elevation - min_elevation)


def draw_grayscale_gradient(filename, width, height):
    image = Image.new(mode='L', size=(width, height))
    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), (int(x / width * 255),))
    image.save(filename)


if __name__ == "__main__":
    my_str = "10 12 9 345 2 78"
    read_line_of_ints(my_str)

    elevations = read_file_into_ints('elevation_test.txt')

    e_map = ElevationMap(elevations)
    print(e_map.intensity_at_coordinate(1, 2))

    draw_grayscale_gradient('test.png', 400, 400)


#code provided but i'm unsure how to tie in
def difference(x, y):
    return abs(x - y)

def test_difference():
    assert difference(2, 1) == 1
    assert difference(1, 2) == 1