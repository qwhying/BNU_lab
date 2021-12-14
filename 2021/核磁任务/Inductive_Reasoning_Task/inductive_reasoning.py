#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on 十一月 29, 2021, at 10:24
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
expName = 'Demo'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + \
    u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='D:\\程序设计\\BNU_lab\\BNU_lab\\2021\\认知训练\\Inductive_Reasoning_Task\\inductive_reasoning.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
# this outputs to the screen, not a file
logging.console.setLevel(logging.WARNING)

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1200, 500], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
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

# Initialize components for Routine "cue"
cueClock = core.Clock()
Cue = visual.ImageStim(
    win=win,
    name='Cue',
    image='Task samples/cue.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
instructions = visual.TextStim(win=win, name='instructions',
                               text='请你通过上方呈现的三个图像中\n找出规则，并在下图的两组图像\n（每组分别有三个图像）中\n选择正确呈现该规则的一组图像\n选择左侧按”1“，右侧按”2“',
                               font='Open Sans',
                               pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0,
                               color='white', colorSpace='rgb', opacity=None,
                               languageStyle='LTR',
                               depth=-1.0)

# Initialize components for Routine "graphic_trial"
graphic_trialClock = core.Clock()
Fixation1 = visual.ImageStim(
    win=win,
    name='Fixation1',
    image='Task samples/Fixation.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Feedback1 = visual.ImageStim(
    win=win,
    name='Fixation1',
    image='Task samples/Fixation.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
graphic_img = visual.ImageStim(
    win=win,
    name='graphic_img',
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
graphic_key_resp = keyboard.Keyboard()

# Initialize components for Routine "number_trial"
number_trialClock = core.Clock()
Fixation2 = visual.ImageStim(
    win=win,
    name='Fixation2',
    image='Task samples/Fixation.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
number_img = visual.ImageStim(
    win=win,
    name='number_img',
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
number_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
# to track time remaining of each (non-slip) routine
routineTimer = core.CountdownTimer()

# ------Prepare to start Routine "cue"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
cueComponents = [Cue, instructions]
for thisComponent in cueComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "cue"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cueClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=cueClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Cue* updates
    if Cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Cue.frameNStart = frameN  # exact frame index
        Cue.tStart = t  # local t and not account for scr refresh
        Cue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cue, 'tStartRefresh')  # time at next scr refresh
        Cue.setAutoDraw(True)
    if Cue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Cue.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Cue.tStop = t  # not accounting for scr refresh
            Cue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cue, 'tStopRefresh')  # time at next scr refresh
            Cue.setAutoDraw(False)

    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        # time at next scr refresh
        win.timeOnFlip(instructions, 'tStartRefresh')
        instructions.setAutoDraw(True)
    if instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instructions.tStop = t  # not accounting for scr refresh
            instructions.frameNStop = frameN  # exact frame index
            # time at next scr refresh
            win.timeOnFlip(instructions, 'tStopRefresh')
            instructions.setAutoDraw(False)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "cue"-------
for thisComponent in cueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
graphic_trials = data.TrialHandler(nReps=1.0, method='random',
                                   extraInfo=expInfo, originPath=-1,
                                   trialList=data.importConditions(
                                       'task_conditions.xlsx', selection='1:30'),
                                   seed=None, name='graphic_trials')
thisExp.addLoop(graphic_trials)  # add the loop to the experiment
# so we can initialise stimuli with some values
thisGraphic_trial = graphic_trials.trialList[0]
# abbreviate parameter names if possible (e.g. rgb = thisGraphic_trial.rgb)
if thisGraphic_trial != None:
    for paramName in thisGraphic_trial:
        exec('{} = thisGraphic_trial[paramName]'.format(paramName))

for thisGraphic_trial in graphic_trials:
    currentLoop = graphic_trials
    # abbreviate parameter names if possible (e.g. rgb = thisGraphic_trial.rgb)
    if thisGraphic_trial != None:
        for paramName in thisGraphic_trial:
            exec('{} = thisGraphic_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "graphic_trial"-------
    continueRoutine = True
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    graphic_img.setImage(images)
    graphic_key_resp.keys = []
    graphic_key_resp.rt = []
    _graphic_key_resp_allKeys = []
    # keep track of which components have finished
    graphic_trialComponents = [Fixation1, graphic_img, graphic_key_resp]
    for thisComponent in graphic_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    # t0 is time of first possible flip
    graphic_trialClock.reset(-_timeToFirstFrame)
    frameN = -1

    # -------Run Routine "graphic_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = graphic_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=graphic_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *Fixation1* updates
        if Fixation1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation1.frameNStart = frameN  # exact frame index
            Fixation1.tStart = t  # local t and not account for scr refresh
            Fixation1.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(Fixation1, 'tStartRefresh')
            Fixation1.setAutoDraw(True)
        if Fixation1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                Fixation1.tStop = t  # not accounting for scr refresh
                Fixation1.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(Fixation1, 'tStopRefresh')
                Fixation1.setAutoDraw(False)

        # *graphic_img* updates
        if graphic_img.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            graphic_img.frameNStart = frameN  # exact frame index
            graphic_img.tStart = t  # local t and not account for scr refresh
            graphic_img.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(graphic_img, 'tStartRefresh')
            graphic_img.setAutoDraw(True)
        if graphic_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > graphic_img.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                graphic_img.tStop = t  # not accounting for scr refresh
                graphic_img.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(graphic_img, 'tStopRefresh')
                graphic_img.setAutoDraw(False)

        # *graphic_key_resp* updates
        if graphic_key_resp.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            graphic_key_resp.frameNStart = frameN  # exact frame index
            graphic_key_resp.tStart = t  # local t and not account for scr refresh
            graphic_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(graphic_key_resp, 'tStartRefresh')
            graphic_key_resp.status = STARTED
            # keyboard checking is just starting
            graphic_key_resp.clock.reset()  # now t=0
            graphic_key_resp.clearEvents(eventType='keyboard')
        if graphic_key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > graphic_key_resp.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                graphic_key_resp.tStop = t  # not accounting for scr refresh
                graphic_key_resp.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(graphic_key_resp, 'tStopRefresh')
                graphic_key_resp.status = FINISHED
        if graphic_key_resp.status == STARTED:
            theseKeys = graphic_key_resp.getKeys(
                keyList=['1', '2'], waitRelease=False)
            _graphic_key_resp_allKeys.extend(theseKeys)
            if len(_graphic_key_resp_allKeys):
                # just the last key pressed
                graphic_key_resp.keys = _graphic_key_resp_allKeys[-1].name
                graphic_key_resp.rt = _graphic_key_resp_allKeys[-1].rt
                # add screen feedback
                graphic_key_resp.tStop = t
                graphic_key_resp.frameNStop = frameN  # exact frame index
                graphic_key_resp.status = FINISHED
                if t < graphic_key_resp.tStart+graphic_key_resp.rt+0.3:
                    Fixation1.draw()
                # was this correct?
                if (graphic_key_resp.keys == str(correctAns)) or (graphic_key_resp.keys == correctAns):
                    graphic_key_resp.corr = 1
                else:
                    graphic_key_resp.corr = 0

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in graphic_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "graphic_trial"-------
    for thisComponent in graphic_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    graphic_trials.addData('Fixation1.started', Fixation1.tStartRefresh)
    graphic_trials.addData('Fixation1.stopped', Fixation1.tStopRefresh)
    graphic_trials.addData('graphic_img.started', graphic_img.tStartRefresh)
    graphic_trials.addData('graphic_img.stopped', graphic_img.tStopRefresh)
    # check responses
    if graphic_key_resp.keys in ['', [], None]:  # No response was made
        graphic_key_resp.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
            graphic_key_resp.corr = 1  # correct non-response
        else:
            graphic_key_resp.corr = 0  # failed to respond (incorrectly)
    # store data for graphic_trials (TrialHandler)
    graphic_trials.addData('graphic_key_resp.keys', graphic_key_resp.keys)
    graphic_trials.addData('graphic_key_resp.corr', graphic_key_resp.corr)
    if graphic_key_resp.keys != None:  # we had a response
        graphic_trials.addData('graphic_key_resp.rt', graphic_key_resp.rt)
    graphic_trials.addData('graphic_key_resp.started', graphic_key_resp.tStart)
    graphic_trials.addData('graphic_key_resp.stopped', graphic_key_resp.tStop)
    thisExp.nextEntry()

# completed 1.0 repeats of 'graphic_trials'


# set up handler to look after randomisation of conditions etc
number_trials = data.TrialHandler(nReps=1.0, method='random',
                                  extraInfo=expInfo, originPath=-1,
                                  trialList=data.importConditions(
                                      'task_conditions.xlsx', selection='31:60'),
                                  seed=None, name='number_trials')
thisExp.addLoop(number_trials)  # add the loop to the experiment
# so we can initialise stimuli with some values
thisNumber_trial = number_trials.trialList[0]
# abbreviate parameter names if possible (e.g. rgb = thisNumber_trial.rgb)
if thisNumber_trial != None:
    for paramName in thisNumber_trial:
        exec('{} = thisNumber_trial[paramName]'.format(paramName))

for thisNumber_trial in number_trials:
    currentLoop = number_trials
    # abbreviate parameter names if possible (e.g. rgb = thisNumber_trial.rgb)
    if thisNumber_trial != None:
        for paramName in thisNumber_trial:
            exec('{} = thisNumber_trial[paramName]'.format(paramName))

    # ------Prepare to start Routine "number_trial"-------
    continueRoutine = True
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    number_img.setImage(images)
    number_key_resp.keys = []
    number_key_resp.rt = []
    _number_key_resp_allKeys = []
    # keep track of which components have finished
    number_trialComponents = [Fixation2, number_img, number_key_resp]
    for thisComponent in number_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    # t0 is time of first possible flip
    number_trialClock.reset(-_timeToFirstFrame)
    frameN = -1

    # -------Run Routine "number_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = number_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=number_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *Fixation2* updates
        if Fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation2.frameNStart = frameN  # exact frame index
            Fixation2.tStart = t  # local t and not account for scr refresh
            Fixation2.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(Fixation2, 'tStartRefresh')
            Fixation2.setAutoDraw(True)
        if Fixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                Fixation2.tStop = t  # not accounting for scr refresh
                Fixation2.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(Fixation2, 'tStopRefresh')
                Fixation2.setAutoDraw(False)

        # *number_img* updates
        if number_img.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            number_img.frameNStart = frameN  # exact frame index
            number_img.tStart = t  # local t and not account for scr refresh
            number_img.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(number_img, 'tStartRefresh')
            number_img.setAutoDraw(True)
        if number_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > number_img.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                number_img.tStop = t  # not accounting for scr refresh
                number_img.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(number_img, 'tStopRefresh')
                number_img.setAutoDraw(False)

        # *number_key_resp* updates
        if number_key_resp.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            number_key_resp.frameNStart = frameN  # exact frame index
            number_key_resp.tStart = t  # local t and not account for scr refresh
            number_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(number_key_resp, 'tStartRefresh')
            number_key_resp.status = STARTED
            # keyboard checking is just starting
            number_key_resp.clock.reset()  # now t=0
            number_key_resp.clearEvents(eventType='keyboard')
        if number_key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > number_key_resp.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                number_key_resp.tStop = t  # not accounting for scr refresh
                number_key_resp.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(number_key_resp, 'tStopRefresh')
                number_key_resp.status = FINISHED
        if number_key_resp.status == STARTED:
            theseKeys = number_key_resp.getKeys(
                keyList=['1', '2'], waitRelease=False)
            _number_key_resp_allKeys.extend(theseKeys)
            if len(_number_key_resp_allKeys):
                # just the last key pressed
                number_key_resp.keys = _number_key_resp_allKeys[-1].name
                number_key_resp.rt = _number_key_resp_allKeys[-1].rt
                number_key_resp.tStop = t
                number_key_resp.frameNStop = frameN  # exact frame index
                number_key_resp.status = FINISHED
                if t < number_key_resp.tStart+number_key_resp.rt+0.3:
                    Fixation2.draw()
                # was this correct?
                if (number_key_resp.keys == str(correctAns)) or (number_key_resp.keys == correctAns):
                    number_key_resp.corr = 1
                else:
                    number_key_resp.corr = 0

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in number_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "number_trial"-------
    for thisComponent in number_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    number_trials.addData('Fixation2.started', Fixation2.tStartRefresh)
    number_trials.addData('Fixation2.stopped', Fixation2.tStopRefresh)
    number_trials.addData('number_img.started', number_img.tStartRefresh)
    number_trials.addData('number_img.stopped', number_img.tStopRefresh)
    # check responses
    if number_key_resp.keys in ['', [], None]:  # No response was made
        number_key_resp.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
            number_key_resp.corr = 1  # correct non-response
        else:
            number_key_resp.corr = 0  # failed to respond (incorrectly)
    # store data for number_trials (TrialHandler)
    number_trials.addData('number_key_resp.keys', number_key_resp.keys)
    number_trials.addData('number_key_resp.corr', number_key_resp.corr)
    if number_key_resp.keys != None:  # we had a response
        number_trials.addData('number_key_resp.rt', number_key_resp.rt)
    number_trials.addData('number_key_resp.started', number_key_resp.tStart)
    number_trials.addData('number_key_resp.stopped', number_key_resp.tStop)
    thisExp.nextEntry()

# completed 1.0 repeats of 'number_trials'


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
