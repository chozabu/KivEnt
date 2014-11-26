from os import environ, remove
from os.path import dirname, join, isfile
from distutils.core import setup
from distutils.extension import Extension
try:
    from Cython.Build import cythonize
    from Cython.Distutils import build_ext
    have_cython = True
except ImportError:
    have_cython = False
import sys

platform = sys.platform
if platform == 'win32':
	cstdarg = '-std=gnu99'
	libraries=['opengl32', 'glu32','glew32']
else:
	cstdarg = '-std=c99'
        libraries=[]

do_clear_existing = True

core_modules = {
    'kivent_core.cmesh': ['kivent_core/cmesh.pyx',],
    'kivent_core.gamesystems': ['kivent_core/gamesystems.pyx',],
    'kivent_core.gameworld': ['kivent_core/gameworld.pyx'],
    'kivent_core.renderers': ['kivent_core/renderers.pyx',],
    'kivent_core.gamescreens': ['kivent_core/gamescreens.pyx']
    }

core_modules_c = {
    'kivent_core.cmesh': ['kivent_core/cmesh.c',],
    'kivent_core.gamesystems': ['kivent_core/gamesystems.c',],
    'kivent_core.gameworld': ['kivent_core/gameworld.c'],
    'kivent_core.renderers': ['kivent_core/renderers.c',],
    'kivent_core.gamescreens': ['kivent_core/gamescreens.c']
    }


check_for_removal = [
    'kivent_core/cmesh.c',
    'kivent_core/gamesystems.c',
    'kivent_core/gameworld.c',
    'kivent_core/gamescreens.c',
    'kivent_core/renderers.c',
    ]

def build_ext(ext_name, files, include_dirs=[]):
    return Extension(ext_name, files, include_dirs,
        extra_compile_args=[cstdarg, '-ffast-math',],
        libraries=libraries)

extensions = []
cymunk_extensions = []
cmdclass = {}

def build_extensions_for_modules_cython(ext_list, modules):
    ext_a = ext_list.append
    for module_name in modules:
        ext = build_ext(module_name, modules[module_name])
        if environ.get('READTHEDOCS', None) == 'True':
            ext.pyrex_directives = {'embedsignature': True}
        ext_a(ext)
    return cythonize(ext_list)

def build_extensions_for_modules(ext_list, modules):
    ext_a = ext_list.append
    for module_name in modules:
        ext = build_ext(module_name, modules[module_name])
        if environ.get('READTHEDOCS', None) == 'True':
            ext.pyrex_directives = {'embedsignature': True}
        ext_a(ext)
    return ext_list

if have_cython:
    if do_clear_existing:
        for file_name in check_for_removal:
            if isfile(file_name):
                remove(file_name)
    core_extensions = build_extensions_for_modules_cython(
        extensions, core_modules)
else:
    core_extensions = build_extensions_for_modules(extensions, core_modules_c)


setup(
    name='KivEnt Core',
    description='''A game engine for the Kivy Framework. 
        https://github.com/Kovak/KivEnt for more info.''',
    author='Jacob Kovac',
    author_email='kovac1066@gmail.com',
    ext_modules=core_extensions,
    cmdclass=cmdclass,
    packages=[
        'kivent_core',
        ],
    package_dir={'kivent_core': 'kivent_core'})
