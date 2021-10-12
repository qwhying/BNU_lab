from psychopy import visual, event, core, gui, data
from pyglet.window import key
from psychopy.hardware import keyboard


import os
import random
import datetime
import sys
import csv
import copy
import math
from math import ceil
import stat


class Balloon():
    def __init__(self):
        self.balloon_pic = balloon
        self.positions = [-210, -157.5, -105, -52.5, 0, 52.5, 105, 157.5, 210]
        self.present_pos = 0
        self.balloon_pic.pos = [0, self.positions[self.present_pos]]
        self.yellow_ball_text = generate_textMark(
            -75, self.balloon_pic.pos[1] + 60, '', 30)
        self.red_ball_text = generate_textMark(
            0, self.balloon_pic.pos[1] + 60, '', 30)
        self.green_ball_text = generate_textMark(
            75, self.balloon_pic.pos[1] + 60, '', 30)
        self.basket_text = generate_textMark(0,
                                             self.balloon_pic.pos[1]-70, '', 30)
        self.red_balloon = visual.Circle(
            win=win,
            size=[balloon.size[0]*0.32, balloon.size[0]*0.32],
            fillColorSpace='rgb255',
            fillColor=[0, 0, 0],
            opacity=0.1,
            pos=[0, self.balloon_pic.pos[1]+balloon.size[0]*0.24]
        )
        self.yellow_balloon = visual.Circle(
            win=win,
            size=[balloon.size[0]*0.32, balloon.size[0]*0.32],
            fillColorSpace='rgb255',
            fillColor=[0, 0, 0],
            opacity=0.1,
            pos=[-balloon.size[0]*0.32+5,
                 self.balloon_pic.pos[1]+balloon.size[0]*0.24]
        )
        self.green_balloon = visual.Circle(
            win=win,
            size=[balloon.size[0]*0.32, balloon.size[0]*0.32],
            fillColorSpace='rgb255',
            fillColor=[0, 0, 0],
            opacity=0.1,
            pos=[balloon.size[0]*0.32-5,
                 self.balloon_pic.pos[1]+balloon.size[0]*0.24]
        )

        self.success_text = generate_textMark(0, 0, "√", 30)
        self.fail_text = generate_textMark(0, 0, "×", 30)

    def draw(self):
        self.balloon_pic.draw()
        self.red_balloon.draw()
        self.green_balloon.draw()
        self.yellow_balloon.draw()
        self.red_ball_text.draw()
        self.yellow_ball_text.draw()
        self.green_ball_text.draw()
        self.basket_text.draw()

    def set_num(self, ytext, rtext, gtext, text1, text2, operator):
        self.operator = operator
        if operator == "+":
            self.answer_num = text1 + text2
        elif operator == "-":
            self.answer_num = ((text1 - text2) ** 2) ** 0.5
        elif operator == "*":
            self.answer_num = text1 * text2
        if ytext == -1:
            ytext = ""
        elif rtext == -1:
            rtext = ""
        elif gtext == -1:
            gtext = ""
        self.red_ball_text.text = rtext
        self.yellow_ball_text.text = ytext
        self.green_ball_text.text = gtext
        self.basket_text.text = str(text1) + "   " + str(text2)
        # if self.operator == "+":
        #     self.answer_num = text1 + text2
        # elif operator == "-":
        #     self.answer_num = ((text1 - text2) ** 2) ** 0.5
        # elif operator == "*":
        #     self.answer_num = text1*text2

    def rise(self, to_rise):
        """显示气球上升的动画，输入参数to_rise是一个bool类型值，to_rise为True时气球上升

        没有返回值"""
        if to_rise:
            if self.present_pos == 8:
                return 0
            clock.reset()
            t = clock.getTime()
            x = self.balloon_pic.pos[0]
            y = self.balloon_pic.pos[1]
            distance = self.positions[self.present_pos+1] - \
                self.positions[self.present_pos]
            while t < 1:
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    save_and_quit()
                self.balloon_pic.pos = [
                    x, y + (distance * t)]
                self.green_balloon.pos = [
                    self.green_balloon.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
                self.red_balloon.pos = [
                    self.red_balloon.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
                self.yellow_balloon.pos = [
                    self.yellow_balloon.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
                self.red_ball_text.pos = [
                    self.red_ball_text.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
                self.yellow_ball_text.pos = [
                    self.yellow_ball_text.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
                self.green_ball_text.pos = [
                    self.green_ball_text.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
                self.basket_text.pos = [
                    self.basket_text.pos[0], self.balloon_pic.pos[1]-70]

                background.draw()
                self.draw()
                win.flip()

                t = clock.getTime()

            self.balloon_pic.pos = [x, self.positions[self.present_pos + 1]]
            self.green_balloon.pos = [
                self.green_balloon.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
            self.red_balloon.pos = [
                self.red_balloon.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
            self.yellow_balloon.pos = [
                self.yellow_balloon.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
            self.red_ball_text.pos = [
                self.red_ball_text.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
            self.yellow_ball_text.pos = [
                self.yellow_ball_text.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
            self.green_ball_text.pos = [
                self.green_ball_text.pos[0], self.balloon_pic.pos[1] + balloon.size[0]*0.24]
            self.basket_text.pos = [
                self.basket_text.pos[0], self.balloon_pic.pos[1]-70]
            self.present_pos = self.present_pos+1
            return 0

    def guess_the_rules(self):
        """猜规则，被试用鼠标左键单击气球，点中哪种颜色的气球则为猜测该种颜色

        函数返回两个参数
        result 为选择的气球 0代表黄气球，1代表绿气球 2代表红气球
        time 为反应时间"""
        clock.reset()
        result = []
        time = []
        while clock.getTime() < present_time:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            xy = mouse.getPos()
            if self.yellow_balloon.contains(xy[0], xy[1]):
                self.yellow_balloon.opacity = 0.3
                self.green_balloon.opacity = 0.1
                self.red_balloon.opacity = 0.1
                if mouse.isPressedIn(self.yellow_balloon):
                    result = 0
                    time = clock.getTime()
                    break
            elif self.green_balloon.contains(xy[0], xy[1]):
                self.green_balloon.opacity = 0.3
                self.yellow_balloon.opacity = 0.1
                self.red_balloon.opacity = 0.1
                if mouse.isPressedIn(self.green_balloon):
                    result = 1
                    time = clock.getTime()
                    break
            elif self.red_balloon.contains(xy[0], xy[1]):
                self.red_balloon.opacity = 0.3
                self.green_balloon.opacity = 0.1
                self.yellow_balloon.opacity = 0.1
                if mouse.isPressedIn(self.red_balloon):
                    result = 2
                    time = clock.getTime()
                    break
            else:
                self.red_balloon.opacity = 0.1
                self.green_balloon.opacity = 0.1
                self.yellow_balloon.opacity = 0.1

            background.draw()

            self.draw()
            win.flip()
        background.draw()
        # if result == 1:
        #     self.success_text.draw()
        self.draw()
        win.flip()

        return result, time

    def showfeedback(self, result):
        """显示反馈，输入参数result是气球的编号

        返回一个bool类型值，True代表正确False代表错误"""
        if result == 1:
            num = int(self.green_ball_text.text)
        elif result == 0:
            num = int(self.yellow_ball_text.text)
        elif result == 2:
            num = int(self.red_ball_text.text)
        else:
            num = 0
        clock.reset()

        if num == self.answer_num:
            while clock.getTime() < feedback_time:
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    save_and_quit()

                correct_text = generate_textMark(
                    0, 0, "√气球上升", 50, color=[255, 67, 17])
                background.draw()

                self.draw()
                correct_text.draw()
                win.flip()
            return True
        else:
            while clock.getTime() < feedback_time:
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    save_and_quit()
                error_text = generate_textMark(0, 0, "×留在原地", 50)
                background.draw()

                self.draw()
                error_text.draw()
                win.flip()
            return False


def save_and_quit():
    """保存后退出"""
    thisExp.saveAsWideText(filename + '.csv', appendFile=True)
    os.chmod(filename + '.csv', stat.S_IREAD)  # 权限改为只读
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    core.quit()


def generate_textMark(x, y, text, size=20,  color=[0, 0, 0]):
    """生成标识数字"""
    textMark = visual.TextStim(
        win=win,
        text=text,
        color=color,
        colorSpace='rgb255',
        pos=(x, y),
        height=size,
        units="pix"
    )
    return textMark


def operator_translate(operators):
    """将+-*/翻译成加减乘除"""
    cn_operator = ""
    if "+" in operators:
        cn_operator = cn_operator + "加"
    if "-" in operators:
        cn_operator = cn_operator + "减"
    if "*" in operators:
        cn_operator = cn_operator + "乘"
    if "/" in operators:
        cn_operator = cn_operator + "除"
    return cn_operator


def one_round(game_level, conditions_f):
    my_balloon = Balloon()
    record = []
    count = 0
    cn_operators = operator_translate(conditions_f[0][1])
    explain.image = "pictures/3.1关卡界面"+cn_operators+"法.png"
    explain.draw()
    level_text = generate_textMark(-90, 90, str(game_level), 41)
    level_text.draw()
    win.flip()
    event.waitKeys()

    for conditioni in conditions_f:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()

        result, rise, re_time = trial(my_balloon, count, int(conditioni[2]), int(conditioni[3]), int(conditioni[4]), int(
            conditioni[5]), int(conditioni[6]), conditioni[0], conditions_f, conditioni, game_level)

        record.append(rise)

        thisExp.addData('level', game_level)
        thisExp.addData('trial', count + 1)
        thisExp.addData('response', result)
        thisExp.addData('result', rise)
        thisExp.addData('response time', re_time)
        thisExp.nextEntry()
        count = count + 1
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

    if record[-1] and record[-2] and record[-3]:
        victory.draw()
        win.flip()
        event.waitKeys()
    else:
        failure.draw()
        win.flip()
        event.waitKeys()

    thisExp.addData('level', game_level)
    thisExp.addData("passed", record[-1] and record[-2] and record[-3])
    thisExp.nextEntry()

    return record[-1] and record[-2] and record[-3]


def trial(my_balloon, n_trial, ytext, rtext, gtext, text1, text2, operator, conditions, conditioni, level):
    """一个试次，前6个参数是气球和篮子上的数字和符号，conditions代表所有试次，conditioni代表本次试次

    level代表第几关"""
    my_balloon.set_num(ytext, rtext,  gtext, text1, text2, operator)

    if conditioni == conditions[-3] and n_trial == trials_in_each_level[level-1]-3:
        intro.image = "pictures/2指导语3.png"
        intro.draw()
        win.flip()
        event.waitKeys()

    result, re_time = my_balloon.guess_the_rules()
    rise = my_balloon.showfeedback(result)
    my_balloon.rise(rise)
    # event.waitKeys()

    return result, rise, re_time


def get_condition(game_level):
    # 获取题目条件,每一次循环获取一关的题目

    # game_level = game_level+1
    conditions_t = []
    conditions_f = []
    mul_conditions = []
    add_conditions = []
    sub_conditions = []
    div_conditions = []
    if game_level > 1:
        for i in range(game_level - 1):
            while trials[0][1] != "":
                trials.pop(0)
            trials.pop(0)

    while trials[0][1] != "":
        # 临时的读取，全部关卡,符号，三个符号位置，红色气球，黄色气球，绿色气球，篮子上左右数字
        conditions_t.append(trials[0][1:])  # 每读取一行，将该行加入到临时条件组中
        if trials[0][1] == "*":  # 下面将改行分类到加减乘除四个组中
            mul_conditions.append(trials[0][1:])
        elif trials[0][1] == "-":
            sub_conditions.append(trials[0][1:])
        elif trials[0][1] == "+":
            add_conditions.append(trials[0][1:])
        elif trials[0][1] == "/":
            div_conditions.append(trials[0][1:])
        trials.pop(0)

    if len(trials) > 0:
        trials.pop(0)

    # 最终的题目条件

    # 将加减乘除每个挑一个加到最终条件组的末尾（用于每一关最后三个trial 测测你学会了吗？ 这里的三个要求必须是三种不同的运算方法）
    if "*" in conditions_t[0][1]:
        conditions_f.append(random.choice(mul_conditions))
        conditions_t.remove(conditions_f[-1])
    if "+" in conditions_t[0][1]:
        conditions_f.append(random.choice(add_conditions))
        conditions_t.remove(conditions_f[-1])
    if "-" in conditions_t[0][1]:
        conditions_f.append(random.choice(sub_conditions))
        conditions_t.remove(conditions_f[-1])
    if "/" in conditions_t[0][1]:
        conditions_f.append(random.choice(div_conditions))
        conditions_t.remove(conditions_f[-1])
    # 将剩余的临时条件组从前面插入到最终条件组
    for i in range(trials_in_each_level[game_level-1]-3):
        conditions_f.insert(0, random.choice(conditions_t))
    a = conditions_f[0: -3]
    b = conditions_f[-3:]
    random.shuffle(a)
    random.shuffle(b)
    conditions_f = a + b
    return conditions_f


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
# from the Builder filename that created this script
expName = 'task2'
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

clock = core.Clock()

present_time = 6.0  # 呈现时间6s
feedback_time = 3.0  # 反馈时间3s

# 窗口
win = visual.Window(
    size=[592, 648],
    units="pix",
    fullscr=False      # fullscr means full-screen mode
)

background = visual.ImageStim(
    win=win,
    image="pictures/1背景.png",
    size=win.size,
    units="pix"
)

if expInfo['session'] == '1' or expInfo['session'] == '01':
    game_level = 1
elif expInfo['session'] == "" and expInfo['participant'] == "" and expInfo['name'] == "":
    # 三个都为空，则被视为调试，
    dlg = gui.Dlg(title="调试模式")

    dlg.addText("检测到三个基础信息都为空，进入调试模式，可以直接进入某一关")
    dlg.addField("关卡：")
    data = dlg.show()
    if dlg.OK == False:
        core.quit()
    print(data)
    game_level = int(data[0])
    filename = _thisDir + os.sep + \
        u'test_data_%s' % (expInfo['date'])
else:
    try:
        os.chmod(filename+'.csv', stat.S_IWRITE)
        with open(filename + '.csv') as f:
            reader = csv.reader(f)

            for row in reader:
                game_level = row[0]  # 读取记录文档的第一列最后一行
            if row[1] == "" and (row[5] == "True" or row[5] == "TRUE"):
                game_level = int(game_level)+1
            else:
                game_level = int(game_level)
    except IOError:
        background.draw()
        remind = generate_textMark(
            0, 0, "没有找到之前训练记录\n请再次确认输入信息是否有误\n按任意键退出", 35)
        remind.draw()
        win.flip()
        event.waitKeys()
        core.quit()

intro = visual.ImageStim(
    win=win,
    image="pictures/2指导语1.png",
    size=win.size,
    units="pix"
)

explain = visual.ImageStim(
    win=win,
    image="pictures/3.1关卡界面加减法.png",
    size=win.size,
    units="pix"
)

balloon = visual.ImageStim(
    win=win,
    image="pictures/气球.png",
    size=[250, 212],
    units="pix"
)

error_feedback = visual.ImageStim(
    win=win,
    image="pictures/4错误反馈.png",
    size=win.size,
    units="pix"
)

correct_feedback = visual.ImageStim(
    win=win,
    image="pictures/4正确反馈.png",
    size=win.size,
    units="pix"
)

victory = visual.ImageStim(
    win=win,
    image="pictures/5闯关成功.png",
    size=win.size,
    units="pix"
)

failure = visual.ImageStim(
    win=win,
    image="pictures/5闯关失败.png",
    size=win.size,
    units="pix"
)
defaultKeyboard = keyboard.Keyboard()


mouse = event.Mouse()
mouse.setVisible(1)

intro.draw()
win.flip()
event.waitKeys()

intro.image = "pictures/2指导语2.png"
intro.draw()
win.flip()
event.waitKeys()

# 打开文件读取关卡信息
with open("game_level.csv", "r") as file:
    reader = csv.reader(file)
    trials = list(reader)

end_level = game_level+6
trials_in_each_level = [12, 12, 12, 9, 9, 9, 9, 12,
                        12, 9, 9, 9, 9, 12, 12, 9, 9, 9, 9]  # 每关的试次数量，固定的


while game_level < end_level or len(trials) == 0:

    if defaultKeyboard.getKeys(keyList=["escape"]):
        save_and_quit()
    temp_level = game_level
    conditions_i = get_condition(game_level)
    passed = one_round(game_level, conditions_i)

    if passed:  # 通关
        game_level = game_level + 1
    else:  # 未通关，则重复这一关
        round_clock = core.Clock()
        round_clock.reset()
        while round_clock.getTime() < 180:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            passed = one_round(game_level, conditions_i)
            if passed:
                game_level = game_level + 1
                break

        if temp_level == game_level:
            # 超过3分钟，还是没有过关直接进入下一关
            game_level = game_level+1

thisExp.saveAsWideText(filename + '.csv', appendFile=True)
os.chmod(filename + '.csv', stat.S_IREAD)  # 权限改为只读
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
core.wait(2)
win.close()
