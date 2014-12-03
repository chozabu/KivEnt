__author__ = 'chozabu'

gameref = None

from math import pi, cos, sin

enable_particles = 1

from random import random

particles = []

class particle:
    def __init__(self, ent, pos,lifespan, moveby):
        self.ent=ent
        self.pos=pos
        self.lifespan=lifespan
        self.maxlifespan=lifespan
        self.moveby=moveby
        self.invmoveby=1.-moveby

def spawn_particles_at(pos, count=1, color=(1,1,1,1), lifespan=1.,moveby=.02, radlimit=140.):
    if enable_particles==0:return
    for np in range(count):
        angle = random()*pi*2.
        npos = (pos[0]+cos(angle)*radlimit,pos[1]+sin(angle)*radlimit)
        pid = create_visual(npos, color=color)
        ent = gameref.gameworld.entities[pid]
        newp = particle(ent,pos,lifespan=lifespan, moveby=moveby)
        particles.append(newp)

def update(dt):
    global particles
    remlist=[]
    for p in particles:
        ent = p.ent
        entpos = ent.position
        dist=(p.pos[0]-entpos.x, p.pos[1]-entpos.y)
        entpos.x+=dist[0]*p.moveby
        entpos.y+=dist[1]*p.moveby
        ent.color.a=p.lifespan/p.maxlifespan
        p.lifespan-=dt
        if p.lifespan<0:
            remlist.append(p)
            gameref.gameworld.remove_entity(ent.entity_id)
    for r in remlist:
        particles.remove(r)



def create_visual(pos, color,start_scale=1.):

    create_component_dict = {
        'puck_renderer': {'texture': 'particle',
        'size': (64, 64)},
        'position': pos, 'rotate': 0, 'color': color,
        #'lerp_system': {},
        'scale':start_scale}
    component_order = ['position', 'rotate', 'color',
        'puck_renderer','scale']
    eid = gameref.gameworld.init_entity(create_component_dict,
        component_order)
    return eid