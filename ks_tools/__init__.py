#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import string
import csv
import random
import numpy as np
import pandas as pd
from fractions import Fraction
from matplotlib import rcParams
import networkx as nx
from string import whitespace
import matplotlib.pyplot as plt
from re import finditer
from sys import exit


def del_repeating(m):
    data_m = []
    for i in range(0, m.shape[0]):
        mm = []
        # 将需要删除的row的内容换为“#”
        for j in range(0, m[i].shape[0]):
            if m[i][j, 0] == m[i][j, 1]:  # 类似“蜜蜂-蜜蜂”这样的重复
                m[i][j, 0] = '#'
                m[i][j, 1] = '#'
        # 将内容不为“#”的row放入新的array中
        for jj in range(0, m[i].shape[0]):
            if m[i][jj, 0] != '#':
                # 下面这个if是避免重复的命题进入新的array
                if [m[i][jj, 0], m[i][jj, 1]] not in mm and [m[i][jj, 1], m[i][jj, 0]] not in mm:
                    mm.append([m[i][jj, 0], m[i][jj, 1]])
        mm = np.array(mm)
        data_m.append(mm)
    data_m = np.array(data_m)
    return data_m


def get_terms(data):
    terms = []
    for i in range(0, data.shape[0]):
        t = []
        for row in range(0, data[i].shape[0]):
            for col in range(0, 2):
                if data[i][row, col] not in t:
                    t.append(data[i][row, col])
        terms.append(t)
    terms = np.array(terms)
    return terms


def get_file_name(path_string):
    # 去掉后缀，获取文件名称
    pattern = re.compile(r'([^<>/\\\|:""\*\?]+)\.\w+$')
    data = pattern.findall(path_string)
    if data:
        return data[0]


def load_matrix(filePath):
    # filePath: 数据所在的文件夹路径
    for folder_name, folder_folder, files in os.walk(filePath):
        # os.walk返回的是list,我们把它转换为['1001.txt' '1002.txt' '1003.txt'……]的矩阵
        files = np.array(files)  # 文件名
        # print(folder_name, folder_folder, files)
        file_num = int(files.shape[0])  # 获取文件数量
        print("From '{}/' input {} files.".format(folder_name, file_num))
        # 依次读取并储存至名为pf的list
        pf = [0] * file_num  # numpy没办法直接把字符串矩阵放进零矩阵，所以先放进list，再转换为矩阵
        print(pf)
        print('Contents:')
        for i in range(0, file_num):
            file_name = get_file_name(files[i])  # 调用自定义函数：去掉后缀
            file_path = '{}/{}'.format(folder_name, files[i])
            file_content = get_list(file_path)  # 调用自定义函数：读取文件内容并转换为list
            pf[i] = file_content
            print('File number: {}, Path: {}, File name: {}，Contents:\n{}'.format(i + 1, file_path, file_name,
                                                                                  file_content))
        # 将pf转换为矩阵
        pf = np.array(pf)
        print('Save all contents to an array:\n{}'.format(pf))
        return pf, file_num, files


def get_list(filename):
    """读取文件内容，转换为list"""
    f = open(filename, 'r', encoding='utf-8')  # 打开文件
    content = f.readlines()  # 读取全部内容
    size = content.__len__()  # 读取行数
    # 创建空列表
    List = []
    for i in range(0, size):
        List.append([])
    # 循环读取每一行的内容，放进列表中
    for i in range(0, content.__len__()):  # (开始/左边界, 结束/右边界, 步长)
        my_list = []  # 空列表, 将第i行数据存入list中
        for word in content[i].split():
            word = word.strip(string.whitespace)
            my_list.append(word)
            List[i] = my_list  # 将my_list放入空列表中
    f.close()  # 关闭文件
    matrix = np.array(List)
    return matrix


def get_words(propositions_matrix):
    """检查关键词，将所有的关键词汇总起来，以检测出类似'8'字形'、'8"字，这样同义词"""
    all_terms = list()
    for i in range(0, propositions_matrix.shape[0]):
        this_matrix = propositions_matrix[i]
        for row in range(0, this_matrix.shape[0]):
            for col in range(0, 2):
                if this_matrix[row, col] not in all_terms:
                    all_terms.append(this_matrix[row, col])
    print('Number of terms: {}; terms array: {}'.format(len(all_terms), all_terms))
    return all_terms


def inspect_terms(ref_terms, data_m, subNum):
    """第一个参数是参考图的terms集合，第二个参数是被试的terms集合
    通过参考图terms集合找出被试使用的同义词"""
    synonyms = list()
    for i in range(0, data_m.shape[0]):
        for j in range(0, data_m[i].shape[0]):
            if data_m[i][j][0] not in ref_terms:
                synonyms.append([subNum[i], data_m[i][j][0]])
            if data_m[i][j][1] not in ref_terms:
                synonyms.append([subNum[i], data_m[i][j][1]])
    synonyms = np.array(synonyms)
    print('Words no occurrence in expert/text maps: ', synonyms)
    return synonyms


def compare_matrix(m1, m2):
    """
    :param m1: 被试的矩阵
    :param m2: 参考矩阵
    :return: common links, overlaps, similarity
    """
    # 获取矩阵大小
    m1_size = m1.shape  # (16, 2)
    m2_size = m2.shape  # (17, 2)
    # 获取links数量
    m1_links = m1_size[0]
    m2_links = m2_size[0]
    print('data1 links: ', m1_links)
    print('data2 links: ', m2_links)
    # 共同命题的数量
    common_links = 0
    # 循环检索，存在相同命题时common_links + 1
    for row1 in range(0, m1_size[0]):
        for row2 in range(0, m2_size[0]):
            if m1[row1, 0] == m2[row2, 0] and m1[row1, 1] == m2[row2, 1]:
                common_links += 1
            if m1[row1, 0] == m2[row2, 1] and m1[row1, 1] == m2[row2, 0]:
                common_links += 1
    print('common links: ', common_links)
    # Overlaps = common_links / (sub_links + ref_links) / 2
    overlaps = common_links / ((m1_links + m2_links) / 2)
    print('overlaps: ', overlaps)
    # Similarity = common_links / (sub_links + ref_links - common_links)
    similarity = common_links / (m1_links + m2_links - common_links)
    print('similarity: ', similarity)
    return m1_links, m2_links, common_links, overlaps, similarity


# def compare_matrix_match(m1, m1_terms, text):
#     """
#     :param m1: 被试的矩阵
#     :param m2: 参考矩阵
#     :return: common links, overlaps, similarity
#     """
#
#     # 构建匹配的文本图
#     m2 = (essay2propositions(text, m1_terms))
#
#     # 获取矩阵大小
#     m1_size = m1.shape  # (16, 2)
#     m2_size = m2.shape  # (17, 2)
#     # 获取links数量
#     m1_links = m1_size[0]
#     m2_links = m2_size[0]
#     # 共同命题的数量
#     common_links = 0
#     # 循环检索，存在相同命题时common_links + 1
#     for row1 in range(0, m1_size[0]):
#         for row2 in range(0, m2_size[0]):
#             if m1[row1, 0] == m2[row2, 0] and m1[row1, 1] == m2[row2, 1]:
#                 common_links += 1
#             if m1[row1, 0] == m2[row2, 1] and m1[row1, 1] == m2[row2, 0]:
#                 common_links += 1
#     print('common links: ', common_links)
#     # Overlaps = common_links / (sub_links + ref_links) / 2
#     overlaps = common_links / ((m1_links + m2_links) / 2)
#     print('overlaps: ', overlaps)
#     # Similarity = common_links / (sub_links + ref_links - common_links)
#     similarity = common_links / (m1_links + m2_links - common_links)
#     print('similarity: ', similarity)
#     return m1_links, m2_links, common_links, overlaps, similarity


def gcent(Array):
    ncent_list = []
    gcent_list = []
    for array in range(0, Array.shape[0]):
        node = []
        word = []
        for row in range(0, Array[array].shape[0]):
            for column in range(0, Array[array].shape[1]):
                # [x[0] for x in node]，意为选取node的第一列的内容，放置在一个新列表中
                if not node or Array[array][row, column] not in [x[0] for x in node]:
                    node_deg = 0
                    for r in range(0, Array[array].shape[0]):
                        if Array[array][row, column] in Array[array][r]:
                            node_deg += 1
                    node.append([Array[array][row, column], node_deg])
                    word.append(Array[array][row, column])
        print('\n第', array, '个矩阵\nnode degree：', node)
        # ncent=node_degree/(nodeNum−1))
        ncent = []
        for i in range(0, len(node)):
            ncent.append([node[i][0], node[i][1] / (len(node) - 1)])
        print('ncent：', ncent)
        # gcent=Σ((MAXncent−ncent[i])/(nodeNum−2))
        gcent = 0
        max_ncent = max([x[1] for x in ncent])
        for i in range(0, len(node)):
            gcent += (max_ncent - ncent[i][1]) / (len(node) - 2)
        print('gcent：', float('%.4f' % gcent))
        gcent_list.append(float('%.4f' % gcent))
        ncent_list.append(ncent)
    print('\ngcent列表:', gcent_list)
    return np.array(ncent_list), np.array(gcent_list)


def save_prx(keyterms, p, filename):
    # 创建一个邻接矩阵
    m = np.zeros((len(keyterms), len(keyterms)))  # n*n adjacent matrix
    for i in range(0, m.shape[0]):
        m[i, i] = 1
    # 检索命题矩阵p，在邻接矩阵中记录出现的命题
    for i in range(0, p.shape[0]):
        if p[i, 0] in keyterms and p[i, 1] in keyterms:  # 如果命题中的两个词属于关键词
            for row in range(0, len(keyterms)):
                if keyterms[row] == p[i, 0]:
                    for column in range(0, len(keyterms)):
                        if keyterms[column] == p[i, 1]:
                            m[row, column] = 1
                            m[column, row] = 1
    # 保存为prx文件
    filename = 'prx_file/' + filename + '.prx'
    np.savetxt(filename, m, fmt='%f', delimiter=' ', encoding='utf-8')
    # 在文件开头添加必要的信息（否则Pathfinder软件无法读取）
    info = 'DATA: Text link.prx\nsimilarities\n{}  items' \
           '\n1 decimals\n0.1 min\n1 max\nmatrix:\n'.format(len(keyterms))
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(info + content)


def pick_words(keywords_list, number):
    # 从keywords_list中随机选择number个词
    picked = []
    for i in range(0, number):
        index = random.randint(0, len(keywords_list) - 1)
        if keywords_list[index] not in picked:
            picked.append(keywords_list[index])
    print('选择', number, '个词:', picked)
    return picked


def create_random_matrix(terms, linksNum):
    # 根据关键词，生成linksNum个命题并返回
    all_done = False
    while not all_done:
        m = []  # 用于存储生成的命题
        for i in range(0, int(round(linksNum))):  # 运行linksNum次
            done_for_this_loop = False
            while not done_for_this_loop:
                # 随机拿出两个词，放入列表m
                first_word = terms[random.randint(0, len(terms) - 1)]  # 确定命题中的第一个词
                find_sec = False
                while not find_sec:
                    second_word = terms[random.randint(0, len(terms) - 1)]  # 确定第二个词
                    if second_word != first_word:  # 第二个词不能和第一个词一样
                        find_sec = True
                # 如果生成的命题不在m中，则放入列表m
                if not m:  # 如果m为空列表
                    m.append([first_word, second_word])  # 那么就放入第一个命题啦
                    done_for_this_loop = True
                elif [first_word, second_word] not in m and [second_word, first_word] not in m:
                    m.append([first_word, second_word])
                    done_for_this_loop = True
        # 检查是否每个关键词至少和另一个词连接，如果“否”，则重新生成矩阵
        count = 0
        for i in range(0, len(terms)):
            for row in range(0, len(m)):
                if terms[i] in m[row]:
                    count += 1
                    break
        if count == len(terms) and len(m) == int(round(linksNum)):
            all_done = True
    print('生成的矩阵:', m)
    return np.array(m)


def draw(m, filename=''):
    m_size = m.shape
    # 绘图
    g = nx.Graph()
    for i in range(0, m_size[0]):
        node1 = m[i, 0]
        node2 = m[i, 1]
        g.add_edge(node1, node2)
    nx.draw(g, node_size=300, node_color='#ffebcd', edge_color='#7ab8cc', with_labels=True)
    rcParams['font.sans-serif'] = ['SimHei']
    rcParams['font.family'] = 'sans-serif'
    if filename != '':
        plt.savefig("{}.png".format(filename), format="PNG", dpi=300)
        plt.show()  # don't show picture when saving
    else:
        plt.show()  # don't show picture when saving


def floyd(dis, r=float('inf')):
    """

    Roger Schvaneveldt (2021).
    Pathfinder Networks
    (https://www.mathworks.com/matlabcentral/fileexchange/59378-pathfinder-networks),
    MATLAB Central File Exchange. Retrieved March 23, 2021.



    Copyright (c) 2016, Roger Schvaneveldt
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this
      list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



    """
    # mindis = floyd(dis,r)
    # dis    | dissimilarity matrix
    # r      | value of the r parameter
    # mindis | minimum distance between nodes
    # links  | links in the PFnet(q=n-1,r)
    # (based on Floyd algorithm for finding shortest paths)

    # in this function, parameter q = n - 1, n = number of nodes

    inf = float('inf')

    n = dis.shape[0]
    mindis = dis.copy()

    for ind in range(0, n):
        for row in range(0, n):
            for col in range(0, n):
                # indirect = minkowski(mindis(row,ind), mindis(ind,col),r)
                indirect = np.linalg.norm([mindis[row, ind], mindis[ind, col]], r)
                if indirect < mindis[row, col]:
                    mindis[row, col] = indirect

    tflinks = (dis < inf) & (abs(mindis - dis) < 1e-14)

    return tflinks


def text2prx(text, terms):
    # error information
    for i in terms:
        for t in terms:
            if i != t and i in t and terms.index(i) < terms.index(t):
                print('\nERROR!\n'
                      '"{}" comes before "{}" in key terms list!\n'
                      'this might conduct some error, \n'
                      'because term "{}" in the text would be detected as term "{}".\n'
                      'please re-order your terms list and insure "{}" after "{}".\n'
                      .format(i, t, i, t, i, t))
                exit()

    chain = []
    prx = np.zeros([len(terms), len(terms)])

    for t in terms:
        for index in finditer(t, text):  # obtain index of terms in the text
            if chain:
                """

                before add the new index into the list "chain",
                we need to check the index to avoid the error.

                for example, when obtain a index of term "bee" in the text,
                it would first check whether this index is contain in the span of term "beekeeper",
                if the answer is "True", this index wouldn't be included in the "chain".

                for this purpose, please insure small terms (e.g., "bee") were after
                bigger terms (e.g., "beekeeper") in the terms list.

                """

                check = False
                for i in chain:
                    if index.span()[0] >= i[0][0] and index.span()[1] <= i[0][1] and index.span() != i[0]:
                        check = True
                        break
                if not check:
                    chain.append([index.span(), terms.index(t)])
            else:
                chain.append([index.span(), terms.index(t)])

    chain.sort()  # sort by order of occurrence
    chain = list(x[1] for x in chain)  # keep index of terms only

    for i in range(len(chain) - 1):
        prx[chain[i], chain[i + 1]] = 1
        prx[chain[i + 1], chain[i]] = 1
        prx[chain[i], chain[i]] = None  # 对角线的元素赋值为NaN

    return prx
