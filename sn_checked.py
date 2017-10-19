


def doitall(_seed):
    from PIL import Image, ImageDraw
    import random

    # NOTE THIS IS NOT golfed not trying to make small yet

    W = 386
    H = 320

    # do everything the same each time
    random.seed(_seed)

    # create a new image
    orig = Image.open("ORIGINAL.png")
    orig = orig.convert("RGBA")
    orig_pix = orig.load()

    output_image = Image.new(orig.mode,(W,H))
    draw = ImageDraw.Draw(output_image)

    for i in range(500):
        # pick a random pixel
        x = random.randint(0,W-1)
        y = random.randint(0,H-1)

        # pick a random diam for a ellipse
        diam = random.randint(0,45)

        # get orig colors at the point we picked
        orig_colors = orig_pix[x,y]

        # pick a random alpha
        alpha = random.randint(0,255-1)
        color = (orig_colors[0],orig_colors[1],orig_colors[2],255)

        draw.ellipse((x,y,x+diam,y+diam), fill=color,
            outline=color)

    output_image.save("output.png")



def checkit():
    import os
    res = os.popen("python validate.py output.png").read().strip()
    return float(res)

def runcontest():
    lowest = 1000000
    seed = 0
    winner_seed = -1
    while True:
        if seed%10 == 0:
            print("running seed",seed)
        doitall(seed)
        res = checkit()

        if res < lowest:
            lowest = res
            winner_seed = seed

        seed = seed + 1

        if seed>100:
            break

    print "lowest",lowest
    print "seed",seed
    print "winner_seed",winner_seed

    print("running winner now...")
    doitall(winner_seed)





runcontest()
