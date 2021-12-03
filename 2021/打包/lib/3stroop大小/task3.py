from math import ceil
import math
import copy
import csv
import sys
import datetime
import random
import os
import xlrd

from psychopy.hardware import keyboard
from psychopy import visual, event, core, gui, data
from pyglet.window import key
import stat


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


def show_feedback(pressed_key, result):
    """pressed_key 是被试按下的键，result是正确结果
    正确返回1
    错误返回0"""
    if pressed_key == result:
        clock.reset()
        while clock.getTime() < 2:
            correct_feedback.draw()
            win.flip()
        return 1
    else:
        clock.reset()
        while clock.getTime() < 2:
            error_feedback.draw()
            win.flip()
        return 0


def read_xlsx(file_name, level):
    """读取xlsx文件，每次读一个关卡
    返回matrix为n行6列的表格"""
    # 打开文件
    workbook = xlrd.open_workbook(file_name)
    # 获取第一个sheet
    sheet1 = workbook.sheet_by_index(0)
    # 获取行数
    nrows = sheet1.nrows

    # 计算这一关的列数
    col_start = (level - 1) * 7  # 表中每一关占7列
    col_end = (level - 1) * 7 + 6  # 前六列有意义，最后一列为空，

    # 读取所需方阵
    matrix = []
    for rownum in range(0, nrows):
        row = sheet1.row_values(rownum, col_start, col_end)  # 行切片

        if row[0] != '':  # 如果这行的这几列存在
            matrix.append(row)

    return matrix


def get_taskdata(task_table, number_of_trials):
    """task_table为read_xlsx函数读取的关卡数据
    number_of_trials为这一关有多少个试次
    这个函数将从富余的试次中随机抽取 number_of_trials 这么多的试次"""
    # 将task_table按照距离难度分成三组
    group1 = []
    group2 = []
    group3 = []

    group1.append(task_table[2])
    taskdata = []  # 用来存放分别从三组随机取得的试次合并后的结果,最后再打乱顺序
    for rown in range(3, len(task_table)):
        if group1[0][0] == task_table[rown][0]:
            group1.append(task_table[rown])
        elif group2 == [] or group2[0][0] == task_table[rown][0]:
            group2.append(task_table[rown])
        elif group3 == [] or group3[0][0] == task_table[rown][0]:
            group3.append(task_table[rown])
    if number_of_trials == 12:
        for i in range(4):
            taskdata.append(random.choice(group1))
            group1.remove(taskdata[i])
        for i in range(4, 8):
            taskdata.append(random.choice(group2))
            group2.remove(taskdata[i])
        for i in range(8, 12):
            taskdata.append(random.choice(group3))
            group3.remove(taskdata[i])
    else:
        for i in range(5):
            taskdata.append(random.choice(group1))
            group1.remove(taskdata[i])
        for i in range(5, 10):
            taskdata.append(random.choice(group2))
            group2.remove(taskdata[i])
        for i in range(10, 16):
            taskdata.append(random.choice(group3))
            group3.remove(taskdata[i])
    # shuffle打乱顺序，成为最终的题目
    random.shuffle(taskdata)

    for trials in taskdata:
        if isinstance(trials[2], float) or str.isalnum(trials[2]):
            if int(trials[2]) < int(trials[4]):
                trials.append("right")
            else:
                trials.append("left")
        else:
            if eval(trials[2]) < eval(trials[4]):
                trials.append("right")
            else:
                trials.append("left")
        if trials[3] == "大":
            trials[3] = True
        else:
            trials[3] = False
        if trials[5] == "大":
            trials[5] = True
        else:
            trials[5] = False

    return taskdata


def trial(l_num, l_big, r_num, r_big, result, level):
    """一个试次
    r_num代表左边的数字（或算式）
    r_big代表左边字体显示较大，True表示左边为大字，False表示左边为小字
    l_num,l_big代表右边，与左边类似
    result表示数字（或算式)值的大小结果，以字符串表示，left表示左边大，right表示右边大"""
    intro.image = "pictures/试次界面.png"
    if isinstance(r_num, float) or str.isalnum(r_num):
        if r_big:
            text_r = generate_textMark(70, 150, str(int(r_num)), 70)
            text_l = generate_textMark(-70, 150, str(int(l_num)), 30)
        else:
            text_r = generate_textMark(70, 150, str(int(r_num)), 30)
            text_l = generate_textMark(-70, 150, str(int(l_num)), 70)
        clock.reset()
        while clock.getTime() < time_of_each_trials[level-1]:
            intro.draw()
            text_l.draw()
            text_r.draw()
            win.flip()
            a = event.getKeys(keyList=["left", "right"])
            if len(a) > 0:
                correct = show_feedback(a[0], result)
                res_time = clock.getTime()
                return correct, res_time
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
    else:
        r_num_1 = r_num[0]
        r_num_2 = r_num[2]
        r_op = r_num[1]
        l_num_1 = l_num[0]
        l_num_2 = l_num[2]
        l_op = l_num[1]
        if r_big:
            text_r_1 = generate_textMark(70, 200, r_num_1, 70)
            text_r_2 = generate_textMark(70, 100, r_num_2, 70)
            text_l_1 = generate_textMark(-70, 200, l_num_1, 30)
            text_l_2 = generate_textMark(-70, 100, l_num_2, 30)
        else:
            text_r_1 = generate_textMark(70, 200, r_num_1, 30)
            text_r_2 = generate_textMark(70, 100, r_num_2, 30)
            text_l_1 = generate_textMark(-70, 200, l_num_1, 70)
            text_l_2 = generate_textMark(-70, 100, l_num_2, 70)
        text_r_op = generate_textMark(70, 150, r_op, 30)
        text_l_op = generate_textMark(-70, 150, l_op, 30)
        clock.reset()
        while clock.getTime() < time_of_each_trials[level-1]:
            intro.draw()
            text_l_1.draw()
            text_l_2.draw()
            text_r_1.draw()
            text_r_2.draw()
            text_r_op.draw()
            text_l_op.draw()
            win.flip()
            a = event.getKeys(keyList=["left", "right"])
            if len(a) > 0:
                correct = show_feedback(a[0], result)
                res_time = clock.getTime()
                return correct, res_time
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
    # 到时间没有操作，则视为失败
    correct = show_feedback("", result)
    res_time = 0
    return correct, res_time


def save_and_quit():
    """保存后退出"""
    os.chmod(filename + '.csv', stat.S_IWRITE)  # 权限改为读写
    thisExp.saveAsWideText(filename + '.csv', appendFile=True)
    os.chmod(filename + '.csv', stat.S_IREAD)  # 权限改为只读
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    core.quit()


def one_round(level):
    """一关
    level关卡数"""
    clock.reset()
    corrects = 0
    time = []

    round_text = generate_textMark(0, 100, "第" + str(level) + "关", 35)
    while clock.getTime() < 4:
        round_pic.draw()
        round_text.draw()
        win.flip()
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()

    task_table = read_xlsx("new_stroop_task_design.xlsx", level)
    task_data = get_taskdata(task_table, number_of_trials[level-1])

    clock.reset()
    for trial_i in task_data:
        correct, res_time = trial(
            trial_i[2], trial_i[3], trial_i[4], trial_i[5], trial_i[6], level)
        corrects = corrects + correct
        thisExp.addData('level', level)
        thisExp.addData('trial', task_data.index(trial_i)+1)
        # thisExp.addData('response', result)
        thisExp.addData('result', correct)
        thisExp.addData('response time', res_time)
        thisExp.nextEntry()

    clock.reset()
    if corrects/len(task_data) > 0.75:
        while clock.getTime() < 2:
            victory.draw()
            win.flip()
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
    else:
        while clock.getTime() < 2:
            failure.draw()
            win.flip()
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()

    thisExp.addData('level', level)
    thisExp.addData('accuracy', corrects / len(task_data))
    thisExp.addData('pass', corrects / len(task_data) > 0.75)
    thisExp.nextEntry()

    return corrects/len(task_data) > 0.75


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)


# 窗口

# Store info about the experiment session
psychopyVersion = '2021.2.3'
# from the Builder filename that created this script
expName = 'task3'
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
# Data file name stem = absolute path + name; later add .p
# \u开头的是一个Unicode码的字符。范围在'\u0000'到'\uFFFF'之间。
# % 是python 字符串格式化符号:
# 保存在统一的data文件夹内
filename = os.path.dirname(os.path.dirname(_thisDir)) + os.sep + \
    u'data_%s_%s' % (expInfo['participant'], expName)
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath=os.path.abspath(__file__),
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)


clock = core.Clock()

win = visual.Window(
    size=[841, 587],
    units="pix",
    fullscr=False      # fullscr means full-screen mode
)

background = visual.ImageStim(
    win=win,
    image="pictures/背景.png",
    size=win.size,
    units="pix"
)


if expInfo['session'] == '1' or expInfo['session'] == '01':
    level = 1
elif expInfo['session'] == "" and expInfo['participant'] == "" and expInfo['name'] == "":
    # 三个都为空，则被视为调试，
    dlg = gui.Dlg(title="调试模式")

    dlg.addText("检测到三个基础信息都为空，进入调试模式，可以直接进入某一关")
    dlg.addField("关卡：")
    data = dlg.show()
    if dlg.OK == False:
        core.quit()
    print(data)
    level = int(data[0])
    filename = _thisDir + os.sep + \
        u'test_data_%s' % (expInfo['date'])
else:
    try:
        os.chmod(filename+'.csv', stat.S_IWRITE)
        with open(filename + '.csv') as f:
            reader = csv.reader(f)

            for row in reader:
                level = row[0]  # 读取记录文档的第一列最后一行
            if row[1] == "" and row[5] == "TRUE":
                level = int(level)+1
            else:
                level = int(level)
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
    image="pictures/指导语1.png",
    size=win.size,
    units="pix"
)

round_pic = visual.ImageStim(
    win=win,
    image="pictures/关卡.png",
    size=win.size,
    units="pix"
)
#
error_feedback = visual.ImageStim(
    win=win,
    image="pictures/错误反馈.png",
    size=win.size,
    units="pix"
)

correct_feedback = visual.ImageStim(
    win=win,
    image="pictures/正确反馈.png",
    size=win.size,
    units="pix"
)

victory = visual.ImageStim(
    win=win,
    image="pictures/闯关成功.png",
    size=win.size,
    units="pix"
)

failure = visual.ImageStim(
    win=win,
    image="pictures/闯关失败.png",
    size=win.size,
    units="pix"
)
defaultKeyboard = keyboard.Keyboard()

mouse = event.Mouse()
mouse.setVisible(1)

intro.draw()
win.flip()
event.waitKeys()

intro.image = "pictures/指导语2.png"
intro.draw()
win.flip()
event.waitKeys()
# trial数
number_of_trials = [12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
                    12, 12, 12, 12, 12, 12, 16, 16, 16, 16, 12, 12, 12, 12]
# 每个trial的时长
time_of_each_trials = [4, 4, 4, 4, 4, 4, 4, 4,
                       4, 4, 4, 4, 4, 4, 4, 4, 2.5, 2.5, 2.5, 2.5, 4, 4, 4, 4, ]

round_clock = core.Clock()
round_clock.reset()
level_end = level+8
while level < level_end:
    temp_level = level

    passed = one_round(level)
    if passed:
        level = level + 1
    else:
        round_clock.reset()
        while round_clock.getTime() < 120:
            passed = one_round(level)
            if passed:
                level = level+1
                break
    if level == temp_level:
        level = level + 1
