import AutoKS as ks

# 【菀麟】将小结文章转换为概念图

# 小结文章放在txt中，所有txt放在一个文件夹中
# 关键词列表
keyterms = ['阿尔茨海默症', '的',  '罹患']  # 需要更改【1】：改为你的关键词

# 获取文件夹下的小结文章文件
filepath = 'C:/Users/韦子谦/Desktop/ad_python_test'  # 需要更改【2】：改为你的文件夹
data = ks.get_data_files_name(filepath)

# 将每个文件中的文本转换为概念图
for text in data:

    # 设置导出的概念图的名称
    name = text.replace(filepath + '/', '')
    name = name.replace('.txt', '')

    # 根据关键词列表，将小结文章转换为概念图
    cmap = ks.text2graph(text=text,
                         keyterms=keyterms,
                         name=name)

    # 将概念图储存为prx文件，保存在这个py文件所在的目录
    ks.graph2prxfile(G=cmap,
                     filetype='array',
                     filename=cmap.name,
                     keyterm_list=keyterms)
