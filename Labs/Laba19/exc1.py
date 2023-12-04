from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wand.display import display

with Image(width=500, height=500, background=Color('white')) as img:

    with Drawing() as draw:
        draw.circle((250, 200),(240, 220))
        draw(img)
        

    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.fill_color = Color('transparent')
        draw.stroke_width = 4

        draw.ellipse( (250, 200), (50, 200) )
        draw(img)
        

    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.fill_color = Color('transparent')
        draw.stroke_width = 4


        draw.ellipse( (250, 200), (200, 50) )
        draw(img)
        img.rotate(45, background = Color('white'))
        
     

    with Drawing() as draw:
        draw.stroke_color = Color('black')
        draw.fill_color = Color('transparent')
        draw.stroke_width = 4

        draw.ellipse( (390, 320), (50, 200) )
        draw(img)

    with Drawing() as draw:
        draw.circle((361, 160),(376, 160))
        draw.circle((310, 447),(325, 447))
        draw.circle((515, 400),(530, 400))
        draw(img)

    img.save(filename='Labs/Laba19/atom.png')

    display(img)

