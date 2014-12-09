from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window

import kivent_core
from kivent_core.renderers import texture_manager

from random import random

texture_manager.load_atlas('assets/background_objects.atlas')
texture_manager.load_image('assets/ship7.png')

class TestGame(Widget):
    def __init__(self, **kwargs):
        super(TestGame, self).__init__(**kwargs)
        Clock.schedule_once(self.init_game, 1.0)

    def init_game(self, dt):
        self.setup_map()
        self.setup_states()
        self.set_state()
        self.draw_some_stuff()
        Clock.schedule_interval(self.update, 0)


    def draw_some_stuff(self):
        angle = 0
        color = (1,1,1,1)
        width = 300.
        width2 = width*.5
        lw=width*1.3
        rw=width*-.2
        create_dict = {
            'position': (200., 200.),
            'renderer': {'texture': 'asteroid1', 'size': (64., 64.)},
            'rotate': angle ,'color':color, 'scale':1.
        }
        for i in range(100):
            create_dict['position']=(random()*width-width2,random()*width-width2,random()*10.-.9)
            self.gameworld.init_entity(create_dict, ['color', 'position', 'rotate', 'renderer', 'scale'])
        create_dict = {
            'position': (200., 275.),
            'renderer': {'texture': 'star1', 'size': (64., 64.)},
            'rotate': angle ,'color':color, 'scale':1.
        }
        for i in range(100):
            create_dict['position']=(random()*width-lw,random()*width*2.-width,random()*10.-.9)
            self.gameworld.init_entity(create_dict, ['color', 'position', 'rotate', 'renderer', 'scale'])
        create_dict = {
            'position': (100., 275.),
            'renderer': {'texture': 'ship7', 'size': (100., 64.)},
            'rotate': angle ,'color':color, 'scale':1.
        }
        for i in range(100):
            create_dict['position']=(random()*width-rw,random()*width*2.-width,random()*10.-.9)
            self.gameworld.init_entity(create_dict, ['color', 'position', 'rotate', 'renderer', 'scale'])
        for i in range(100):
            create_dict['position']=(-300,-300,random()*10.-.9)
            self.gameworld.init_entity(create_dict, ['color', 'position', 'rotate', 'renderer', 'scale'])

    def setup_map(self):
        gameworld = self.gameworld
        gameworld.currentmap = gameworld.systems['map']

    def update(self, dt):
        self.gameworld.update(dt)

    def setup_states(self):
        self.gameworld.add_state(state_name='main', 
            systems_added=['color', 'rotate', 'renderer', 'scale'],
            systems_removed=[], systems_paused=[],
            systems_unpaused=['color', 'rotate', 'renderer', 'scale'],
            screenmanager_screen='main')

    def set_state(self):
        self.gameworld.state = 'main'


class YourAppNameApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1.)


if __name__ == '__main__':
    YourAppNameApp().run()
