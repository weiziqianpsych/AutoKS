import AutoKS as ks

# data
text_s = 'C:/Users/韦子谦/Desktop/ad_python_test/ad_symptom.txt'
text_g = 'C:/Users/韦子谦/Desktop/ad_python_test/ad_genes.txt'
text_d = 'C:/Users/韦子谦/Desktop/ad_python_test/ad_down.txt'

keyterm_s = [
    '大脑变化',
    '记忆',
    '思维',
    '淀粉样斑块',
    '神经元纤维缠结',
    '症状',
    '第一信号',
    '轻度认知障碍',
    '早期阶段',
    '生物标记物',
    '高风险人群',
    '诊断',
    '病史'
]
keyterm_g = [
    '基因',
    '亲生父母',
    '遗传突变',
    '遗传变异',
    '六十岁',
    '晚发型',
    '十九号染色体',
    '载脂蛋白E',
    '患病概率',
    '早发型',
    '二十一号染色体',
    '淀粉样前体蛋白',
    '血液测试'
]
keyterm_d = [
    '唐氏综合征患者',
    '痴呆',
    '染色体',
    '智力缺陷',
    '三十岁',
    '基线数据文档',
    '科学家',
    '志愿者',
    '临床研究',
    '风险和收益',
    '符合研究要求',
    '家庭成员/监护人'
]

# ks conversion
ad_s = ks.text2graph(text_s, keyterm_s, name='ad_s')
ad_g = ks.text2graph(text_g, keyterm_g, name='ad_g', as_lower=False)
ad_d = ks.text2graph(text_d, keyterm_d, name='ad_d')

# gcent
ad_dict = {'ad_s': [ad_s, keyterm_s],
           'ad_g': [ad_g, keyterm_g],
           'ad_d': [ad_d, keyterm_d]}
for ad in ad_dict:
    print('\n', ad_dict[ad][0].name)
    print(f'nodes: {len(ad_dict[ad][0].nodes)}/{len(ad_dict[ad][1])}')
    print('gcent:', ks.calc_gcent(ad_dict[ad][0]))
    print('propositions num:', len(ad_dict[ad][0].edges))

# ks.calc_gcent(ad_g, detailed=True)
ks.draw(ad_g)

# draw
# ks.draw_html(ad_s, show=False)
# ks.draw_html(ad_g, show=False)
# ks.draw_html(ad_d)

# # ad text
# text = text_s + text_g + text_d
# total_keyterms_list = list(set(keyterm_s + keyterm_g + keyterm_d))
# ad = ks.text2graph(text, total_keyterms_list, name='ad', read_from_file=False)
# print('AD text gcent: ', ks.calc_gcent(ad))  # gcent
# # ks.draw_html(ad)  # graph
#
# # shared links
# shared = []
# for pair in ad.edges:
#     for group in [keyterm_s, keyterm_g, keyterm_d]:
#         if pair[0] in group and pair[1] not in group:
#             if pair[0] not in ['阿尔茨海默症', '科学家', '研究者', '研究', '患者'] and pair[1] not in ['阿尔茨海默症', '科学家', '研究者', '研究', '患者']:
#                 if [pair[0], pair[1]] not in shared and [pair[1], pair[0]] not in shared:
#                     shared.append(pair)



