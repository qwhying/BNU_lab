import random

import psychopy.visual
import psychopy.event

from psychopy import core, gui, data
from math import log2
import numpy as np
import os
import csv
from psychopy.hardware import keyboard
import stat


class my_button():
    """生成按钮"""

    def __init__(self, length, height, text, pos=[0, 0], textColor=[0, 0, 0],
                 textSize=20, fillColor=None):
        self.text = generate_textMark(
            pos[0], pos[1], text, textSize, textColor)
        self.button = generate_button(
            length, height, pos, fillColor)

    def draw(self):
        self.button.draw()
        self.text.draw()


def generate_textMark(x, y, text, size=40,  color=[0, 0, 0]):
    """生成标识数字"""
    textMark = psychopy.visual.TextStim(
        win=win,
        text=text,
        color=color,
        colorSpace='rgb255',
        pos=(x, y),
        height=size,
        units="pix"
    )
    return textMark


def generate_button(length, height, pos=[0, 0], fillColor=[255, 255, 255]):
    acceptBoxleft = -length/2
    acceptBoxright = length/2
    acceptBoxtop = height/2
    acceptBoxbot = -height/2

    delta = 0.025 * 400
    delta2 = delta/7
    acceptBoxVertices = [
        [acceptBoxleft, acceptBoxtop - delta],
        [acceptBoxleft + delta2, acceptBoxtop - 3 * delta2],
        [acceptBoxleft + 3 * delta2, acceptBoxtop - delta2],
        [acceptBoxleft + delta, acceptBoxtop],
        [acceptBoxright - delta, acceptBoxtop],
        [acceptBoxright - 3 * delta2, acceptBoxtop - delta2],
        [acceptBoxright - delta2, acceptBoxtop - 3 * delta2],
        [acceptBoxright, acceptBoxtop - delta],
        [acceptBoxright, acceptBoxbot + delta],
        [acceptBoxright - delta2, acceptBoxbot + 3 * delta2],
        [acceptBoxright - 3 * delta2, acceptBoxbot + delta2],
        [acceptBoxright - delta, acceptBoxbot],
        [acceptBoxleft + delta, acceptBoxbot],
        [acceptBoxleft + 3 * delta2, acceptBoxbot + delta2],
        [acceptBoxleft + delta2, acceptBoxbot + 3 * delta2],
        [acceptBoxleft, acceptBoxbot + delta]]

    button = psychopy.visual.ShapeStim(
        win=win, vertices=acceptBoxVertices,
        fillColor=fillColor, lineColor=fillColor,
        fillColorSpace="rgb255", lineColorSpace="rgb255",
        pos=pos,
        autoLog=False)

    return button


def trials(pathlist):

    mouse = psychopy.event.Mouse()

    # fixation呈现
    background.image = 'pictures/fixation.png'
    background.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:  # 刺激呈现时间内持续呈现
        background.image = 'pictures/background.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
    # 图形呈现
    picturepath = ''
    while 1 == 1:
        #path1 = random.randint(3,6)
        path1 = random.randint(3, 6)
        path2 = random.randint(1, 3)
        path3 = random.randint(3, 6)
        path4 = random.randint(1, 3)
        path5 = random.randint(1, 2)
        picturepath = 'pictures/material_new/' + \
            str(path1)+'_'+str(path2)+'and'+str(path3) + \
            '_'+str(path4)+'and'+str(path5)
        if picturepath not in pathlist:
            pathlist.append(picturepath)
            break

    graph = psychopy.visual.ImageStim(
        win=win,
        image=picturepath,
        pos=[150, 0],
        units="pix",
        size=[250, 250]
    )
    boolanswer = random.randint(1, 10)
    if boolanswer <= 2:
        corranswer = path1+path3
    else:
        if path5 == 1:
            corranswer = path1+path3-2
        if path5 == 2:
            corranswer = path1+path3-1
    background.draw()
    graph.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        Yaoyaxin = 1
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()

    # 第三屏

    button_answer1 = my_button(80, 40, path1+path3, [-350, 0], textColor=[0, 0, 0],
                               textSize=40)
    button_answer1cover = my_button(80, 40, path1+path3, [-350, 0], textColor=[0, 0, 0],
                                    textSize=40, fillColor=[224, 220, 163])
    button_answer2 = my_button(80, 40, path1+path3-1, [0, 0], textColor=[0, 0, 0],
                               textSize=40)
    button_answer2cover = my_button(80, 40, path1+path3-1, [0, 0], textColor=[0, 0, 0],
                                    textSize=40, fillColor=[224, 220, 163])
    button_answer3 = my_button(80, 40, path1+path3-2, [350, 0], textColor=[0, 0, 0],
                               textSize=40)
    button_answer3cover = my_button(80, 40, path1+path3-2, [350, 0], textColor=[0, 0, 0],
                                    textSize=40, fillColor=[224, 220, 163])
    button_next = my_button(160, 80, '下一个', [0, -300], textColor=[0, 0, 0],
                            textSize=40, fillColor=[242, 202, 167])
    text.text = '请选择你破译的结果'
    text.pos = [0, 300]
    background.image = 'pictures/blank'
    background.draw()
    text.draw()

    button_answer1.draw()
    button_answer2.draw()
    button_answer3.draw()
    button_next.draw()
    win.flip()
    clock.reset()
    clickornot = 0
    feedback = 888
    while 1 == 1:
        if clickornot != 1:
            if mouse.isPressedIn(button_answer1.button):
                background.draw()
                text.draw()
                button_next.draw()
                button_answer1cover.draw()
                button_answer2.draw()
                button_answer3.draw()
                win.flip()
                if path1+path3 == corranswer:
                    feedback = 1
                else:
                    feedback = 0
                time = clock.getTime()
                clickornot = 1
        if clickornot != 2:
            if mouse.isPressedIn(button_answer2.button):
                background.draw()
                text.draw()
                button_next.draw()
                button_answer2cover.draw()
                button_answer1.draw()
                button_answer3.draw()
                win.flip()
                if path1+path3-1 == corranswer:
                    feedback = 1
                else:
                    feedback = 0
                time = clock.getTime()
                clickornot = 2
        if clickornot != 3:
            if mouse.isPressedIn(button_answer3.button):
                background.draw()
                text.draw()
                button_next.draw()
                button_answer3cover.draw()
                button_answer1.draw()
                button_answer2.draw()
                win.flip()
                if path1+path3-2 == corranswer:
                    feedback = 1
                else:
                    feedback = 0
                time = clock.getTime()
                clickornot = 3
        if mouse.isPressedIn(button_next.button):
            if feedback != 888:
                return feedback, time, picturepath, pathlist
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()


def trials_easy(pathlist):
    mouse = psychopy.event.Mouse()

    # fixation呈现
    background.image = 'pictures/fixation.png'
    background.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:  # 刺激呈现时间内持续呈现
        background.image = 'pictures/background.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
    # 图形呈现
    picturepath = ''
    while 1 == 1:
        #path1 = random.randint(3,6)
        path1 = random.randint(3, 6)
        path2 = random.randint(1, 3)
        path3 = random.randint(3, 6)
        path4 = random.randint(1, 3)
        path5 = random.randint(1, 2)
        picturepath = 'pictures/material_new/' + \
            str(path1)+'_'+str(path2)+'and'+str(path3) + \
            '_'+str(path4)+'and'+str(path5)
        if picturepath not in pathlist:
            pathlist.append(picturepath)
            break
    graph = psychopy.visual.ImageStim(
        win=win,
        image=picturepath,
        pos=[150, 0],
        units="pix",
        size=[250, 250]
    )
    boolanswer = random.randint(1, 10)
    print(boolanswer)
    if boolanswer <= 2:
        if path5 == 1:
            corranswer = path1+path3-2
        if path5 == 2:
            corranswer = path1+path3-1
    else:
        if path5 == 1:
            corranswer = path1+path3-1
        if path5 == 2:
            corranswer = path1+path3-2
    background.draw()
    graph.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        Yaoyaxin = 1
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()

    # 第三屏

    button_answer2 = my_button(80, 40, path1+path3-1, [-200, 0], textColor=[0, 0, 0],
                               textSize=40)
    button_answer2cover = my_button(80, 40, path1+path3-1, [-200, 0], textColor=[0, 0, 0],
                                    textSize=40, fillColor=[224, 220, 163])
    button_answer3 = my_button(80, 40, path1+path3-2, [200, 0], textColor=[0, 0, 0],
                               textSize=40)
    button_answer3cover = my_button(80, 40, path1+path3-2, [200, 0], textColor=[0, 0, 0],
                                    textSize=40, fillColor=[224, 220, 163])
    button_next = my_button(160, 80, '下一个', [0, -300], textColor=[0, 0, 0],
                            textSize=40, fillColor=[242, 202, 167])
    text.text = '请选择你破译的结果'
    text.pos = [0, 300]
    background.image = 'pictures/blank'
    background.draw()
    text.draw()

    button_answer2.draw()
    button_answer3.draw()
    button_next.draw()
    win.flip()
    clock.reset()
    clickornot = 0
    feedback = 888
    while 1 == 1:
        if clickornot != 2:
            if mouse.isPressedIn(button_answer2.button):
                background.draw()
                text.draw()
                button_next.draw()
                button_answer2cover.draw()
                button_answer3.draw()
                win.flip()
                if path1+path3-1 == corranswer:
                    feedback = 1
                else:
                    feedback = 0
                time = clock.getTime()
                clickornot = 2
        if clickornot != 3:
            if mouse.isPressedIn(button_answer3.button):
                background.draw()
                text.draw()
                button_next.draw()
                button_answer3cover.draw()
                button_answer2.draw()
                win.flip()
                if path1+path3-2 == corranswer:
                    feedback = 1
                else:
                    feedback = 0
                time = clock.getTime()
                clickornot = 3
        if mouse.isPressedIn(button_next.button):
            if feedback != 888:
                return feedback, time, picturepath, pathlist
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()


def show_feedback(feedback, scores):
    """显示反馈
    feedback=1为正确，显示笑脸
    feedback=0为错误，显示哭脸
    feedback=2为未选择，显示提示语
    函数返回正确为1错误或者未选择为0（用于正确率计算）"""
    if feedback == 1:
        text.text = "破译成功！\n地球文明又前进了一步\n+1分\n总分："+str(scores)
        feedback_picture = smilling_face
    elif feedback == 0:
        text.text = "破译失败！\n-1分\n总分："+str(scores)
        feedback_picture = crying_face
    else:
        text.text = "你没有按键！"
        feedback_picture = crying_face
        feedback_picture.opacity = 0
        feedback = 0
    text.pos = [0, 200]
    text.heigh = 15
    0
    clock.reset()
    while clock.getTime() < feedback_duration_s:
        background.draw()
        feedback_picture.draw()
        text.draw()
        win.flip()
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
    return feedback


def save_and_quit():
    """保存后退出"""
    os.chmod(filename + '.csv', stat.S_IWRITE)  # 权限改为读写
    thisExp.saveAsWideText(filename + '.csv', appendFile=True)
    os.chmod(filename + '.csv', stat.S_IREAD)  # 权限改为只读
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    core.quit()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
# from the Builder filename that created this script
expName = 'task9'
expInfo = {'被试实验编号': '', '姓名拼音': '', '第几次训练': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['participant'] = expInfo.pop("被试实验编号")
expInfo['name'] = expInfo.pop("姓名拼音")
expInfo['session'] = expInfo.pop("第几次训练")
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = os.path.dirname(os.path.dirname(_thisDir)) + os.sep + \
    u'data/%s_%s' % (expInfo['participant'], expName)
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=os.path.abspath(__file__),
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# 窗口
win = psychopy.visual.Window(
    size=[1360, 759],
    units="pix",
    fullscr=False,         # fullscr means full-screen mode
)
# # store frame rate of monitor if we can measure it
# expInfo['frameRate'] = win.getActualFrameRate()
# if expInfo['frameRate'] != None:
#     frameDur = 1.0 / round(expInfo['frameRate'])
# else:
#     frameDur = 1.0 / 60.0  # could not measure, so guess
background = psychopy.visual.ImageStim(
    win=win,
    image='pictures/background-图片透明度降低20%.png',
    units='pix',
    size=win.size,
    opacity=0.8
)

smilling_face = psychopy.visual.ImageStim(
    win=win,
    image="pictures/positive_.png",
    units="pix",
    size=[250, 250],
    pos=[0, -100]
)

crying_face = psychopy.visual.ImageStim(
    win=win,
    image="pictures/negative_.png",
    units="pix",
    size=[250, 250],
    pos=[0, -100]
)


defaultKeyboard = keyboard.Keyboard()

pre_duration_s = 0.5  # 500ms的黑屏
stim_static_s = 1.0  # 1000ms的刺激呈现
stim_dynamict_s = 2.5  # 500ms刺激移动
interal_duration_s = 1.0  # 1000ms的幕间暂停
res_duration_s = 4  # 2500ms的反应时间
feedback_duration_s = 2.0  # 2000ms的反馈时间

trials_in_block = 90

clock = psychopy.core.Clock()

text = psychopy.visual.TextStim(
    win=win,
    units="pix",
    height=55,
    bold=True,
    font="STXINWEI",
    color='black',
    pos=(0, 0),
    # wrapWidth=None, ori=0,
    # color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',
    # depth=0.0, font='Arial'
)

background.draw()
win.flip()
psychopy.event.waitKeys()
scores = 20
pathlist = []
for i_trials in range(trials_in_block):
    if i_trials < 25:
        feedback, time, picturepath, pathlist = trials_easy(pathlist)
    else:
        feedback, time, picturepath, pathlist = trials(pathlist)
    pathlist = pathlist
    if feedback == 1:
        scores = scores + 1
    else:
        scores = scores - 1
    feedback = show_feedback(feedback, scores)
    # 保存结果
    thisExp.addData('trial', i_trials+1)
    thisExp.addData('feedback', feedback)
    thisExp.addData('reaction time', time)
    thisExp.addData('picture', picturepath)
    thisExp.nextEntry()

    #thisExp.addData('log_difference', log_difference)
    #thisExp.addData('accuracy', corrects / 20)
    # thisExp.nextEntry()
save_and_quit()
background.image = 'pictures/close.png'
background.draw()
win.flip()
psychopy.event.waitKeys()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
core.wait(2)
win.close()
