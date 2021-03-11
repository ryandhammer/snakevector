import pygame

from math import pi, sin, cos

TO_RADS = pi / 180

class shape2d:
    def __init__(self, source):
        self.source = source
        self.verticies = []
        self.lines = []
        self.load2d(self.source)
        self.tx = 0
        self.ty = 0

    def load2d(self, source):
        """Loads a shape file which contains a series of verticies and lines.
        Lines starting with a v are verticies and are defined as x/y coordinates.
        Lines starting with an h are lines and are a pair of verticies to draw
        lines between.  This is a stupid and brittle parser right now."""

        fh = open(self.source)
        for line in fh.readlines():
            if line[0] == '#':
                next
            if line[0] == 'v':
                self.verticies.append((int(line.split(':')[1]), int(line.split(':')[2])))
            if line[0] == 'l':
                self.lines.append((int(line.split(':')[1]), int(line.split(':')[2])))


    def draw(self, surface):
        """Accepts a pygame surface and draws the shape to that surface."""

        def origin_convert(vertex, surf_size):
            """Only needed in the draw function, moves the shape to the
            center of the screen."""

            width, height = surf_size
            x,y = vertex[0], vertex[1]
            x1 = x + width / 2
            y1 = -y + height / 2

            return (x1, y1)

        surf_sz = surface.get_size()
    
        for entry in self.lines:
            # put the shape at the center of the screen
            start = origin_convert(self.verticies[entry[0]], surf_sz)
            end = origin_convert(self.verticies[entry[1]], surf_sz)

            # add translation offset
            start = (start[0] + self.tx, start[1] + self.ty)
            end = (end[0] + self.tx, end[1] + self.ty)
        
            # and print
            pygame.draw.line(surface, (0, 255, 0), start, end)


    def translate(self, dx, dy):
        """Accepts a delta x and y value and modifies tx and ty which store
        the offset to draw the shape at.  These are referenced by .draw()
        instead of changing the verticies since that would make rotation
        stop working correctly."""
        self.tx += dx
        self.ty += dy


    def scale(self, factor):
        """Shrinks or enlarges the shape based on factor.  Values lower than
        1.0 shrink it and greater than 1.0 grow it.  1 is a waste of time.
        Because scaling doesn't change the local origin, it is safe to apply
        the scaling factor to the verticies."""

        # nyah
        if factor == 1:
            return

        # unfortunatly, we're working with tuples, so we'll have to replace
        # them instead of changing their value in place. :(
        for vert in range(len(self.verticies)):
            x, y = self.verticies[vert]
            self.verticies[vert] = (x * factor, y * factor)


    def rotate(self, angle):
        """Rotates all verticies around the origin of the shape by angle,
        which is specified in degrees.  This is why translation is written
        the way it is :)"""

        theta = angle * TO_RADS

        # Once again, tuples so we'll have to iterate over the list and
        # replace them with the rotated values.
        for vert in range(len(self.verticies)):
            x, y = self.verticies[vert]

            xr = x * cos(theta) - y * sin(theta)
            yr = x * sin(theta) + y * cos(theta)

            self.verticies[vert] = (xr, yr)
