import autoKS as ks

# -------------- pairs & array data --------------
triangle = 'data/different_formats/triangle.prx'
description_file = 'data/different_formats/description_en.txt'

keyterms = ['蜜蜂', '养蜂人', '蜂蜜', '科学家', '采蜜', '冬天', '疫情', '农药',
            '花田', '太阳', '8字形', '震动', '腹部', '果树', '全球气候变暖', '授粉']

a = ks.cmap2graph(triangle, data_type='array', keyterms=keyterms, read_from=7, pfnet=True, max=1000, min=0.1)
description = ks.cmap2graph(description_file, data_type='pairs')
# ks.draw_html(a, show=False)
# ks.draw_html(b)

# -------------- text data --------------
# Bees (Chinese version), read from file
keyterms_cn = ['蜜蜂', '太阳', '花蜜', '家蜂', '水份', '距离', '蜂巢', '震动',
               '蜂蜜', '腹部', '8字形', '矿物质', '蜜蜡', '蒸发', '风干', '果树']
bees_cn = ks.text2graph('data/different_formats/bees_cn.txt', keyterms_cn)

# Bees (English version), read from string
text_en = "Bees make honey to survive. It is their only essential food. If there are 60,000 bees in a hive about one third of them will be involved in gathering nectar which is then made into honey by the house bees. A small number of bees work as foragers or searchers. They find a source of nectar, then return to the hive to tell the other bees where it is. Foragers let the other bees know where the source of the nectar is by performing a dance which gives information about the direction and the distance the bees will need to fly. During this dance the bee shakes her abdomen from side to side while running in circles in the shape of a figure 8. . If the middle part of the figure 8 points straight up it means that bees can find the food if they fly straight towards the sun. If the middle part of the figure 8 points to the right, the food is to the right of the sun. The distance of the food from the hive is indicated by the length of time that the bee shakes her abdomen. If the food is quite near the bee shakes her abdomen for a short time. If it is a long way away she shakes her abdomen for a long time. When the bees arrive at the hive carrying nectar they give this to the house bees. The house bees move the nectar around with their mandibles, exposing it to the warm dry air of the hive. When it is first gathered the nectar contains sugar and minerals mixed with about 80% water. After ten to twenty minutes, when much of the excess water has evaporated, the house bees put the nectar in a cell in the honeycomb where evaporation continues. After three days, the honey in the cells contains about 20% water. At this stage, the bees cover the cells with lids which they make out of beeswax. At any one time the bees in a hive usually gather nectar from the same type of blossom and from the same area. Some of the main sources of nectar are fruit trees, clover and flowering trees. "
text_en = text_en.replace('honeycomb', 'hive')  # replace synonym (honeycomb --> hive)
keyterms_en = ['beeswax', 'sun', 'nectar', 'house bees', 'water', 'distance',
               'hive', 'shake', 'honey', 'abdomen', 'figure 8', 'minerals',
               'bees', 'evaporation', 'dry', 'fruit trees']
bees_en = ks.text2graph(text_en, keyterms_en, read_from_file=False)

# cc = ks.draw_html(c, show=False)
# dd = ks.draw_html(d)

bees_student_en = ks.cmap2graph('data/different_formats/bees_student_cmap_en.txt', data_type='pairs')
ks.draw_html(bees_student_en)

ks.calc_tversky(bees_en, bees_student_en, comparison='propositional', detailed=True)

# cc = ks.draw_html(c, show=False)
# ss = ks.draw_html(s)

aaa = ks.text2graph('data/different_formats/bees_cn.txt', keyterms_cn)
