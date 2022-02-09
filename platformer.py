# Import all of ursina
from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

def update():
    global speed, dx, switch
    if switch == 1:
        dx += speed*time.dt 
        if abs(dx) > 2:
            speed *= -1
            dx = 0
        for enemy in enemies:
            enemy.x += speed*time.dt
            # Check the collision with enemies
            if abs(player.x-enemy.x)<1 and abs(player.y - enemy.y)<1:
                player.rotation_z=90
                switch = 0
        
    # Check the collision with traps
    dis = abs(player.x - trap.x)
    if (abs(dis-size)%size<=1 or abs(dis-size)%size>=size-1) and abs(player.y - ground.y)<=1:
        player.color = color.red
    else:
        player.color = color.white                     
        
class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.model = "cube"
        self.texture = "assets/ghost.png"
        self.color = color.green
        self.x = x
        self.y = y

# Declare the app
speed = 1
dx = 0
app = Ursina()

enemies = []
enemy = Enemy(1, 1)
enemies.append(enemy)

enemy = Enemy(-2.5-1, 2)
enemies.append(enemy)

size=13
bg = Entity(model='quad', scale=(size,6), texture='assets/sky_cloud', z=1)

    
player = PlatformerController2d(y=1, z=-.01, scale_y=1, color=color.white, texture='assets\guy.png')

ground = Entity(model='quad', y=-2, scale_x=10, collider='box', color=color.yellow)


wall = Entity(model='quad', color=color.azure, scale=(1,5), x=5.5, collider='box')


level = Entity(model='quad', color=color.red, scale=(3,1), x=2, collider='box')


ceiling = Entity(model='quad', color=color.cyan, scale=(3,1), x=-2.5, y=1, collider='box')

trap = Entity(model='quad', scale=(2,1), x=-6, y=-2, texture='assets/trap.png', collider='box')

extention = 1
for m in range(extention):
    enemy = Enemy(2-1+size*(m-1), 1)
    enemies.append(enemy)
    enemy = Enemy(2-1-size*(m-1), 1)
    enemies.append(enemy)    
    enemy = Enemy(-2.5-1+size*(m-1), 2)
    enemies.append(enemy)
    enemy = Enemy(-2.5-1-size*(m-1), 2)
    enemies.append(enemy)       
    duplicate(bg, x=size*(m+1))
    duplicate(bg, x=-size*(m+1))
    duplicate(ground, x=size*(m+1))
    duplicate(ground, x=-size*(m+1))
    duplicate(wall, x=5.5+size*(m+1))
    duplicate(wall, x=5.5-size*(m+1))
    duplicate(level, x=2+size*(m+1))
    duplicate(level, x=2-size*(m+1))
    duplicate(ceiling, x=-2.5+size*(m+1))
    duplicate(ceiling, x=-2.5-size*(m+1))    
    duplicate(trap, x=-6+size*(m+1))
    duplicate(trap, x=-6-size*(m+1))    
    
switch = 1    
camera.add_script(SmoothFollow(target=player, offset=[0, 1, -30], speed=4))
# Run the app
app.run()
