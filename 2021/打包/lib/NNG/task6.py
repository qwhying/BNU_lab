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


class Progress_bar():
    """进度条，用于显示所剩时间"""

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
                8, 25, [-self.width / 2 + i*gap, self.y]))

    def reset(self):
        self.my_clock.reset()

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


class Integer_unit():
    """整数坐标点（用来组成100个点阵），将圆形图案和文字组合成一个整体，单独作为一个类"""

    def __init__(self, value, x, y):
        self.x = x
        self.y = y
        self.value = value
        self.circle = visual.Circle(
            win=win,
            units='pix',
            size=[35, 35],
            opacity=0.3,
            colorSpace='rgb255',
            fillColor=[14, 82, 152],
            lineWidth=0,
            pos=[x, y]
        )
        self.circle.opacity = 0.15
        self.text = generate_textMark(x, y, str(value), 20, [255, 255, 255])

    def draw(self):
        self.circle.draw()
        self.text.draw()


class my_button():
    """生成按钮"""

    def __init__(self, length, height, text, pos=[0, 0], textColor=[0, 0, 0], textSize=20, fillColor=[255, 255, 255], lineColor=[255, 255, 255]):
        self.button = generate_button(
            length, height, pos, fillColor, lineColor)
        self.text = generate_textMark(
            pos[0], pos[1], text, textSize, textColor)

    def draw(self):
        self.button.draw()
        self.text.draw()


class my_arrow():
    def __init__(self, startx, starty, endx, endy, color=[0, 0, 0], lineWidth=2, opacity=1):
        # 以终点为原点，转换为极坐标，通过旋转，画出箭头
        theta = math.atan2(starty-endy, startx-endx)  # 这个角度是以终点为原点，起点的角度θ
        r = 6
        end_x = endx + r * math.cos(theta)
        end_y = endy + r * math.sin(theta)
        start_x = startx - r * math.cos(theta)
        start_y = starty-r*math.sin(theta)
        self.line = line = visual.Line(
            win=win,
            units="pix",
            lineColor=color,
            colorSpace="rgb255",
            opacity=opacity
        )
        line.lineWidth = lineWidth

        line.start = [start_x, start_y]
        line.end = [end_x, end_y]
        # self.k = (endy - starty) / (endx - startx)
        self.r = 20

        # 将起点的角度θ，分别顺时针和逆时针旋转45°得到箭头两个点的角度θ1和θ2
        theta1 = theta + math.pi/6
        theta2 = theta - math.pi/6
        # 将极坐标转换回直角坐标
        self.points = [[0, 0], [self.r * math.cos(theta1), self.r * math.sin(theta1)], [
            self.r * math.cos(theta2), self.r * math.sin(theta2)]]
        # point_1 = [self.r * math.cos(theta1), self.r * math.sin(theta1)]
        # point_2 = [self.r * math.cos(theta2), self.r * math.sin(theta2)]

        self.arrowhead = visual.ShapeStim(
            win=win,
            vertices=self.points,
            colorSpace='rgb255',
            fillColor=color,
            lineWidth=0,
            pos=[endx, endy]
        )

    def draw(self):
        self.arrowhead.draw()
        self.line.draw()
        # self.arrowhead.draw()


class side_bar():
    """画面左侧一栏，包括路径显示，加减乘除按键和奖牌显示"""

    def __init__(self, pos=[-300, 0], is_energy=True):
        """初始化
        pos为位置
        is_energy为模式选择，is_energy为True时为最小能量模式，如果is_energy为False则为最小步数模式"""
        self.button_width = 80/1800*win.size[0]
        self.button_height = 40/1000*win.size[1]
        self.text_height = self.button_height
        self.button_fillColor = [47, 127, 248]
        self.button_fillColor_cancel = [220, 80, 67]
        self.button_lineColor = [47, 127, 248]
        # 显示终点位置的标题

        self.scroll = visual.ImageStim(
            win=win,
            image="NNG_Picture/interface_小图标/feedback1.png",
            size=[win.size[0]/4.5, win.size[1]*0.25],
            units="pix",
            pos=[- win.size[0] / 2.6471, -win.size[1]*0.35]
        )
        self.gold_medal = visual.ImageStim(
            win=win,
            image="NNG_Picture/interface_小图标/feedback2.png",
            size=[70, 80],
            units="pix",
            pos=[- win.size[0]/2.2785, -win.size[1]*0.32]
        )
        self.silver_medal = visual.ImageStim(
            win=win,
            image="NNG_Picture/interface_小图标/feedback3.png",
            size=[70, 80],
            units="pix",
            pos=[- win.size[0]/2.2785, -win.size[1]*0.32]
        )
        self.medal_number_text = generate_textMark(
            - win.size[0]/2.8, -win.size[1]*0.32, str(medal), 35, color=[255, 255, 255])
        # 能量或者步数
        if is_energy:
            self.is_energy = True
            self.score_image = energy
        else:
            self.is_energy = False
            self.score_image = step
        self.step = 0
        self.energy = 0
        self.score_image.pos = [-win.size[0]/2.4, -win.size[1]*0.19]
        self.score_text = generate_textMark(-win.size[0]/2.7692, -
                                            win.size[1] * 0.19, "0", size=40, color=[255, 255, 255])
        # 下面四个是加减乘除四则运算符号按键
        self.button_plus = my_button(self.button_width, self.button_height, "+", [pos[0] - self.button_width/2-10, pos[1] + self.button_height+30], textColor=[
                                     255, 255, 255], textSize=self.text_height, fillColor=self.button_fillColor, lineColor=self.button_lineColor)
        self.button_minus = my_button(self.button_width, self.button_height, "-", [pos[0] + self.button_width/2+10, pos[1] + self.button_height+30], textColor=[
                                      255, 255, 255], textSize=self.text_height, fillColor=self.button_fillColor, lineColor=self.button_lineColor)
        self.button_multi = my_button(self.button_width, self.button_height, "×", [pos[0] - self.button_width/2-10, pos[1] - self.button_height+30], textColor=[
                                      255, 255, 255], textSize=self.text_height, fillColor=self.button_fillColor, lineColor=self.button_lineColor)
        self.button_divisor = my_button(self.button_width, self.button_height, "÷", [pos[0] + self.button_width/2+10, pos[1] - self.button_height+30], textColor=[
                                        255, 255, 255], textSize=self.text_height, fillColor=self.button_fillColor, lineColor=self.button_lineColor)
        self.button_cancel = my_button(self.button_width, self.button_height, "取消", [pos[0], pos[1] - 2*self.button_height], textColor=[
            255, 255, 255], textSize=(self.text_height*0.75), fillColor=self.button_fillColor_cancel, lineColor=self.button_fillColor_cancel)

    def reset_score(self):
        self.energy = 0
        self.step = 0
        self.score_text.text = str(0)

    def set_score(self, score):
        self.step = self.step + 1
        self.energy = self.energy+score
        if self.is_energy:
            self.score_text.text = str(self.energy)
        else:
            self.score_text.text = str(self.step)

    def draw(self, is_explore=False):
        self.button_divisor.draw()
        self.button_minus.draw()
        self.button_plus.draw()
        self.button_multi.draw()
        self.button_cancel.draw()
        if not is_explore:
            self.score_image.draw()
            self.score_text.draw()
            self.scroll.draw()
            self.gold_medal.draw()
            self.medal_number_text.draw()

    def click(self, mouse, this_map, is_explore=False):
        clicked = []
        clock.reset()
        while clock.getTime() < 5:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            background.draw()
            my_progress_bar.draw(is_practice=is_explore)
            this_map.draw(is_explore=is_explore)
            self.draw(is_explore=is_explore)
            win.flip()

            if mouse.isPressedIn(self.button_plus.button):
                self.button_plus.button.fillColor = [220, 80, 67]
                clicked = "+"
                break
            elif mouse.isPressedIn(self.button_minus.button):
                self.button_minus.button.fillColor = [220, 80, 67]
                clicked = "-"
                break
            elif mouse.isPressedIn(self.button_multi.button):
                self.button_multi.button.fillColor = [220, 80, 67]
                clicked = "×"
                break
            elif mouse.isPressedIn(self.button_divisor.button):
                self.button_divisor.button.fillColor = [220, 80, 67]
                clicked = "÷"
                break
        if len(clicked) > 0:
            background.draw()
            my_progress_bar.draw(is_practice=is_explore)
            this_map.draw(is_explore=is_explore)
            self.draw(is_explore=is_explore)
            win.flip()

            # self.color_restore()

        return clicked

    # def cancel(self,mouse,this_map):

    def color_restore(self):
        self.button_plus.button.fillColor = self.button_fillColor
        self.button_minus.button.fillColor = self.button_fillColor
        self.button_multi.button.fillColor = self.button_fillColor
        self.button_divisor.button.fillColor = self.button_fillColor


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


class my_map():
    """地图"""

    def __init__(self, pos, start_point, end_point, covered_points=[]):
        """start_point起点数值，end_point终点数值
        covered_points是一个数组（列表）存放被黑洞遮挡的point数值
        pos为地图整体的位置"""
        self.covered_points = covered_points
        self.present_point = start_point
        self.present_point_textmark = generate_textMark(
            - win.size[0] / 2.6471, win.size[1] / 3.3, self.present_point, 45, [255, 255, 255])
        self.start_point = start_point
        self.end_point = end_point
        self.fillColor = [14, 82, 152]
        self.covered_fillColor = [226, 32, 24]
        # 创建左侧一栏
        my_map, my_box = generate_map(pos[0], pos[1], win.size[0] / 14.4, win.size[1] /
                                      11.37, start_point, end_point, covered_points=covered_points)
        self.map = my_map
        self.boxes = my_box
        self.path = []

    def draw(self, is_explore=False, dynamic=False):
        """作画
        dynamic表示动态的，飞船在移动的时候使用，（也就是动画演示的几秒钟内），默认为静态"""
        if dynamic:
            for i in range(len(self.map)):
                self.map[i].draw()
        else:
            self.map[-1].pos = self.map[self.present_point - 1].circle.pos
            for i in range(len(self.map)):
                self.map[i].draw()
        for i in range(len(self.boxes)):
            self.boxes[i].draw()
        self.present_point_textmark.text = str(self.present_point)
        self.present_point_textmark.draw()
        my_progress_bar.draw(is_practice=is_explore)

    def travel(self, target_point, this_side_bar, is_explore=False):
        """飞船航行函数，
        target_point指明飞船所要到达的目标位置
        this_side_bar变量为了在draw 的过程中，将侧栏同时刷新，所以作为变量传进来"""
        target_x = self.map[target_point - 1].circle.pos[0]
        target_y = self.map[target_point - 1].circle.pos[1]
        present_x = self.map[self.present_point - 1].circle.pos[0]
        present_y = self.map[self.present_point - 1].circle.pos[1]

        hint = 0
        clock.reset()
        t = clock.getTime()
        while t < 1:
            x = (target_x - present_x) * t + present_x
            y = (target_y - present_y) * t + present_y

            # hint = 0  # 提示：0代表正确 分两种模式，判断方式不同
            # if this_side_bar.is_energy:
            #     if target_point in self.covered_points:
            #         hint = 1  # 提示：0代表正确，1代表错误
            #         spacecraft.size = [60 * math.e **
            #                            (-2*t), 60 * math.e ** (-2*t)]
            #     self.map[-1].pos = [x, y]
            # else:
            self.map[-1].pos = [x, y]
            for point_i in covered_points:
                if self.boxes[point_i - 1].contains(x, y):
                    hint = 1
                    spacecraft.size = [60 * math.e **
                                       (-2 * t), 60 * math.e ** (-2 * t)]
                    break
            background.draw()
            my_progress_bar.draw(is_practice=is_explore)
            self.draw(is_explore=is_explore, dynamic=True)
            this_side_bar.draw(is_explore=is_explore)
            win.flip()

            t = clock.getTime()

        # if target_point not in self.covered_points:
        if not hint == 1:
            self.present_point = target_point
        self.map[-1].pos = [target_x, target_y]
        spacecraft.size = [60, 60]

        return hint

    def depart(self, operator, this_side_bar, is_explore=False):
        number = []
        clicked = []
        temp_present_point = self.present_point
        target_point = -1
        clock.reset()
        while clock.getTime() < 5:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            background.draw()
            my_progress_bar.draw(is_practice=is_explore)
            self.draw(is_explore=is_explore)
            this_side_bar.draw(is_explore=is_explore)
            win.flip()

            if mouse.isPressedIn(this_side_bar.button_cancel.button):
                # 按取消键
                this_side_bar.button_cancel.button.fillColor = this_side_bar.button_fillColor
                clock.reset()
                while clock.getTime() < 0.1:
                    background.draw()
                    my_progress_bar.draw(is_practice=is_explore)
                    this_side_bar.draw(is_explore=is_explore)
                    self.draw(is_explore=is_explore)
                    win.flip()
                this_side_bar.button_cancel.button.fillColor = this_side_bar.button_fillColor_cancel
                return 2
            for i in range(100):
                if mouse.isPressedIn(self.map[i].circle):
                    self.map[i].circle.fillColor = [255, 206, 69]
                    clicked = i
                    number = i + 1
                    if operator == "+":
                        target_point = self.present_point + number
                    elif operator == '-':
                        target_point = self.present_point - number
                    elif operator == "×":
                        target_point = self.present_point * number
                    elif operator == "÷" and self.present_point % number == 0:
                        target_point = int(self.present_point / number)
                    this_side_bar.set_score(number)
                    this_side_bar.color_restore()
                    break
            if target_point != -1:
                break
        if target_point != -1 and target_point <= 100 and target_point >= 0:
            clock.reset()
            while clock.getTime() < 0.1:
                background.draw()
                my_progress_bar.draw(is_practice=is_explore)
                self.draw(is_explore=is_explore, dynamic=False)
                this_side_bar.draw(is_explore=is_explore)
                win.flip()
            if number in self.covered_points:
                self.map[i].circle.fillColor = self.covered_fillColor
                hint = 2
            else:
                self.map[i].circle.fillColor = self.fillColor
                self.map[i].circle.opacity = 0.3
                hint = self.travel(
                    target_point, this_side_bar, is_explore=is_explore)
                self.path.append((operator, number, hint))
            if hint == 0:
                return operator + str(number)
            else:
                self.error_warning(hint, temp_present_point, target_point)
                this_side_bar.reset_score()
                return 0
        else:
            self.map[i].circle.fillColor = self.covered_fillColor
            self.error_warning(3, temp_present_point, target_point)
            this_side_bar.reset_score()
            this_side_bar.color_restore()
            return 0

    def error_warning(self, mode, start_point, end_point=[]):
        # TODO::这块可能有些问题后续需要补充
        """错误提示"""
        if mode == 1:
            text = generate_textMark(-win.size[0]/2.647,
                                     0, "不可经过黑洞\n请重新选择路线", 30, [255, 255, 255])
            pos1 = self.boxes[start_point - 1].pos
            pos2 = self.boxes[end_point - 1].pos
            arrow = my_arrow(pos1[0], pos1[1], pos2[0], pos2[1], color=[
                252, 1, 26], lineWidth=6, opacity=0.9)
            background.draw()
            my_progress_bar.draw(is_practice=False)
            self.draw()
            arrow.draw()
        elif mode == 2:
            text = generate_textMark(
                - win.size[0] / 2.647, 0, "不能使用标红的数字进行运算，请重新选择路线", 30, [255, 255, 255])
            text.draw()
        else:
            text = generate_textMark(
                - win.size[0] / 2.647, 0, "运算结果超出地图范围，请重新选择路线", 30, [255, 255, 255])
        text.draw()
        win.flip()
        event.waitKeys()


def generate_map(x, y, length, height, start_point, end_point, covered_points=[]):
    """生成100个数字坐标点
    length,height代表地图，相邻两个坐标之间的间隔，length是左右间隔，height是竖直间隔"""
    points = []
    boxes = []
    # 生成一百个点，从左到右1-10从上到下1、11、21...91
    for i in range(100):
        xi = x-9*length/2 + ((i) % 10) * length
        yi = y+9*height/2 - int((i) / 10) * height
        points.append(Integer_unit(
            i + 1, xi, yi))

    for i in range(100):
        x_i = x - 9 * length / 2 + ((i) % 10) * length
        y_i = y + 9 * height / 2 - int((i) / 10) * height
        boxes.append(generate_Rect(length*0.8, height*0.8, [x_i, y_i], fillColor=[
                     255, 255, 255], lineColor=[0, 0, 0], opacity=0.3))

    spacecraft.pos = points[start_point-1].circle.pos
    points.append(spacecraft)

    for j in range(len(covered_points)):  # 被黑洞覆盖的点，变成红色
        points[covered_points[j]-1].circle.fillColor = [226, 32, 24]

    a = 25
    sin18 = math.sin(math.pi * 18 / 180)
    sin36 = math.sin(math.pi * 36 / 180)
    cos18 = math.cos(math.pi * 18 / 180)
    cos36 = math.cos(math.pi * 36 / 180)
    tan18 = math.tan(math.pi * 18 / 180)
    A = (a + a * sin18, 0)
    A1 = (a * sin18, 0)
    B = (a * cos36, -a * cos36 / tan18 + a * cos18)
    B1 = ((2 * sin18 + 1) * a * sin18, -(2 * sin18 + 1) * a * cos18+a*cos18)
    C = (-a * cos36, -a * cos36 / tan18 + a * cos18)
    C1 = (0, -a * cos36 / tan18 + a * cos18 + a * sin36)
    D = (-a - a * sin18, 0)
    D1 = (-(2 * sin18 + 1) * a * sin18, -
          (2 * sin18 + 1) * a * cos18 + a * cos18)
    E = (0, a * cos18)
    E1 = (-a * sin18, 0)
    star = visual.ShapeStim(
        win=win,
        vertices=[E, A1, A, B1, B, C1, C, D1, D, E1],
        fillColor=[226, 32, 24],
        lineColor=[226, 32, 24],
        colorSpace="rgb255",
        pos=[points[end_point-1].circle.pos[0],
             points[end_point-1].circle.pos[1]+5]
    )
    points[end_point-1].circle = star  # 终点变成星星

    return points, boxes


def generate_button(length, height, pos=[0, 0], fillColor=[255, 255, 255], lineColor=[255, 255, 255]):
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

    button = visual.ShapeStim(
        win=win, vertices=acceptBoxVertices,
        fillColor=fillColor, lineColor=lineColor,
        colorSpace="rgb255",
        pos=pos,
        autoLog=False)

    return button


def generate_Rect(length, height, pos=[0, 0], fillColor=[255, 255, 255], lineColor=[255, 255, 255], opacity=0):
    rectangle = visual.Rect(
        win=win,
        size=[length, height],
        pos=pos,
        fillColor=fillColor,
        lineColor=lineColor,
        colorSpace="rgb255",
        opacity=opacity
    )
    return rectangle


def explore_mode(covered_points):
    all_point = list(range(1, 101))
    available_point = list(set(all_point)-set(covered_points))
    start_point = random.choice(available_point)
    available_point.remove(start_point)
    end_point = random.choice(available_point)

    number_map = my_map([win.size[0] * 0.1111, 0],
                        start_point, end_point, covered_points)
    my_side_bar = side_bar(pos=[-win.size[0] / 2.647, 0])
    clock.reset()
    while not number_map.present_point == number_map.end_point:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
        operator = my_side_bar.click(mouse, number_map, is_explore=True)
        print(operator)
        if len(operator) > 0:
            error = number_map.depart(operator, my_side_bar, is_explore=True)
            if error == 0:
                number_map.present_point = number_map.start_point
            elif error == 2:
                my_side_bar.color_restore()


def trial(is_energy, covered_points, start_point, end_point):

    number_map = my_map([win.size[0]*0.1111, 0],
                        start_point, end_point, covered_points)
    my_side_bar = side_bar(
        pos=[-win.size[0] / 2.647, 0], is_energy=is_energy)

    clock.reset()
    while not number_map.present_point == number_map.end_point:
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()
        operator = my_side_bar.click(mouse, number_map)
        print(operator)
        if len(operator) > 0:
            error = number_map.depart(operator, my_side_bar)
            if error == 0:
                number_map.present_point = number_map.start_point
            elif error == 2:
                my_side_bar.color_restore()
        if my_progress_bar.getTime() >= 200 and first_alert == False:
            first_alert = True
            intro.image = "NNG_Picture/first_alert.png"
            # bell.pos = [0, win.size[0]*0.125]
            intro.draw()
            # bell.draw()
            win.flip()
            event.waitKeys()
        if my_progress_bar.getTime() >= 400 and second_alert == False:
            second_alert = True
            intro.image = "NNG_Picture/second_alert.png"
            intro.draw()
            win.flip()
            event.waitKeys()

    return number_map, my_side_bar


def save_and_quit():
    """保存后退出"""
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
expName = 'task6'
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
win = visual.Window(
    size=[1500, 800],
    units="pix",
    fullscr=False      # fullscr means full-screen mode
)
background = visual.ImageStim(
    win=win,
    image="NNG_Picture/interface_只有框框版.jpg",
    size=win.size,
    units="pix"
)

spacecraft = visual.ImageStim(
    win=win,
    image="NNG_Picture/spacecraft.png",
    size=[60, 60],
    units="pix"
)
intro = visual.ImageStim(
    win=win,
    image="NNG_Picture/Intro.png",
    size=win.size,
    units="pix"
)

energy = visual.ImageStim(
    win=win,
    image="NNG_Picture/interface_小图标/energy.png",
    size=[70, 70],
    units="pix"
)

step = visual.ImageStim(
    win=win,
    image="NNG_Picture/interface_小图标/step.png",
    size=[70, 70],
    units="pix"
)

bell = visual.ImageStim(
    win=win,
    image="NNG_Picture/interface_小图标/bell.png",
    size=[90, 90],
    units="pix"
)

intro.draw()
win.flip()
event.waitKeys()

intro.image = "NNG_Picture/IntroTaskPrac.png"
intro.draw()
win.flip()
event.waitKeys()


clock = core.Clock()
defaultKeyboard = keyboard.Keyboard()

cue_words = generate_textMark(0, 0, "成功到达终点，继续下一题吧！", 30, [255, 255, 255])

covered_points = [18, 19, 28, 29, 23, 32, 33,
                  34, 42, 43, 44, 53, 59, 68, 69, 70, 79]
# (起点，终点，energy，step,能量或步数)
paths = [(56, 83, 18, 4, True), (90, 50, 7, 2, True), (35, 82, 8, 2, True), (11, 78, 7, 2, True), (39, 26, 5, 2, True),
         (56, 83, 18, 4, False), (90, 50, 7, 2, False), (35, 82, 8, 2, False), (11, 78, 7, 2, False), (39, 26, 5, 2, False)]

my_progress_bar = Progress_bar(600, core.Clock(), win.size[1]/2-20)
mouse = event.Mouse()
mouse.setVisible(1)
medal = 0
for i in range(3):
    explore_mode(covered_points)

my_progress_bar.reset()
first_alert = False
second_alert = False
for trial_i in range(10):
    path_i = random.choice(paths)
    paths.remove(path_i)

    if path_i[4] == True:
        intro.image = "NNG_Picture/IntroTask2.png"
        intro.draw()
        win.flip()
        event.waitKeys()
    else:
        intro.image = "NNG_Picture/IntroTask1.png"
        intro.draw()
        win.flip()
        event.waitKeys()
    number_map, my_side_bar = trial(
        path_i[4], covered_points, path_i[0], path_i[1])
    thisExp.addData("trial", trial_i)
    thisExp.addData("is_energy", path_i[4])
    thisExp.addData("start_number", path_i[0])
    thisExp.addData("end_number", path_i[1])
    thisExp.addData("path", number_map.path)
    thisExp.addData("step", my_side_bar.step)
    thisExp.addData("energy", my_side_bar.energy)
    thisExp.nextEntry()

    if path_i[4] == True:
        if my_side_bar.energy <= path_i[2] + 10 and my_side_bar.energy >= path_i[2] - 10:
            medal = medal + 1
    else:
        if my_side_bar.step <= path_i[3] + 3 and my_side_bar.step >= path_i[3] - 3:
            medal = medal + 1
    background.draw()
    my_side_bar.draw()
    my_progress_bar.draw(is_practice=False)
    cue_words.draw()
    win.flip()
    event.waitKeys()
    if my_progress_bar.getTime() >= 200 and first_alert == False:
        first_alert = True
        intro.image = "NNG_Picture/first_alert.png"
        # bell.pos = [0, win.size[0]*0.125]
        intro.draw()
        # bell.draw()
        win.flip()
        event.waitKeys()
    if my_progress_bar.getTime() >= 400 and second_alert == False:
        second_alert = True
        intro.image = "NNG_Picture/second_alert.png"
        intro.draw()
        win.flip()
        event.waitKeys()
    if my_progress_bar.getTime() >= 603:
        break

intro.image = "NNG_Picture/final_alert.png"
intro.draw()
win.flip()
event.waitKeys()

thisExp.saveAsWideText(filename + '.csv', appendFile=True)
os.chmod(filename + '.csv', stat.S_IREAD)  # 权限改为只读
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
core.wait(2)
win.close()
