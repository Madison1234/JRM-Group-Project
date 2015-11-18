image = Image.open("x.png")
draw = ImageDraw.Draw(image)
draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,255))
