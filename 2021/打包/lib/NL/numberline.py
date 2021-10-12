from psychopy import visual, event, core, gui, data
from pyglet.window import key
from psychopy.hardware import keyboard


import os
import random
import datetime
import sys
import csv
import copy
from math import ceil

# 现在就是按照难度固定，实际位置和标识位置的距离固定


class Numberline():
    """数轴类，创建数轴，显示答案，操作数轴等，都由这个类来完成"""

    def __init__(self, length, y, answer):
        """初始化方法"""
        self.length = length  # 轴的数值长度，也就是标出来的长度
        self.L = 700  # 轴的像素长度，也就是物理长度
        self.y = y
        self.ans = answer
        self.mark_pos = 0
        self.tolerance = [0.10, 0.16, 0.20]
        self.main_axis = generate_Line(-490, y, +490, y)
        self.start_bar = generate_Line(-self.L/2, y - 10, -self.L/2, y + 10)
        self.end_bar = generate_Line(+self.L/2, y - 10, +self.L/2, y + 10)
        self.zero_mark = generate_textMark(-self.L/2, y - 30, "0")
        self.max_mark = generate_textMark(+self.L/2, y - 30, str(length))
        self.triangle_mark = visual.ShapeStim(
            win=win,
            fillColor=[28, 214, 108],
            colorSpace='rgb255',
            lineWidth=0,
            vertices=[[0, 0], [-10, 16], [10, 16]],
            pos=[-self.L/2, y]
        )
        self.ans_bar = generate_Line(-self.L/2 + answer / length *
                                     self.L, y + 10, -self.L/2 + answer / length * self.L, y, color=[26, 161, 95], lineWidth=4)
        self.ans_text = generate_textMark(-self.L/2 + answer / length *
                                          self.L, y - 20, str(answer), 20, color=[47, 127, 247])
        self.start_arrow = visual.ShapeStim(
            win=win,
            lineColor="black",
            fillColor="black",
            units="pix",
            vertices=[[-5, 0], [0, 5], [0, -5]],
            pos=[-490, y]
        )
        self.end_arrow = visual.ShapeStim(
            win=win,
            lineColor="black",
            fillColor="black",
            units="pix",
            vertices=[[5, 0], [0, +5], [0, -5]],
            pos=[490, y]
        )
        self.frog = visual.ImageStim(
            win=win,
            image="Picture/frog.png",
            units="pix",
            size=[60, 60]
        )
        self.frog.pos = [self.triangle_mark.pos[0], y+45]
        self.rabbit = visual.ImageStim(
            win=win,
            image="Picture/rabbit2.png",
            units="pix",
            size=[60, 60]
        )
        self.rabbit.pos = [self.triangle_mark.pos[0], y+45]
        self.rabbit_opp = visual.ImageStim(
            win=win,
            image="Picture/rabbit2_opp.png",
            units="pix",
            size=[60, 60]
        )
        self.rabbit_opp.pos = [self.triangle_mark.pos[0], y+45]

    def frog_rabbit_draw(self, frog_or_rabbit):
        if frog_or_rabbit == 0:
            self.frog.draw()
        elif frog_or_rabbit == 1:
            self.rabbit.draw()
        else:
            self.rabbit_opp.draw()

    def draw(self):
        """画出数轴，包括主轴，0和终点的标识以及箭头等"""
        self.main_axis.draw()
        self.start_bar.draw()
        self.end_bar.draw()
        self.zero_mark.draw()
        self.max_mark.draw()
        self.triangle_mark.draw()
        self.start_arrow.draw()
        self.end_arrow.draw()

    def set_mark_pos(self):
        self.mark_pos = (
            self.triangle_mark.pos[0] + self.L/2) / self.L * self.length

    def get_mark_pos(self):
        return self.mark_pos

    def is_correct(self):
        return ((self.mark_pos-self.ans)**2)**0.5 < [x*self.length for x in self.tolerance]

    def show_feedback(self, show_ans=True):
        ans_pos = self.ans / self.length * self.L - self.L / 2
        max_tolerance_1 = self.ans + self.length * self.tolerance[0]
        min_tolerance_1 = self.ans - self.length * self.tolerance[0]

        gap = (max_tolerance_1 - min_tolerance_1)/10

        y1 = self.y
        y2 = self.y + 10
        scale_marks = []

        for i in range(1, 5):
            scale_marks.append(generate_Line((max_tolerance_1 - i * gap) / self.length * self.L - self.L / 2,
                                             y1, (max_tolerance_1 - i * gap) / self.length * self.L - self.L / 2, y2, color=[26, 161, 95], lineWidth=3, opacity=0.5))
        for i in range(1, 5):
            scale_marks.append(generate_Line((min_tolerance_1 + i * gap) / self.length * self.L - self.L / 2,
                                             y1, (min_tolerance_1 + i * gap) / self.length * self.L - self.L / 2, y2, color=[26, 161, 95], lineWidth=3, opacity=0.5))
        scale_marks.append(generate_Line(max_tolerance_1 / self.length * self.L - self.L / 2,
                                         y1, max_tolerance_1 / self.length * self.L - self.L / 2, y2, color=[26, 161, 95], lineWidth=4))
        scale_marks.append(generate_Line(min_tolerance_1/self.length*self.L-self.L/2,
                                         y1, min_tolerance_1 / self.length * self.L - self.L / 2, y2, color=[26, 161, 95], lineWidth=4))

        self.ans_bar.draw()
        if show_ans:
            self.ans_text.draw()
        for scale_mark_i in scale_marks:
            scale_mark_i.draw()

    def slider(self, mouse, text_mark, first=True, frog_or_rabbit=0, is_practice=False):
        no_operation = True
        if not first:
            triangle_1 = copy.copy(self.triangle_mark)
            self.triangle_mark.fillColor = [45, 195, 213]
        while clock.getTime() < 10:
            background.draw()
            my_progress_bar.draw(is_practice)
            score_text.draw()
            if frog_or_rabbit != 3:
                self.frog_rabbit_draw(frog_or_rabbit)
            self.draw()
            text_mark.draw()
            if text_mark.text == "+" or text_mark.text == "-":
                frog.draw()
                rabbit.draw()
            win.flip()
            if defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            if mouse.isPressedIn(self.triangle_mark):
                no_operation = False
                while clock.getTime() < 10:
                    buttons = mouse.getPressed(getTime=False)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    if buttons == [1, 0, 0]:
                        background.draw()
                        my_progress_bar.draw(is_practice)
                        score_text.draw()
                        if frog_or_rabbit != 3:
                            self.frog_rabbit_draw(frog_or_rabbit)
                        self.draw()
                        if not first:
                            triangle_1.draw()
                        text_mark.draw()
                        if text_mark.text == "+" or text_mark.text == "-":
                            frog.draw()
                            rabbit.draw()
                        win.flip()
                        mouse_pos = mouse.getPos()
                        self.triangle_mark.pos = [mouse_pos[0], self.y]
                        mouse.clickReset()
                    else:
                        break
                break
        return no_operation, clock.getTime()

    def jump(self, jump_length, frog_or_rabbit=0, is_practice=False):
        if frog_or_rabbit == 0:
            temp = self.frog
        elif frog_or_rabbit == 1:
            temp = self.rabbit
        else:
            temp = self.rabbit_opp
        x0 = temp.pos[0]
        y0 = temp.pos[1]
        clock.reset()
        t = clock.getTime()
        if frog_or_rabbit == 2:
            while t < 0.5:
                t = clock.getTime()
                x = x0 - 2 * t * jump_length * self.L / self.length
                y = y0 + 2*t*(1-2*t) * 200
                temp.pos = [x, y]
                background.draw()
                my_progress_bar.draw(is_practice)
                score_text.draw()
                temp.draw()
                self.draw()
                win.flip()
        else:
            while t < 0.5:
                t = clock.getTime()
                x = x0 + 2 * t * jump_length * self.L / self.length
                # 这是原公式，不知道为什么会出错，然后化简之后就是下面的y，把平方项约掉了
                # y = y0 + (2 * jump_length ** 2 * t - 4 *
                #           jump_length ** 2 * t ** 2) * self.L / self.length/(jump_length**2)*20
                # 又做了修改，直接×一个常数，也就是不论多远跳的一样高
                y = y0+2*t*(1-2*t)*200
                temp.pos = [x, y]
                background.draw()
                my_progress_bar.draw(is_practice)
                score_text.draw()
                temp.draw()
                self.draw()
                win.flip()
        temp.pos = [self.triangle_mark.pos[0], y0]
        # temp.pos[0] = self.triangle_mark.pos[0]
        # temp.pos[1] = y0
        # 不要这样去赋值pos，draw（）的时候位置会不变，虽然pos值变了，但是画出来位置还是没变，跟draw函数源码有关系，目前没搞清楚为啥

    def pos_translate(self, pos):
        return +pos/self.length*self.L-self.L/2


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


def match_tirals(length, frog_or_rabbit, is_practice):
    """匹配任务
    length代表长度（50，100，200）
    frog_or_rabbit表示选择青蛙还是兔子，0表示青蛙，1表示兔子"""
    mouse = event.Mouse()
    mouse.setVisible(1)

    ans_pos = random.randint(1, length-1)
    text_ans = generate_textMark(0, 150, str(
        ans_pos), 32)

    my_numberline = Numberline(length, -50, ans_pos)
    no_operation = True
    numberlineRecord = []

    clock.reset()
    mouse.clickReset()
    # 拖动圆点，至合适位置 no_operation表示是否进行操作
    no_operation, time = my_numberline.slider(
        mouse, text_ans, first=True, frog_or_rabbit=frog_or_rabbit, is_practice=is_practice)

    my_numberline.set_mark_pos()
    my_numberline.jump(my_numberline.get_mark_pos(),
                       frog_or_rabbit, is_practice=is_practice)
    clock.reset()
    is_correct = my_numberline.is_correct()
    if no_operation:
        is_correct = False
    while clock.getTime() < 3.0:  # 反馈时间
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        background.draw()
        my_progress_bar.draw(is_practice)
        score_text.draw()
        my_numberline.draw()
        score = 0
        if no_operation:
            text_response = generate_textMark(0, 150, "未操作!", 50)
            text.draw()
        else:
            my_numberline.frog_rabbit_draw(frog_or_rabbit)
            my_numberline.show_feedback()
            if is_correct[0]:
                gold_medal.draw()
                text_score = generate_textMark(
                    150, 150, "+5", 40, [226, 32, 24])
                text_score.draw()
                score = 5
            else:
                if is_correct[1]:
                    silver_medal.draw()
                    text_score = generate_textMark(
                        150, 150, "+3", 40, [226, 32, 24])
                    score = 3
                elif is_correct[2]:
                    copper_medal.draw()
                    text_score = generate_textMark(
                        150, 150, "+2", 40, [226, 32, 24])
                    score = 2
                else:
                    text_score = generate_textMark(
                        150, 150, "0", 40, [226, 32, 24])
                    score = 0
                text_score.draw()
            score_text.text = "得分:" + str(cumulative_score + score)
            score_text.draw()
            win.flip()

    return my_numberline.mark_pos, ans_pos, time, score


def computing_trials(length, add_trial, is_practice):
    """数值运算任务
    length代表数轴长度
    add_trial代表加减法，add_trial取True为加法，反之为减法"""
    mouse = event.Mouse()
    mouse.setVisible(1)

    if add_trial:
        ans_pos = random.randint(1, length-1)  # 答案数量
        addend_1 = round(random.uniform(1, ans_pos-1))  # 加数1
        addend_2 = ans_pos - addend_1  # 加数2
        formula = str(addend_1) + " + " + str(addend_2) + " = ?"  # 生成公式
    else:
        minuend = random.randint(2, length - 1)  # 被减数
        subtractor = random.randint(1, minuend - 1)  # 减数
        ans_pos = minuend - subtractor
        formula = str(minuend) + " - " + str(subtractor) + " = ?"

    text_formula = generate_textMark(
        0, 150, formula, 32)

    my_numberline = Numberline(length, -50, ans_pos)
    no_operation = True

    time = [-1, -1, -1]
    clock.reset()
    mouse.clickReset()
    # 拖动三角，至合适位置 no_operation表示是否进行操作
    no_operation, time[0] = my_numberline.slider(
        mouse, text_formula, is_practice=is_practice)

    my_numberline.set_mark_pos()
    op_1_pos = my_numberline.get_mark_pos()
    my_numberline.jump(op_1_pos, 0, is_practice=is_practice)

    my_numberline.rabbit.pos[0] = my_numberline.pos_translate(op_1_pos)
    my_numberline.rabbit_opp.pos[0] = my_numberline.pos_translate(op_1_pos)
    clock.reset()
    mouse.clickReset()
    no_operation, time[1] = my_numberline.slider(
        mouse, text_formula, first=False, frog_or_rabbit=-int(add_trial)+2, is_practice=is_practice)
    my_numberline.set_mark_pos()
    op_2_pos = my_numberline.get_mark_pos()
    my_numberline.jump(((my_numberline.get_mark_pos()-op_1_pos)**2)**0.5,
                       frog_or_rabbit=-int(add_trial) + 2, is_practice=is_practice)

    # 第一遍反馈
    clock.reset()
    if no_operation:
        is_correct = False
    while clock.getTime() < 3.0:  # 反馈时间
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        background.draw()
        my_progress_bar.draw(is_practice)
        score_text.draw()
        my_numberline.draw()
        score = 0
        if no_operation:
            text_response = generate_textMark(0, 150, "未操作!", 50)
            text_response.draw()
        else:
            my_numberline.frog_rabbit_draw(0)
            my_numberline.frog_rabbit_draw(frog_or_rabbit=-int(add_trial) + 2)
            my_numberline.show_feedback(show_ans=False)
            win.flip()
    my_numberline_2 = Numberline(length, -50, ans_pos)
    no_operation = True
    numberlineRecord = []

    clock.reset()
    mouse.clickReset()
    no_operation, time[2] = my_numberline_2.slider(
        mouse, text_formula, first=True, frog_or_rabbit=3, is_practice=is_practice)

    my_numberline_2.set_mark_pos()
    op_3_pos = my_numberline_2.get_mark_pos()
    is_correct = my_numberline_2.is_correct()
    clock.reset()
    if no_operation:
        is_correct = False
    while clock.getTime() < 3.0:  # 反馈时间
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        background.draw()
        my_progress_bar.draw(is_practice)
        score_text.draw()
        my_numberline_2.draw()
        score = 0
        if no_operation:
            text_response = generate_textMark(0, 150, "未操作!", 50)
            text_response.draw()
        else:
            my_numberline.show_feedback()
            if is_correct[0]:
                gold_medal.draw()
                text_score = generate_textMark(
                    150, 150, "+5", 40, [226, 32, 24])
                text_score.draw()
                score = 5
            else:
                if is_correct[1]:
                    silver_medal.draw()
                    text_score = generate_textMark(
                        150, 150, "+3", 40, [226, 32, 24])
                    score = 3
                elif is_correct[2]:
                    copper_medal.draw()
                    text_score = generate_textMark(
                        150, 150, "+2", 40, [226, 32, 24])
                    score = 2
                else:
                    text_score = generate_textMark(
                        150, 150, "0", 40, [226, 32, 24])
                    score = 0
                text_score.draw()
            score_text.text = "得分:"+str(cumulative_score+score)
            score_text.draw()
            win.flip()
    reaction_pos = [op_1_pos, op_2_pos, op_3_pos]
    return reaction_pos, ans_pos, time, score


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


def generate_Line(startx, starty, endx, endy, color=[0, 0, 0], lineWidth=2, opacity=1):
    """画线"""
    line = visual.Line(
        win=win,
        units="pix",
        lineColor=color,
        colorSpace="rgb255",
        opacity=opacity
    )

    line.lineWidth = lineWidth

    line.start = [startx, starty]
    line.end = [endx, endy]

    return line


def generate_rectangle(length, height, pos=[0, 0], fillColor=[255, 255, 255], lineColor=[255, 255, 255]):
    rectangle = visual.Rect(
        win=win,
        size=[length, height],
        pos=pos,
        fillColor=fillColor,
        lineColor=lineColor,
        colorSpace="rgb255"
    )

    return rectangle


def numberline_trials(length, add_trial, is_practice):
    """数周运算匹配数轴位置
    """
    mouse = event.Mouse()
    mouse.setVisible(1)

    # 正确答案的位置：0+difficulty*length 到 length-difficulty*length
    ans_pos = random.randint(2, length - 1)

    ran = random.getrandbits(1)
    Xs = [50, -50]
    if add_trial:  # 加法
        pos_1 = random.randint(1, ans_pos-1)
        pos_2 = ans_pos - pos_1
        hint_text = generate_textMark(0, 230, "+", 60)
        frog.pos = [Xs[ran], 230]
        rabbit.pos = [Xs[int(not bool(ran))], 230]
    else:
        pos_1 = random.randint(ans_pos + 1, length)
        pos_2 = pos_1 - ans_pos
        hint_text = generate_textMark(0, 230, "-", 60)
        frog.pos = [Xs[ran], 230]
        rabbit.pos = [Xs[int(not bool(ran))], 230]
    question_mark = generate_textMark(100, 230, "= ?", 55)
    choices = [pos_1, pos_2]
    frog_numberline = Numberline(length, 90, choices[ran])
    frog_numberline.triangle_mark.pos = [
        frog_numberline.L * pos_1 / length - frog_numberline.L / 2, frog_numberline.y]
    frog_numberline.frog.pos[0] = frog_numberline.triangle_mark.pos[0]
    rabbit_numberline = Numberline(length, -110, choices[int(not bool(ran))])
    rabbit_numberline.triangle_mark.pos = [
        rabbit_numberline.L * pos_2 / length - rabbit_numberline.L / 2, rabbit_numberline.y]
    rabbit_numberline.rabbit.pos[0] = rabbit_numberline.triangle_mark.pos[0]

    # text_ans = generate_textMark(0, 100, str(ans_pos), 25, [1, 217 / 255, 9 / 255])

    clock.reset()
    while clock.getTime() < 4:
        background.draw()
        my_progress_bar.draw(is_practice)
        score_text.draw()
        frog_numberline.draw()
        frog_numberline.frog_rabbit_draw(0)
        rabbit_numberline.draw()
        rabbit_numberline.frog_rabbit_draw(1)
        hint_text.draw()
        question_mark.draw()
        frog.draw()
        rabbit.draw()
        win.flip()

    my_numberline = Numberline(length, -50, ans_pos)
    no_operation = True
    numberlineRecord = []

    clock.reset()
    mouse.clickReset()
    no_operation, time = my_numberline.slider(
        mouse, hint_text, first=True, frog_or_rabbit=3, is_practice=is_practice)

    my_numberline.set_mark_pos()
    # my_numberline.jump(my_numberline.get_mark_pos())
    is_correct = my_numberline.is_correct()
    clock.reset()
    if no_operation:
        is_correct = False
    while clock.getTime() < 3.0:  # 反馈时间
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        background.draw()
        my_progress_bar.draw(is_practice)
        score_text.draw()
        my_numberline.draw()
        score = 0
        if no_operation:
            text_response = generate_textMark(0, 150, "未操作!", 50)
            text.draw()
        else:
            my_numberline.show_feedback()
            if is_correct[0]:
                gold_medal.draw()
                text_score = generate_textMark(
                    150, 150, "+5", 40, [226, 32, 24])
                text_score.draw()
                score = 5
            else:
                if is_correct[1]:
                    silver_medal.draw()
                    text_score = generate_textMark(
                        150, 150, "+3", 40, [226, 32, 24])
                    score = 3
                elif is_correct[2]:
                    copper_medal.draw()
                    text_score = generate_textMark(
                        150, 150, "+2", 40, [226, 32, 24])
                    score = 2
                else:
                    text_score = generate_textMark(
                        150, 150, "0", 40, [226, 32, 24])
                    score = 0
                text_score.draw()
            score_text.text = "得分:"+str(cumulative_score+score)
            score_text.draw()
            win.flip()

    return my_numberline.mark_pos, ans_pos, time, score


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
# from the Builder filename that created this script
expName = 'NL'
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
    u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['session'])
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=os.path.abspath(__file__),
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# 窗口
win = visual.Window(
    size=[1200, 800],
    units="pix",
    fullscr=False           # fullscr means full-screen mode
)


defaultKeyboard = keyboard.Keyboard()

difficulty_s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

length_s = [50, 100, 200]

trial_duration_s = 4.0  # 4000ms的刺激呈现时间

trials_in_block = 30

text = visual.TextStim(win=win)

background = visual.ImageStim(
    win=win,
    image="Picture/response.png",
    units='pix',
    size=win.size,
)

silver_medal = visual.ImageStim(
    win=win,
    image="Picture/medal2.png",
    units="pix",
    size=[80, 110],
    pos=[0, 200]
)

gold_medal = visual.ImageStim(
    win=win,
    image="Picture/medal1.png",
    units="pix",
    size=[80, 110],
    pos=[0, 200]
)

copper_medal = visual.ImageStim(
    win=win,
    image="Picture/medal3.png",
    units="pix",
    size=[80, 110],
    pos=[0, 200]
)

intro = visual.ImageStim(
    win=win,
    image="Picture/intro.png",
    units="pix",
    size=win.size
)

bell = visual.ImageStim(
    win=win,
    image="Picture/bell.png",
    units="pix",
    size=[70, 70]
)

frog = visual.ImageStim(
    win=win,
    image="Picture/frog.png",
    units="pix",
    size=[40, 40]
)
rabbit = visual.ImageStim(
    win=win,
    image="Picture/rabbit2.png",
    units="pix",
    size=[40, 40]
)

intro.draw()
win.flip()
event.waitKeys()


clock = core.Clock()

cumulative_score = 0
score_text = generate_textMark(
    0, -300, "得分:"+str(cumulative_score), 30, color=[216, 77, 65])

my_progress_bar = Progress_bar(600, core.Clock(), win.size[1]/2-20)
# # 练习部分
if expInfo['session'] == '01' or expInfo['session'] == '1':

    intro.image = "Picture/introTask1.png"
    intro.draw()
    win.flip()
    event.waitKeys()

    reaction_pos, correct_pos, time, score = match_tirals(
        50, frog_or_rabbit=0, is_practice=True)

    score_text.text = "得分:"+str(cumulative_score)
    intro.image = "Picture/introTask2.png"
    intro.draw()
    win.flip()
    event.waitKeys()

    reaction_pos, correct_pos, time, score = computing_trials(
        50, add_trial=False, is_practice=True)

    score_text.text = "得分:"+str(cumulative_score)
    intro.image = "Picture/introTask3.png"
    intro.draw()
    win.flip()
    event.waitKeys()

    reaction_pos, correct_pos, time, score = computing_trials(
        50, add_trial=True, is_practice=True)

    score_text.text = "得分:"+str(cumulative_score)
    intro.image = "Picture/introTask4.png"
    intro.draw()
    win.flip()
    event.waitKeys()

    reaction_pos, correct_pos, time, score = numberline_trials(
        50, add_trial=True, is_practice=True)

    score_text.text = "得分:"+str(cumulative_score)
    intro.image = "Picture/introTask5.png"
    intro.draw()
    win.flip()
    event.waitKeys()

    reaction_pos, correct_pos, time, score = numberline_trials(
        50, add_trial=False, is_practice=True)

background.draw()
score_text.text = "得分:"+str(cumulative_score)
intro.image = "Picture/正式开始.png"
intro.draw()
win.flip()
event.waitKeys()
my_progress_bar.my_clock.reset()
trials = 0
half_time = False
for mode_i in difficulty_s:
    clock.reset()
    mode = mode_i % 5
    length_difficulty = int((mode_i-1) / 5)
    correct = 0
    trial_clock = core.Clock()
    if mode == 1:
        intro.image = "Picture/introTask1.png"
    elif mode == 2:
        intro.image = "Picture/introTask3.png"
    elif mode == 3:
        intro.image = "Picture/introTask2.png"
    elif mode == 4:
        intro.image = "Picture/introTask4.png"
    else:
        intro.image = "Picture/introTask5.png"
    clock.reset()
    while clock.getTime() < 1:
        # if frog_or_rabbit == 0:
        #     intro.image = "Picture/标位置fro.png"
        # else:
        #     intro.image = "Picture/标位置rabb.png"
        intro.draw()
        my_progress_bar.draw(is_practice=False)
        win.flip()
    while correct < 5:
        if mode == 1:  # 匹配任务
            frog_or_rabbit = random.getrandbits(1)
            reaction_pos, correct_pos, time, score = match_tirals(
                length_s[length_difficulty], frog_or_rabbit=frog_or_rabbit, is_practice=False)
        elif mode == 2:  # 公式计算,加法
            reaction_pos, correct_pos, time, score = computing_trials(
                length_s[length_difficulty], add_trial=True, is_practice=False)
        elif mode == 3:  # 公式计算,减法
            reaction_pos, correct_pos, time, score = computing_trials(
                length_s[length_difficulty], add_trial=False, is_practice=False)
        elif mode == 4:  # 数轴运算，加法
            reaction_pos, correct_pos, time, score = numberline_trials(
                length_s[length_difficulty], add_trial=True, is_practice=False)
        else:  # 数轴运算,减法
            reaction_pos, correct_pos, time, score = numberline_trials(
                length_s[length_difficulty], add_trial=False, is_practice=False)
        correct += int(score / 5)
        cumulative_score += score
        trials += 1
        if isinstance(reaction_pos, list):
            precision = ((reaction_pos[2] - correct_pos)
                         ** 2) ** 0.5 / length_s[length_difficulty]
        else:
            precision = ((reaction_pos - correct_pos) **
                         2) ** 0.5 / length_s[length_difficulty]
        # 保存结果

        thisExp.addData('trial', trials)
        thisExp.addData('answer pos', correct_pos)
        thisExp.addData('reaction pos', reaction_pos)
        thisExp.addData('accuracy', int(score/5))
        thisExp.addData('mode', mode_i)
        thisExp.addData('score', score)
        thisExp.addData('precision', precision)
        thisExp.addData('response time', time)
        thisExp.nextEntry()

        if trial_clock.getTime() > 180.0:
            break
        if my_progress_bar.getTime() >= 300 and half_time == False:
            half_time = True
            intro.image = "Picture/half_alert.png"
            bell.pos = [0, win.size[0]*0.125]
            intro.draw()
            bell.draw()
            win.flip()
            event.waitKeys()
        if my_progress_bar.getTime() >= 603:

            break

    if my_progress_bar.getTime() >= 603:
        break
intro.image = "Picture/time_alert.png"
bell.pos = [0, win.size[0]*0.125]
total_score = generate_textMark(
    win.size[0]*0.13, win.size[0]*0.125, "总得分：" + str(score), 35, color=[255, 1, 26])
intro.draw()
bell.draw()
total_score.draw()
win.flip()
event.waitKeys()
thisExp.saveAsWideText(filename + '.csv', appendFile=True)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
core.wait(2)
win.close()
