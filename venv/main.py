from support import *


#故事背景
list_bg = []#事情发生的背景
list_time = ['百年前','千年前','万年前','十万年前','百万年前','千万年前','亿万年前','一个时代前']#时代
list_state = ['神州大陆','通玄大陆','兔子大陆','中华大陆','魔法大陆','斗罗大陆']#地点
list_party = []#阵营分为
list_rw = []#人物

time = []
state = rd(list_state)
ren_temp = []

for i in range(3):
    ren_temp.append(Ren())
    ren_temp[i].creat_title()
    time.append(rd(list_time))

bg = '    ' + state + '浩瀚无边，其上承载亿万生灵。历经无数时代，诞生强者不知几何。' \
    + time[0] + '，' + ren_temp[0].title + '承载天命，一世独尊。' \
    + time[1] + '，' + ren_temp[1].title + '统治整个时代，天下无敌。'\
    + time[2] + '，更是有' + ren_temp[2].title + '三世共尊！'\
    + '而这万古的幕后黑手' + zj.title + zj.name + '却无人知晓。\n'
bg +='  然而这一世，'
#
#
#
#
#
#

print(bg)

a = Party(1)
for i in range(4):
    a.add()











