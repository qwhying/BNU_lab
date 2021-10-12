from psychopy import locale_setup
from psychopy import prefs
from psychopy import gui, visual, core, data, event,  clock
from pyglet.window import key
from psychopy.hardware import keyboard

import xlrd
import stat
import os
import random
import datetime
import sys
import csv
import copy
import math
from math import ceil


def save_and_quit():
    """保存后退出"""
    os.chmod(filename + '.csv', stat.S_IWRITE)  # 权限改为可读写
    thisExp.saveAsWideText(filename + '.csv', appendFile=True)
    os.chmod(filename + '.csv', stat.S_IREAD)  # 权限改为只读
    # make sure everything is closed down
    thisExp.abort()  # or data files will save again on exit
    core.quit()


def get_key(answer_text_now, clock, response_time):
    text_input = ""
    continueRuntine = True

    while continueRuntine:
        if clock.getTime() > response_time:
            break
        background.draw()
        question_1.draw()
        answer_text_now.draw()
        win.flip()
        kb.clock.reset()
        keys = kb.getKeys(["0", "1", "2", "3", "4", "5", "6",
                           "7", "8", "9", "backspace", "return"])
        if len(keys):
            if "backspace" in keys:
                text_input = text_input[:-1]
            elif "return" in keys:
                continueRuntine = False
            else:
                text_input = text_input + keys[0].name

                answer_text_now.text = text_input

    return text_input


def trial(mode, pre_n, mat_1, op_1, mat_2, op_2, mat_3, op_3=[], mat_4=[]):
    """mode表示模式0代表运算+回忆，1代表运算 回忆 分离，2代表运算，3代表回忆"""
    preload_number = int(pre_n)

    math_1_number = int(mat_1)
    math_2_number = int(mat_2)
    math_3_number = int(mat_3)
    math_4_number = int(mat_4)

    operator_1 = op_1
    operator_2 = op_2
    operator_3 = op_3

    recall_preload = []
    preload_time = 0
    calculate_time = 0

    if mat_4 == []:
        correct_answer = get_answer(get_answer(math_1_number, math_2_number,
                                               operator_1), math_3_number, operator_2)
    else:
        correct_answer = get_answer(get_answer(get_answer(
            math_1_number, math_2_number, operator_1), math_3_number, operator_2), math_4_number, operator_3)
    if mode == 0:

        preload_text = generate_textMark(
            38, 170, str(preload_number), 42, color=[255, 59, 48])
        clock.reset()
        while clock.getTime() <= Preload:
            cue_1.draw()

            preload_text.draw()
            win.flip()

        math_1_text = generate_textMark(
            38, 170, str(math_1_number), 42, color=[255, 255, 255])
        clock.reset()
        while clock.getTime() <= Math_1:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            cue_2.draw()

            math_1_text.draw()
            win.flip()

        math_2_text = generate_textMark(
            38, 170, operator_1+str(math_2_number), 42, color=[255, 255, 255])
        clock.reset()
        while clock.getTime() <= Math_2:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            background.draw()

            math_2_text.draw()
            win.flip()

        if mat_4 != []:
            math_3_text = generate_textMark(
                38, 170, operator_2+str(math_3_number), 42, color=[255, 255, 255])
            clock.reset()
            while clock.getTime() <= Math_3:
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    save_and_quit()
                background.draw()

                math_3_text.draw()
                win.flip()
            math_4_text = generate_textMark(
                20, 170, operator_3, 42, color=[0, 0, 0])
            math_4_text_2 = generate_textMark(
                42, 170, "?", 42, color=[255, 59, 48])
            clock.reset()
            while clock.getTime() <= Recall_preload:
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    save_and_quit()
                background.draw()
                question_3.draw()

                math_4_text.draw()
                math_4_text_2.draw()
                win.flip()
                kb.clock.reset()
                a = kb.getKeys(
                    keyList=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
                if len(a) > 0:
                    math_4_text.text = operator_3 + a[0].name
                    math_4_text_2.text = ""
                    recall_preload = int(a[0].name)
                    preload_time = clock.getTime()
        else:
            math_3_text = generate_textMark(
                20, 170, operator_2, 42, color=[0, 0, 0])
            math_3_text_2 = generate_textMark(
                42, 170, "?", 42, color=[255, 59, 48])
            clock.reset()
            while clock.getTime() <= Math_3:
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    save_and_quit()
                background.draw()
                question_3.draw()

                math_3_text.draw()
                math_3_text_2.draw()
                win.flip()
                kb.clock.reset()
                a = kb.getKeys(
                    keyList=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
                if len(a) > 0:
                    math_3_text.text = operator_2 + a[0].name
                    math_3_text_2.text = ""
                    recall_preload = int(a[0].name)
                    preload_time = clock.getTime()

        # 计算环节
        clock.reset()
        answer_text = generate_textMark(
            38, 170, "=？", 42, color=[255, 255, 255])
        input_text = []
        while clock.getTime() <= Calculation:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            background.draw()

            question_1.draw()

            answer_text.draw()
            win.flip()
            if len(input_text) < 1:
                input_text = get_key(answer_text, clock, Calculation)
                calculate_time = clock.getTime()
        if input_text == "":
            answer = -100
        else:
            answer = int(answer_text.text)

        # 回忆环节
        clock.reset()
        input_text = []
        answer_text = generate_textMark(0, 0, "", 42, color=[255, 255, 255])
        while clock.getTime() <= Recall_preload:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            background.draw()
            question_4.draw()
            answer_text.draw()
            win.flip()
            kb.clock.reset()
            a = kb.getKeys(keyList=["0"])
            if len(a):
                break

        if answer == correct_answer and recall_preload == preload_number:
            clock.reset()
            while clock.getTime() < 3:
                correct_feedback.draw()
                win.flip()
            result = True
        else:
            clock.reset()
            while clock.getTime() < 3:
                error_feedback.draw()
                win.flip()
            result = False
        return result, recall_preload, preload_time, answer, calculate_time

    if mode == 1:

        preload_text = generate_textMark(
            38, 170, str(preload_number), 42, color=[255, 59, 48])
        clock.reset()
        while clock.getTime() <= Preload:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            cue_1.draw()

            preload_text.draw()
            win.flip()

        math_1_text = generate_textMark(
            38, 170, str(math_1_number), 42, color=[255, 255, 255])
        clock.reset()
        while clock.getTime() <= Math_1:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            cue_2.draw()

            math_1_text.draw()
            win.flip()

        math_2_text = generate_textMark(
            38, 170, operator_1+str(math_2_number), 42, color=[255, 255, 255])
        clock.reset()
        while clock.getTime() <= Math_2:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            background.draw()

            math_2_text.draw()
            win.flip()

        math_3_text = generate_textMark(
            38, 170, operator_2+str(math_3_number), 42, color=[255, 255, 255])
        clock.reset()

        while clock.getTime() <= Math_3:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            background.draw()

            math_3_text.draw()
            win.flip()

        if mat_4 != []:
            math_4_text = generate_textMark(
                38, 170, operator_3+str(math_4_number), 42, color=[255, 255, 255])
            clock.reset()

            while clock.getTime() <= Math_4:
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    save_and_quit()
                background.draw()

                math_4_text.draw()
                win.flip()

        # 计算环节
        clock.reset()
        answer_text_cal = generate_textMark(
            38, 170, "=？", 42, color=[255, 255, 255])
        input_text = []
        while clock.getTime() <= Calculation:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            background.draw()

            question_1.draw()

            answer_text_cal.draw()
            win.flip()
            if len(input_text) < 1:
                input_text = get_key(answer_text_cal, clock, Calculation)
                calculate_time = clock.getTime()
                # answer_text_cal.text = input_text
        if input_text == "":
            answer_1 = -100
        else:
            answer_1 = int(input_text)

        # 回忆环节
        clock.reset()
        recall_preload = []
        answer_text_recal = generate_textMark(
            38, 170, "", 42, color=[255, 255, 255])
        while clock.getTime() <= Recall_preload:
            background.draw()
            question_2.draw()
            answer_text_recal.draw()
            win.flip()
            kb.clock.reset()
            recall_preload = kb.getKeys(
                keyList=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
            if len(recall_preload) > 0:
                answer_text_recal.text = recall_preload[0].name
                preload_time = clock.getTime()
        if len(answer_text_recal.text) > 0:
            answer_2 = int(answer_text_recal.text)
        else:
            answer_2 = []
        if answer_1 == correct_answer and answer_2 == preload_number:
            clock.reset()
            while clock.getTime() < 3:
                correct_feedback.draw()
                win.flip()
            result = True
        else:
            clock.reset()
            while clock.getTime() < 3:
                error_feedback.draw()
                win.flip()
            result = False
        return result, answer_2, preload_time, answer_1, calculate_time

    # if mode == 2:  # 只计算
    #     preload_text = generate_textMark(
    #         42, 0, str(preload_number), 42, color=[96, 96, 96])
    #     clock.reset()
    #     while clock.getTime() <= Preload:
    #         background.draw()

    #         preload_text.draw()
    #         win.flip()
    #         a = event.getKeys(keyList=[str(preload_number)])
    #         if len(a) > 0:
    #             break

    #     math_1_text = generate_textMark(
    #         0, 0, str(math_1_number), 42, color=[255, 255, 255])
    #     clock.reset()
    #     while clock.getTime() <= Math_1:
    #         background.draw()

    #         math_1_text.draw()
    #         win.flip()
    #         a = event.getKeys(keyList=[str(preload_number)])
    #         if len(a) > 0:
    #             break

    #     math_2_text = generate_textMark(
    #         0, 0, operator_1+str(math_2_number), 42, color=[255, 255, 255])
    #     clock.reset()
    #     while clock.getTime() <= Math_2:
    #         background.draw()

    #         math_2_text.draw()
    #         win.flip()
    #         a = event.getKeys(keyList=[str(preload_number)])
    #         if len(a) > 0:
    #             break

    #     input_text = []
    #     while clock.getTime() <= Calculation:
    #         # background.draw()

    #         # question_1.draw()

    #         # answer_text.draw()
    #         # win.flip()
    #         if len(input_text) < 1:
    #             input_text = get_key(answer_text, clock, Calculation)
    #             # answer_text.text = input_text

    #     answer = int(answer_text.text)
    #     if answer == correct_answer:
    #         background.draw()
    #         victory.draw()
    #         win.flip()
    #         event.waitKeys()
    #     else:
    #         background.draw()
    #         failure.draw()
    #         win.flip()
    #         event.waitKeys()
    #      # 回忆环节
    #     clock.reset()
    #     input_text = []
    #     answer_text = generate_textMark(0, 0, "0", 42, color=[96, 96, 96])
    #     while clock.getTime() <= Recall_preload:
    #         background.draw()
    #         question_2.draw()
    #         answer_text.draw()
    #         win.flip()
    #         a = event.waitKeys(keyList=["0"])
    #         break

    #     return 0
    # return 0


def get_answer(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*" or operator == "x":
        return num1 * num2
    elif operator == "÷" or operator == "/":
        return num1/num2


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


def read_xlsx(file_name, level):
    """读取xlsx文件，每次读一个关卡
    返回matrix为n行6列的表格"""
    # 打开文件
    workbook = xlrd.open_workbook(file_name)
    # 获取第二个sheet
    sheet1 = workbook.sheet_by_index(1)
    # 获取行数
    nrows = sheet1.nrows

    rown = 0
    # 计算这一关的数
    # col_start = (level - 1) * 7  # 表中每一关占7列
    # col_end = (level - 1) * 7 + 6  # 前六列有意义，最后一列为空，

    # 读取所需方阵
    if level > 1:
        for i in range(level-1):
            for rownum in range(rown, nrows):
                row = sheet1.row_values(rownum)
                if row[0] == "":
                    break
            rown = rownum + 1
    else:
        rown = 1
    matrix = []
    for rownum in range(rown, nrows):
        row = sheet1.row_values(rownum)  # 行切片

        if row[0] != '':  # 如果这行的这几列存在
            matrix.append(row)
        else:
            break

    return matrix


def get_taskdata(task_table, number_of_trials):
    """task_table为read_xlsx函数读取的关卡数据
    number_of_trials为这一关有多少个试次
    这个函数将从富余的试次中随机抽取 number_of_trials 这么多的试次"""
    taskdata = []
    for i in range(number_of_trials):
        taskdata.append(random.choice(task_table))
        # 做标记，如果是分离则为1，整合则为0
        if isinstance(taskdata[-1][-2], float):
            taskdata[-1][0] = 1
        elif taskdata[-1][-2][0] == "按":
            taskdata[-1][0] = 0
        else:
            taskdata[-1][0] = 0
        task_table.remove(taskdata[-1])

    # shuffle打乱顺序，成为最终的题目
    random.shuffle(taskdata)

    return taskdata


def one_round(game_level):
    """一关游戏（一轮）"""

    corrects = 0

    round_text = generate_textMark(0, 100, "第" + str(game_level) + "关", 60)
    while clock.getTime() < 5:
        background.draw()
        round_text.draw()
        win.flip()
        if defaultKeyboard.getKeys(keyList=["escape"]):
            save_and_quit()

    task_table = read_xlsx("integration_task_design.xlsx", game_level)
    task_data = get_taskdata(task_table, number_of_trials[game_level - 1])
    for trial_i in task_data:
        trials = task_table[0]
        result_i, pre_ans, pre_time, cal_ans, cal_time = trial(trial_i[0], trial_i[2], trial_i[3], trial_i[4],
                                                               trial_i[5], trial_i[6], trial_i[7], trial_i[8], trial_i[9])
        if result_i == True:
            corrects += 1
        thisExp.addData('level', game_level)
        thisExp.addData('trial', task_data.index(trial_i) + 1)
        thisExp.addData('taskdesign', trial_i)
        thisExp.addData('tasktype', trial_i[0])
        # thisExp.addData('response', result)
        thisExp.addData('result', result_i)
        thisExp.addData('calculate_result', cal_ans)
        thisExp.addData('calculate time', cal_time)
        thisExp.addData('preload_result', pre_ans)
        thisExp.addData('preload_time', pre_time)
        thisExp.nextEntry()

    clock.reset()
    if corrects / len(task_data) >= 0.75:
        while clock.getTime() < 3:
            victory.draw()
            win.flip()
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
    else:
        while clock.getTime() < 3:
            failure.draw()
            win.flip()
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
    thisExp.addData("level", game_level)
    thisExp.addData('accuracy', corrects / len(task_data))
    thisExp.addData('pass', corrects / len(task_data) >= 0.75)
    thisExp.nextEntry()
    return corrects / len(task_data) >= 0.75


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
# from the Builder filename that created this script
expName = 'task1'
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
# 保存在统一的data文件夹内
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
    size=[894, 682],
    units="pix",
    fullscr=False      # fullscr means full-screen mode
)

background = visual.ImageStim(
    win=win,
    image="pictures/纯背景（备用1）.png",
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
        with open(filename + '.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)

            for row in reader:
                game_level = row[0]  # 读取记录文档的第一列最后一行
            if row[1] == "" and (row[9] == "TRUE" or row[9] == 'True' or row[9] == True):
                game_level = int(game_level)+1
            else:
                game_level = int(game_level)
            dlg = gui.Dlg(title="提示")
            dlg.addText("训练记录检测到上次训练最后一关为：" +
                        str(row[0]) + ",通关状态为:" + str(row[9]) + ",即将开始训练关卡为:" + str(game_level))
            dlg.show()
            if dlg.OK == False:
                core.quit()
    except IOError:
        background.draw()
        remind = generate_textMark(
            0, 0, "没有找到之前训练记录\n请再次确认输入信息是否有误\n按任意键退出", 35)
        remind.draw()
        win.flip()
        event.waitKeys()
        core.quit()

sun = visual.ImageStim(
    win=win,
    image="pictures/太阳.png",
    size=[170, 170],
    units="pix"
)

# sun = visual.ImageStim(
#     win=win,
#     image="pictures/黄色枫叶.png",
#     siz0=[170, 170],
#     units="pix"
# )

intro = visual.ImageStim(
    win=win,
    image="pictures/指导语1.png",
    size=win.size,
    units="pix"
)

error_feedback = visual.ImageStim(
    win=win,
    image="pictures/试次错误反馈.png",
    size=win.size,
    units="pix"
)

correct_feedback = visual.ImageStim(
    win=win,
    image="pictures/试次正确反馈.png",
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

cue_1 = visual.ImageStim(
    win=win,
    image="pictures/纯背景-请记住数字.png",
    size=win.size
)

cue_2 = visual.ImageStim(
    win=win,
    image="pictures/纯背景-请运算数字.png",
    size=win.size
)

question_1 = visual.ImageStim(
    win=win,
    image="pictures/分离条件-5运算结果.png",
    size=win.size
)
question_2 = visual.ImageStim(
    win=win,
    image="pictures/分离条件-6回忆preload.png",
    size=win.size
)

question_3 = visual.ImageStim(
    win=win,
    image="pictures/整合条件-4回忆preload.png",
    size=win.size
)

question_4 = visual.ImageStim(
    win=win,
    image="pictures/整合条件-6按零键.png",
    size=win.size
)

number_of_trials = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]

defaultKeyboard = keyboard.Keyboard()


# 时间设置
# Fixation = 2.50
Preload = 3
Math_1 = 3
Math_2 = 3
Math_3 = 3
Math_4 = 3
Calculation = 4
Recall_preload = 4


intro.draw()
win.flip()
event.waitKeys()

intro.image = "pictures/指导语2.png"
intro.draw()
win.flip()
event.waitKeys()

clock = core.Clock()
kb = keyboard.Keyboard()


end_level = game_level + 6

# 训练开始
while game_level < end_level:

    if defaultKeyboard.getKeys(keyList=["escape"]):
        save_and_quit()
    temp_level = game_level
    passed = one_round(game_level)

    if passed:  # 通关
        game_level = game_level + 1
    else:  # 未通关，则重复这一关
        round_clock = core.Clock()
        round_clock.reset()
        while round_clock.getTime() < 180:
            if defaultKeyboard.getKeys(keyList=["escape"]):
                save_and_quit()
            passed = one_round(game_level)
            if passed:
                game_level = game_level + 1
                break

        if temp_level == game_level:
            # 超过3分钟，还是没有过关直接进入下一关
            game_level = game_level+1


save_and_quit()
