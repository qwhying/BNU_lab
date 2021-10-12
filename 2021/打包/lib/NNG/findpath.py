import copy
import csv
import random


def find_all_path(start_point, end_point, step, points, energy, present_path, covered_points):
    """start_point是起始点
    end_point是终点
    step是第几步
    points是可用的数字（这里面只可以用1-10）
    energy能量（最小能量模式的能量）
    present_path当前路径：格式为 步数：[运算数字,到达的而数字,运算符号]"""
    global path_
    if energy >= 20:
        return
    elif start_point == end_point:
        paths.append(present_path)
        paths[path_][-1] = [energy, step]
        path_ = path_+1
    elif step >= max_step:
        return
    else:
        for point_i in points:
            # if start_point + point_i <= 100 and start_point < end_point:
            if start_point+point_i <= 100 and (start_point+point_i) not in covered_points:
                temp_path = copy.copy(present_path)
                temp_path[step+1] = [point_i, start_point+point_i, "+"]
                find_all_path(start_point + point_i,
                              end_point, step + 1, points, energy+point_i, temp_path, covered_points)
            # if start_point - point_i >= 1 and start_point > end_point:
            if start_point - point_i >= 1 and (start_point-point_i) not in covered_points:
                temp_path = copy.copy(present_path)
                temp_path[step+1] = [point_i, start_point-point_i, "-"]
                find_all_path(start_point - point_i,
                              end_point, step + 1, points, energy+point_i, temp_path, covered_points)
            if start_point * point_i <= 100 and start_point < end_point and point_i != 1 and (start_point*point_i) not in covered_points:
                temp_path = copy.copy(present_path)
                temp_path[step+1] = [point_i, start_point*point_i, "*"]
                find_all_path(start_point * point_i,
                              end_point, step + 1, points, energy+point_i, temp_path, covered_points)
            if ((start_point % point_i) == 0) and ((start_point / point_i) >= 1) and start_point > end_point and point_i != 1 and (start_point/point_i) not in covered_points:
                temp_path = copy.copy(present_path)
                temp_path[step+1] = [point_i, start_point/point_i, "/"]
                find_all_path(start_point / point_i,
                              end_point, step + 1, points, energy+point_i, temp_path, covered_points)


def find_min_energy_path(number_of_path, paths):
    # 找到最小的能量路径
    min_energy = 100
    min_path = []
    min_path_list = []
    temp_paths=copy.copy(paths)
    for top_i in range(number_of_path):
        for i in range(len(temp_paths)):
            if temp_paths[i][-1][0] <= min_energy:
                min_path = i
                min_energy = temp_paths[i][-1][0]
    # for top_i in range(number_of_path):
    #     for i in range(len(paths)):
    #         if (paths[i][-1][0] <= min_energy and paths[i][-1][1] <= min_step) or paths[i][-1][0] < min_energy:
    #             min_path = i
    #             min_energy = paths[i][-1][0]
    #             min_step = paths[i][-1][1]

        # print(str(top_i+1)+" minmal energy: " + str(min_energy))
        min_path_list.append(temp_paths[min_path])
        temp_paths.pop(min_path)
        min_path = []
        min_energy = 100
    return min_path_list


def find_min_step_path(number_of_path, paths):
    # 找到最小的步数路径
    min_step = 15
    min_path = []
    min_path_list = []
    temp_paths=copy.copy(paths)
    for top_i in range(number_of_path):
        for i in range(len(temp_paths)):
            if temp_paths[i][-1][1] <= min_step:
                min_path = i
                min_step = temp_paths[i][-1][1]
        min_path_list.append(temp_paths[min_path])
        temp_paths.pop(min_path)
        min_path = []
        min_step = 15
    return min_path_list


# 可以改动的参数
max_step = 6  # 这里限制了最多的步数，这里是6步，基本上最小的能量都在这里面，这个参数可以改


# 可以用的操作数字，限制在1-10以内，如果被遮挡，可以修改
points_can_use = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
covered_points = [18, 19, 28, 29, 23, 32, 33,
                  34, 42, 43, 44, 53, 59, 68, 69, 70, 79]

# 调用函数，开始遍历
file = open("paths.csv", 'a')
writer = csv.writer(file)
count = 0
while count <= 9:
    path_ = 0
    paths = []
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    if a > b or b > a:
        start_number = min(a, b)
        end_number = max(a, b)
    else:
        continue
    if start_number in covered_points:
        continue
    elif end_number in covered_points:
        continue
    else:
        initial_path = {0: start_number}
        find_all_path(start_number, end_number, 0, points_can_use,
                      0, initial_path, covered_points)
        min_path_list = find_min_energy_path(10, paths)
        min_path_list_step = find_min_step_path(10, paths)

        # reader = csv.reader(file)
        writer.writerow(
            ["第 "+str(count+1)+" 道题,起点："+str(start_number)+",终点:"+str(end_number)])
        for row in range(len(min_path_list)):
            writer.writerow(
                ["" + str(row + 1), min_path_list[row], min_path_list_step[row]])
        count = count+1

file.close()
