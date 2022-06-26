import AutoKS as ks

ref = ks.cmap2graph("C:\\Users\\韦子谦\\Desktop\\ref.txt", data_type='pair')
# print(ks.calc_gcent(ref))

d1 = ks.cmap2graph("C:\\Users\\韦子谦\\Desktop\\1101.txt", data_type='pair')
d2 = ks.cmap2graph("C:\\Users\\韦子谦\\Desktop\\1102.txt", data_type='pair')
d3 = ks.cmap2graph("C:\\Users\\韦子谦\\Desktop\\1103.txt", data_type='pair')
d4 = ks.cmap2graph("C:\\Users\\韦子谦\\Desktop\\1104.txt", data_type='pair')
d5 = ks.cmap2graph("C:\\Users\\韦子谦\\Desktop\\1105.txt", data_type='pair')

for d in [d1, d2, d3, d4, d5]:
    gcent = ks.calc_gcent(d)
    result1 = ks.calc_tversky(d, ref, comparison='concept')
    result2 = ks.calc_tversky(d, ref, comparison='propositional')
    result3 = ks.calc_tversky(d, ref, comparison='semantic')
    print(gcent, result1, result2, result3)

# keyterms = ['这里写关键词', '每个元素是一个词', '要和矩阵的词的顺序一致']
# output = ks.cmap2graph(file='这里写文件目录',
#                        data_type='array',
#                        keyterms=keyterms,
#                        pfnet=True,
#                        sim_max='这里改成prx文件里的max的值（数值型）',
#                        sim_min='这里改成min的值'
#                        )
# ks.draw(output)
# d1 = [['遵义会议', '长征'],
#       ['长征', '“左”倾错误'],
#       ['“左”倾错误', '反“围剿”战争'],
#       ['长征', '反“围剿”战争'],
#       ['反“围剿”战争', '土地革命'],
#       ['土地革命', '农村包围城市、武装夺取政权'],
#       ['反“围剿”战争', '农村包围城市、武装夺取政权'],
#       ['农村包围城市、武装夺取政权', '毛泽东思想'],
#       ['农村包围城市、武装夺取政权', '古田会议'],
#       ['农村包围城市、武装夺取政权', '八七会议'],
#       ['八七会议', '南昌起义'],
#       ['南昌起义', '宁汉合流'],
#       ['南昌起义', '秋收起义'],
#       ['秋收起义', '广州起义']
#       ]
#
# d1ks = ks.cmap2graph(
#     file=d1,
#     data_type='pair',
#     read_from_file=False)
#
# ks.draw_html(d1ks, show=False, save=True,
#              filename='C:/Users/韦子谦/Desktop/d1ks',
#              encoding='UTF-8')
#
# d2 = [['宁汉合流', '八七会议'],
#       ['八七会议', '南昌起义'],
#       ['南昌起义', '秋收起义'],
#       ['秋收起义', '广州起义'],
#       ['广州起义', '农村包围城市、武装夺取政权'],
#       ['古田会议', '农村包围城市、武装夺取政权'],
#       ['古田会议', '毛泽东思想'],
#       ['古田会议', '土地革命'],
#       ['古田会议', '反“围剿”战争'],
#       ['反“围剿”战争', '“左”倾错误'],
#       ['“左”倾错误', '遵义会议'],
#       ['遵义会议', '长征']
#       ]
#
# d2ks = ks.cmap2graph(
#     file=d2,
#     data_type='pair',
#     read_from_file=False)
#
# ks.draw_html(d2ks, show=False, save=True,
#              filename='C:/Users/韦子谦/Desktop/d2ks',
#              encoding='UTF-8')
#
# # bees_student_en = ks.cmap2graph(file='data/different_formats/bees_student_cmap_en.txt', data_type='pairs')
#
# # -------------- text data --------------
# # Bees (Chinese version), read from file
# # keyterms_cn = ['蜜蜂', '太阳', '花蜜', '家蜂', '水份', '距离', '蜂巢', '震动',
# #                '蜂蜜', '腹部', '8字形', '矿物质', '蜜蜡', '蒸发', '风干', '果树']
# # bees_cn = ks.text2graph('data/different_formats/bees_cn.txt', keyterms_cn)
#
# # keyterms_en = ['beeswax', 'sun', 'nectar', 'house bees', 'water', 'distance',
# #                'hive', 'shake', 'honey', 'abdomen', 'figure 8', 'minerals',
# #                'bees', 'evaporation', 'dry', 'fruit trees']
# #
# # bees_en = ks.text2graph(text='data/different_formats/bees_en.txt',
# #                         keyterms=keyterms_en,
# #                         synonym={'hive': ['honeycomb']}
# #                         )
# #
# # ks.calc_gcent(bees_student_en, detailed=True)
# # print(ks.calc_surface_matching(bees_en, bees_student_en))
# # print(ks.calc_graphical_matching(bees_en, bees_student_en))
#
# # ks.calc_tversky(bees_en, bees_student_en, comparison='concept')
# # ks.calc_tversky(bees_en, bees_student_en, comparison='propositional')
# # ks.calc_tversky(bees_en, bees_student_en, comparison='semantic')
#
# # ks.draw_html(bees_student_en, show=False)
# # ks.draw_html(bees_en)
