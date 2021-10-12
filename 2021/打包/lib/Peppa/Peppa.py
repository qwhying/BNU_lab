import random
import psychopy
from math import log2
import numpy as np
import os
import csv
from psychopy.hardware import keyboard
from psychopy import visual, event, core, gui, data
from pyglet.window import key
import datetime
import sys
import copy
import math
from math import ceil

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

def trials(difficult):
    information = ['','','','','']
    mouse = psychopy.event.Mouse()
    #问题列表
    questionlist1 = ['学校今天留了\n多少道题目？','佩奇上午做了\n多少道数学题？',
                        '佩奇下午做了\n多少道数学题？','佩奇有几道数\n学题没做完?']
    questionlist2 = ['学校今天留了\n多少道题目？','佩奇在学校做\n了多少道数学题？',
                        '佩奇在家里做了\n多少道数学题？','佩奇有几道数学\n题没做完?']
    #随机选择提什么问题
    Qnumbool = random.choice([True, False])
    Qnum = random.randint(0,3) 
    if difficult > 1 and difficult < 5 :
        Qnum = random.randint(0,2) 
    if Qnumbool == 1:
        question = questionlist1[Qnum]
    else:
        question = questionlist2[Qnum]
    information[0] = question
     #根据难度设置信息呈现参数   
    if difficult == 1:
        m = random.randint(10,100) #m为数字之和的大小取值
    if difficult == 2:
        m = random.randint(10,20)
    if difficult == 3:
        m = random.randint(21,50)
    if difficult == 4:
        m = random.randint(51,100)
    if difficult == 5:
        m = random.randint(10,20)
    if difficult == 6:
        m = random.randint(21,50)
    if difficult == 7:
        m = random.randint(51,100)

    #第一屏信息
    bool1 = 1
    if Qnum == 0:
        bool1 = 0
    if difficult == 1:
        bool1 = 1
    mstr = str(m)#学校留的作业数转为字符串
    background.image='pictures/Antelope.png'
    background.draw()
    text1_1 = '学校今天留了\n'+mstr+'道数学题'
    text1_2 = '学校今天留了一\n些数学题目'
    if bool1 == 1:
        text.text = text1_1
        information[1] = text1_1
    else:
        text.text = text1_2
        information[1] = text1_2
    text.pos=[-250,100]
    text.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:#刺激呈现时间内持续呈现
        Yaoyaxin = 1

    #第二屏呈现
    background.image='pictures/Peppa.png'
    m1 = random.randint(2,m-6)
    m1str =str(m1)
    bool2 = 1
    if Qnum == 1:
        bool2 = 0
    if difficult == 1:
        bool2 = 1
    text2_1 = '我今天上午在学校\n做了'+m1str+'道数学题' 
    text2_2 = '我今天在学校做\n了一些数学题'
    if bool2 == 1:
        text.text = text2_1
        information[2] = text2_1
    else:
        text.text = text2_2
        information[2] = text2_2
    text.pos=[-40,120]
    background.draw()
    text.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        Yaoyaxin = 1
    

    #第三屏
    background.image='pictures/Antelope.png'
    if difficult > 2 and difficult < 5:
        m2 = m-m1
    else:
        m2 = random.randint(2,m-m1-2)
    m2str = str(m2)
    bool3 = 1
    if Qnum == 2:
        bool3 = 0
    if difficult == 1:
        bool3 = 1
    text3_1 = '佩奇晚上在家里\n做了'+m2str+'道数学题' 
    text3_2 = '佩奇晚上在家里做了\n一些数学题'
    if bool3 == 1:
        text.text = text3_1
        information[3] = text3_1
    else:
        information[3] = text3_2
        text.text = text3_2
    text.pos=[-270,100]
    background.draw()
    text.draw()
    win.flip()
    
    #第四屏
    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        Yaoyaxin = 1
    background.image='pictures/Peppa.png'
    m3 = m - m1 -m2
    m3str = str(m3)
    bool4 = 1
    if Qnum == 3:
        bool4 = 0
    if difficult == 1:
        bool4 =1
    text4_1 = '我还有'+m3str+'道题\n没做完' 
    text4_2 = '我今天的数学作\n业没有做完'
    text4_3 = '我今天做完了数\n学作业'
    if bool4 == 1:
        text.text = text4_1
        information[4] = text4_1
    else:
        text.text = text4_2
        information[4] = text4_2
    if difficult > 1 and difficult < 5 :
        text.text = text4_3
        information[4] = text4_3
    text.pos=[-40,100]
    background.draw()
    text.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        Yaoyaxin = 1

    #第五屏
    background.image='pictures/Antelope.png'
    background.draw()
    text.text = question
    text.pos = [-270,100]
    text.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        Yaoyaxin = 1
        
    #答案选择页面
    AnswerArray = [mstr,m1str,m2str,m3str]#字符串格式备选答案
    AnswerArrayint = [m,m1,m2,m3]
    background.image='pictures/blank'
    background.draw()
    Answerbool2 = random.randint(0,3)#错误答案大小
    Answerbool3 = random.randint(0,3)
    while Answerbool2 == Answerbool3:
        Answerbool2 = random.randint(0,3)#错误答案大小
        Answerbool3 = random.randint(0,3)
    Answerlevel = [-2,-1,1,2]
    erranswer1 = AnswerArrayint[Qnum]+Answerlevel[Answerbool2]
    erranswer2 = AnswerArrayint[Qnum]+Answerlevel[Answerbool3]
    
    answer_button = [AnswerArrayint[Qnum],erranswer1,erranswer2]
    random.shuffle(answer_button)#将答案随机打乱
    button_answer1_text = str(answer_button[0])
    button_answer2_text = str(answer_button[1])
    button_answer3_text = str(answer_button[2])
    button_answer1 =  my_button(160, 80, button_answer1_text, [-350,0], textColor=[0, 0, 0], 
                                    textSize=80)
    button_answer1cover =  my_button(160, 80, button_answer1_text, [-350,0], textColor=[0, 0, 0], 
                                    textSize=80,fillColor=[250,240,230])
    button_answer2 =  my_button(160, 80, button_answer2_text, [0,0], textColor=[0, 0, 0], 
                                    textSize=80)
    button_answer2cover =  my_button(160, 80, button_answer2_text, [0,0], textColor=[0, 0, 0], 
                                    textSize=80,fillColor=[250,240,230])
    button_answer3 =  my_button(160, 80, button_answer3_text, [350,0], textColor=[0, 0, 0], 
                                    textSize=80)
    button_answer3cover =  my_button(160, 80, button_answer3_text, [350,0], textColor=[0, 0, 0], 
                                    textSize=80,fillColor=[250,240,230])
    button_next =  my_button(160, 80, '下一题', [0,-300], textColor=[0, 0, 0], 
                                    textSize=50,fillColor=[245,245,245])
    text.text = '请选择你的答案'
    text.heigh = 60
    text.pos = [0,300]
    text.draw()

    button_answer1.draw()
    button_answer2.draw()
    button_answer3.draw()
    button_next.draw()
    win.flip()
    clock.reset()
    clickornot = 0
    while 1 == 1 :
        if clickornot!=1:
            if mouse.isPressedIn(button_answer1.button):
                background.draw()
                text.draw()
                button_next.draw()
                button_answer1cover.draw()
                button_answer2.draw()
                button_answer3.draw()
                win.flip()
                if answer_button[0] == AnswerArrayint[Qnum]:
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
                if answer_button[1] == AnswerArrayint[Qnum]:
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
                if answer_button[2] == AnswerArrayint[Qnum]:
                    feedback = 1
                else:
                    feedback = 0
                time = clock.getTime()
                clickornot = 3
        if mouse.isPressedIn(button_next.button):
            if clickornot != 0:
                feedback = show_feedback(feedback)
                return feedback, time,information
            

def show_feedback(feedback):
    """显示反馈
    feedback=1为正确，显示笑脸
    feedback=0为错误，显示哭脸
    feedback=2为未选择，显示提示语
    函数返回正确为1错误或者未选择为0（用于正确率计算）"""
    if feedback == 1:
        text.text = ""
        feedback_picture = smilling_face
    elif feedback == 0:
        text.text = ""
        feedback_picture = crying_face
        feedback_picture.opacity = 1
    else:
        text.text = "你没有按键！"
        feedback_picture = crying_face
        feedback_picture.opacity = 0
        feedback = 0
    text.pos = [0, 0]
    clock.reset()
    while clock.getTime() < feedback_duration_s:
        background.draw()
        feedback_picture.draw()
        text.draw()
        win.flip()
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    return feedback




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
# from the Builder filename that created this script
expName = 'Peppa'
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
    size=[1350, 891],
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
    size=[250, 250]
)

crying_face = psychopy.visual.ImageStim(
    win=win,
    image="pictures/negative_.png",
    units="pix",
    size=[250, 250]
)


defaultKeyboard = keyboard.Keyboard()

pre_duration_s = 0.5  # 500ms的黑屏
stim_static_s = 1.0  # 1000ms的刺激呈现
stim_dynamict_s = 2.5  # 500ms刺激移动
interal_duration_s = 1.0  # 1000ms的幕间暂停
res_duration_s = 4  # 2500ms的反应时间
feedback_duration_s = 2.0  # 2000ms的反馈时间

trials_in_block = 45

clock = psychopy.core.Clock()

text = psychopy.visual.TextStim(
    win=win,
    units="pix",
    height=40,
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

difficulty = 1
accuracy = []
for i_trials in range(trials_in_block):
    
    if len(accuracy) > 4:
        if sum(accuracy)/len(accuracy) >= 0.8:
            del accuracy[:]
            if difficulty < 8:
                difficulty = difficulty +1

    
    feedback, time,information = trials(difficulty)
    accuracy.append(feedback)
        # 保存结果
    thisExp.addData('trial', i_trials+1)
    thisExp.addData('feedback', feedback)
    thisExp.addData('reaction time', time)
    thisExp.addData('difficulty',difficulty)
    thisExp.addData('question', information[0])
    thisExp.addData('screen1', information[1])
    thisExp.addData('screen2', information[2])
    thisExp.addData('screen3', information[3])
    thisExp.addData('screen4', information[4])
    thisExp.nextEntry()
    
    #thisExp.addData('log_difference', log_difference)
    #thisExp.addData('accuracy', corrects / 20)
    #thisExp.nextEntry()
thisExp.saveAsWideText(filename + '.csv', appendFile=True)
background.image = 'pictures/close.png'
background.draw()
win.flip()
psychopy.event.waitKeys()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
core.wait(2)
win.close()
