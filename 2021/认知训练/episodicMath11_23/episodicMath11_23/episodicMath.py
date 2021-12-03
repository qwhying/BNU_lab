import random
import xlrd
import psychopy.visual
import psychopy.event

from psychopy import core, gui, data
from math import log2
import numpy as np
import os
import csv
from psychopy.hardware import keyboard
import sys
import time

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
# from the Builder filename that created this script
expName = 'EpisodicMath'

expInfo = {'被试实验编号': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['participant'] = expInfo.pop("被试实验编号")
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + \
    u'data/%s_%s' % (expInfo['participant'], expName)
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=os.path.abspath(__file__),
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# 窗口
win = psychopy.visual.Window(
    units="pix",
    fullscr= False, # fullscr means full-screen mode
    size = [1920,1080]
)

background = psychopy.visual.ImageStim(
    win=win,
    image='depend/pictures/Direction.png',
    units='pix',
    size=win.size,
    opacity=0.8
)

pre_duration_s = 0.5  # 500ms的黑屏
stim_static_s = 1.0  # 1000ms的刺激呈现
stim_dynamict_s = 2.5  # 500ms刺激移动
interal_duration_s = 1.0  # 1000ms的幕间暂停
res_duration_s = 4  # 2500ms的反应时间
feedback_duration_s = 2.0  # 2000ms的反馈时间

trials_in_block = 30

clock = psychopy.core.Clock()



text = psychopy.visual.TextStim(
    win=win,
    units="pix",
    height=55,
    bold=True,
    font="STXINWEI",
    color='black',
    pos=(0, 0),
)

background.draw()
win.flip()

#读取配置excel文件
taskSerise = xlrd.open_workbook('depend/taskSerise.xlsx');
sht1 =  taskSerise.sheets()[0];
taskSerisePrice = xlrd.open_workbook('depend/taskSerisePrice.xlsx');
sht2 =  taskSerisePrice.sheets()[0];
quetionLocation = xlrd.open_workbook('depend/questionLocation.xlsx');
sht3 =  quetionLocation.sheets()[0];
price = xlrd.open_workbook('depend/price.xlsx');
sht4 =  price.sheets()[0];
psychopy.event.waitKeys()

def trials(i_trials,sht1,sht2,sht3,sht4):
    #提取当前trial信息


    row1 = sht1.row_values(i_trials)
    row2 = sht2.row_values(i_trials)
    row3 = sht3.row_values(i_trials)
    defaultKeyboard = keyboard.Keyboard()
    #fixation呈现
    background.image='depend/pictures/fixation.png'
    background.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < 1:#刺激呈现时间内持续呈现
        background.image='depend/pictures/饮料机10.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    #所有饮料呈现
    background.draw()
    path1 = 'depend/pictures/'+str(int(row1[0]))+'_'+str(int(row2[0]))+'.png'
    path2 = 'depend/pictures/'+str(int(row1[1]))+'_'+str(int(row2[1]))+'.png'
    path3 = 'depend/pictures/'+str(int(row1[2]))+'_'+str(int(row2[2]))+'.png'
#    path4 = 'depend/pictures/'+str(int(row1[3]))+'_'+str(int(row2[3]))+'.png'

    graph1 = psychopy.visual.ImageStim(
    win=win,
    image=path1,
    pos = [-168,182],
    units="pix",
    size=[157.5,225]
    )
    graph1.draw()
    graph2 = psychopy.visual.ImageStim(
    win=win,
    image=path2,
#    pos = [-78,182],
    pos = [-258,-65],
    units="pix",
    size=[157.5,225]
    )
    graph2.draw()
    graph3 = psychopy.visual.ImageStim(
    win=win,
    image=path3,
#    pos = [-258,-65],
    pos = [-78,-65],
    units="pix",
    size=[157.5,225]
    )
    graph3.draw()
#    graph4 = psychopy.visual.ImageStim(
#    win=win,
#    image=path4,
#    pos = [-78,-65],
#    units="pix",
#    size=[157.5,225]
#    )
#    graph4.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < 7:#刺激呈现时间内持续呈现
        background.image='depend/pictures/10饮料机.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    #问题cue
    questionsort = int(row3[2]) #1是情景Cue，0是空间Cue

    graphA = psychopy.visual.ImageStim(
    win=win,
    pos = [0,0],
    units="pix",
    size=[350,500]
    )
#    graphB = psychopy.visual.ImageStim(
#    win=win,
#    pos = [300,0],
#    units="pix",
#    size=[350,500]
#    )
    
    #情景Cue
    if questionsort == 1:
        background.image='depend/pictures/black.png'
        background.draw()
        picPathA = 'depend/pictures/'+str(int(row1[int(row3[0])-1]))+'.png'
#        picPathB = 'depend/pictures/'+str(int(row1[int(row3[1])-1]))+'.png'
        graphA.image = picPathA
#        graphB.image = picPathB
        graphA.draw()
#        graphB.draw()
        win.flip()
        clock.reset()
        while clock.getTime() < 3:#刺激呈现时间内持续呈现
            background.image='depend/pictures/black.png'
            if defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
    #空间Cue
    if questionsort == 0:
        background.image='depend/pictures/10饮料机.png'
        background.draw()
        graph1 = psychopy.visual.ImageStim(
        win=win,
        image='depend/pictures/white.png',
        pos = [-168,182],
        units="pix",
        size=[157.5,225]
        )
        graph1.draw()
        graph2 = psychopy.visual.ImageStim(
        win=win,
        image='depend/pictures/white.png',
        pos = [-258,-65],
        units="pix",
        size=[157.5,225]
        )
        graph2.draw()
        graph3 = psychopy.visual.ImageStim(
        win=win,
        image='depend/pictures/white.png',
        pos = [-78,-65],
        units="pix",
        size=[157.5,225]
        )
        graph3.draw()
#        graph4 = psychopy.visual.ImageStim(
#        win=win,
#        image='depend/pictures/white.png',
#        pos = [-78,-65],
#        units="pix",
#        size=[157.5,225]
#        )
#        graph4.draw()
        
        graphA.image = 'depend/pictures/star1.png'
        graphA.size = [94,102]
        if int(row3[0]) == 1:
            graphA.pos = [-168,182]
        if int(row3[0]) == 2:
            graphA.pos = [-258,-65]
        if int(row3[0]) == 3:
            graphA.pos = [-78,-65]
#        if int(row3[0]) == 4:
#            graphA.pos = [-78,-65]
        graphA.draw()
#        graphB.image = 'depend/pictures/star2.png'
#        graphB.size = [63,63]
#        if int(row3[1]) == 1:
#            graphB.pos = [-258,182]
#        if int(row3[1]) == 2:
#            graphB.pos = [-78,182]
#        if int(row3[1]) == 3:
#            graphB.pos = [-258,-65]
#        if int(row3[1]) == 4:
#            graphB.pos = [-78,-65]
#        graphB.draw()
        win.flip()
        clock.reset()
        while clock.getTime() < 3:#刺激呈现时间内持续呈现
            background.image='depend/pictures/black.png'
            if defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

    #问题呈现


    price1 = sht4.row_values(int(row1[int(row3[0])-1])-1)[int(row2[int(row3[0]-1)])]
#    price2 = sht4.row_values(int(row1[int(row3[1])-1])-1)[int(row2[int(row3[1]-1)])]

    
    text1 = psychopy.visual.TextStim(
    win=win,
    units="pix",
    height=55,
    bold=True,
    font="STXINWEI",
    color='white',
    pos=(-50, 300),
    )
    text2 = psychopy.visual.TextStim(
    win=win,
    units="pix",
    height=55,
    bold=True,
    font="STXINWEI",
    color='white',
    pos=(-300, -100),
    )
    text3 = psychopy.visual.TextStim(
    win=win,
    units="pix",
    height=55,
    bold=True,
    font="STXINWEI",
    color='white',
    pos=(300,-100),
    )
    text4 = psychopy.visual.TextStim(
    text = '*',
    win=win,
    units="pix",
    height=55,
    bold=True,
    font="STXINWEI",
    color='white',
    pos=(0,0),
    )
    if row3[3] == 0:
        text1.text = '买这瓶饮料找零多少钱'
        corranswer = 10-price1
        print(corranswer)
    if row3[3] == 1:
        text1.text = '买这瓶饮料需要多少钱'
        corranswer = price1
        print(corranswer)
    text2.text = str(int(row3[6]))+'元'
    text3.text = str(int(row3[7]))+'元'
    background.draw()
    text1.draw()
    text2.draw()
    text3.draw()
    win.flip()
    clock.reset()
    keyName = 9#初始化按键为9，表示被试没有按键
    time = 0#初始化反应时为0
    pressKey = 0
    kb = keyboard.Keyboard()
    kb.clearEvents(eventType='keyboard')
    while clock.getTime() < 4:#刺激呈现时间内持续呈现
        keys = kb.getKeys(keyList=["1","2"])
        if keys and pressKey == 0:
            background.draw()
            text1.draw()
            text2.draw()
            text3.draw()
            text4.draw()
            win.flip()
            time = clock.getTime()
            print(keys)
            keyName = keys[0].name
            pressKey = 1
            kb.stop()
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    if int(keyName) == int(row3[4]):
        accuracy = 1
    else:
        accuracy = 0
    return time,keyName,accuracy




# Ensure that relative paths start from the same directory as this script



for i_trials in range(trials_in_block):

    [time,keyName,accuracy] = trials(i_trials,sht1,sht2,sht3,sht4)
        # 保存结果
    thisExp.addData('trial', i_trials+1)
    thisExp.addData('pressKey', keyName)
    thisExp.addData('reaction time', time)
    thisExp.addData('accuracy',accuracy)
    thisExp.nextEntry()
thisExp.saveAsWideText(filename + '.csv', appendFile=True)
background.image = 'pictures/close.png'
background.draw()
win.flip()
psychopy.event.waitKeys()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
core.wait(2)
win.close()


