import pygame
import random
import math

pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blaine Colwell")

# create background, assign color
background = pygame.Surface(screen.get_size())
background = background.convert()
# this is just a nice gray
background.fill((126, 126, 126))

# create cat
cat = pygame.image.load("kale.png")
cat = cat.convert_alpha()
# these numbers aren't anything special, just 25% of the original image size
cat = pygame.transform.scale(cat, (66, 123))
# some starting values; originally here just because that's where I wanted the image to start
# now they're here because they keep it from freaking out on the edges
cat_x = 250
cat_y = 100
# Generate a random angle
randomAngle = math.radians(random.randint(0, 360))
# This separates the angles -- angle only changes based on which side it hits, instead of changing both angles every time
randomAngle_x = randomAngle
randomAngle_y = randomAngle

# create clock object
clock = pygame.time.Clock()

continueMainLoop = True
while continueMainLoop:
    clock.tick(30)

    # check if quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continueMainLoop = False

    # cosine of an angle gives the ratio between the angle and x-axis; this is multiplied by 12 (constant speed)
    # which gives the change needed in order to match the angle
    # This does cause the image to speed up sometimes, although I don't entirely understand why yet
    cat_x += 12 * math.cos(randomAngle_x)
    # same as above for y-axis
    cat_y += 12 * math.sin(randomAngle_y)

    # Check if the cat is out of bounds, and correct the angle if it is
    if int(round(cat_x)) not in range(0, screen.get_width() - 66):

        # if it's off the side of the screen, put it back in
        # it gets stuck if it's placed exactly inside the screen, so 1 instead
        if cat_x <= 0:
            cat_x = 1
        else:
            cat_x = screen.get_width() - 67

        # flip the angle
        randomAngle_x = 180 - randomAngle_x

    # same as above but for y-axis
    if int(round(cat_y)) not in range(0, screen.get_height() - 123):
        if cat_y <=0:
            cat_y = 1
        else:
            cat_y = screen.get_height() - 124
        # this has to be flipped
        randomAngle_y = randomAngle_y - 180

    # update screen
    screen.blit(background, (0,0))
    screen.blit(cat, (cat_x, cat_y))
    pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()
