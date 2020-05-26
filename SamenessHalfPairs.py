
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This is an visual search experiment
"""
#===================
# Import Libraries
#===================
from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
import random
import os, sys  # handy system and path functions
import copy
import pandas as pd # for mask orientation list, save as a seperate csv
import math
import itertools
from collections import defaultdict

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)) #.decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

from experiment_helper import *
from stimuli_helper import *
from data_helper import *
#========================
# Setup Experiments
#========================

# Store info about the experiment session
exp_name = 'Sameness - Half Match Pairs'  # from the Builder filename that created this script
default_info = {u'session': u'', u'participant': u''}
exp_info = exp_info_GUI(name = exp_name, default_info = default_info)
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
subj_file = u'%s_%s_%s' % (exp_info['exp_name'], exp_info['participant'], exp_info['date'])
filename = _thisDir + os.sep + u'data_half_pairs/' + subj_file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = exp_handler_setup(exp_name, exp_info, filename)

# win_size = (1440, 900) # mackbook
win_size = (1920, 1080) # chaz lab display
# win_size = (1680, 1050) # lab testing mac
# win_size = (1080, 720)
win = create_window(size = win_size, fullscr = False, screen = 0, units = 'height')

#============================
# Setup Experiment parameters
#============================
# Initialize components for Routine "exp"
expClock = core.Clock()

# start message
start_msg = create_msg(win,
            text="For each trial, you will need to look to see if there is a unique element.\n\n If there is, press 'f'"
                 ", if not, press 'j'. \n\n Press 'Space' to continue." ,
            height = 0.04)

# break, every 48 trials
break_msg = create_msg(win,
                text="Take a quick break for at least 5 seconds. \nWhen you are ready to continue, press'SPACE'.")

path = defaultdict(list)

# settings - times
target_on, target_off = 0, 0.5
delay = 0.9
test_on = target_off + delay
inter_trial_interval = 1

# Create some handy timers
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

n_trials = 360 # total trials

# Makes stimuli list
letter_list = ['B', 'C', 'D', 'E', 'F', 'G', 'J', 'K', 'L', 'P', 'Q', 'R', 'S', 'Z']
same_list = []
diff_list = []

for i in letter_list:
    for j in letter_list:
        if i == j:
            same_list.append(i + j)
        else:
            diff_list.append(i + j)

same_list_diff_letters = ['BC', 'CB', 'CE', 'EC', 'DJ', 'JD', 'ER', 'RE', 'FC', 'CF',
                          'GB', 'BG', 'JP', 'PJ', 'KA', 'AK', 'LC', 'CL', 'PG', 'GP',
                          'QZ', 'ZQ', 'RE', 'ER', 'SQ', 'QS', 'ZA', 'AZ', 'FR', 'RF']

both_cond = {}
for i in range(len(same_list)):
    for j in range(1, 3):
        both_cond[same_list[i]] = [same_list_diff_letters[i*j], same_list_diff_letters[i*j+1]]
        j += 1

# Three Different Properties of Trials
same_cond_1 = ['same'] # categories: color, poly, chinese character, letter, object, cube
diff_cond_1 = ['different']
load_list = [4, 8, 12] # of choices: 4, 8, 12
target_present_list = ['yes', 'no']

# All combinations of properties in equal proportions.
cond = []

for item in itertools.product(same_cond_1, load_list, target_present_list, both_cond):
    cond.append({'same_different': item[0], 'load': item[1], 'target_present': item[2], 'letter': item[3],
                 'pair': both_cond[item[3]][0]})
    cond.append({'same_different': item[0], 'load': item[1], 'target_present': item[2], 'letter': item[3],
                 'pair': both_cond[item[3]][1]})

for item in itertools.product(same_cond_1, load_list, target_present_list):
    cond.append({'same_different': item[0], 'load': item[1], 'target_present': item[2], 'letter': 'FF',
                 'pair': 'FR'})
    cond.append({'same_different': item[0], 'load': item[1], 'target_present': item[2], 'letter': 'FF',
                 'pair': 'RF'})

firstDiffList = random.sample(diff_list, k = 15)
diff_list = firstDiffList

# Letter = Target
# Pair = Distractor
for item in itertools.product(diff_cond_1, load_list, target_present_list, diff_list):
    cond.append({'same_different': item[0], 'load': item[1], 'target_present': item[2], 'letter': item[3], 'pair': item[3][0] + item[3][0]})
    cond.append({'same_different': item[0], 'load': item[1], 'target_present': item[2], 'letter': item[3], 'pair': item[3][1] + item[3][1]})
trial_prop = [1/360] * 360 # proportions of conditions

# make list and shuffle
same_trial_list = list() #trial list
diff_trial_list = list()
for ind, proportion in enumerate(trial_prop):
    con_trial_num = int(n_trials * proportion)
    if cond[ind]['same_different'] == 'same':
        same_trial_list.extend([cond[ind]] * con_trial_num)
    elif cond[ind]['same_different'] == 'different':
        diff_trial_list.extend([cond[ind]] * con_trial_num)
shuffle(same_trial_list)
shuffle(diff_trial_list)

trials = create_trial_database(n_trials = n_trials, exp_info = exp_info, name ='trials')
thisExp.addLoop(trials)  # add the loop to the experiment

#======================
# Present Experiments
#======================
# experiment instruction
start_msg.draw()
win.flip()
event.waitKeys(keyList='space')

win.flip(clearBuffer = True)
core.wait(inter_trial_interval)

rand = random.randrange(2)

for trial_id, trial in enumerate(trials):
    # ------Prepare to start Routine "exp"-------
    event.clearEvents(eventType='keyboard')
    core.wait(0.25)

    # get break midway of the task
    if trial_id % 60 == 0 and trial_id != 0:
        break_msg.draw()
        win.flip()
        core.wait(5)
        # can response after 5s' break
        event.waitKeys(keyList='space')
        win.flip(clearBuffer = True)
        core.wait(inter_trial_interval)

    expClock.reset()
    t, frameN = 0, -1
    #=========================
    # prepare trial parameters
    #=========================

    if rand == 1:
        if trial_id < n_trials/2:
            same_cond = same_trial_list[trial_id]['same_different']
            load = same_trial_list[trial_id]['load']
            target_present = same_trial_list[trial_id]['target_present']
            letter = same_trial_list[trial_id]['letter']
            pair = same_trial_list[trial_id]['pair']
        else:
            same_cond = diff_trial_list[trial_id - n_trials//2]['same_different']
            load = diff_trial_list[trial_id - n_trials//2]['load']
            target_present = diff_trial_list[trial_id - n_trials//2]['target_present']
            letter = diff_trial_list[trial_id - n_trials//2]['letter']
            pair = diff_trial_list[trial_id - n_trials//2]['pair']
    else:
        if trial_id < n_trials/2:
            same_cond = diff_trial_list[trial_id]['same_different']
            load = diff_trial_list[trial_id]['load']
            target_present = diff_trial_list[trial_id]['target_present']
            letter = diff_trial_list[trial_id]['letter']
            pair = diff_trial_list[trial_id]['pair']
        else:
            same_cond = same_trial_list[trial_id - n_trials//2]['same_different']
            load = same_trial_list[trial_id - n_trials//2]['load']
            target_present = same_trial_list[trial_id - n_trials//2]['target_present']
            letter = same_trial_list[trial_id - n_trials//2]['letter']
            pair = same_trial_list[trial_id - n_trials//2]['pair']

    # get target, choices
    #target = get_target(win, target_p)

    tests = []
    #target = get_target(win, target_p)
    twoLetters = []
    correct_ans = 0
    rt = 0
    response = 'a'
    cell_locs = [[-0.28, 0.21], [-0.14, 0.21], [0, 0.21], [0.14, 0.21], [0.28, 0.21],
                 [-0.28, 0.07], [-0.14, 0.07], [0, 0.07], [0.14, 0.07], [0.28, 0.07],
                 [-0.28, -0.07], [-0.14, -0.07], [0, -0.07], [0.14, -0.07], [0.28, -0.07],
                 [-0.28, -0.21], [-0.14, -0.21], [0, -0.21], [0.14, -0.21], [0.28, -0.21]]

    jitter = 0.02  # +/- 1 degree jitter
    for cell_loc in cell_locs:
        x = random.uniform(-jitter, jitter)
        y = random.uniform(-jitter, jitter)
        cell_loc[0] = cell_loc[0] + x
        cell_loc[1] = cell_loc[1] + y

    # get stim positions
    pos = random.sample(cell_locs, k = load)
    shuffle(diff_list)
    shuffle(same_list)
    if target_present == 'yes':
        for i in range(load - 1):
            twoLetters.append(pair)
        twoLetters.append(letter)
    elif target_present == 'no':
        for i in range(load):
            twoLetters.append(pair)
    random.shuffle(twoLetters)

    for i in range(load):
        tests.append(get_stims(win, twoLetters[i], pos[i]))

    key_resp = event.BuilderKeyResponse()
    key_resp.status = NOT_STARTED
    # -------Start Routine "exp"-------
    continueRoutine = True
    reset_auto_draw(tests)
    t = expClock.getTime()

    while continueRoutine:
        # get current time
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

        theseKeys = event.getKeys(keyList=['f', 'j'])

        
        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
            win.flip(clearBuffer=True)

        for test in tests:
            test.draw()

        # keep track of start time/frame for later
        key_resp.status = STARTED
        key_resp.tStart = t
        key_resp.frameNStart = frameN  # exact frame index
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
        if len(theseKeys) > 0:  # at least one key was pressed & within time constraint
            response = theseKeys[-1]  # just the last key pressed
            resp_time = expClock.getTime() # the time of response
            rt = resp_time - t # reaction time = time of response - time of stimulus onset
            # a response ends the routine
            reset_auto_draw(tests)
            if target_present == 'yes' and response == 'f':
                correct_ans = 1
            elif target_present == 'yes' and response == 'j':
                correct_ans = 0
            elif target_present == 'no' and response == 'f':
                correct_ans = 0
            elif target_present == 'no' and response == 'j':
                correct_ans = 1

            continueRoutine = False

        win.flip(clearBuffer=True)
    # -------End Routine "load"-------

    # -------Ending Routine "exp"-------
    win.flip()
    core.wait(inter_trial_interval)
    trials = save_cond(trials, load, same_cond, target_present)
    trials = save_response(trials, response, rt, correct_ans)
    trials = save_loc_data(trials, twoLetters, pos)
    routineTimer.reset()
    thisExp.nextEntry()
#=================
# Finish Experiment
#==================
# completed 960 repeats of 'trials'

# save files
save_trial_file(trials, filename)
save_exp_file(thisExp, filename)

logging.flush()

# finish experiments
thisExp.abort()
win.close()
core.quit()
