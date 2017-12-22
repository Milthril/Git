# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import math


class Point(object):
    x = 0
    y = 0

    # 定义构造方法
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Vector(object):
    def __init__(self, start_point, end_point):
        self.start, self.end = start_point, end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y


class Line(object):
    # a=0
    # b=0
    # c=0
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class PolyLine(object):
    def __init__(self, pt_list):
        self.point_list = pt_list


# 初始化数据
p1 = Point(0, 0)
p2 = Point(1, 1)
line1 = Line(p1, p2)

p3 = Point(11.3, 0)
p4 = Point(5, 2)
line2 = Line(p3, p4)
ZERO = 1e-9


# 判断线段是否相交
def negative(vector):
    """取反"""
    return Vector(vector.end, vector.start)


def vector_product(vectorA, vectorB):
    '''计算 x_1 * y_2 - x_2 * y_1'''
    return vectorA.x * vectorB.y - vectorB.x * vectorA.y


def is_intersected(A, B, C, D):
    '''A, B, C, D 为 Point 类型'''
    AC = Vector(A, C)
    AD = Vector(A, D)
    BC = Vector(B, C)
    BD = Vector(B, D)
    CA = negative(AC)
    CB = negative(BC)
    DA = negative(AD)
    DB = negative(BD)

    return (vector_product(AC, AD) * vector_product(BC, BD) <= ZERO) \
        and (vector_product(CA, CB) * vector_product(DA, DB) <= ZERO)


result = is_intersected(p1, p2, p3, p4)
print("两条线段是否相交:", result)


# 计算线段交点
def GetLinePara(line):
    line.a = line.p1.y - line.p2.y
    line.b = line.p2.x - line.p1.x
    line.c = line.p1.x * line.p2.y - line.p2.x * line.p1.y


def GetCrossPoint(l1, l2):

    GetLinePara(l1)
    GetLinePara(l2)
    if l1.a == l2.a and l2.b == l1.b:
        return None

    d = l1.a * l2.b - l2.a * l1.b
    p = Point()
    p.x = (l1.b * l2.c - l2.b * l1.c) * 1.0 / d
    p.y = (l1.c * l2.a - l2.c * l1.a) * 1.0 / d
    return p


Pc = GetCrossPoint(line1, line2)
print("Cross point:", Pc.x, Pc.y)


# 求平面中任意多段线按照左右方向平移一定距离的新线
def GetLineNormal(pt1, pt2, is_left):
    dir_vec = Vector(pt1, pt2)
    start_pt = Point(0, 0)
    end_pt = Point(0, 0)
    end_pt.x = -dir_vec.y
    end_pt.y = dir_vec.x
    if is_left:
        return Vector(start_pt, end_pt)
    else:
        return Vector(end_pt, start_pt)


def NormalizeVec(vector):
    length = vector.x * vector.x + vector.y * vector.y
    new_x = vector.x / length
    new_y = vector.y / length
    start_pt = Point(0, 0)
    end_pt = Point(new_x, new_y)
    return Vector(start_pt, end_pt)


def GetPtByVec(pt, vector, dis):
    vec_shift = NormalizeVec(vector)
    x = pt.x + vec_shift.x * dis
    y = pt.y + vec_shift.y * dis
    new_pt = Point(x, y)
    return new_pt


def GetNewPolyLine(poly_line, is_left, dis):
    if len(poly_line.point_list) != len(dis) + 1:
        return

    old_ploy_list = poly_line.point_list
    new_poly_list = list()
    for i in range(0, len(old_ploy_list) - 2):
        temp_pt1 = old_ploy_list[i]
        temp_pt2 = old_ploy_list[i + 1]
        temp_pt3 = old_ploy_list[i + 2]
        line_norm_front = GetLineNormal(temp_pt1, temp_pt2, is_left)
        line_norm_back = GetLineNormal(temp_pt2, temp_pt3, is_left)
        new_front_pt1 = GetPtByVec(temp_pt1, line_norm_front, dis[i])
        new_front_pt2 = GetPtByVec(temp_pt2, line_norm_front, dis[i])
        new_back_pt1 = GetPtByVec(temp_pt2, line_norm_back, dis[i + 1])
        new_back_pt2 = GetPtByVec(temp_pt3, line_norm_back, dis[i + 1])

        if i == 0:
            new_poly_list.append(new_front_pt1)

        new_pt = Point(0, 0)
        if new_front_pt2.x == new_back_pt1.x\
           and new_front_pt2.y == new_back_pt1.y:
            new_pt = new_front_pt2
            new_poly_list.append(new_pt)
        else:
            new_front_line = Line(new_front_pt1, new_front_pt2)
            new_back_line = Line(new_back_pt1, new_back_pt2)
            if GetCrossPoint(new_front_line, new_back_line) is None:
                new_poly_list.append(new_front_pt2)
                new_poly_list.append(new_back_pt1)
            else:
                new_pt = GetCrossPoint(new_front_line, new_back_line)
                new_poly_list.append(new_pt)

        if i == len(old_ploy_list) - 3:
            new_poly_list.append(new_back_pt2)

    new_poly_line = PolyLine(new_poly_list)
    return new_poly_line


pt_list = list()
dis_list = list()
x_len = 20
dis_step = 0.3
for i in range(1, x_len):
    x = i
    y = i % 2
    if i < x_len / 2 + 1:
        dis = 1 - dis_step + i * dis_step
    else:
        dis = 1 + dis_step * (x_len / 2) - (i - x_len / 2) * dis_step
    pt = Point(x, y)
    pt_list.append(pt)
    dis_list.append(dis)
del dis_list[0]
poly_line = PolyLine(pt_list)
new_poly_line = GetNewPolyLine(poly_line, True, dis_list)
new_poly_line2 = GetNewPolyLine(poly_line, False, dis_list)

# 绘制两条线段和交点
figure, ax = plt.subplots()
# 设置x，y值域
ax.set_xlim(left=-50, right=50)
ax.set_ylim(bottom=-50, top=50)

# 绘制polyline数据
x1_list = list()
y1_list = list()
for pt in poly_line.point_list:
    x1_list.append(pt.x)
    y1_list.append(pt.y)
plt.plot(x1_list, y1_list, linewidth=2, color='red')
plt.scatter(x1_list, y1_list, s=10, color='red')

x2_list = list()
y2_list = list()
for pt in new_poly_line.point_list:
    x2_list.append(pt.x)
    y2_list.append(pt.y)
plt.plot(x2_list, y2_list, linewidth=2, color='blue')
plt.scatter(x2_list, y2_list, s=10, color='blue')

x3_list = list()
y3_list = list()
for pt in new_poly_line2.point_list:
    x3_list.append(pt.x)
    y3_list.append(pt.y)
plt.plot(x3_list, y3_list, linewidth=2, color='blue')
plt.scatter(x3_list, y3_list, s=10, color='blue')

plt.show()
