import random

import psychopy.visual
import psychopy.event

from psychopy import core, gui, data
from math import log2
import numpy as np
import os
import csv
from psychopy.hardware import keyboard


class my_button():
    """生成按钮"""

    def __init__(self, length, height, text, pos=[0, 0], textColor=[0, 0, 0], 
                        textSize=20, fillColor=[0,0,0]):
        self.text = generate_textMark(
            pos[0], pos[1], text, textSize, textColor)
        self.button = generate_button(
            length, height, pos, fillColor)
    def draw(self):
        self.button.draw()
        self.text.draw()
        
def generate_textMark(x, y, text, size=40,  color=[255,255,255]):
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

def generate_button(length, height, pos=[0, 0], fillColor=[0,0,0]):
    button = psychopy.visual.ImageStim(
        win=win,
        image="pictures/tree.png",
        pos = pos,
        size=[length, height])

    return button

def four_trials(difficulty):
    level = difficulty
    answerarray = []#备选答案数组
    selectanswer = []#被试已经选择答案数组
    questionnumber = 0
    mouse = psychopy.event.Mouse()
    if level == 1:
        numberOFanswer = 1 #被试需要选择答案的数量
        questionnumber = random.randint(11,29)
        answerarray.append(questionnumber)
        while len(answerarray)<4:#生成不相同的备选答案
            otheranswer = random.randint(11,29)
            if otheranswer not in answerarray:
                answerarray.append(otheranswer)
    else:
        numberOFanswer = 2
        questionnumber = random.randint(25,38)
        trueanswer = random.randint(11,questionnumber-11)
        while trueanswer == questionnumber/2:
            trueanswer = random.randint(11,questionnumber-11)
        answerarray.append(trueanswer)
        otheranswer = questionnumber - trueanswer
        answerarray.append(otheranswer)
        while len(answerarray)<4:
            otheranswer = random.randint(11,29)
            if otheranswer not in answerarray:
                answerarray.append(otheranswer)
    random.shuffle(answerarray)#答案位置打乱
    
    answerlist = ''
    for i in range(len(answerarray)):
        answerlist =answerlist + str(answerarray[i-1])+','
    
    #生成备选图片
    answer1 =  my_button(240, 120, str(answerarray[0]), [-350,100], textColor=[255, 255, 255], 
                                    textSize=40)
    answer2 =  my_button(240, 120, str(answerarray[1]), [350,100], textColor=[255, 255, 255], 
                                    textSize=40)
    answer3 =  my_button(240, 120, str(answerarray[2]), [-350,-100], textColor=[255, 255, 255], 
                                    textSize=40)
    answer4 =  my_button(240, 120, str(answerarray[3]), [350,-100], textColor=[255, 255, 255], 
                                    textSize=40)


    #第一屏信息
    background.image='pictures/fixation.png'
    background.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:#刺激呈现时间内持续呈现
        Yaoyaxin = 1
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    #第二屏呈现
    background.image='pictures/background.png'
    background.draw()
    answer1.draw()
    answer2.draw()
    answer3.draw()
    answer4.draw()
    
    win.flip()
    clock.reset()
    while clock.getTime() < res_duration_s:#数字呈现4s
        background.image='pictures/cangbaotu.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
   #d第三屏
    background.draw()
    if numberOFanswer == 1:
        text.text = '宝藏在'+str(questionnumber)+'号树后面'
    if numberOFanswer == 2:
        text.text = '两个宝藏所在树桩\n的数字之和是'+str(questionnumber)
    question = text.text
    text.pos = [-100,0]
    text.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        background.image='pictures/background.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
   
    answer1 =  my_button(240, 120, '', [-350,100], textColor=[0, 0, 0], 
                                    textSize=40)
    answer2 =  my_button(240, 120, '', [350,100], textColor=[0, 0, 0], 
                                    textSize=40)
    answer3 =  my_button(240, 120, '', [-350,-100], textColor=[0, 0, 0], 
                                    textSize=40)
    answer4 =  my_button(240, 120, '', [350,-100], textColor=[0, 0, 0], 
                                    textSize=40)
    text.text = '请帮光头强找出'+str(numberOFanswer)+'个宝藏'
    text.width
    text.pos = [0,300]
    background.draw()
    answer1.draw()
    answer2.draw()
    answer3.draw()
    answer4.draw()
    text.draw()
    win.flip()
    clock.reset()
    
    clickornot = 0
    while len(selectanswer)!=numberOFanswer:
        if clickornot != 1:
            if mouse.isPressedIn(answer1.button):
                answer1 =  my_button(240, 120, answerarray[0], [-350,100], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                win.flip()
                selectanswer.append(answerarray[0])
                time = clock.getTime()
                clickornot = 1
        if clickornot != 2:
            if mouse.isPressedIn(answer2.button):
                answer2 =  my_button(240, 120, answerarray[1], [350,100], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                win.flip()
                selectanswer.append(answerarray[1])
                time = clock.getTime()
                clickornot = 2
        if clickornot != 3:
            if mouse.isPressedIn(answer3.button):
                answer3 =  my_button(240, 120, answerarray[2], [-350,-100], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                win.flip()
                selectanswer.append(answerarray[2])
                time = clock.getTime()
                clickornot = 3
        if clickornot != 4:
            if mouse.isPressedIn(answer4.button):
                answer4 =  my_button(240, 120, answerarray[3], [350,-100], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                win.flip()
                selectanswer.append(answerarray[3])
                time = clock.getTime()
                clickornot = 4

    clock.reset()
    if len(selectanswer) == numberOFanswer:
        while clock.getTime() < stim_dynamict_s:
            Yaoyaxin = 1
            if defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()    
        if sum(selectanswer)==questionnumber:
            feedback = 1
        else:
            feedback = 0
        feedback = show_feedback(feedback)
        return feedback, time,question,answerlist

def six_trials(difficulty):
    level = difficulty
    answerarray = []#备选答案数组
    selectanswer = []#被试已经选择答案数组
    questionnumber = 0
    mouse = psychopy.event.Mouse()
    if level == 2:
        numberOFanswer = 1 #被试需要选择答案的数量
        questionnumber = random.randint(11,29)
        answerarray.append(questionnumber)
        while len(answerarray)<6:
            otheranswer = random.randint(11,29)
            if otheranswer not in answerarray:
                answerarray.append(otheranswer)
    if level == 5:
        numberOFanswer = 2
        questionnumber = random.randint(25,38)
        trueanswer = random.randint(11,questionnumber-11)
        while trueanswer == questionnumber/2:
            trueanswer = random.randint(11,questionnumber-11)
        answerarray.append(trueanswer)
        otheranswer = questionnumber - trueanswer
        answerarray.append(otheranswer)
        while len(answerarray)<6:
            otheranswer = random.randint(11,29)
            if otheranswer not in answerarray:
                answerarray.append(otheranswer)
    if level == 7:
        numberOFanswer = 4
        questionnumber = random.randint(25,38)
        trueanswer = random.randint(11,questionnumber-11)
        while trueanswer == questionnumber/2:
            trueanswer = random.randint(11,questionnumber-11)
        answerarray.append(trueanswer)
        otheranswer = questionnumber - trueanswer
        answerarray.append(otheranswer)
        trueanswer1 = random.randint(11,questionnumber-11)
        while trueanswer == questionnumber/2 or trueanswer1 in answerarray:
            trueanswer1 = random.randint(11,questionnumber-11)
        answerarray.append(trueanswer1)
        otheranswer1 = questionnumber - trueanswer1
        answerarray.append(otheranswer1)
        while len(answerarray)<6:
            otheranswer = random.randint(11,29)
            if otheranswer not in answerarray:
                answerarray.append(otheranswer)

    random.shuffle(answerarray)#答案位置打乱
    answerlist = ''
    for i in range(len(answerarray)):
        answerlist =answerlist + str(answerarray[i-1])+','
    #生成备选图片
    answer1 =  my_button(160, 80, str(answerarray[0]), [-500,100], textColor=[255, 255, 255], 
                                    textSize=40)
    answer2 =  my_button(160, 80, str(answerarray[1]), [500,100], textColor=[255, 255, 255], 
                                    textSize=40)
    answer3 =  my_button(160, 80, str(answerarray[2]), [0,100], textColor=[255, 255, 255], 
                                    textSize=40)
    answer4 =  my_button(160, 80, str(answerarray[3]), [-500,-100], textColor=[255, 255, 255], 
                                    textSize=40)
    answer5 =  my_button(160, 80, str(answerarray[4]), [500,-100], textColor=[255, 255, 255], 
                                    textSize=40)
    answer6 =  my_button(160, 80, str(answerarray[5]), [0,-100], textColor=[255, 255, 255], 
                                    textSize=40)

    #第一屏信息
    background.image='pictures/fixation.png'
    background.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:#刺激呈现时间内持续呈现
        Yaoyaxin = 1
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    #第二屏呈现
    background.image='pictures/background.png'
    background.draw()
    answer1.draw()
    answer2.draw()
    answer3.draw()
    answer4.draw()
    answer5.draw()
    answer6.draw()

    win.flip()
    clock.reset()
    while clock.getTime() < res_duration_s:#数字呈现4s
        background.image='pictures/cangbaotu.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
   #d第三屏
    background.draw()
    if numberOFanswer == 1:
        text.text = '宝藏在'+str(questionnumber)+'号树后面'
    if numberOFanswer == 2:
        text.text = '两个宝藏所在树桩\n数字之和是'+str(questionnumber)
    if numberOFanswer == 4:
        text.text = '这个宝藏有4份\n两份宝藏所在树桩的数字之和'+str(questionnumber)+'\n后两份所在树桩的数字之和'+str(questionnumber)
    text.pos = [-100,0]
    question = text.text
    text.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        background.image='pictures/background.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    answer1 =  my_button(160, 80, '', [-500,100], textColor=[0,0,0], 
                                    textSize=40)
    answer2 =  my_button(160, 80, '', [500,100], textColor=[0,0,0], 
                                    textSize=40)
    answer3 =  my_button(160, 80, '', [0,100], textColor=[0,0,0], 
                                    textSize=40)
    answer4 =  my_button(160, 80, '', [-500,-100], textColor=[0,0,0], 
                                    textSize=40)
    answer5 =  my_button(160, 80, '', [500,-100], textColor=[0,0,0], 
                                    textSize=40)
    answer6 =  my_button(160, 80, '', [0,-100], textColor=[0,0,0], 
                                    textSize=40)


    background.draw()
    text.text = '请帮光头强找出'+str(numberOFanswer)+'个宝藏'
    text.pos = [0,300]
    answer1.draw()
    answer2.draw()
    answer3.draw()
    answer4.draw()
    answer5.draw()
    answer6.draw()
    win.flip()
    clock.reset()
    
    clickornot = 0
    while len(selectanswer)!=numberOFanswer:
        if clickornot != 1:
            if mouse.isPressedIn(answer1.button):
                answer1 =  my_button(160, 80, str(answerarray[0]), [-500,100], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                win.flip()
                selectanswer.append(answerarray[0])
                time = clock.getTime()
                clickornot = 1
        if clickornot != 2:
            if mouse.isPressedIn(answer2.button):
                answer2 =  my_button(160, 80, str(answerarray[1]), [500,100], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                win.flip()
                selectanswer.append(answerarray[1])
                time = clock.getTime()
                clickornot = 2
        if clickornot != 3:
            if mouse.isPressedIn(answer3.button):
                answer3 =  my_button(160, 80, str(answerarray[2]), [0,100], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                win.flip()
                selectanswer.append(answerarray[2])
                time = clock.getTime()
                clickornot = 3
        if clickornot != 4:
            if mouse.isPressedIn(answer4.button):
                answer4 =  my_button(160, 80, str(answerarray[3]), [-500,-100], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                win.flip()
                selectanswer.append(answerarray[3])
                time = clock.getTime()
                clickornot = 4
        if clickornot != 5:
            if mouse.isPressedIn(answer5.button):
                answer5 =  my_button(160, 80, str(answerarray[4]), [500,-100], textColor=[255,255,255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                win.flip()
                selectanswer.append(answerarray[4])
                time = clock.getTime()
                clickornot = 5
        if clickornot != 6:
            if mouse.isPressedIn(answer6.button):
                answer6 =  my_button(160, 80, str(answerarray[5]), [0,-100], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                win.flip()
                selectanswer.append(answerarray[5])
                time = clock.getTime()
                clickornot = 6
        if len(selectanswer) == 2:
            if sum(selectanswer) != questionnumber:
                selectanswer.append(0)
                selectanswer.append(0)
                break

        

    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        Yaoyaxin = 1
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    if numberOFanswer != 4:
        if sum(selectanswer)==questionnumber:
            feedback = 1
        else:
            feedback = 0
    else:
        if selectanswer[3]+selectanswer[2] == questionnumber:
            feedback = 1
        else:
            feedback = 0
    feedback = show_feedback(feedback)
    return feedback, time,question,answerlist

def eight_trials(difficulty):
    level = difficulty
    answerarray = []#备选答案数组
    selectanswer = []#被试已经选择答案数组
    questionnumber = 0
    mouse = psychopy.event.Mouse()
    
    ##设置备选答案不重复
    if level == 3:
        numberOFanswer = 1 #被试需要选择答案的数量
        questionnumber = random.randint(11,29)
        answerarray.append(questionnumber)
        while len(answerarray)<8:
            otheranswer = random.randint(11,29)
            if otheranswer not in answerarray:
                answerarray.append(otheranswer)
    if level == 6:
        numberOFanswer = 2
        questionnumber = random.randint(25,38)
        trueanswer = random.randint(11,questionnumber-11)
        while trueanswer == questionnumber/2:
            trueanswer = random.randint(11,questionnumber-11)
        answerarray.append(trueanswer)
        otheranswer = questionnumber - trueanswer
        answerarray.append(otheranswer)
        while len(answerarray)<8:
            otheranswer = random.randint(25,38)
            if otheranswer not in answerarray:
                answerarray.append(otheranswer)
    if level == 8:
        numberOFanswer = 4
        questionnumber = random.randint(25,38)
        trueanswer = random.randint(11,questionnumber-11)
        while trueanswer == questionnumber/2:
            trueanswer = random.randint(11,questionnumber-11)
        answerarray.append(trueanswer)
        otheranswer = questionnumber - trueanswer
        answerarray.append(otheranswer)
        trueanswer1 = random.randint(11,questionnumber-11)
        while trueanswer == questionnumber/2 or trueanswer1 in answerarray:
            trueanswer1 = random.randint(11,questionnumber-11)
        answerarray.append(trueanswer1)
        otheranswer1 = questionnumber - trueanswer1
        answerarray.append(otheranswer1)
        while len(answerarray)<8:
            otheranswer = random.randint(11,29)
            if otheranswer not in answerarray:
                answerarray.append(otheranswer)

    random.shuffle(answerarray)#答案位置打乱
    answerlist = ''
    for i in range(len(answerarray)):
        answerlist =answerlist + str(answerarray[i-1])+','
    #生成备选图片
    answer1 =  my_button(160, 80, str(answerarray[0]), [350,150], textColor=[255, 255, 255], 
                                    textSize=40)
    answer2 =  my_button(160, 80, str(answerarray[1]), [0,150], textColor=[255, 255, 255], 
                                    textSize=40)
    answer3 =  my_button(160, 80, str(answerarray[2]), [-350,150], textColor=[255, 255, 255], 
                                    textSize=40)
    answer4 =  my_button(160, 80, str(answerarray[3]), [200,-0], textColor=[255, 255, 255], 
                                    textSize=40)
    answer5 =  my_button(160, 80, str(answerarray[4]), [-200,-0], textColor=[255, 255, 255], 
                                    textSize=40)
    answer6 =  my_button(160, 80, str(answerarray[5]), [350,-150], textColor=[255, 255, 255], 
                                    textSize=40)
    answer7 =  my_button(160, 80, str(answerarray[6]), [0,-150], textColor=[255, 255, 255], 
                                    textSize=40)
    answer8 =  my_button(160, 80, str(answerarray[7]), [-350,-150], textColor=[255, 255, 255], 
                                    textSize=40)

    #第一屏信息
    background.image='pictures/fixation.png'
    background.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:#刺激呈现时间内持续呈现
        Yaoyaxin = 1
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    #第二屏呈现
    background.image='pictures/background.png'
    background.draw()
    answer1.draw()
    answer2.draw()
    answer3.draw()
    answer4.draw()
    answer5.draw()
    answer6.draw()
    answer7.draw()
    answer8.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < res_duration_s:#数字呈现4s
        background.image='pictures/cangbaotu.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
   #d第三屏
    background.draw()
    if numberOFanswer == 1:
        text.text = '宝藏在'+str(questionnumber)+'号树后面'
    if numberOFanswer == 2:
        text.text = '两个宝藏所在树桩\n数字之和是'+str(questionnumber)
    if numberOFanswer == 4:
        text.text = '这个宝藏有4份\n前两份宝藏所在树桩的数字之和为'+str(questionnumber)+'\n后两份所在树桩的数字之和也是'+str(questionnumber)
    text.pos = [-100,0]
    question = text.text
    text.draw()
    win.flip()
    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        background.image='pictures/background.png'
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    answer1 =  my_button(160, 80, '', [350,150], textColor=[0, 0, 0], 
                                    textSize=40)
    answer2 =  my_button(160, 80, '', [0,150], textColor=[0, 0, 0], 
                                    textSize=40)
    answer3 =  my_button(160, 80, '', [-350,150], textColor=[0, 0, 0], 
                                    textSize=40)
    answer4 =  my_button(160, 80, '', [200,-0], textColor=[0, 0, 0], 
                                    textSize=40)
    answer5 =  my_button(160, 80, '', [-200,-0], textColor=[0, 0, 0], 
                                    textSize=40)
    answer6 =  my_button(160, 80, '', [350,-150], textColor=[0, 0, 0], 
                                    textSize=40)
    answer7 =  my_button(160, 80, '', [0,-150], textColor=[0, 0, 0], 
                                    textSize=40)
    answer8 =  my_button(160, 80, '', [-350,-150], textColor=[0, 0, 0], 
                                    textSize=40)



    background.draw()
    text.text = '请帮光头强找出'+str(numberOFanswer)+'个宝藏'
    text.pos = [0,300]
    answer1.draw()
    answer2.draw()
    answer3.draw()
    answer4.draw()
    answer5.draw()
    answer6.draw()
    answer7.draw()
    answer8.draw()
    text.draw()
    win.flip()
    clock.reset()
    
    clickornot = 0
    while len(selectanswer)!=numberOFanswer:
        if clickornot != 1:
            if mouse.isPressedIn(answer1.button):
                answer1 =  my_button(160, 80, str(answerarray[0]), [350,150], textColor=[255, 255, 255], 
                                    textSize=40)
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                answer7.draw()
                answer8.draw()
                win.flip()
                selectanswer.append(answerarray[0])
                time = clock.getTime()
                clickornot = 1
        if clickornot != 2:
            if mouse.isPressedIn(answer2.button):
                answer2 =  my_button(160, 80, str(answerarray[1]), [0,150], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                answer7.draw()
                answer8.draw()
                win.flip()
                selectanswer.append(answerarray[1])
                time = clock.getTime()
                clickornot = 2
        if clickornot != 3:
            if mouse.isPressedIn(answer3.button):
                answer3 =  my_button(160, 80, str(answerarray[2]), [-350,150], textColor=[255, 255, 255], 
                                    textSize=40)
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                answer7.draw()
                answer8.draw()
                win.flip()
                selectanswer.append(answerarray[2])
                time = clock.getTime()
                clickornot = 3
        if clickornot != 4:
            if mouse.isPressedIn(answer4.button):
                answer4 =  my_button(160, 80, str(answerarray[3]), [200,-0], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                answer7.draw()
                answer8.draw()
                win.flip()
                selectanswer.append(answerarray[3])
                time = clock.getTime()
                clickornot = 4
        if clickornot != 5:
            if mouse.isPressedIn(answer5.button):
                answer5 =  my_button(160, 80, str(answerarray[4]), [-200,-0], textColor=[255,255,255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                answer7.draw()
                answer8.draw()
                win.flip()
                selectanswer.append(answerarray[4])
                time = clock.getTime()
                clickornot = 5
        if clickornot != 6:
            if mouse.isPressedIn(answer6.button):
                answer6 =  my_button(160, 80, str(answerarray[5]), [350,-150], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                answer7.draw()
                answer8.draw()
                win.flip()
                selectanswer.append(answerarray[5])
                time = clock.getTime()
                clickornot = 6
        if clickornot != 7:
            if mouse.isPressedIn(answer7.button):
                answer7 =  my_button(160, 80, str(answerarray[6]), [0,-150], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                answer7.draw()
                answer8.draw()
                win.flip()
                selectanswer.append(answerarray[6])
                time = clock.getTime()
                clickornot = 7
        if clickornot != 8:
            if mouse.isPressedIn(answer8.button):
                answer8 =  my_button(160, 80, str(answerarray[7]), [-350,-150], textColor=[255, 255, 255], 
                                    textSize=40)
                background.draw()
                answer1.draw()
                answer2.draw()
                answer3.draw()
                answer4.draw()
                answer5.draw()
                answer6.draw()
                answer7.draw()
                answer8.draw()
                win.flip()
                selectanswer.append(answerarray[7])
                time = clock.getTime()
                clickornot = 8
        if len(selectanswer) == 2:
            if sum(selectanswer) != questionnumber:
                selectanswer.append(0)
                selectanswer.append(0)
                break

        

    clock.reset()
    while clock.getTime() < stim_dynamict_s:
        Yaoyaxin = 1
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    if numberOFanswer != 4:
        if sum(selectanswer)==questionnumber:
            feedback = 1
        else:
            feedback = 0
    else:
        if selectanswer[3]+selectanswer[2] == questionnumber:
            feedback = 1
        else:
            feedback = 0
    feedback = show_feedback(feedback)
    return feedback, time,question,answerlist

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
expName = 'number_space'
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
    size=[1359, 758],
    units="pix",
    fullscr=False,         # fullscr means full-screen mode
    allowGUI=None,
)
# # store frame rate of monitor if we can measure it
# expInfo['frameRate'] = win.getActualFrameRate()
# if expInfo['frameRate'] != None:
#     frameDur = 1.0 / round(expInfo['frameRate'])
# else:
#     frameDur = 1.0 / 60.0  # could not measure, so guess
background = psychopy.visual.ImageStim(
    win=win,
    image='pictures/guidance.png',
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

trials_in_block = 50

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
difficulty = 1
accuracy = []
for i_trials in range(trials_in_block):
    
    if len(accuracy) > 4:
        if sum(accuracy)/len(accuracy) >= 0.8:
            del accuracy[:]
            if difficulty < 8:
                difficulty = difficulty +1
    if difficulty == 1 or difficulty == 4:
        feedback, time,question,answerlist = four_trials(difficulty)
    if difficulty == 2 or difficulty == 5 or difficulty == 7:
        feedback, time,question,answerlist = six_trials(difficulty)
    if difficulty == 3 or difficulty == 6 or difficulty == 8:
        feedback, time,question,answerlist = eight_trials(difficulty)
    accuracy.append(feedback)
    # 保存结果
    #thisExp.addData('block', i_blocks+1)
    thisExp.addData('trial', i_trials+1)
    thisExp.addData('feedback', feedback)
    thisExp.addData('reaction time', time)
    thisExp.addData('difficulty', difficulty)
    thisExp.addData('question', question)
    thisExp.addData('answerlist', answerlist)
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
