#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 九月 20, 2021, at 14:27
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

print('1')
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'main'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + \
    u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=os.path.abspath(__file__),
                                 savePickle=True, saveWideText=False,
                                 dataFileName=filename)
# this outputs to the screen, not a file
logging.console.setLevel(logging.WARNING)

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 768], fullscr=False, screen=0,
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
background_img = visual.ImageStim(
    win=win, image="./lib/background.jpg", name="background", size=win.size, units="pix")
trialClock = core.Clock()
button_1_img = visual.ImageStim(
    win=win, image="./lib/button.png", pos=(-0.3, 0.28), size=[0.4, 0.12], units='height', name='button1_img')
button_1 = visual.ButtonStim(win,
                             text='', font='Open Sans',
                             pos=(-0.3, 0.28),
                             letterHeight=0.04,
                             size=[0.3, 0.1], borderWidth=1,
                             fillColor='deepskyblue', borderColor='white',
                             color='white', colorSpace='rgb',
                             opacity=0,
                             bold=True, italic=False,
                             padding=None,
                             anchor='center',
                             name='button'
                             )
text_1 = visual.TextStim(win=win, name='text_1',
                         text='1植物大战僵尸',
                         font='Open Sans',
                         pos=(-0.3, 0.28), height=0.04, wrapWidth=None, ori=0.0,
                         color='black', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-4.0)
button_1.buttonClock = core.Clock()
button_2_img = visual.ImageStim(
    win=win, image="./lib/button.png", pos=(0.3, 0.28), size=[0.4, 0.12], units='height', name='button2_img')
button_2 = visual.ButtonStim(win,
                             text='', font='Open Sans',
                             pos=(0.3, 0.28),
                             letterHeight=0.04,
                             size=[0.3, 0.1], borderWidth=1,
                             fillColor='deepskyblue', borderColor='white',
                             color='white', colorSpace='rgb',
                             opacity=None,
                             bold=True, italic=False,
                             padding=None,
                             anchor='center',
                             name='button_2'
                             )
text_2 = visual.TextStim(win=win, name='text_2',
                         text='2小熊的热气球',
                         font='Open Sans',
                         pos=(0.3, 0.28), height=0.04, wrapWidth=None, ori=0.0,
                         color='black', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-4.0)
button_2.buttonClock = core.Clock()
button_3_img = visual.ImageStim(
    win=win, image="./lib/button.png", pos=(-0.3, 0.13), size=[0.4, 0.12], units='height', name='button3_img')
button_3 = visual.ButtonStim(win,
                             text=u'', font='SimSun',
                             pos=(-0.3, 0.13),
                             letterHeight=0.04,
                             size=[0.3, 0.1], borderWidth=1,
                             fillColor='deepskyblue', borderColor='white',
                             color='white', colorSpace='rgb',
                             opacity=None,
                             bold=True, italic=False,
                             padding=None,
                             anchor='center',
                             name='button_3'
                             )
text_3 = visual.TextStim(win=win, name='text_3',
                         text='3海绵宝宝抓水母',
                         font='Open Sans',
                         pos=(-0.3, 0.13), height=0.04, wrapWidth=None, ori=0.0,
                         color='black', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-4.0)
button_3.buttonClock = core.Clock()
button_4_img = visual.ImageStim(
    win=win, image="./lib/button.png", pos=(0.3, 0.13), size=[0.4, 0.12], units='height', name='button4_img')
button_4 = visual.ButtonStim(win,
                             text='', font='Open Sans',
                             pos=(0.3, 0.13),
                             letterHeight=0.04,
                             size=[0.3, 0.1], borderWidth=1,
                             fillColor='darkorange', borderColor='white',
                             color='white', colorSpace='rgb',
                             opacity=None,
                             bold=True, italic=False,
                             padding=None,
                             anchor='center',
                             name='button_4'
                             )
text_4 = visual.TextStim(win=win, name='text_4',
                         text='4收豆子',
                         font='Open Sans',
                         pos=(0.3, 0.13), height=0.04, wrapWidth=None, ori=0.0,
                         color='black', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-4.0)
button_4.buttonClock = core.Clock()
button_5_img = visual.ImageStim(
    win=win, image="./lib/button.png", pos=(-0.3, -0.02), size=[0.4, 0.12], units='height', name='button5_img')
button_5 = visual.ButtonStim(win,
                             text='', font='Open Sans',
                             pos=(-0.3, -0.02),
                             letterHeight=0.04,
                             size=[0.3, 0.1], borderWidth=1,
                             fillColor='darkorange', borderColor='white',
                             color='white', colorSpace='rgb',
                             opacity=None,
                             bold=True, italic=False,
                             padding=None,
                             anchor='center',
                             name='button'
                             )
text_5 = visual.TextStim(win=win, name='text_5',
                         text='5跳远比赛',
                         font='Open Sans',
                         pos=(-0.3, -0.02), height=0.04, wrapWidth=None, ori=0.0,
                         color='black', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-4.0)
button_6_img = visual.ImageStim(
    win=win, image="./lib/button.png", pos=(0.3, -0.02), size=[0.4, 0.12], units='height', name='button6_img')
button_6 = visual.ButtonStim(win,
                             text='', font='Open Sans',
                             pos=(0.3, -0.02),
                             letterHeight=0.04,
                             size=[0.3, 0.1], borderWidth=1,
                             fillColor='darkorange', borderColor='white',
                             color='white', colorSpace='rgb',
                             opacity=None,
                             bold=True, italic=False,
                             padding=None,
                             anchor='center',
                             name='button'
                             )
text_6 = visual.TextStim(win=win, name='text_1',
                         text='6太空勘探',
                         font='Open Sans',
                         pos=(0.3, -0.02), height=0.04, wrapWidth=None, ori=0.0,
                         color='black', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-4.0)

title = visual.TextStim(win=win, name='text',
                        text='欢迎参与训练',
                        font='Open Sans',
                        pos=(0, 0.42), height=0.07, wrapWidth=None, ori=0.0,
                        color='black', colorSpace='rgb', opacity=None,
                        languageStyle='LTR',
                        depth=-4.0)
button_7_img = visual.ImageStim(win=win, image="./lib/button.png",
                                pos=(-0.3, -0.17), size=[0.4, 0.12], units='height', name='button7_img')
button_7 = visual.ButtonStim(win,
                             text='', font='Open Sans',
                             pos=(-0.3, -0.17),
                             letterHeight=0.04,
                             size=[0.3, 0.1], borderWidth=1,
                             fillColor='mediumspringgreen', borderColor='white',
                             color='white', colorSpace='rgb',
                             opacity=None,
                             bold=True, italic=False,
                             padding=None,
                             anchor='center',
                             name='button_7'
                             )
text_7 = visual.TextStim(win=win, name='text_7',
                         text='7寻宝记',
                         font='Open Sans',
                         pos=(-0.3, -0.17), height=0.04, wrapWidth=None, ori=0.0,
                         color='black', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-4.0)
button_8_img = visual.ImageStim(win=win, image="./lib/button.png",
                                pos=(0.3, -0.17), size=[0.4, 0.12], units='height', name='button8_img')
button_8 = visual.ButtonStim(win,
                             text='', font='Open Sans',
                             pos=(0.3, -0.17),
                             letterHeight=0.04,
                             size=[0.3, 0.1], borderWidth=1,
                             fillColor='mediumspringgreen', borderColor='white',
                             color='white', colorSpace='rgb',
                             opacity=None,
                             bold=True, italic=False,
                             padding=None,
                             anchor='center',
                             name='button_8'
                             )
text_8 = visual.TextStim(win=win, name='text_8',
                         text='8小猪佩奇的一天',
                         font='Open Sans',
                         pos=(0.3, -0.17), height=0.04, wrapWidth=None, ori=0.0,
                         color='black', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-4.0)
button_9_img = visual.ImageStim(win=win, image="./lib/button.png",
                                pos=(-0.3, -0.32), size=[0.4, 0.12], units='height', name='button9_img')
button_9 = visual.ButtonStim(win,
                             text='', font='Open Sans',
                             pos=(-0.3, -0.32),
                             letterHeight=0.04,
                             size=[0.3, 0.1], borderWidth=1,
                             fillColor='mediumspringgreen', borderColor='white',
                             color='white', colorSpace='rgb',
                             opacity=None,
                             bold=True, italic=False,
                             padding=None,
                             anchor='center',
                             name='button_9'
                             )
text_9 = visual.TextStim(win=win, name='text_9',
                         text='9破译密码',
                         font='Open Sans',
                         pos=(-0.3, -0.32), height=0.04, wrapWidth=None, ori=0.0,
                         color='black', colorSpace='rgb', opacity=None,
                         languageStyle='LTR',
                         depth=-4.0)
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
# to track time remaining of each (non-slip) routine
routineTimer = core.CountdownTimer()

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [background_img,
                   button_1, button_2, button_3,
                   button_4, button_5, button_6,
                   button_7, button_8, button_9, title,
                   text_1, text_2, text_3, text_4,
                   text_5, text_6, text_7, text_8, text_9,
                   button_1_img, button_2_img, button_3_img,
                   button_4_img, button_5_img, button_6_img,
                   button_7_img, button_8_img, button_9_img]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *button* updates
    if button_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_1.frameNStart = frameN  # exact frame index
        button_1.tStart = t  # local t and not account for scr refresh
        button_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_1, 'tStartRefresh')  # time at next scr refresh
        button_1.setAutoDraw(True)
    if button_1.status == STARTED:
        # check whether button has been pressed
        if button_1.isClicked:
            if not button_1.wasClicked:
                # store time of first click
                button_1.timesOn.append(button_1.buttonClock.getTime())
                # store time clicked until
                button_1.timesOff.append(button_1.buttonClock.getTime())
            else:
                # update time clicked until
                button_1.timesOff[-1] = button_1.buttonClock.getTime()
            if not button_1.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                os.system('start pythonw ./lib/1整合运算_v5/task1.py')
                None
            # if button is still clicked next frame, it is not a new click
            button_1.wasClicked = True
        else:
            button_1.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button_1.wasClicked = False  # if button is clicked next frame, it is a new click

    # *button_2* updates
    if button_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_2.frameNStart = frameN  # exact frame index
        button_2.tStart = t  # local t and not account for scr refresh
        button_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
        button_2.setAutoDraw(True)
    if button_2.status == STARTED:
        # check whether button_2 has been pressed
        if button_2.isClicked:
            if not button_2.wasClicked:
                # store time of first click
                button_2.timesOn.append(button_2.buttonClock.getTime())
                # store time clicked until
                button_2.timesOff.append(button_2.buttonClock.getTime())
            else:
                # update time clicked until
                button_2.timesOff[-1] = button_2.buttonClock.getTime()
            if not button_2.wasClicked:
                continueRoutine = False  # end routine when button_2 is clicked
                os.system('start pythonw ./lib/2规则转换/task2.py')
                None
            # if button_2 is still clicked next frame, it is not a new click
            button_2.wasClicked = True
        else:
            button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click
    else:
        button_2.wasClicked = False  # if button_2 is clicked next frame, it is a new click

    # *button_3* updates
    if button_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_3.frameNStart = frameN  # exact frame index
        button_3.tStart = t  # local t and not account for scr refresh
        button_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
        button_3.setAutoDraw(True)
    if button_3.status == STARTED:
        # check whether button_3 has been pressed
        if button_3.isClicked:
            if not button_3.wasClicked:
                # store time of first click
                button_3.timesOn.append(button_3.buttonClock.getTime())
                # store time clicked until
                button_3.timesOff.append(button_3.buttonClock.getTime())
            else:
                # update time clicked until
                button_3.timesOff[-1] = button_3.buttonClock.getTime()
            if not button_3.wasClicked:
                continueRoutine = False  # end routine when button_3 is clicked
                os.system('start pythonw ./lib/3stroop大小/task3.py')
                None
            # if button_3 is still clicked next frame, it is not a new click
            button_3.wasClicked = True
        else:
            button_3.wasClicked = False  # if button_3 is clicked next frame, it is a new click
    else:
        button_3.wasClicked = False  # if button_3 is clicked next frame, it is a new click

    # *button_4* updates
    if button_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_4.frameNStart = frameN  # exact frame index
        button_4.tStart = t  # local t and not account for scr refresh
        button_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_4, 'tStartRefresh')  # time at next scr refresh
        button_4.setAutoDraw(True)
    if button_4.status == STARTED:
        # check whether button_4 has been pressed
        if button_4.isClicked:
            if not button_4.wasClicked:
                # store time of first click
                button_4.timesOn.append(button_4.buttonClock.getTime())
                # store time clicked until
                button_4.timesOff.append(button_4.buttonClock.getTime())
            else:
                # update time clicked until
                button_4.timesOff[-1] = button_4.buttonClock.getTime()
            if not button_4.wasClicked:
                continueRoutine = False  # end routine when button_4 is clicked
                os.system('start pythonw ./lib/AA/dot.py')
                None
            # if button_4 is still clicked next frame, it is not a new click
            button_4.wasClicked = True
        else:
            button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click
    else:
        button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click

    # *button_5* updates
    if button_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_5.frameNStart = frameN  # exact frame index
        button_5.tStart = t  # local t and not account for scr refresh
        button_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_5, 'tStartRefresh')  # time at next scr refresh
        button_5.setAutoDraw(True)
    if button_5.status == STARTED:
        # check whether button_4 has been pressed
        if button_5.isClicked:
            if not button_5.wasClicked:
                # store time of first click
                button_5.timesOn.append(button_5.buttonClock.getTime())
                # store time clicked until
                button_5.timesOff.append(button_5.buttonClock.getTime())
            else:
                # update time clicked until
                button_5.timesOff[-1] = button_5.buttonClock.getTime()
            if not button_5.wasClicked:
                continueRoutine = False  # end routine when button_4 is clicked
                os.system('start pythonw ./lib/NL/numberline.py')
                None
            # if button_4 is still clicked next frame, it is not a new click
            button_5.wasClicked = True
        else:
            button_5.wasClicked = False  # if button_4 is clicked next frame, it is a new click
    else:
        button_5.wasClicked = False  # if button_4 is clicked next frame, it is a new click

    # *button_4* updates
    if button_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_6.frameNStart = frameN  # exact frame index
        button_6.tStart = t  # local t and not account for scr refresh
        button_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_4, 'tStartRefresh')  # time at next scr refresh
        button_6.setAutoDraw(True)
    if button_6.status == STARTED:
        # check whether button_4 has been pressed
        if button_6.isClicked:
            if not button_6.wasClicked:
                # store time of first click
                button_6.timesOn.append(button_6.buttonClock.getTime())
                # store time clicked until
                button_6.timesOff.append(button_6.buttonClock.getTime())
            else:
                # update time clicked until
                button_6.timesOff[-1] = button_6.buttonClock.getTime()
            if not button_6.wasClicked:
                continueRoutine = False  # end routine when button_4 is clicked
                os.system('start pythonw ./lib/NNG/NNG.py')
                None
            # if button_4 is still clicked next frame, it is not a new click
            button_6.wasClicked = True
        else:
            button_6.wasClicked = False  # if button_4 is clicked next frame, it is a new click
    else:
        button_6.wasClicked = False  # if button_4 is clicked next frame, it is a new click

    # *button_7* updates
    if button_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_7.frameNStart = frameN  # exact frame index
        button_7.tStart = t  # local t and not account for scr refresh
        button_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_7, 'tStartRefresh')  # time at next scr refresh
        button_7.setAutoDraw(True)
    if button_7.status == STARTED:
        # check whether button_7 has been pressed
        if button_7.isClicked:
            if not button_7.wasClicked:
                # store time of first click
                button_7.timesOn.append(button_7.buttonClock.getTime())
                # store time clicked until
                button_7.timesOff.append(button_7.buttonClock.getTime())
            else:
                # update time clicked until
                button_7.timesOff[-1] = button_7.buttonClock.getTime()
            if not button_7.wasClicked:
                continueRoutine = False  # end routine when button_4 is clicked
                os.system('start pythonw ./lib/number_space/number_space.py')
                None
            # if button_7 is still clicked next frame, it is not a new click
            button_7.wasClicked = True
        else:
            button_7.wasClicked = False  # if button_7 is clicked next frame, it is a new click
    else:
        button_7.wasClicked = False  # if button_7 is clicked next frame, it is a new click

    # *button_8* updates
    if button_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_8.frameNStart = frameN  # exact frame index
        button_8.tStart = t  # local t and not account for scr refresh
        button_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_8, 'tStartRefresh')  # time at next scr refresh
        button_8.setAutoDraw(True)
    if button_8.status == STARTED:
        # check whether button_8 has been pressed
        if button_8.isClicked:
            if not button_8.wasClicked:
                # store time of first click
                button_8.timesOn.append(button_8.buttonClock.getTime())
                # store time clicked until
                button_8.timesOff.append(button_8.buttonClock.getTime())
            else:
                # update time clicked until
                button_8.timesOff[-1] = button_8.buttonClock.getTime()
            if not button_8.wasClicked:
                continueRoutine = False  # end routine when button_8 is clicked
                os.system('start pythonw ./lib/Peppa/Peppa.py')
                None
            # if button_8 is still clicked next frame, it is not a new click
            button_8.wasClicked = True
        else:
            button_8.wasClicked = False  # if button_8 is clicked next frame, it is a new click
    else:
        button_8.wasClicked = False  # if button_8 is clicked next frame, it is a new click

    # *button_9* updates
    if button_9.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_9.frameNStart = frameN  # exact frame index
        button_9.tStart = t  # local t and not account for scr refresh
        button_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_9, 'tStartRefresh')  # time at next scr refresh
        button_9.setAutoDraw(True)
    if button_9.status == STARTED:
        # check whether button_9 has been pressed
        if button_9.isClicked:
            if not button_9.wasClicked:
                # store time of first click
                button_9.timesOn.append(button_9.buttonClock.getTime())
                # store time clicked until
                button_9.timesOff.append(button_9.buttonClock.getTime())
            else:
                # update time clicked until
                button_9.timesOff[-1] = button_9.buttonClock.getTime()
            if not button_9.wasClicked:
                continueRoutine = False  # end routine when button_4 is clicked
                os.system(
                    'start pythonw ./lib/reinforcement_learning/reinforcement_learning.py')
                None
            # if button_9 is still clicked next frame, it is not a new click
            button_9.wasClicked = True
        else:
            button_9.wasClicked = False  # if button_9 is clicked next frame, it is a new click
    else:
        button_9.wasClicked = False  # if button_9 is clicked next frame, it is a new click

    # *text* updates
    if title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        title.frameNStart = frameN  # exact frame index
        title.tStart = t  # local t and not account for scr refresh
        title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(title, 'tStartRefresh')  # time at next scr refresh
        background_img.setAutoDraw(True)
        title.setAutoDraw(True)
        button_1_img.setAutoDraw(True)
        text_1.setAutoDraw(True)
        button_2_img.setAutoDraw(True)
        text_2.setAutoDraw(True)
        button_3_img.setAutoDraw(True)
        text_3.setAutoDraw(True)
        button_4_img.setAutoDraw(True)
        text_4.setAutoDraw(True)
        button_5_img.setAutoDraw(True)
        text_5.setAutoDraw(True)
        button_6_img.setAutoDraw(True)
        text_6.setAutoDraw(True)
        button_7_img.setAutoDraw(True)
        text_7.setAutoDraw(True)
        button_8_img.setAutoDraw(True)
        text_8.setAutoDraw(True)
        button_9_img.setAutoDraw(True)
        text_9.setAutoDraw(True)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('button_1.started', button_1.tStartRefresh)
thisExp.addData('button_1.stopped', button_1.tStopRefresh)
thisExp.addData('button_1.numClicks', button_1.numClicks)
if button_1.numClicks:
    thisExp.addData('button_1.timesOn', button_1.timesOn)
    thisExp.addData('button_1.timesOff', button_1.timesOff)
else:
    thisExp.addData('button_1.timesOn', "")
    thisExp.addData('button_1.timesOff', "")
thisExp.addData('button_2.started', button_2.tStartRefresh)
thisExp.addData('button_2.stopped', button_2.tStopRefresh)
thisExp.addData('button_2.numClicks', button_2.numClicks)
if button_2.numClicks:
    thisExp.addData('button_2.timesOn', button_2.timesOn)
    thisExp.addData('button_2.timesOff', button_2.timesOff)
else:
    thisExp.addData('button_2.timesOn', "")
    thisExp.addData('button_2.timesOff', "")
thisExp.addData('button_3.started', button_3.tStartRefresh)
thisExp.addData('button_3.stopped', button_3.tStopRefresh)
thisExp.addData('button_3.numClicks', button_3.numClicks)
if button_3.numClicks:
    thisExp.addData('button_3.timesOn', button_3.timesOn)
    thisExp.addData('button_3.timesOff', button_3.timesOff)
else:
    thisExp.addData('button_3.timesOn', "")
    thisExp.addData('button_3.timesOff', "")
thisExp.addData('button_4.started', button_4.tStartRefresh)
thisExp.addData('button_4.stopped', button_4.tStopRefresh)
thisExp.addData('button_4.numClicks', button_4.numClicks)
if button_4.numClicks:
    thisExp.addData('button_4.timesOn', button_4.timesOn)
    thisExp.addData('button_4.timesOff', button_4.timesOff)
else:
    thisExp.addData('button_4.timesOn', "")
    thisExp.addData('button_4.timesOff', "")
thisExp.addData('button_5.started', button_5.tStartRefresh)
thisExp.addData('button_5.stopped', button_5.tStopRefresh)
thisExp.addData('button_5.numClicks', button_5.numClicks)
if button_5.numClicks:
    thisExp.addData('button.timesOn', button_5.timesOn)
    thisExp.addData('button.timesOff', button_5.timesOff)
else:
    thisExp.addData('button.timesOn', "")
    thisExp.addData('button.timesOff', "")
thisExp.addData('button_6.started', button_6.tStartRefresh)
thisExp.addData('button_6.stopped', button_6.tStopRefresh)
thisExp.addData('button_6.numClicks', button_6.numClicks)
if button_6.numClicks:
    thisExp.addData('button_6.timesOn', button_6.timesOn)
    thisExp.addData('button_6.timesOff', button_6.timesOff)
else:
    thisExp.addData('button_6.timesOn', "")
    thisExp.addData('button_6.timesOff', "")
thisExp.addData('button_7.started', button_7.tStartRefresh)
thisExp.addData('button_7.stopped', button_7.tStopRefresh)
thisExp.addData('button_7.numClicks', button_7.numClicks)
if button_1.numClicks:
    thisExp.addData('button_7.timesOn', button_7.timesOn)
    thisExp.addData('button_7.timesOff', button_7.timesOff)
else:
    thisExp.addData('button_7.timesOn', "")
    thisExp.addData('button_7.timesOff', "")
thisExp.addData('button_9.started', button_9.tStartRefresh)
thisExp.addData('button_9.stopped', button_9.tStopRefresh)
thisExp.addData('button_9.numClicks', button_9.numClicks)
if button_1.numClicks:
    thisExp.addData('button_9.timesOn', button_9.timesOn)
    thisExp.addData('button_9.timesOff', button_9.timesOff)
else:
    thisExp.addData('button_9.timesOn', "")
    thisExp.addData('button_9.timesOff', "")
thisExp.addData('button_8.started', button_8.tStartRefresh)
thisExp.addData('button_8.stopped', button_8.tStopRefresh)
thisExp.addData('button_8.numClicks', button_8.numClicks)
if button_1.numClicks:
    thisExp.addData('button_8.timesOn', button_8.timesOn)
    thisExp.addData('button_8.timesOff', button_8.timesOff)
else:
    thisExp.addData('button_8.timesOn', "")
    thisExp.addData('button_8.timesOff', "")
thisExp.addData('title.started', title.tStartRefresh)
thisExp.addData('title.stopped', title.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
