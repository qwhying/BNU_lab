#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 九月 20, 2021, at 14:26
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
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\BNU\\2021\\程序\\打包\\main_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 768], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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
trialClock = core.Clock()
button = visual.ButtonStim(win, 
    text='1', font='Arvo',
    pos=(-0.4, 0.3),
    letterHeight=0.05,
    size=[0.2,0.1], borderWidth=0.0,
    fillColor='deepskyblue', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button'
)
button.buttonClock = core.Clock()
button_2 = visual.ButtonStim(win, 
    text='2', font='Arvo',
    pos=(0.4, 0.3),
    letterHeight=0.05,
    size=[0.2,0.1], borderWidth=0.0,
    fillColor='deepskyblue', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_2'
)
button_2.buttonClock = core.Clock()
button_3 = visual.ButtonStim(win, 
    text='3', font='Arvo',
    pos=(-0.4, 0.15),
    letterHeight=0.05,
    size=[0.2,0.1], borderWidth=0.0,
    fillColor='deepskyblue', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_3'
)
button_3.buttonClock = core.Clock()
button_4 = visual.ButtonStim(win, 
    text='4', font='Arvo',
    pos=(0.4, 0.15),
    letterHeight=0.05,
    size=[0.2,0.1], borderWidth=0.0,
    fillColor='deepskyblue', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_4'
)
button_4.buttonClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='请选择任务',
    font='Open Sans',
    pos=(0, 0.4), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [button, button_2, button_3, button_4, text]
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
    if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
            else:
                button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = True  # if button is still clicked next frame, it is not a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button.wasClicked = False  # if button is clicked next frame, it is a new click
    
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
                button_2.timesOn.append(button_2.buttonClock.getTime()) # store time of first click
                button_2.timesOff.append(button_2.buttonClock.getTime()) # store time clicked until
            else:
                button_2.timesOff[-1] = button_2.buttonClock.getTime() # update time clicked until
            if not button_2.wasClicked:
                continueRoutine = False  # end routine when button_2 is clicked
                None
            button_2.wasClicked = True  # if button_2 is still clicked next frame, it is not a new click
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
                button_3.timesOn.append(button_3.buttonClock.getTime()) # store time of first click
                button_3.timesOff.append(button_3.buttonClock.getTime()) # store time clicked until
            else:
                button_3.timesOff[-1] = button_3.buttonClock.getTime() # update time clicked until
            if not button_3.wasClicked:
                continueRoutine = False  # end routine when button_3 is clicked
                None
            button_3.wasClicked = True  # if button_3 is still clicked next frame, it is not a new click
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
                button_4.timesOn.append(button_4.buttonClock.getTime()) # store time of first click
                button_4.timesOff.append(button_4.buttonClock.getTime()) # store time clicked until
            else:
                button_4.timesOff[-1] = button_4.buttonClock.getTime() # update time clicked until
            if not button_4.wasClicked:
                continueRoutine = False  # end routine when button_4 is clicked
                None
            button_4.wasClicked = True  # if button_4 is still clicked next frame, it is not a new click
        else:
            button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click
    else:
        button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
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
thisExp.addData('button.started', button.tStartRefresh)
thisExp.addData('button.stopped', button.tStopRefresh)
thisExp.addData('button.numClicks', button.numClicks)
if button.numClicks:
   thisExp.addData('button.timesOn', button.timesOn)
   thisExp.addData('button.timesOff', button.timesOff)
else:
   thisExp.addData('button.timesOn', "")
   thisExp.addData('button.timesOff', "")
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
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
