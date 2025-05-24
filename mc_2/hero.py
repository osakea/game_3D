key_switch_camera = 'c'
key_switch_mode = 'z'

k_for = 'w'
k_b = 's'
k_l = 'a'
k_r = 'd'
k_u = 'e'
k_d = 'q'

key_turn_left = 'n'
key_turn_right = 'm'

key_build = 'b'
key_destroy = 'v' 

key_savemap = 's'
key_loadmap = 'l'

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.setPos( 0, 0, 1.5)
        base.camera.reparentTo(self.hero)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else: 
            self.cameraBind()

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def look_at(self, angle):
        # returns the coor which the hero at the point(x,y) moves to if they step towards angle

        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from
    
    def just_move(self, angle):
        # move to the desired coor in any case
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def check_dir(self,angle):
        if angle >= 0 and angle <= 20:
            return (0,-1)
        elif angle <= 65:
            return(1, -1)
        elif angle <= 110:
            return(1, 0)
        elif angle <= 155:
            return(1, 1)
        elif angle <= 200:
            return(0, 1)
        elif angle <= 245:
            return(-1, 1)
        elif angle <= 290:
            return(-1, 0)
        elif angle <= 335:
            return(-1, -1)
        else:
            return(0, -1)

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)
    
    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)
        
    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def try_move(self, angle):
        #moves if they can
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            #there is free space, move down if can
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            #if no free space, can climb
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
                #unable to climb = we stand still
    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def build(self):
        angle = (self.hero.getH()) % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        angle = (self.hero.getH()) % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

    def accept_events(self):
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + '-repeat', self.turn_right)

        base.accept(k_for, self.forward)
        base.accept(k_for + '-repeat', self.forward)
        base.accept(k_b, self.back)
        base.accept(k_b + '-repeat', self.back)
        base.accept(k_l, self.left)
        base.accept(k_l + '-repeat', self.left)
        base.accept(k_r, self.right)
        base.accept(k_r + '-repeat', self.right)

        base.accept(key_switch_camera, self.changeView)

        base.accept(key_switch_mode, self.changeMode)

        base.accept(k_u, self.up)
        base.accept(k_u + '-repeat', self.up)
        
        base.accept(k_d, self.down)
        base.accept(k_d + '-repeat', self.down)

        base.accept(key_build, self.build)
        base.accept(key_destroy, self.destroy)

        base.accept(key_savemap, self.land.saveMap)
        base.accept(key_loadmap, self.land.loadMap)