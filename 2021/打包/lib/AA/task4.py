import random

import psychopy.visual as visual
import psychopy.event

from psychopy import core, gui, data
from math import log2
import numpy as np
import os
import csv
from psychopy.hardware import keyboard
import stat


class Progress_bar():

    def __init__(self, time, clock, position_y):
        self.width = win.size[0] * 0.9
        self.my_clock = core.Clock()
        self.total_time = time
        self.y = position_y
        self.passed_time = int(self.my_clock.getTime())
        self.passed_time_width = self.passed_time/self.total_time*self.width
        self.total_time_bar = generate_rectangle(
            self.width+10, 25, [0, position_y], fillColor=[255, 255, 255])
        self.passed_time_bar = generate_rectangle(self.passed_time_width, 15, [
            0 - (self.width / 2) + (self.passed_time_width / 2), position_y], fillColor=[81, 210, 108], lineColor=[81, 210, 108])
        self.generate_fences()

    def generate_fences(self):
        self.fences = []
        gap = (self.width+10-9*8)/10
        for i in range(1, 10):
            self.fences.append(generate_rectangle(
                8, 25, [-self.width/2+i*gap, self.y]))

    def refresh(self):
        self.passed_time = int(self.my_clock.getTime())
        self.passed_time_width = self.passed_time/self.total_time*self.width
        if self.passed_time >= self.total_time:
            self.passed_time_bar = generate_rectangle(
                self.width, 15, [0, self.y], fillColor=[221, 81, 69], lineColor=[49, 193, 231])
        else:
            self.passed_time_bar = generate_rectangle(self.passed_time_width, 15, [
                0-(self.width/2)+(self.passed_time_width/2), self.y], fillColor=[81, 210, 108], lineColor=[81, 210, 108])

    def draw(self, is_practice):
        if not is_practice:
            self.refresh()

            self.total_time_bar.draw()

            self.passed_time_bar.draw()
            for i in range(len(self.fences)):
                self.fences[i].draw()

    def getTime(self):
        self.refresh()
        return self.passed_time


def save_and_quit():
    """???????????????"""
    os.chmod(filename + '.csv', stat.S_IWRITE)  # ??????????????????
    thisExp.saveAsWideText(filename + '.csv', appendFile=True)
    os.chmod(filename + '.csv', stat.S_IREAD)  # ??????????????????
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    core.quit()


def generate_rectangle(length, height, pos=[0, 0], fillColor=[255, 255, 255], lineColor=[255, 255, 255]):
    """???????????????
    length??????
    height??????
    pos??????"""
    rectangle = visual.Rect(
        win=win,
        size=[length, height],
        pos=pos,
        fillColor=fillColor,
        lineColor=lineColor,
        colorSpace="rgb255"
    )

    return rectangle


def practice_trials(add_trials, match_or_compare, modes=1):
    """???????????????????????????????????????????????????????????????"""

    if add_trials == 0 and match_or_compare == 0:
        intro.image = "pictures/New/????????????.png"
    elif match_or_compare == 1:
        intro.image = "pictures/New/???????????????.png"
    elif match_or_compare == 0 and add_trials == 1:
        intro.image = "pictures/New/????????????.png"

    intro.draw()
    win.flip()
    psychopy.event.waitKeys()

    n_dots3, mode, colors = trials(add_trials == 0, modes, is_practice=True)

    if match_or_compare == 0:
        feedback, time, compare, correct = match_trials(
            n_dots3, log2(3), mode, colors, is_practice=True)
    else:
        feedback, time = compare_trials(
            n_dots3, log2(3), mode, colors, is_practice=True)

    return feedback


def trials(add_trials, mode, is_practice=False, colors=[]):
    """???????????????????????????????????????trial
    add_trials=True????????????,??????????????????
    mode?????????????????????1???2???3???4????????????????????????
    practice??????????????????
    colors??????????????????????????????mode????????????"""
    if not is_practice:
        n_dots1 = round(random.uniform(8, 24))  # ??????
        n_dots2 = round(random.uniform(8, 32 - n_dots1))
        if add_trials == False:
            n_dots1 = round(random.uniform(16, 32))
            n_dots2 = int(random.uniform(8, n_dots1 - 8))
    else:
        n_dots1 = round(random.uniform(1, 9))
        n_dots2 = round(random.uniform(1, 10 - n_dots1))
        if add_trials == False:
            n_dots1 = round(random.uniform(5, 10))
            n_dots2 = int(random.uniform(1, n_dots1-1))

    choices = [0, 1, 2, 3]

    if len(colors) == 0:
        color_s = random.sample(choices, mode)
    else:
        color_s = colors
    # ????????????1
    dot_stim = generate_dots(n_dots1, +500, 0, mode, color_s)
    # ????????????2
    dot_stim2 = generate_dots(n_dots2, -500, 0, mode, color_s)

    jar = psychopy.visual.ImageStim(
        win=win,
        image='pictures/jar.png',
        units='pix',
        size=[400, 400]
    )

    # Operand A
    clock.reset()
    while clock.getTime() < pre_duration_s:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
        background.draw()
        if not is_practice:
            my_progress_bar.draw(is_practice)
        jar.draw()
        win.flip()

    while clock.getTime() < pre_duration_s + stim_static_s:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
        background.draw()
        if not is_practice:
            my_progress_bar.draw(is_practice)
        dot_stim.draw()
        jar.draw()
        win.flip()

    clock.reset()

    # ?????????????????????????????????
    while clock.getTime() < stim_dynamict_s:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
        t = clock.getTime()
        # print(t)
        # print(100-t*100)
        dot_stim.setFieldPos((round(500 - t * 1000), 0))
        background.draw()
        if not is_practice:
            my_progress_bar.draw(is_practice)
        dot_stim.draw()
        jar.draw()
        win.flip()

    if not add_trials:
        jar.ori = 300
    # Operand B
    clock.reset()
    while clock.getTime() < interal_duration_s:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
        background.draw()
        if not is_practice:
            my_progress_bar.draw(is_practice)
        jar.draw()
        win.flip()

    # ?????????????????????????????????
    clock.reset()
    if add_trials:  # ????????????
        # ????????????2 ????????????
        while clock.getTime() < stim_static_s:
            background.draw()
            if not is_practice:
                my_progress_bar.draw(is_practice)
            dot_stim2.draw()
            jar.draw()
            win.flip()
        clock.reset()
        while clock.getTime() < stim_dynamict_s:
            t = clock.getTime()
            dot_stim2.setFieldPos((round(-500 + t * 1000), 0))
            background.draw()
            if not is_practice:
                my_progress_bar.draw(is_practice)
            dot_stim2.draw()
            jar.draw()
            win.flip()
    else:  # ????????????
        while clock.getTime() < stim_dynamict_s:
            t = clock.getTime()
            dot_stim2.setFieldPos((round(-t * 800), round(t*450)))
            background.draw()
            if not is_practice:
                my_progress_bar.draw(is_practice)
            dot_stim2.draw()
            jar.draw()
            win.flip()
        clock.reset()
        while clock.getTime() < stim_static_s:
            background.draw()
            if not is_practice:
                my_progress_bar.draw(is_practice)
            dot_stim2.draw()
            jar.draw()
            win.flip()

    if add_trials:
        n_dots3 = n_dots1 + n_dots2
    else:
        n_dots3 = n_dots1 - n_dots2

    return n_dots3, mode, color_s


def show_feedback(feedback, is_practice):
    """????????????
    feedback=1????????????????????????
    feedback=0????????????????????????
    feedback=2??????????????????????????????
    ?????????????????????1????????????????????????0???????????????????????????"""
    if feedback == 1:
        text.text = ""
        feedback_picture = smilling_face
    elif feedback == 0:
        text.text = ""
        feedback_picture = crying_face
        feedback_picture.opacity = 1
    else:
        text.text = "??????????????????"
        feedback_picture = crying_face
        feedback_picture.opacity = 0
        feedback = 0
    text.pos = [0, 0]
    clock.reset()
    while clock.getTime() < feedback_duration_s:
        background.draw()
        if not is_practice:
            my_progress_bar.draw(is_practice)
        feedback_picture.draw()
        text.draw()
        win.flip()
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
    return feedback


def compare_trials(correct_ans_n_dots, log_difference, mode, colors=[0], is_practice=False):
    """????????????"""

    if colors[0] == 0:
        color_text = "??????"
    elif colors[0] == 1:
        color_text = "??????"
    elif colors[0] == 2:
        color_text = "??????"
    elif colors[0] == 3:
        color_text = "??????"
    # ???????????????????????????????????????????????????
    greater_than_correct = random.getrandbits(1)
    if correct_ans_n_dots == 1:  # ????????????????????????1??????????????????????????????????????????
        greater_than_correct = 1
    if greater_than_correct == 1:
        compare_ans_n_dots = round(correct_ans_n_dots * (2 ** log_difference))
    else:
        compare_ans_n_dots = round(correct_ans_n_dots / (2 ** log_difference))

    dot_res_com = generate_dots(compare_ans_n_dots, 0, 0, 1, colors)

    # 500ms??????
    clock.reset()
    while clock.getTime() < pre_duration_s:
        background.draw()
        if not is_practice:
            my_progress_bar.draw(is_practice)
        win.flip()

    compare_tips_1 = psychopy.visual.TextStim(
        win=win,
        units="pix",
        height=55,
        bold=True,
        font="STXINWEI",
        color='black',
        pos=(-350, 0),
        text="???"
    )
    compare_tips_2 = psychopy.visual.TextStim(
        win=win,
        units="pix",
        height=55,
        bold=True,
        font="STXINWEI",
        color='black',
        pos=(350, 0),
        text="???"
    )

    background.draw()
    if not is_practice:
        my_progress_bar.draw(is_practice)
    dot_res_com.draw()
    compare_tips_1.draw()
    compare_tips_2.draw()
    win.flip()
    clock.reset()
    kb.clock.reset()
    while clock.getTime() < res_duration_s:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
        keys = kb.getKeys(keyList=['left', 'right'])
        if len(keys) > 0:
            if keys[0].name == 'left':
                if greater_than_correct == 1:
                    feedback = 1
                else:
                    feedback = 0
                time = keys[0].rt
                feedback = show_feedback(feedback, is_practice)
                return feedback, time
            elif keys[0].name == 'right':
                if greater_than_correct == 1:
                    feedback = 0
                else:
                    feedback = 1
                time = keys[0].rt
                feedback = show_feedback(feedback, is_practice)
                return feedback, time

    feedback = 2
    feedback = show_feedback(feedback, is_practice)
    time = 0
    return feedback, time


def overlap(x, y, R1, dot_Rs, dot_xys):
    for i in range(len(dot_xys)):
        if (x - dot_xys[i][0]) ** 2 + (y - dot_xys[i][1]) ** 2 < ((R1+dot_Rs[i][0])/2) ** 2:
            return True
    return False


def generate_dots(dots_num, x, y, mode=1, colors=[0]):
    """?????????
    dots_num??????????????????????????????
    x,y????????????????????????
    mode??????????????????????????????1????????????????????????2??????????????????????????????3???????????????????????????4??????3???????????????
    colors???????????????????????????????????????????????????mode?????????????????????"""
    dot_xys = []  # ?????????????????????
    max_num = 100
    if dots_num >= max_num:
        dots_num = max_num

    # ???????????????????????????????????????????????????????????????????????????????????????

    colors = [0]

    area = 0
    all_area = 5625
    left_area = all_area
    change_area = 300
    minimum_area = 200

    dot_area = all_area/dots_num

    color_s = [[238, 134, 3], [227, 80, 67], [25, 161, 95], [0, 0, 0]]

    dot_colors = []

    dots = [dots_num, 0, 0, 0]
    dot_sizes = []
    if mode >= 2:
        dots[1] = round(random.uniform(1, dots_num / 4))  # ???????????????1???4??????????????????
    if mode >= 3:
        dots[2] = round(random.uniform(1, dots_num / 4))
    if mode == 4:
        dots[3] = round(random.uniform(1, dots_num / 4))

    for i_area in range(dots_num, 0, -1):  # ???????????????????????????????????????????????????step
        average_area = left_area / i_area
        if random.getrandbits(1) == 1:
            dot_area = random.uniform(0, 1) * dot_area + average_area
        else:
            dot_area = -random.uniform(0, 1) * dot_area + average_area
        if i_area == 1:
            dot_area = left_area
        if dot_area < minimum_area:
            dot_area = minimum_area
        left_area = left_area-dot_area
        dot_sizes.append([dot_area ** 0.5, dot_area**0.5])

    for i in range(4):
        while len(dot_xys) < sum(dots[:i+1]):
            dot_x = random.uniform(-90, 90)
            dot_y = random.uniform(-90, 90)
            if not overlap(dot_x, dot_y, dot_sizes[len(dot_xys)][0], dot_sizes, dot_xys):
                dot_xys.append([dot_x, dot_y])
                dot_colors.append(color_s[colors[i]])

    dots_array = psychopy.visual.ElementArrayStim(
        win=win,
        units="pix",
        fieldPos=(x, y),
        nElements=sum(dots),
        xys=dot_xys,
        elementTex=None,
        sizes=dot_sizes,
        elementMask='pictures/??????.png',
        # elementMask='circle',  # ?????????????????????????????????
        colors=dot_colors,
        colorSpace='rgb255'
    )

    return dots_array


def match_trials(correct_ans_n_dots, log_difference, mode, colors=[0], is_practice=False):
    """????????????"""

    if colors[0] == 0:
        color_text = "??????"
    elif colors[0] == 1:
        color_text = "??????"
    elif colors[0] == 2:
        color_text = "??????"
    elif colors[0] == 3:
        color_text = "??????"

    correct_on_left = random.getrandbits(1)

    # ???????????????????????????????????????????????????
    greater_than_correct = random.getrandbits(1)
    if correct_ans_n_dots == 1:  # ????????????????????????1??????????????????????????????????????????
        greater_than_correct = 1
    if greater_than_correct == 1:
        compare_ans_n_dots = round(correct_ans_n_dots * (2 ** log_difference))
    else:
        compare_ans_n_dots = round(correct_ans_n_dots / (2 ** log_difference))

    # ???????????????????????????
    if correct_on_left == 1:
        dot_res_com = generate_dots(
            compare_ans_n_dots, +250, 0, 1, colors)  # ???????????????????????????
        dot_res_cor = generate_dots(
            correct_ans_n_dots, -250, 0, 1, colors)  # ????????????
    else:
        dot_res_com = generate_dots(compare_ans_n_dots, -250, 0, 1, colors)
        dot_res_cor = generate_dots(correct_ans_n_dots, +250, 0, 1, colors)
    # 500ms??????
    clock.reset()
    while clock.getTime() < pre_duration_s:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
        background.draw()
        if not is_practice:
            my_progress_bar.draw(is_practice)
        win.flip()

    text.text = "???"
    text.pos = [0, -150]
    background.draw()
    if not is_practice:
        my_progress_bar.draw(is_practice)
    dot_res_cor.draw()
    dot_res_com.draw()
    text.draw()
    win.flip()
    clock.reset()
    kb.clock.reset()
    while clock.getTime() < res_duration_s:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
        keys = kb.getKeys(keyList=['left', 'right'])
        if len(keys) > 0:
            if keys[0].name == 'left':
                if correct_on_left == 1:
                    feedback = 1
                else:
                    feedback = 0
                time = keys[0].rt
                feedback = show_feedback(feedback, is_practice)
                return feedback, time, compare_ans_n_dots, correct_ans_n_dots
            elif keys[0].name == 'right':
                if correct_on_left == 1:
                    feedback = 0
                else:
                    feedback = 1
                time = keys[0].rt
                feedback = show_feedback(feedback, is_practice)
                return feedback, time, compare_ans_n_dots, correct_ans_n_dots

    # ???????????????
    feedback = 2
    feedback = show_feedback(feedback, is_practice)
    time = 0
    return feedback, time, compare_ans_n_dots, correct_ans_n_dots


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'task4'  # from the Builder filename that created this script
expInfo = {'??????????????????': '', '????????????': '', '???????????????': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['participant'] = expInfo.pop("??????????????????")
expInfo['name'] = expInfo.pop("????????????")
expInfo['session'] = expInfo.pop("???????????????")
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
# ??????????????????data????????????
filename = os.path.dirname(os.path.dirname(_thisDir)) + os.sep + \
    u'data/%s_%s' % (expInfo['participant'], expName)
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=os.path.abspath(__file__),
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)

# ??????
win = psychopy.visual.Window(
    size=[1800, 1000],
    units="pix",
    fullscr=False,         # fullscr means full-screen mode
)
# # store frame rate of monitor if we can measure it
# expInfo['frameRate'] = win.getActualFrameRate()
# if expInfo['frameRate'] != None:
#     frameDur = 1.0 / round(expInfo['frameRate'])
# else:
#     frameDur = 1.0 / 60.0  # could not measure, so guess
kb = keyboard.Keyboard()
background = psychopy.visual.ImageStim(
    win=win,
    image='pictures/background-?????????????????????20%',
    units='pix',
    size=win.size,
    opacity=0.8
)

intro = psychopy.visual.ImageStim(
    win=win,
    image="pictures/intro-1.png",
    units='pix',
    size=win.size
)

bell = visual.ImageStim(
    win=win,
    image="pictures/bell.png",
    units="pix",
    size=[100, 100]
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
)

if expInfo['session'] == '01' or expInfo['session'] == '1':
    log_difference = 1.5
else:
    log_difference = []
    try:
        os.chmod(filename+'.csv', stat.S_IWRITE)
        with open(filename + '.csv') as f:
            reader = csv.reader(f)

            for row in reader:
                log_difference = row[6]
    except IOError:
        background.draw()
        text.text = "??????????????????????????????\n???????????????????????????????????????\n??????????????????"
        text.draw()
        win.flip()
        psychopy.event.waitKeys()
        core.quit()
log_difference = float(log_difference)

defaultKeyboard = keyboard.Keyboard()

pre_duration_s = 0.5  # 500ms?????????
stim_static_s = 1.0  # 1000ms???????????????
stim_dynamict_s = 0.5  # 500ms????????????
interal_duration_s = 1.0  # 1000ms???????????????
res_duration_s = 4.0  # 4000ms???????????????
feedback_duration_s = 2.0  # 2000ms???????????????

trials_in_block = 20

decline_log_difference = [0.08, 0.09, 0.10, 0.11, 0.12]  # ??????????????????
ascend_log_difference = [0.13, 0.14, 0.15, 0.16, 0.17]  # ??????????????????

clock = psychopy.core.Clock()


background.draw()
intro.draw()
win.flip()
psychopy.event.waitKeys()

if expInfo['session'] == '01' or expInfo['session'] == '1':
    # ????????????
    correct_rate = 0

    while correct_rate < 0.75:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()

        practice_corrects = 0
        count = 0
        for i in range(1):
            for add_or_sub in range(2):
                for mat_or_com in range(2):
                    count += 1
                    practice_corrects += practice_trials(
                        add_or_sub, mat_or_com)

        correct_rate = practice_corrects / count
        if correct_rate >= 0.75:
            intro.image = "pictures/New/????????????.png"
        else:
            intro.image = "pictures/intro-5.png"

        background.draw()
        intro.draw()

        win.flip()

        psychopy.event.waitKeys()


corrects = 0

modes = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],
         [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1],
         [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
         [4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]]

my_progress_bar = Progress_bar(600, core.Clock(), win.size[1] / 2 - 20)
half_time = False
for i_blocks in range(6):
    if i_blocks > 0 and (corrects / 20) <= 0.70:  # ???????????????0.7????????????
        log_difference += random.choice(decline_log_difference)
    elif i_blocks > 0 and (corrects / 20) >= 0.85:  # ???????????????0.85????????????
        log_difference -= random.choice(ascend_log_difference)

    corrects = 0  # ???????????????

    text.text = "??????????????????????????????????????????"
    text.pos = [0, 0]

    background.draw()
    text.draw()
    my_progress_bar.draw(is_practice=False)
    win.flip()

    psychopy.event.waitKeys()
    for i_trials in range(trials_in_block):
        clock.reset()

        # ????????????????????????????????????????????????????????????????????????
        add_trial = bool(random.getrandbits(1))
        n_dots3, mode, colors = trials(add_trial, modes[0][i_trials])

        match_or_compare = bool(random.getrandbits(1))
        if match_or_compare:
            # ?????????true????????????????????????
            feedback, time, compare, correct = match_trials(
                n_dots3, log_difference, mode, colors)
        else:
            # ?????????????????????
            feedback, time = compare_trials(
                n_dots3, log_difference, mode, colors)

        if feedback == 1:
            corrects += 1

        # ????????????
        thisExp.addData('block', i_blocks+1)
        thisExp.addData('trial', i_trials+1)
        thisExp.addData('add or subtract', add_trial)
        thisExp.addData('match or compare', match_or_compare)
        thisExp.addData('feedback', feedback)
        thisExp.addData('reaction time', time)
        thisExp.nextEntry()
        if my_progress_bar.getTime() >= 300 and half_time == False:
            half_time = True
            intro.image = "pictures/half_alert.png"
            bell.pos = [0, win.size[0]*0.125]
            intro.draw()
            bell.draw()
            win.flip()
            psychopy.event.waitKeys()
        if my_progress_bar.getTime() >= 603:
            break

    thisExp.addData('log_difference', log_difference)
    thisExp.addData('accuracy', corrects / 20)
    thisExp.nextEntry()
    if my_progress_bar.getTime() >= 603:
        break

intro.image = "pictures/final_alert.png"
bell.pos = [0, win.size[0]*0.125]
intro.draw()
bell.draw()
win.flip()
psychopy.event.waitKeys()

thisExp.saveAsWideText(filename + '.csv', appendFile=True)
os.chmod(filename + '.csv', stat.S_IREAD)  # ??????????????????
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
core.wait(2)
win.close()
