__author__ = 'chozabu'

import os, json

defaultSettingsDict = {
    "do_profile":0.,
    "ai_action_chance":0.001,
    "enable_airhole_extras":0.,
    "observer_points_per_second":200.,
    "goal_height":600,
    'goal_thickness':120,
    'airhole_xnum':22,
    'airhole_radius':60,
    'airhole_collision_radius':.001,
    'airhole_type':'hole',#hole, triangle,square
    'faded_air_hole_alpha':.075,
    'enable_particles':1,
    'volume_multi':.85,
    'puck_max':2,
    'paddle_max':2,
    'puck_storm_at_points':8,
    'wall_duration':14.,
    'vortex_duration':7.5,
    'vortex_alpha':0.3,
    'vortex_particle_chance':.4,
    'vortex_power':.6,
    'vortex_radius':140,
    'vortex_static':1

}

settingsDict = {}

datadir = ""

def loadSettings():
    global settingsDict
    fileNamePath = datadir+"LightHockeySettings.jso"
    if os.path.exists(fileNamePath):
        if os.path.isfile(fileNamePath):
            with open(fileNamePath) as fo:
                settingsDict = json.load(fo)

    for a,b in defaultSettingsDict.iteritems():
        if a not in settingsDict:
            settingsDict[a]=b
    saveSettings()



def saveSettings():
    fileNamePath = datadir+"LightHockeySettings.jso"
    with open(fileNamePath, 'w') as fo:
        json.dump(settingsDict, fo)

