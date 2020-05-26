import os
import math
from psychopy import visual
import random
from random import uniform, shuffle, sample

def create_msg(win, name='msg', text='default text',
    font='Arial', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, color = 'black'):
    return visual.TextStim(win=win, name=name, text=text, font=font,
        pos=pos, height=height, wrapWidth=wrapWidth, ori=ori, color=color)


def get_stims(win, letter, pos):
    return visual.TextStim(  # Generates Text boxes per polygon.
            win=win, name='iteratedText',
            text=letter,
            font=u'Arial',
            pos=pos, height=0.05, wrapWidth=None, ori=0,
            color=u'black', colorSpace='rgb', opacity=1,
            depth=-2.0)

def get_shape_stim(win, vertices):
        return visual.ShapeStim(
              win=win, vertices=vertices, radius=0.025, name='iteratedPolygon', color=u'black'  
        )

def reset_auto_draw(stimuli):
    for s in stimuli:
        s.setAutoDraw(False)
