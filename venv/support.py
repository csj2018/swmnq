import random

def rd(list):
    r = random.randint(0,len(list)-1)
    result = list[r]
    return result

class Ren:
    def __init__(self):
        self.name = ''
        self.xb = ['男','女'][random.randint(0,1)]
        self.title = ''
        self.power = 0
        self.core = []#功法
        self.skill = []
        self.weapon = []
        self.age = ''
        self.stand = ''

    def creat_title(self):#产生一个名字
        a = ['金','木','水','火','土','银','铁','刚','巨','百''千','万','圣','大','鬼','猛','神','明','黑','白','血','灵']
        b = ['角','腿','猿','牛','鸡','凤','龙','皇','雀','力','敏','鬼','魔','蟒','蛟','麒麟','马','驴','针','瓜','鲸','扇']
        c1 = ['圣君','天君','天尊','真君','魔王','天神','谪仙','魔皇','怪','精灵','神','天神','仙帝','王','帝']
        c2 = ['娘娘','仙子','天仙','女王','女帝','天帝','天女','阿姨','姐']
        if self.xb == '男':
            c = rd(c1)
        else:
            c = rd(c2)
        self.title = rd(a) + rd(b) + c

    def creat_name(self, xing = ''):
        a = ['宁','赵','钱','孙','李','周','吴','郑','王','南宫','北冥','玉','东方','西门','长空','月']
        b = ['华','强','如龙','无声','无缺','鱼儿','小小','龟','怪','大壮','少倾','狗','三桂','峰','无敌','巨基','定','飞'
            ,'如月','天龙','凌风','翔','凌翔','江','槐','云']
        if xing == '':
            self.name = rd(a) + rd(b)
        else:
            self.name = xing + rd(b)

class Party:
    def __init__(self,r = 4):
        self.name = ''
        self.xing = ''
        self.type = ''
        self.power = ''
        self.stand = ''
        self.list_ren = []

        if r > 3:
            r = random.randint(0,3)
        if r == 0:
            self.stand = '友善'
            self.power = int(0.4 * zj.power)
        elif r == 1:
            self.stand = '中立'
            self.power = int(0.2 * zj.power)
        elif r == 2 :
            self.stand = '冷漠'
            self.power = int(0.5 * zj.power)
        else:
            self.stand = '敌对'
            self.power = int(0.7*zj.power)
        #世家 门派
        a = ['金陵','南海','西北','东北','东南','西南','北方','南方','大漠','北洋','珞珈山','玄武湖','岭南','东海']
        b = ['陈','轩辕','东方','北冥','王','李','白','张','百里','独孤','西门','康','胡','赵','孙']
        c = ['玄武','藏剑','万兽','百花','药王','九天','昆仑','苍穹','万古','血魔','九幽','麒麟','霞','影','神剑']
        d = ['宗','派','仙宗','古派','洞','洞府','殿','神殿','宫','教','神教','领域']
        r = random.randint(0,1)
        if r == 0:
            self.xing =rd(b)
            self.name = rd(a) + self.xing + '家'
            self.type = '家族'
        else:
            self.name = rd(c) + rd(d)
            self.type = '门派'

    def add(self):
        a = Ren()
        if self.type == '家族':
            a.creat_name(xing = self.xing)
        else:
            a.creat_name()
        a.creat_title()
        a.stand = self.stand
        self.list_ren.append(a)
        print('%s-%s加入了%s，对待主角态度为%s' %(a.title, a.name, self.name, a.stand))










zj = Ren()
zj.creat_title()
