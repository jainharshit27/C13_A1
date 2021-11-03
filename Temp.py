import pygame, pymunk
import pymunk.pygame_util

def create_arrow():
    vs = [(-80, 0), (0, 2), (2, 0), (0, -2)]
    arrow_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    arrow_shape = pymunk.Poly(arrow_body, vs)
    arrow_shape.density = 0.1
    arrow_body.position = 100, 140
    return arrow_body, arrow_shape

pygame.init()

height = 600
width = 690
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 1000
wind = 200
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

vs_rect = [(1, -80), (1, 80), (-1, 80), (-1, -80)]
target_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
target_shape = pymunk.Poly(target_body, vs_rect)
target_body.position = 600,400
space.add(target_body, target_shape)

#remove bow

arrow_body, arrow_shape = create_arrow()
space.add(arrow_body, arrow_shape)

flying_arrows = []

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Check if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1, if yes:
                #set start_time = pygame.time.get_ticks(). Similarly,
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                #end_time = pygame.time.get_ticks()
                
                #find difference between start_time and end_time
                #find minimum value among diff and 1000. Multiply the resultant value to 13.5 and assign the value to power
                #create a tuple called impulse with value (power*1, 0)
                arrow_body.body_type = pymunk.Body.DYNAMIC
                #assign arrow_body the apply_impulse_at_world_point(impulse, arrow_body.position) method.
                
                flying_arrows.append(arrow_body)
                arrow_body, arrow_shape = create_arrow()
                space.add(arrow_body, arrow_shape)      
    
    #Check if pygame.mouse.get_pressed()[0] which checks if the left mouse click is pressed, if yes:
        #print(pygame.mouse.get_pressed()) to explain them the tuple printed that 3 values belong to 3 mouse keys
        #calculate current_time using pygame.time.get_ticks()
        #calculate diff by subtracting start_time with current_time
        #create power and assign min(diff, 1000)
        #create variable h and assign power / 2
        #run function pygame.draw.line(screen, (255, 0, 0), (650, 550), (650, 550 - h), 10) to draw the powerbar.
        
    space.debug_draw(draw_options)
    
    #space reload
    space.step(1/60)
    pygame.display.update()
    clock.tick(60)
