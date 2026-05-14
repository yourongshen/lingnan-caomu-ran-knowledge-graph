from pyvis.network import Network

# 1. 岭南草木染三元组（保持不变）
triples = [
    ("薯莨", "适配工艺", "香云纱工艺"),
    ("板蓝", "适配工艺", "墩头蓝扎染"),
    ("槐花", "配色辅助", "墩头蓝扎染"),
    ("苏木", "适配工艺", "岭南媒染工艺"),
    ("红花", "适配工艺", "岭南媒染工艺"),
    ("墩头蓝扎染", "归属民俗", "客家民俗"),
    ("香云纱工艺", "归属民俗", "广府非遗民俗"),
    ("岭南媒染工艺", "归属民俗", "瑶族节庆服饰文化"),
    ("香云纱工艺", "数字化保存", "3D扫描存档"),
    ("墩头蓝扎染", "数字化保存", "3D扫描存档"),
    ("墩头蓝扎染", "制作成品", "草木染围巾"),
    ("墩头蓝扎染", "制作成品", "蓝染T恤"),
    ("岭南媒染工艺", "制作成品", "节庆非遗服饰"),
    ("香云纱工艺", "发源地", "顺德岭南村落"),
    ("墩头蓝扎染", "发源地", "河源客家古村"),
    ("岭南媒染工艺", "发源地", "连南瑶族村寨"),
]

# 2. 古风配色方案（适配宣纸背景，不刺眼）
color_map = {
    "植物原料": "#2F4F4F",    # 深墨绿（像草木）
    "染织工艺": "#483D8B",    # 靛蓝（蓝染主色）
    "民俗文化": "#8B0000",    # 暗红（传统朱红）
    "文创场景": "#DAA520",    # 古铜黄（传统纹样色）
    "地域村落": "#8B4513",    # 棕褐（古村落色调）
    "数字技术": "#2F4F4F"     # 深墨绿（和原料呼应）
}

# 3. 节点配置（核心工艺节点放大，字体适配古风）
node_config = {}
# 植物原料
for n in ["薯莨", "板蓝", "槐花", "苏木", "红花"]:
    node_config[n] = {"color": color_map["植物原料"], "size": 20}
# 染织工艺（核心节点放大）
for n in ["香云纱工艺", "墩头蓝扎染", "岭南媒染工艺"]:
    node_config[n] = {"color": color_map["染织工艺"], "size": 35}
# 数字技术
node_config["3D扫描存档"] = {"color": color_map["数字技术"], "size": 25}
# 民俗文化
for n in ["客家民俗", "广府非遗民俗", "瑶族节庆服饰文化"]:
    node_config[n] = {"color": color_map["民俗文化"], "size": 25}
# 文创场景
for n in ["草木染围巾", "蓝染T恤", "节庆非遗服饰"]:
    node_config[n] = {"color": color_map["文创场景"], "size": 25}
# 地域村落
for n in ["顺德岭南村落", "河源客家古村", "连南瑶族村寨"]:
    node_config[n] = {"color": color_map["地域村落"], "size": 25}

# 4. 创建图谱（关键：设置古风背景）
net = Network(
    height="900px",
    width="100%",
    bgcolor="#F5F0E6",  # 宣纸米白色底色
    font_color="#333333",
    select_menu=False,
    filter_menu=False
)

# 5. 添加节点和关系（线条用浅墨色，更柔和）
for s, r, t in triples:
    if s not in net.nodes:
        net.add_node(
            s,
            label=s,
            color=node_config.get(s, {}).get("color", "#888888"),
            size=node_config.get(s, {}).get("size", 20),
            title=f"实体：{s}"
        )
    if t not in net.nodes:
        net.add_node(
            t,
            label=t,
            color=node_config.get(t, {}).get("color", "#888888"),
            size=node_config.get(t, {}).get("size", 20),
            title=f"实体：{t}"
        )
    net.add_edge(
        s, t,
        label=r,
        color="#666666",  # 浅墨色线条
        width=1.5,
        title=f"关系：{r}"
    )

# 6. 优化布局，让节点分布更舒展
net.barnes_hut(gravity=-8000, central_gravity=0.3, spring_length=180)

# 7. 生成最终古风图谱
net.show("岭南草木染_古风版.html", notebook=False)
print("✅ 古风宣纸背景图谱已生成：岭南草木染_古风版.html")