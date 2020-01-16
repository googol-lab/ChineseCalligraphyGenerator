import json

# most popular 3500 characters
charset = ["的", "一", "是", "不", "了", "在", "人", "有", "我", "他", "这", "个", "们", "中", "来", "上", "大", "为", "和", "国", "地", "到",
           "以", "说", "时", "要", "就", "出", "会", "可", "也", "你", "对", "生", "能", "而", "子", "那", "得", "于", "着", "下", "自", "之",
           "年", "过", "发", "后", "作", "里", "用", "道", "行", "所", "然", "家", "种", "事", "成", "方", "多", "经", "么", "去", "法", "学",
           "如", "都", "同", "现", "当", "没", "动", "面", "起", "看", "定", "天", "分", "还", "进", "好", "小", "部", "其", "些", "主", "样",
           "理", "心", "她", "本", "前", "开", "但", "因", "只", "从", "想", "实", "日", "军", "者", "意", "无", "力", "它", "与", "长", "把",
           "机", "十", "民", "第", "公", "此", "已", "工", "使", "情", "明", "性", "知", "全", "三", "又", "关", "点", "正", "业", "外", "将",
           "两", "高", "间", "由", "问", "很", "最", "重", "并", "物", "手", "应", "战", "向", "头", "文", "体", "政", "美", "相", "见", "被",
           "利", "什", "二", "等", "产", "或", "新", "己", "制", "身", "果", "加", "西", "斯", "月", "话", "合", "回", "特", "代", "内", "信",
           "表", "化", "老", "给", "世", "位", "次", "度", "门", "任", "常", "先", "海", "通", "教", "儿", "原", "东", "声", "提", "立", "及",
           "比", "员", "解", "水", "名", "真", "论", "处", "走", "义", "各", "入", "几", "口", "认", "条", "平", "系", "气", "题", "活", "尔",
           "更", "别", "打", "女", "变", "四", "神", "总", "何", "电", "数", "安", "少", "报", "才", "结", "反", "受", "目", "太", "量", "再",
           "感", "建", "务", "做", "接", "必", "场", "件", "计", "管", "期", "市", "直", "德", "资", "命", "山", "金", "指", "克", "许", "统",
           "区", "保", "至", "队", "形", "社", "便", "空", "决", "治", "展", "马", "科", "司", "五", "基", "眼", "书", "非", "则", "听", "白",
           "却", "界", "达", "光", "放", "强", "即", "像", "难", "且", "权", "思", "王", "象", "完", "设", "式", "色", "路", "记", "南", "品",
           "住", "告", "类", "求", "据", "程", "北", "边", "死", "张", "该", "交", "规", "万", "取", "拉", "格", "望", "觉", "术", "领", "共",
           "确", "传", "师", "观", "清", "今", "切", "院", "让", "识", "候", "带", "导", "争", "运", "笑", "飞", "风", "步", "改", "收", "根",
           "干", "造", "言", "联", "持", "组", "每", "济", "车", "亲", "极", "林", "服", "快", "办", "议", "往", "元", "英", "士", "证", "近",
           "失", "转", "夫", "令", "准", "布", "始", "怎", "呢", "存", "未", "远", "叫", "台", "单", "影", "具", "罗", "字", "爱", "击", "流",
           "备", "兵", "连", "调", "深", "商", "算", "质", "团", "集", "百", "需", "价", "花", "党", "华", "城", "石", "级", "整", "府", "离",
           "况", "亚", "请", "技", "际", "约", "示", "复", "病", "息", "究", "线", "似", "官", "火", "断", "精", "满", "支", "视", "消", "越",
           "器", "容", "照", "须", "九", "增", "研", "写", "称", "企", "八", "功", "吗", "包", "片", "史", "委", "乎", "查", "轻", "易", "早",
           "曾", "除", "农", "找", "装", "广", "显", "吧", "阿", "李", "标", "谈", "吃", "图", "念", "六", "引", "历", "首", "医", "局", "突",
           "专", "费", "号", "尽", "另", "周", "较", "注", "语", "仅", "考", "落", "青", "随", "选", "列", "武", "红", "响", "虽", "推", "势",
           "参", "希", "古", "众", "构", "房", "半", "节", "土", "投", "某", "案", "黑", "维", "革", "划", "敌", "致", "陈", "律", "足", "态",
           "护", "七", "兴", "派", "孩", "验", "责", "营", "星", "够", "章", "音", "跟", "志", "底", "站", "严", "巴", "例", "防", "族", "供",
           "效", "续", "施", "留", "讲", "型", "料", "终", "答", "紧", "黄", "绝", "奇", "察", "母", "京", "段", "依", "批", "群", "项", "故",
           "按", "河", "米", "围", "江", "织", "害", "斗", "双", "境", "客", "纪", "采", "举", "杀", "攻", "父", "苏", "密", "低", "朝", "友",
           "诉", "止", "细", "愿", "千", "值", "仍", "男", "钱", "破", "网", "热", "助", "倒", "育", "属", "坐", "帝", "限", "船", "脸", "职",
           "速", "刻", "乐", "否", "刚", "威", "毛", "状", "率", "甚", "独", "球", "般", "普", "怕", "弹", "校", "苦", "创", "假", "久", "错",
           "承", "印", "晚", "兰", "试", "股", "拿", "脑", "预", "谁", "益", "阳", "若", "哪", "微", "尼", "继", "送", "急", "血", "惊", "伤",
           "素", "药", "适", "波", "夜", "省", "初", "喜", "卫", "源", "食", "险", "待", "述", "陆", "习", "置", "居", "劳", "财", "环", "排",
           "福", "纳", "欢", "雷", "警", "获", "模", "充", "负", "云", "停", "木", "游", "龙", "树", "疑", "层", "冷", "洲", "冲", "射", "略",
           "范", "竟", "句", "室", "异", "激", "汉", "村", "哈", "策", "演", "简", "卡", "罪", "判", "担", "州", "静", "退", "既", "衣", "您",
           "宗", "积", "余", "痛", "检", "差", "富", "灵", "协", "角", "占", "配", "征", "修", "皮", "挥", "胜", "降", "阶", "审", "沉", "坚",
           "善", "妈", "刘", "读", "啊", "超", "免", "压", "银", "买", "皇", "养", "伊", "怀", "执", "副", "乱", "抗", "犯", "追", "帮", "宣",
           "佛", "岁", "航", "优", "怪", "香", "著", "田", "铁", "控", "税", "左", "右", "份", "穿", "艺", "背", "阵", "草", "脚", "概", "恶",
           "块", "顿", "敢", "守", "酒", "岛", "托", "央", "户", "烈", "洋", "哥", "索", "胡", "款", "靠", "评", "版", "宝", "座", "释", "景",
           "顾", "弟", "登", "货", "互", "付", "伯", "慢", "欧", "换", "闻", "危", "忙", "核", "暗", "姐", "介", "坏", "讨", "丽", "良", "序",
           "升", "监", "临", "亮", "露", "永", "呼", "味", "野", "架", "域", "沙", "掉", "括", "舰", "鱼", "杂", "误", "湾", "吉", "减", "编",
           "楚", "肯", "测", "败", "屋", "跑", "梦", "散", "温", "困", "剑", "渐", "封", "救", "贵", "枪", "缺", "楼", "县", "尚", "毫", "移",
           "娘", "朋", "画", "班", "智", "亦", "耳", "恩", "短", "掌", "恐", "遗", "固", "席", "松", "秘", "谢", "鲁", "遇", "康", "虑", "幸",
           "均", "销", "钟", "诗", "藏", "赶", "剧", "票", "损", "忽", "巨", "炮", "旧", "端", "探", "湖", "录", "叶", "春", "乡", "附", "吸",
           "予", "礼", "港", "雨", "呀", "板", "庭", "妇", "归", "睛", "饭", "额", "含", "顺", "输", "摇", "招", "婚", "脱", "补", "谓", "督",
           "毒", "油", "疗", "旅", "泽", "材", "灭", "逐", "莫", "笔", "亡", "鲜", "词", "圣", "择", "寻", "厂", "睡", "博", "勒", "烟", "授",
           "诺", "伦", "岸", "奥", "唐", "卖", "俄", "炸", "载", "洛", "健", "堂", "旁", "宫", "喝", "借", "君", "禁", "阴", "园", "谋", "宋",
           "避", "抓", "荣", "姑", "孙", "逃", "牙", "束", "跳", "顶", "玉", "镇", "雪", "午", "练", "迫", "爷", "篇", "肉", "嘴", "馆", "遍",
           "凡", "础", "洞", "卷", "坦", "牛", "宁", "纸", "诸", "训", "私", "庄", "祖", "丝", "翻", "暴", "森", "塔", "默", "握", "戏", "隐",
           "熟", "骨", "访", "弱", "蒙", "歌", "店", "鬼", "软", "典", "欲", "萨", "伙", "遭", "盘", "爸", "扩", "盖", "弄", "雄", "稳", "忘",
           "亿", "刺", "拥", "徒", "姆", "杨", "齐", "赛", "趣", "曲", "刀", "床", "迎", "冰", "虚", "玩", "析", "窗", "醒", "妻", "透", "购",
           "替", "塞", "努", "休", "虎", "扬", "途", "侵", "刑", "绿", "兄", "迅", "套", "贸", "毕", "唯", "谷", "轮", "库", "迹", "尤", "竞",
           "街", "促", "延", "震", "弃", "甲", "伟", "麻", "川", "申", "缓", "潜", "闪", "售", "灯", "针", "哲", "络", "抵", "朱", "埃", "抱",
           "鼓", "植", "纯", "夏", "忍", "页", "杰", "筑", "折", "郑", "贝", "尊", "吴", "秀", "混", "臣", "雅", "振", "染", "盛", "怒", "舞",
           "圆", "搞", "狂", "措", "姓", "残", "秋", "培", "迷", "诚", "宽", "宇", "猛", "摆", "梅", "毁", "伸", "摩", "盟", "末", "乃", "悲",
           "拍", "丁", "赵", "硬", "麦", "蒋", "操", "耶", "阻", "订", "彩", "抽", "赞", "魔", "纷", "沿", "喊", "违", "妹", "浪", "汇", "币",
           "丰", "蓝", "殊", "献", "桌", "啦", "瓦", "莱", "援", "译", "夺", "汽", "烧", "距", "裁", "偏", "符", "勇", "触", "课", "敬", "哭",
           "懂", "墙", "袭", "召", "罚", "侠", "厅", "拜", "巧", "侧", "韩", "冒", "债", "曼", "融", "惯", "享", "戴", "童", "犹", "乘", "挂",
           "奖", "绍", "厚", "纵", "障", "讯", "涉", "彻", "刊", "丈", "爆", "乌", "役", "描", "洗", "玛", "患", "妙", "镜", "唱", "烦", "签",
           "仙", "彼", "弗", "症", "仿", "倾", "牌", "陷", "鸟", "轰", "咱", "菜", "闭", "奋", "庆", "撤", "泪", "茶", "疾", "缘", "播", "朗",
           "杜", "奶", "季", "丹", "狗", "尾", "仪", "偷", "奔", "珠", "虫", "驻", "孔", "宜", "艾", "桥", "淡", "翼", "恨", "繁", "寒", "伴",
           "叹", "旦", "愈", "潮", "粮", "缩", "罢", "聚", "径", "恰", "挑", "袋", "灰", "捕", "徐", "珍", "幕", "映", "裂", "泰", "隔", "启",
           "尖", "忠", "累", "炎", "暂", "估", "泛", "荒", "偿", "横", "拒", "瑞", "忆", "孤", "鼻", "闹", "羊", "呆", "厉", "衡", "胞", "零",
           "穷", "舍", "码", "赫", "婆", "魂", "灾", "洪", "腿", "胆", "津", "俗", "辩", "胸", "晓", "劲", "贫", "仁", "偶", "辑", "邦", "恢",
           "赖", "圈", "摸", "仰", "润", "堆", "碰", "艇", "稍", "迟", "辆", "废", "净", "凶", "署", "壁", "御", "奉", "旋", "冬", "矿", "抬",
           "蛋", "晨", "伏", "吹", "鸡", "倍", "糊", "秦", "盾", "杯", "租", "骑", "乏", "隆", "诊", "奴", "摄", "丧", "污", "渡", "旗", "甘",
           "耐", "凭", "扎", "抢", "绪", "粗", "肩", "梁", "幻", "菲", "皆", "碎", "宙", "叔", "岩", "荡", "综", "爬", "荷", "悉", "蒂", "返",
           "井", "壮", "薄", "悄", "扫", "敏", "碍", "殖", "详", "迪", "矛", "霍", "允", "幅", "撒", "剩", "凯", "颗", "骂", "赏", "液", "番",
           "箱", "贴", "漫", "酸", "郎", "腰", "舒", "眉", "忧", "浮", "辛", "恋", "餐", "吓", "挺", "励", "辞", "艘", "键", "伍", "峰", "尺",
           "昨", "黎", "辈", "贯", "侦", "滑", "券", "崇", "扰", "宪", "绕", "趋", "慈", "乔", "阅", "汗", "枝", "拖", "墨", "胁", "插", "箭",
           "腊", "粉", "泥", "氏", "彭", "拔", "骗", "凤", "慧", "媒", "佩", "愤", "扑", "龄", "驱", "惜", "豪", "掩", "兼", "跃", "尸", "肃",
           "帕", "驶", "堡", "届", "欣", "惠", "册", "储", "飘", "桑", "闲", "惨", "洁", "踪", "勃", "宾", "频", "仇", "磨", "递", "邪", "撞",
           "拟", "滚", "奏", "巡", "颜", "剂", "绩", "贡", "疯", "坡", "瞧", "截", "燃", "焦", "殿", "伪", "柳", "锁", "逼", "颇", "昏", "劝",
           "呈", "搜", "勤", "戒", "驾", "漂", "饮", "曹", "朵", "仔", "柔", "俩", "孟", "腐", "幼", "践", "籍", "牧", "凉", "牲", "佳", "娜",
           "浓", "芳", "稿", "竹", "腹", "跌", "逻", "垂", "遵", "脉", "貌", "柏", "狱", "猜", "怜", "惑", "陶", "兽", "帐", "饰", "贷", "昌",
           "叙", "躺", "钢", "沟", "寄", "扶", "铺", "邓", "寿", "惧", "询", "汤", "盗", "肥", "尝", "匆", "辉", "奈", "扣", "廷", "澳", "嘛",
           "董", "迁", "凝", "慰", "厌", "脏", "腾", "幽", "怨", "鞋", "丢", "埋", "泉", "涌", "辖", "躲", "晋", "紫", "艰", "魏", "吾", "慌",
           "祝", "邮", "吐", "狠", "鉴", "曰", "械", "咬", "邻", "赤", "挤", "弯", "椅", "陪", "割", "揭", "韦", "悟", "聪", "雾", "锋", "梯",
           "猫", "祥", "阔", "誉", "筹", "丛", "牵", "鸣", "沈", "阁", "穆", "屈", "旨", "袖", "猎", "臂", "蛇", "贺", "柱", "抛", "鼠", "瑟",
           "戈", "牢", "逊", "迈", "欺", "吨", "琴", "衰", "瓶", "恼", "燕", "仲", "诱", "狼", "池", "疼", "卢", "仗", "冠", "粒", "遥", "吕",
           "玄", "尘", "冯", "抚", "浅", "敦", "纠", "钻", "晶", "岂", "峡", "苍", "喷", "耗", "凌", "敲", "菌", "赔", "涂", "粹", "扁", "亏",
           "寂", "煤", "熊", "恭", "湿", "循", "暖", "糖", "赋", "抑", "秩", "帽", "哀", "宿", "踏", "烂", "袁", "侯", "抖", "夹", "昆", "肝",
           "擦", "猪", "炼", "恒", "慎", "搬", "纽", "纹", "玻", "渔", "磁", "铜", "齿", "跨", "押", "怖", "漠", "疲", "叛", "遣", "兹", "祭",
           "醉", "拳", "弥", "斜", "档", "稀", "捷", "肤", "疫", "肿", "豆", "削", "岗", "晃", "吞", "宏", "癌", "肚", "隶", "履", "涨", "耀",
           "扭", "坛", "拨", "沃", "绘", "伐", "堪", "仆", "郭", "牺", "歼", "墓", "雇", "廉", "契", "拼", "惩", "捉", "覆", "刷", "劫", "嫌",
           "瓜", "歇", "雕", "闷", "乳", "串", "娃", "缴", "唤", "赢", "莲", "霸", "桃", "妥", "瘦", "搭", "赴", "岳", "嘉", "舱", "俊", "址",
           "庞", "耕", "锐", "缝", "悔", "邀", "玲", "惟", "斥", "宅", "添", "挖", "呵", "讼", "氧", "浩", "羽", "斤", "酷", "掠", "妖", "祸",
           "侍", "乙", "妨", "贪", "挣", "汪", "尿", "莉", "悬", "唇", "翰", "仓", "轨", "枚", "盐", "览", "傅", "帅", "庙", "芬", "屏", "寺",
           "胖", "璃", "愚", "滴", "疏", "萧", "姿", "颤", "丑", "劣", "柯", "寸", "扔", "盯", "辱", "匹", "俱", "辨", "饿", "蜂", "哦", "腔",
           "郁", "溃", "谨", "糟", "葛", "苗", "肠", "忌", "溜", "鸿", "爵", "鹏", "鹰", "笼", "丘", "桂", "滋", "聊", "挡", "纲", "肌", "茨",
           "壳", "痕", "碗", "穴", "膀", "卓", "贤", "卧", "膜", "毅", "锦", "欠", "哩", "函", "茫", "昂", "薛", "皱", "夸", "豫", "胃", "舌",
           "剥", "傲", "拾", "窝", "睁", "携", "陵", "哼", "棉", "晴", "铃", "填", "饲", "渴", "吻", "扮", "逆", "脆", "喘", "罩", "卜", "炉",
           "柴", "愉", "绳", "胎", "蓄", "眠", "竭", "喂", "傻", "慕", "浑", "奸", "扇", "柜", "悦", "拦", "诞", "饱", "乾", "泡", "贼", "亭",
           "夕", "爹", "酬", "儒", "姻", "卵", "氛", "泄", "杆", "挨", "僧", "蜜", "吟", "猩", "遂", "狭", "肖", "甜", "霞", "驳", "裕", "顽",
           "於", "摘", "矮", "秒", "卿", "畜", "咽", "披", "辅", "勾", "盆", "疆", "赌", "塑", "畏", "吵", "囊", "嗯", "泊", "肺", "骤", "缠",
           "冈", "羞", "瞪", "吊", "贾", "漏", "斑", "涛", "悠", "鹿", "俘", "锡", "卑", "葬", "铭", "滩", "嫁", "催", "璇", "翅", "盒", "蛮",
           "矣", "潘", "歧", "赐", "鲍", "锅", "廊", "拆", "灌", "勉", "盲", "宰", "佐", "啥", "胀", "扯", "禧", "辽", "抹", "筒", "棋", "裤",
           "唉", "朴", "咐", "孕", "誓", "喉", "妄", "拘", "链", "驰", "栏", "逝", "窃", "艳", "臭", "纤", "玑", "棵", "趁", "匠", "盈", "翁",
           "愁", "瞬", "婴", "孝", "颈", "倘", "浙", "谅", "蔽", "畅", "赠", "妮", "莎", "尉", "冻", "跪", "闯", "葡", "後", "厨", "鸭", "颠",
           "遮", "谊", "圳", "吁", "仑", "辟", "瘤", "嫂", "陀", "框", "谭", "亨", "钦", "庸", "歉", "芝", "吼", "甫", "衫", "摊", "宴", "嘱",
           "衷", "娇", "陕", "矩", "浦", "讶", "耸", "裸", "碧", "摧", "薪", "淋", "耻", "胶", "屠", "鹅", "饥", "盼", "脖", "虹", "翠", "崩",
           "账", "萍", "逢", "赚", "撑", "翔", "倡", "绵", "猴", "枯", "巫", "昭", "怔", "渊", "凑", "溪", "蠢", "禅", "阐", "旺", "寓", "藤",
           "匪", "伞", "碑", "挪", "琼", "脂", "谎", "慨", "菩", "萄", "狮", "掘", "抄", "岭", "晕", "逮", "砍", "掏", "狄", "晰", "罕", "挽",
           "脾", "舟", "痴", "蔡", "剪", "脊", "弓", "懒", "叉", "拐", "喃", "僚", "捐", "姊", "骚", "拓", "歪", "粘", "柄", "坑", "陌", "窄",
           "湘", "兆", "崖", "骄", "刹", "鞭", "芒", "筋", "聘", "钩", "棍", "嚷", "腺", "弦", "焰", "耍", "俯", "厘", "愣", "厦", "恳", "饶",
           "钉", "寡", "憾", "摔", "叠", "惹", "喻", "谱", "愧", "煌", "徽", "溶", "坠", "煞", "巾", "滥", "洒", "堵", "瓷", "咒", "姨", "棒",
           "郡", "浴", "媚", "稣", "淮", "哎", "屁", "漆", "淫", "巢", "吩", "撰", "啸", "滞", "玫", "硕", "钓", "蝶", "膝", "姚", "茂", "躯",
           "吏", "猿", "寨", "恕", "渠", "戚", "辰", "舶", "颁", "惶", "狐", "讽", "笨", "袍", "嘲", "啡", "泼", "衔", "倦", "涵", "雀", "旬",
           "僵", "撕", "肢", "垄", "夷", "逸", "茅", "侨", "舆", "窑", "涅", "蒲", "谦", "杭", "噢", "弊", "勋", "刮", "郊", "凄", "捧", "浸",
           "砖", "鼎", "篮", "蒸", "饼", "亩", "肾", "陡", "爪", "兔", "殷", "贞", "荐", "哑", "炭", "坟", "眨", "搏", "咳", "拢", "舅", "昧",
           "擅", "爽", "咖", "搁", "禄", "雌", "哨", "巩", "绢", "螺", "裹", "昔", "轩", "谬", "谍", "龟", "媳", "姜", "瞎", "冤", "鸦", "蓬",
           "巷", "琳", "栽", "沾", "诈", "斋", "瞒", "彪", "厄", "咨", "纺", "罐", "桶", "壤", "糕", "颂", "膨", "谐", "垒", "咕", "隙", "辣",
           "绑", "宠", "嘿", "兑", "霉", "挫", "稽", "辐", "乞", "纱", "裙", "嘻", "哇", "绣", "杖", "塘", "衍", "轴", "攀", "膊", "譬", "斌",
           "祈", "踢", "肆", "坎", "轿", "棚", "泣", "屡", "躁", "邱", "凰", "溢", "椎", "砸", "趟", "帘", "帆", "栖", "窜", "丸", "斩", "堤",
           "塌", "贩", "厢", "掀", "喀", "乖", "谜", "捏", "阎", "滨", "虏", "匙", "芦", "苹", "卸", "沼", "钥", "株", "祷", "剖", "熙", "哗",
           "劈", "怯", "棠", "胳", "桩", "瑰", "娱", "娶", "沫", "嗓", "蹲", "焚", "淘", "嫩", "韵", "衬", "匈", "钧", "竖", "峻", "豹", "捞",
           "菊", "鄙", "魄", "兜", "哄", "颖", "镑", "屑", "蚁", "壶", "怡", "渗", "秃", "迦", "旱", "哟", "咸", "焉", "谴", "宛", "稻", "铸",
           "锻", "伽", "詹", "毙", "恍", "贬", "烛", "骇", "芯", "汁", "桓", "坊", "驴", "朽", "靖", "佣", "汝", "碌", "迄", "冀", "荆", "崔",
           "雁", "绅", "珊", "榜", "诵", "傍", "彦", "醇", "笛", "禽", "勿", "娟", "瞄", "幢", "寇", "睹", "贿", "踩", "霆", "呜", "拱", "妃",
           "蔑", "谕", "缚", "诡", "篷", "淹", "腕", "煮", "倩", "卒", "勘", "馨", "逗", "甸", "贱", "炒", "灿", "敞", "蜡", "囚", "栗", "辜",
           "垫", "妒", "魁", "谣", "寞", "蜀", "甩", "涯", "枕", "丐", "泳", "奎", "泌", "逾", "叮", "黛", "燥", "掷", "藉", "枢", "憎", "鲸",
           "弘", "倚", "侮", "藩", "拂", "鹤", "蚀", "浆", "芙", "垃", "烤", "晒", "霜", "剿", "蕴", "圾", "绸", "屿", "氢", "驼", "妆", "捆",
           "铅", "逛", "淑", "榴", "丙", "痒", "钞", "蹄", "犬", "躬", "昼", "藻", "蛛", "褐", "颊", "奠", "募", "耽", "蹈", "陋", "侣", "魅",
           "岚", "侄", "虐", "堕", "陛", "莹", "荫", "狡", "阀", "绞", "膏", "垮", "茎", "缅", "喇", "绒", "搅", "凳", "梭", "丫", "姬", "诏",
           "钮", "棺", "耿", "缔", "懈", "嫉", "灶", "匀", "嗣", "鸽", "澡", "凿", "纬", "沸", "畴", "刃", "遏", "烁", "嗅", "叭", "熬", "瞥",
           "骸", "奢", "拙", "栋", "毯", "桐", "砂", "莽", "泻", "坪", "梳", "杉", "晤", "稚", "蔬", "蝇", "捣", "顷", "麽", "尴", "镖", "诧",
           "尬", "硫", "嚼", "羡", "沦", "沪", "旷", "彬", "芽", "狸", "冥", "碳", "咧", "惕", "暑", "咯", "萝", "汹", "腥", "窥", "俺", "潭",
           "崎", "麟", "捡", "拯", "厥", "澄", "萎", "哉", "涡", "滔", "暇", "溯", "鳞", "酿", "茵", "愕", "瞅", "暮", "衙", "诫", "斧", "兮",
           "焕", "棕", "佑", "嘶", "妓", "喧", "蓉", "删", "樱", "伺", "嗡", "娥", "梢", "坝", "蚕", "敷", "澜", "杏", "绥", "冶", "庇", "挠",
           "搂", "倏", "聂", "婉", "噪", "稼", "鳍", "菱", "盏", "匿", "吱", "寝", "揽", "髓", "秉", "哺", "矢", "啪", "帜", "邵", "嗽", "挟",
           "缸", "揉", "腻", "驯", "缆", "晌", "瘫", "贮", "觅", "朦", "僻", "隋", "蔓", "咋", "嵌", "虔", "畔", "琐", "碟", "涩", "胧", "嘟",
           "蹦", "冢", "浏", "裔", "襟", "叨", "诀", "旭", "虾", "簿", "啤", "擒", "枣", "嘎", "苑", "牟", "呕", "骆", "凸", "熄", "兀", "喔",
           "裳", "凹", "赎", "屯", "膛", "浇", "灼", "裘", "砰", "棘", "橡", "碱", "聋", "姥", "瑜", "毋", "娅", "沮", "萌", "俏", "黯", "撇",
           "粟", "粪", "尹", "苟", "癫", "蚂", "禹", "廖", "俭", "帖", "煎", "缕", "窦", "簇", "棱", "叩", "呐", "瑶", "墅", "莺", "烫", "蛙",
           "歹", "伶", "葱", "哮", "眩", "坤", "廓", "讳", "啼", "乍", "瓣", "矫", "跋", "枉", "梗", "厕", "琢", "讥", "釉", "窟", "敛", "轼",
           "庐", "胚", "呻", "绰", "扼", "懿", "炯", "竿", "慷", "虞", "锤", "栓", "桨", "蚊", "磅", "孽", "惭", "戳", "禀", "鄂", "馈", "垣",
           "溅", "咚", "钙", "礁", "彰", "豁", "眯", "磷", "雯", "墟", "迂", "瞻", "颅", "琉", "悼", "蝴", "拣", "渺", "眷", "悯", "汰", "慑",
           "婶", "斐", "嘘", "镶", "炕", "宦", "趴", "绷", "窘", "襄", "珀", "嚣", "拚", "酌", "浊", "毓", "撼", "嗜", "扛", "峭", "磕", "翘",
           "槽", "淌", "栅", "颓", "熏", "瑛", "颐", "忖", "牡", "缀", "徊", "梨", "肪", "涕", "惫", "摹", "踱", "肘", "熔", "挚", "氯", "凛",
           "绎", "庶", "脯", "迭", "睦", "窍", "粥", "庵", "沧", "怠", "沁", "奕", "咙", "氨", "矗", "盔", "拇", "沛", "榻", "揣", "崭", "鞘",
           "鞠", "垦", "洽", "唾", "橱", "仕", "蜘", "痰", "袜", "峙", "柬", "蝉", "蟹", "谏", "鹃", "擎", "皓", "朕", "疤", "禺", "铲", "酶",
           "钝", "氓", "匣", "弧", "峨", "锥", "揪", "杠", "吭", "崛", "诬", "冉", "抒", "庚", "悍", "靡", "晦", "醋", "壕", "锯", "夭", "咦",
           "侈", "婢", "猾", "徘", "硝", "煽", "皂", "舵", "嗦", "狈", "靴", "捂", "疮", "郝", "苛", "秽", "茜", "搓", "芸", "酱", "赁", "檐",
           "饷", "蕉", "铀", "苔", "赦", "缎", "舷", "筷", "朔", "婪", "紊", "厮", "婿", "寥", "兢", "糙", "卦", "槐", "扒", "裴", "祀", "埔",
           "絮", "芭", "屉", "痪", "霄", "绽", "宵", "邑", "霖", "岔", "饵", "茄", "韧", "琪", "邹", "瑚", "憋", "殆", "噜", "忒", "忿", "衅",
           "淳", "悖", "髦", "孜", "粤", "隘", "濒", "铮", "畸", "剔", "坞", "篱", "淀", "蓦", "唬", "锣", "汀", "趾", "缉", "嫦", "斟", "鞍",
           "扳", "拴", "诅", "谟", "呃", "懦", "逞", "犁", "忏", "拧", "亥", "佟", "叱", "舜", "绊", "龚", "腮", "邸", "椒", "蔚", "湛", "狩",
           "眶", "栈", "薇", "肮", "瀑", "渣", "褂", "叽", "臀", "妞", "巍", "唔", "疚", "鲤", "戎", "肇", "笃", "辙", "娴", "阮", "札", "懊",
           "焘", "恤", "疹", "潇", "铝", "涤", "恃", "喽", "砌", "遁", "楞", "阱", "咎", "洼", "炳", "噬", "枫", "拷", "哆", "矶", "苇", "翩",
           "窒", "侬", "靶", "胰", "芜", "辫", "嚎", "妾", "幌", "踉", "佃", "葫", "皖", "拽", "滤", "睬", "俞", "匕", "谤", "嗤", "捍", "孵",
           "倪", "瘾", "敝", "匡", "磋", "绫", "淆", "尧", "蕊", "烘", "璋", "亢", "轧", "赂", "蝗", "榆", "骏", "诛", "勺", "梵", "炽", "笠",
           "颌", "闸", "狒", "樊", "镕", "垢", "瘟", "缪", "菇", "琦", "剃", "迸", "溺", "炫", "惚", "嗨", "陨", "赃", "羁", "臻", "嘀", "膳",
           "赣", "踌", "殉", "桔", "瞿", "闽", "豚", "掺", "沌", "惰", "喳", "椭", "咪", "霎", "侃", "猝", "窖", "戮", "祠", "瞩", "菁", "躇",
           "佬", "肋", "咄", "忡", "雍", "忱", "蕾", "跄", "硅", "伎", "炊", "钊", "蝠", "屎", "拭", "谛", "褪", "丞", "卉", "隧", "茸", "钳",
           "啃", "伢", "闺", "舔", "蹬", "挛", "眺", "袱", "陇", "殴", "柿", "梧", "惺", "弛", "侥", "琛", "捅", "酝", "薯", "曳", "澈", "锈",
           "稠", "眸", "咆", "簧", "鸥", "疡", "渎", "汲", "嬉", "脓", "骡", "穗", "槛", "拎", "巳", "邢", "廿", "搀", "曙", "樵", "隅", "筛",
           "谒", "倭", "痹", "猖", "佯", "肛", "奚", "甭", "抨", "蛾", "唠", "荧", "嵩", "漱", "酋", "攘", "诘", "篡", "睿", "噩", "怅", "盎",
           "徙", "鞅", "漓", "祟", "睫", "攸", "翎", "呛", "筐", "堑", "檀", "寅", "磊", "驭", "惘", "吠", "驮", "瑙", "炬", "痉", "曝", "恺",
           "胺", "萤", "敕", "筝", "幡", "霹", "竺", "烙", "毗", "鸠", "埠", "蒜", "阜", "嘈", "乒", "帷", "啄", "鳌", "毡", "阙", "褥", "搔",
           "笋", "冕", "狞", "韶", "骼", "蔼", "烹", "奄", "嫖", "沐", "噗", "岑", "蛟", "掳", "咏", "弩", "捻", "圃", "孚", "悴", "诣", "呱",
           "祁", "捶", "钠", "袄", "澎", "氮", "恪", "雏", "撮", "堰", "彷", "鹦", "晖", "犀", "腑", "沽", "橄", "掐", "亵", "龋", "嗒", "咀",
           "祺", "锚"]

myjson = {
    'kr': [], 'jp': [], 'gb2312': [], 'gb2312_t': [], 'gbk': charset, 'gb775': [], 'gb6763': []
}
print(len(charset))
with open("cjk_cn.json", "w") as f:
    json.dump(myjson, f)