# -*- coding: utf-8 -*-

from matplotlib.lines import Line2D
import matplotlib.pyplot as plt


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
    if is_left:
        end_pt.x = dir_vec.y
        end_pt.y = dir_vec.x
    else:
        end_pt.x = dir_vec.y
        end_pt.y = -dir_vec.x
    return Vector(start_pt, end_pt)


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


def GetNewPolyLine(poly_line,is_left,dis):
    old_ploy_list = poly_line.point_list
    for i in range(len(old_ploy_list)-2):
        temp_pt1 = old_ploy_list[i]
        temp_pt2 = old_ploy_list.[i+1]
        temp_pt3 = old_ploy_list.[i+2]
        line_norm_front = GetLineNormal(temp_pt1, temp_pt2, is_left)
        line_norm_back = GetLineNormal(temp_pt2, temp_pt3, is_left)
        new_front_pt1 = GetPtByVec(temp_pt1, line_norm_front, dis)
        new_front_pt2 = GetPtByVec(temp_pt2, line_norm_front, dis)
        new_back_pt1 = GetPtByVec(temp_pt2, line_norm_back, dis)
        new_back_pt2 = GetPtByVec(temp_pt3, line_norm_back, dis)
        

        



# 绘制两条线段和交点
figure, ax = plt.subplots()
# 设置x，y值域
ax.set_xlim(left=0, right=20)
ax.set_ylim(bottom=0, top=10)
# 两条line的数据
line1 = [(p1.x, p1.y), (p2.x, p2.y)]
line2 = [(p3.x, p3.y), (p4.x, p4.y)]
line3 = [(p1.x, p1.y), (Pc.x, Pc.y)]
line4 = [(p3.x, p3.y), (Pc.x, Pc.y)]
(line1_xs, line1_ys) = zip(*line1)
(line2_xs, line2_ys) = zip(*line2)
(line3_xs, line3_ys) = zip(*line3)
(line4_xs, line4_ys) = zip(*line4)
# 创建两条线，并添加
ax.add_line(Line2D(line1_xs, line1_ys, linewidth=2, color='blue'))
ax.add_line(Line2D(line2_xs, line2_ys, linewidth=2, color='red'))
ax.add_line(Line2D(line3_xs, line3_ys, linewidth=1, color='yellow'))
ax.add_line(Line2D(line4_xs, line4_ys, linewidth=1, color='green'))
# 展示
plt.plot(Pc.x, Pc.y, 'ro')
plt.plot()
plt.show()
