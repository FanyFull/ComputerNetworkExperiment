string = """北京: [116.398, 39.9082],
天津: [117.252, 39.1039],
上海: [121.476, 31.2244],
重庆: [106.548, 29.5549],
石家庄: [114.476, 38.0483],
唐山: [118.167, 39.6353],
秦皇岛: [119.59, 39.9479],
邯郸: [114.489, 36.5994],
邢台: [114.504, 37.0717],
保定: [115.466, 38.8799],
张家口: [114.89, 40.8262],
承德: [117.935, 40.9955],
沧州: [116.866, 38.3124],
廊坊: [116.706, 39.5193],
衡水: [115.698, 37.7354],
太原: [112.531, 37.8551],
大同: [113.3, 40.0784],
阳泉: [113.58, 37.8567],
长治: [113.117, 36.1922],
晋城: [112.853, 35.4906],
朔州: [112.429, 39.3186],
晋中: [112.752, 37.6883],
运城: [110.998, 35.0315],
忻州: [112.735, 38.4158],
临汾: [111.527, 36.1021],
吕梁: [111.13, 37.5203],
呼和浩特: [111.667, 40.8083],
包头: [109.871, 40.6617],
乌海: [106.814, 39.6692],
赤峰: [118.957, 42.2673],
通辽: [122.261, 43.6059],
鄂尔多斯: [110.003, 39.8223],
呼伦贝尔: [119.756, 49.2458],
巴彦淖尔: [107.376, 40.7801],
乌兰察布: [113.121, 41.0317],
兴安: [122.135, 46.0872],
锡林郭勒: [116.099, 43.9455],
阿拉善: [105.686, 38.8464],
沈阳: [123.434, 41.8057],
大连: [121.617, 38.9143],
鞍山: [123.002, 41.1158],
抚顺: [123.924, 41.8678],
本溪: [123.786, 41.2984],
丹东: [124.398, 40.1325],
锦州: [121.148, 41.1261],
营口: [122.25, 40.6716],
阜新: [121.654, 42.0143],
辽阳: [123.179, 41.2778],
盘锦: [122.071, 41.1188],
铁岭: [123.843, 42.2867],
朝阳: [120.45, 41.5735],
葫芦岛: [120.856, 40.7481],
长春: [125.325, 43.8869],
吉林: [126.571, 43.8458],
四平: [124.398, 43.1725],
辽源: [125.145, 42.9058],
通化: [125.94, 41.7292],
白山: [126.424, 41.9401],
松原: [124.824, 45.1409],
白城: [122.838, 45.6204],
延边朝鲜族自治: [129.498, 42.8942],
哈尔滨: [126.652, 45.7613],
齐齐哈尔: [123.937, 47.3416],
鸡西: [130.97, 45.2952],
鹤岗: [130.279, 47.3311],
双鸭山: [131.16, 46.6469],
大庆: [125.094, 46.5883],
伊春: [128.901, 47.7247],
佳木斯: [130.37, 46.8075],
七台河: [131.008, 45.7719],
牡丹江: [129.623, 44.5848],
黑河: [127.501, 50.2479],
绥化: [126.99, 46.637],
大兴安岭地: [124.397, 51.6737],
南京: [118.792, 32.0562],
无锡: [120.359, 31.5611],
徐州: [117.174, 34.2586],
常州: [119.975, 31.7698],
苏州: [120.639, 31.3205],
南通: [120.871, 32.0093],
连云港: [119.173, 34.5959],
淮安: [119.015, 33.612],
盐城: [120.139, 33.3794],
扬州: [119.413, 32.4195],
镇江: [119.442, 32.211],
泰州: [119.921, 32.4617],
宿迁: [118.297, 33.9539],
杭州: [120.173, 30.274],
宁波: [121.544, 29.8683],
温州: [120.638, 28.027],
嘉兴: [120.759, 30.7539],
湖州: [120.097, 30.8706],
绍兴: [120.586, 29.9958],
金华: [119.652, 29.0896],
衢州: [118.874, 28.9359],
舟山: [122.106, 30.0132],
台州: [121.456, 28.6708],
丽水: [119.917, 28.4522],
合肥: [117.296, 31.8693],
芜湖: [118.376, 31.3273],
蚌埠: [117.402, 32.9302],
淮南: [117.0, 32.6383],
马鞍山: [118.502, 31.693],
淮北: [116.793, 33.969],
铜陵: [117.811, 30.9446],
安庆: [117.051, 30.527],
黄山: [118.317, 29.7099],
滁州: [118.318, 32.3011],
阜阳: [115.82, 32.8971],
宿州: [116.984, 33.6381],
巢湖: [117.87, 31.6009],
六安: [116.491, 31.7426],
亳州: [115.783, 33.8696],
池州: [117.489, 30.6557],
宣城: [118.755, 30.9469],
福州: [119.306, 26.0761],
厦门: [118.117, 24.4838],
莆田: [119.005, 25.434],
三明: [117.64, 26.2681],
泉州: [118.585, 24.9295],
漳州: [117.666, 24.5124],
南平: [118.179, 26.6399],
龙岩: [117.033, 25.0946],
宁德: [119.537, 26.6528],
南昌: [115.897, 28.6788],
景德镇: [117.193, 29.298],
萍乡: [113.852, 27.6227],
九江: [115.99, 29.7156],
新余: [114.918, 27.8163],
鹰潭: [117.034, 28.2394],
赣州: [114.942, 25.8553],
吉安: [114.987, 27.1136],
宜春: [114.399, 27.8068],
抚州: [116.363, 27.9793],
上饶: [117.969, 28.4456],
济南: [117.021, 36.6594],
青岛: [120.357, 36.084],
淄博: [118.05, 36.8063],
枣庄: [117.309, 34.8127],
东营: [118.675, 37.4321],
烟台: [121.392, 37.5379],
潍坊: [119.122, 36.7159],
济宁: [116.588, 35.4133],
泰安: [117.121, 36.1813],
威海: [122.122, 37.5043],
日照: [119.526, 35.4188],
莱芜: [117.679, 36.2136],
临沂: [118.346, 35.0538],
德州: [116.302, 37.4545],
聊城: [115.986, 36.4561],
滨州: [118.016, 37.3832],
郑州: [113.663, 34.7619],
开封: [114.34, 34.7893],
洛阳: [112.401, 34.6567],
平顶山: [113.304, 33.7274],
安阳: [114.346, 36.1112],
鹤壁: [114.297, 35.7481],
新乡: [113.89, 35.3015],
焦作: [113.228, 35.2338],
濮阳: [115.029, 35.7632],
许昌: [113.832, 34.0222],
漯河: [114.036, 33.5673],
三门峡: [111.192, 34.7758],
南阳: [112.534, 32.9993],
商丘: [115.651, 34.4389],
信阳: [114.075, 32.124],
周口: [114.653, 33.6166],
驻马店: [114.028, 32.9832],
武汉: [114.281, 30.5781],
黄石: [115.06, 30.2063],
十堰: [110.782, 32.6553],
宜昌: [111.295, 30.7012],
襄樊: [112.135, 32.062],
鄂州: [114.904, 30.3898],
荆门: [112.196, 31.0277],
孝感: [113.919, 30.9246],
荆州: [112.245, 30.3252],
黄冈: [114.875, 30.4465],
咸宁: [114.336, 29.8337],
随州: [113.375, 31.7167],
恩施土家族苗族自治: [109.482, 30.2899],
长沙: [113.009, 28.2085],
株洲: [113.149, 27.8406],
湘潭: [112.907, 27.8612],
衡阳: [112.612, 26.8962],
邵阳: [111.467, 27.2371],
岳阳: [113.108, 29.3663],
常德: [111.703, 29.0366],
张家界: [110.477, 29.1197],
益阳: [112.356, 28.58],
郴州: [113.032, 25.7968],
永州: [111.608, 26.438],
怀化: [109.977, 27.5484],
娄底: [111.998, 27.7259],
湘西土家族苗族自治: [109.601, 27.9472],
广州: [113.322, 23.1341],
韶关: [113.598, 24.8024],
深圳: [114.056, 22.5421],
珠海: [113.547, 22.2532],
汕头: [116.724, 23.3601],
佛山: [113.121, 23.0305],
江门: [113.085, 22.583],
湛江: [110.421, 21.1989],
茂名: [110.927, 21.6616],
肇庆: [112.476, 23.0734],
惠州: [114.417, 23.0896],
梅州: [116.118, 24.2988],
汕尾: [115.368, 22.7782],
河源: [114.697, 23.7503],
阳江: [111.984, 21.872],
清远: [113.045, 23.6882],
东莞: [113.759, 23.0384],
中山: [113.372, 22.525],
潮州: [116.642, 23.6713],
揭阳: [116.37, 23.5276],
云浮: [112.044, 22.9294],
南宁: [108.311, 22.8178],
柳州: [109.413, 24.3068],
桂林: [110.285, 25.2827],
梧州: [111.304, 23.5036],
北海: [109.123, 21.4788],
防城港: [108.346, 21.6146],
钦州: [108.609, 21.9509],
贵港: [109.606, 23.0939],
玉林: [110.151, 22.6255],
百色: [106.621, 23.9018],
贺州: [111.563, 24.4279],
河池: [108.062, 24.6972],
来宾: [109.222, 23.7351],
崇左: [107.339, 22.4248],
海口: [110.32, 20.0323],
三亚: [109.514, 18.2355],
成都: [104.066, 30.6581],
自贡: [104.77, 29.3534],
攀枝花: [101.699, 26.5733],
泸州: [105.444, 28.8889],
德阳: [104.388, 31.1368],
绵阳: [104.726, 31.467],
广元: [105.834, 32.4384],
遂宁: [105.583, 30.5137],
内江: [105.063, 29.5825],
乐山: [103.746, 29.5866],
南充: [106.095, 30.7844],
眉山: [103.826, 30.0389],
宜宾: [104.621, 28.7705],
广安: [106.642, 30.4706],
达州: [107.488, 31.2126],
雅安: [103.015, 29.9937],
巴中: [106.755, 31.8574],
资阳: [104.651, 30.1286],
阿坝藏族羌族自治: [102.222, 31.8992],
甘孜藏族自治: [101.866, 30.1414],
凉山彝族自治: [102.242, 27.9095],
贵阳: [106.713, 26.5768],
六盘水: [104.873, 26.5821],
遵义: [106.931, 27.6926],
安顺: [105.927, 26.2573],
铜仁地: [109.188, 27.7184],
黔西南布依族苗族自治: [104.895, 25.0935],
毕节地: [105.288, 27.3032],
黔东南苗族侗族自治: [107.981, 26.5831],
黔南布依族苗族自治: [107.511, 26.283],
昆明: [102.703, 25.0499],
曲靖: [103.784, 25.4913],
玉溪: [102.536, 24.3472],
保山: [99.1647, 25.1249],
昭通: [103.704, 27.3656],
丽江: [100.277, 26.9229],
临沧: [100.085, 23.8971],
楚雄彝族自治: [101.545, 25.0549],
红河哈尼族彝族自治: [103.18, 23.4301],
文山壮族苗族自治: [104.255, 23.3803],
西双版纳傣族自治: [100.799, 22.0109],
大理白族自治: [100.222, 25.5842],
德宏傣族景颇族自治: [98.5669, 24.4484],
怒江傈僳族自治: [98.903, 25.8583],
迪庆藏族自治: [99.709, 27.859],
拉萨: [91.1189, 29.6553],
昌都地: [97.1503, 31.1816],
山南地: [91.805, 29.2407],
日喀则地: [88.8884, 29.2717],
那曲地: [92.0593, 31.4524],
阿里地: [80.1027, 32.5517],
林芝地: [94.4083, 29.6352],
西安: [108.954, 34.2649],
铜川: [108.948, 34.9005],
宝鸡: [107.139, 34.3698],
咸阳: [108.71, 34.3268],
渭南: [109.51, 34.5073],
延安: [109.496, 36.5948],
汉中: [107.031, 33.0799],
榆林: [109.754, 38.2954],
安康: [109.031, 32.6917],
商洛: [109.943, 33.8825],
兰州: [103.835, 36.0599],
嘉峪关: [98.2536, 39.8001],
金昌: [102.175, 38.4764],
白银: [104.151, 36.5506],
天水: [105.702, 34.5875],
武威: [102.634, 37.9317],
张掖: [100.451, 38.931],
平凉: [106.725, 35.5097],
酒泉: [98.5139, 39.7563],
庆阳: [107.862, 35.9344],
定西: [104.622, 35.5852],
陇南: [104.934, 33.4695],
临夏回族自治: [103.201, 35.5914],
甘南藏族自治: [102.899, 34.9854],
西宁: [101.777, 36.6172],
海东地: [102.086, 36.5092],
海北藏族自治: [100.973, 36.9433],
黄南藏族自治: [102.027, 35.5399],
海南藏族自治: [100.638, 36.3244],
果洛藏族自治: [100.295, 34.4775],
玉树藏族自治: [97.013, 33.0183],
海西蒙古族藏族自治: [97.3632, 37.4214],
银川: [106.283, 38.4628],
石嘴山: [106.386, 39.0146],
吴忠: [106.194, 37.9852],
固原: [106.281, 36.011],
中卫: [105.686, 37.4829],
乌鲁木齐: [87.6168, 43.8235],
克拉玛依: [84.9312, 45.5964],
吐鲁番地: [89.2107, 43.007],
哈密地: [93.5502, 42.8991],
昌吉回族自治: [87.9882, 44.0044],
博尔塔拉蒙古自治: [82.0787, 44.9126],
巴音郭楞蒙古自治: [86.1827, 41.8974],
阿克苏地: [80.2445, 41.1239],
克孜勒苏柯尔克孜自治: [76.67, 39.8878],
喀什地: [75.9994, 39.4657],
和田地: [79.7641, 37.2296],
伊犁哈萨克自治: [81.3383, 43.9233],
塔城地: [83.0148, 46.7523],
阿勒泰地: [88.069, 47.81],
仙桃: [113.453, 30.3646],
潜江: [112.894, 30.4198],
天门: [113.164, 30.6513],
神农架林: [110.676, 31.7448],
五指山: [109.517, 18.7773],
琼海: [110.46, 19.248],
儋州: [109.579, 19.5199],
文昌: [110.748, 19.6159],
万宁: [110.388, 18.8122],
东方: [108.693, 19.0807],
定安县: [110.447, 19.4883],
屯昌县: [110.097, 19.3686],
澄迈县: [110.016, 19.7302],
临高县: [109.689, 19.8973],
白沙黎族自治县: [109.44, 19.2375],
昌江黎族自治县: [109.036, 19.3083],
乐东黎族自治县: [109.175, 18.7435],
陵水黎族自治县: [110.029, 18.5167],
保亭黎族苗族自治县: [109.7, 18.6263],
琼中黎族苗族自治县: [109.832, 19.0467],
石河子: [86.0526, 44.3051]"""
# string = string.split(\n)
# res = []
# for line in string:
#     tmp = line.split(":")
#     print(tmp[0])
#     res.append(tmp[0])

res = ["北京", "天津", "上海", "重庆", "石家庄", "唐山", "秦皇岛", "邯 郸", "邢台", "保定", "张家口", "承德", "沧州", "廊坊", "衡水", "太原", "大同", "阳泉", "长治", "晋城", "朔州", "晋中", "运城", "忻州", "临汾", "吕梁", "呼和浩特", "包头", "乌海", "赤峰", "通辽", "鄂尔多斯", "呼伦贝尔", "巴彦淖尔", "乌兰察布", "兴安", "锡林郭勒", "阿拉善", "沈阳", "大连", "鞍山", "抚顺", "本溪", "丹东", "锦州", "营口", "阜新", "辽阳", "盘锦", "铁岭", "朝阳", "葫芦岛", "长春", "吉林", "四平", "辽源", "通化", "白山", "松原", "白城", "延边朝鲜族自治", "哈尔滨", "齐齐哈尔", "鸡西", "鹤岗", "双鸭山", "大庆", "伊春", "佳木斯", "七台河", "牡丹江", "黑河", "绥化", "大兴安岭地", "南京", "无锡", "徐州", "常州", "苏州", "南通", "连云港", "淮安", "盐城", "扬州", "镇江", "泰州", "宿迁", "杭州", "宁波", "温州", "嘉兴", "湖州", "绍兴", "金华", "衢州", "舟山", "台州", "丽水", "合肥", "芜湖", "蚌埠", "淮南", "马鞍山", "淮北", "铜陵", "安庆", "黄山", "滁州", "阜阳", "宿州", "巢湖", "六安", "亳州", "池州", "宣城", "福州", "厦门", "莆田", "三明", "泉州", "漳州", "南平", "龙岩", "宁德", "南昌", "景德镇", "萍乡", "九江", "新余", "鹰潭", "赣州", "吉安", "宜春", "抚州", "上饶", "济南", "青岛", "淄博", "枣庄", "东营", "烟台", "潍坊", "济宁", "泰安", "威海", "日照", "莱芜", "临沂", "德州", "聊城", "滨州", "郑州", "开封", "洛阳", "平顶山", "安阳", "鹤壁", "新乡", "焦作", "濮阳", "许昌", "漯河", "三门峡", "南阳", "商丘", "信阳", "周口", "驻马店", "武汉", "黄石", "十堰", "宜昌", "襄樊", "鄂州", "荆门", "孝感", "荆州", "黄冈", "咸宁", "随州", "恩施土家族苗族自治", "长沙", "株洲", "湘潭", "衡阳", "邵阳", "岳阳", "常德", "张家界",
       "益阳", "郴州", "永州", "怀化", "娄底", "湘西土家族苗族自治", "广州", "韶关", "深圳", "珠海", "汕头", "佛山", "江门", "湛江", "茂名", "肇庆", "惠州", "梅州", "汕尾", "河源", "阳江", "清远", "东莞", "中山", "潮州", "揭阳", "云浮", "南宁", "柳州", "桂林", "梧州", "北海", "防城港", "钦州", "贵港", "玉林", "百色", "贺州", "河池", "来宾", "崇左", "海口", "三亚", "成都", "自贡", "攀枝花", "泸州", "德阳", "绵阳", "广元", "遂宁", "内江", "乐山", "南充", "眉山", "宜宾", "广安", "达州", "雅安", "巴中", "资阳", "阿坝藏族羌族自治", "甘孜藏族自治", "凉山彝族自治", "贵阳", "六盘水", "遵义", "安顺", "铜仁地", "黔西南布依族苗族自治", "毕节地", "黔东南苗族侗族自治", "黔南布依族苗族自治", "昆明", "曲靖", "玉溪", "保山", "昭通", "丽江", "临沧", "楚雄彝族自治", "红河哈尼族彝族自治", "文山壮族苗族自治", "西双版纳傣族自治", "大理白族自治", "德宏傣族景颇族自治", "怒江傈僳族自治", "迪庆藏族自治", "拉萨", "昌都地", "山南地", "日喀则地", "那曲地", "阿里地", "林芝地", "西安", "铜川", "宝鸡", "咸阳", "渭南", "延安", "汉中", "榆林", "安康", "商洛", "兰州", "嘉峪关", "金昌", "白银", "天水", "武威", "张掖", "平凉", "酒泉", "庆阳", "定西", "陇南", "临夏回族自治", "甘南藏族自治", "西宁", "海东地", "海北藏族自治", "黄南藏族自治", "海南藏族自治", "果洛藏族自治", "玉树藏族自治", "海西蒙古族藏族自治", "银川", "石嘴山", "吴忠", "固原", "中卫", "乌鲁木齐", "克拉玛依", "吐鲁番地", "哈密地", "昌吉回族自治", "博尔塔拉蒙古自治", "巴音郭楞蒙古自治", "阿克苏地", "克孜勒苏柯尔克孜自治", "喀什地", "和田地", "伊犁哈萨克自治", "塔城地", "阿勒泰地", "仙桃", "潜江", "天门", "神农架林", "五指山", "琼海", "儋州", "文昌", "万宁", "东方", "定安县", "屯昌县", "澄迈县", "临高县", "白沙黎族自治县", "昌江黎族自治县", "乐东黎族自治县", "陵水黎族自治县", "保亭黎族苗族自治县", "琼中黎族苗族自治县", "石河子"]

print(res)