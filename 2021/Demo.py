#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.1),
    on 八月 12, 2021, at 16:13
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
psychopyVersion = '2021.2.1'
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
                                 originPath='D:\\程序设计\\2021\\Demo.py',
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
    size=[1536, 864], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
Fixation1 = visual.ImageStim(
    win=win,
    name='Fixation1',
    image='Task samples/Fixation.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Trial1 = visual.ImageStim(
    win=win,
    name='Trial1',
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
Fixation2 = visual.ImageStim(
    win=win,
    name='Fixation2',
    image='Task samples/Fixation.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Trial2 = visual.ImageStim(
    win=win,
    name='Trial2',
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.7),
    color=[1, 1, 1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

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
trials = data.TrialHandler(nReps=1.0, method='random',
                           extraInfo=expInfo, originPath=-1,
                           trialList=data.importConditions(
                               'task_conditions.xlsx', selection='1:30'),
                           seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
# so we can initialise stimuli with some values
thisTrial = trials.trialList[0]
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    Trial1.setImage(images)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trial1Components = [Fixation1, Trial1, key_resp]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
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

        # *Trial1* updates
        if Trial1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            Trial1.frameNStart = frameN  # exact frame index
            Trial1.tStart = t  # local t and not account for scr refresh
            Trial1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial1, 'tStartRefresh')  # time at next scr refresh
            Trial1.setAutoDraw(True)
        if Trial1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial1.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                Trial1.tStop = t  # not accounting for scr refresh
                Trial1.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(Trial1, 'tStopRefresh')
                Trial1.setAutoDraw(False)

        # *key_resp* updates
        if key_resp.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(key_resp, 'tStartRefresh')
            key_resp.status = STARTED
            # keyboard checking is just starting
            key_resp.clock.reset()  # now t=0
            key_resp.clearEvents(eventType='keyboard')
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(key_resp, 'tStopRefresh')
                key_resp.status = FINISHED
        if key_resp.status == STARTED:
            theseKeys = key_resp.getKeys(keyList=['1', '2'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                # just the last key pressed
                key_resp.keys = _key_resp_allKeys[-1].name
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(correctAns)) or (key_resp.keys == correctAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Fixation1.started', Fixation1.tStartRefresh)
    trials.addData('Fixation1.stopped', Fixation1.tStopRefresh)
    trials.addData('Trial1.started', Trial1.tStartRefresh)
    trials.addData('Trial1.stopped', Trial1.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
            key_resp.corr = 1  # correct non-response
        else:
            key_resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys', key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStart)
    trials.addData('key_resp.stopped', key_resp.tStop)
    thisExp.nextEntry()

# completed 1.0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions(
                                 'task_conditions.xlsx', selection='31:60'),
                             seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
# so we can initialise stimuli with some values
thisTrial_2 = trials_2.trialList[0]
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial2"-------
    continueRoutine = True
    routineTimer.add(9.000000)
    # update component parameters for each repeat
    Trial2.setImage(images)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    trial2Components = [Fixation2, Trial2, key_resp_2]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
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

        # *Trial2* updates
        if Trial2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            Trial2.frameNStart = frameN  # exact frame index
            Trial2.tStart = t  # local t and not account for scr refresh
            Trial2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial2, 'tStartRefresh')  # time at next scr refresh
            Trial2.setAutoDraw(True)
        if Trial2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial2.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                Trial2.tStop = t  # not accounting for scr refresh
                Trial2.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(Trial2, 'tStopRefresh')
                Trial2.setAutoDraw(False)

        # *key_resp_2* updates
        if key_resp_2.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(key_resp_2, 'tStartRefresh')
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            key_resp_2.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                # time at next scr refresh
                win.timeOnFlip(key_resp_2, 'tStopRefresh')
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED:
            theseKeys = key_resp_2.getKeys(
                keyList=['1', '2'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                # just the last key pressed
                key_resp_2.keys = _key_resp_2_allKeys[-1].name
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # was this correct?
                if (key_resp_2.keys == str(correctAns)) or (key_resp_2.keys == correctAns):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('Fixation2.started', Fixation2.tStartRefresh)
    trials_2.addData('Fixation2.stopped', Fixation2.tStopRefresh)
    trials_2.addData('Trial2.started', Trial2.tStartRefresh)
    trials_2.addData('Trial2.stopped', Trial2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
            key_resp_2.corr = 1  # correct non-response
        else:
            key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_2.keys', key_resp_2.keys)
    trials_2.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    trials_2.addData('key_resp_2.started', key_resp_2.tStart)
    trials_2.addData('key_resp_2.stopped', key_resp_2.tStop)
    thisExp.nextEntry()

# completed 1.0 repeats of 'trials_2'


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
