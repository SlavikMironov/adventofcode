import networkx as nx
import matplotlib.pyplot as plt

# הגדרת הנתונים
numeric_keypad = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("4", "^"), ("2", ">")],
    "2": [("5", "^"), ("1", "<"), ("0", "v"), ("3", ">")],
    "3": [("6", "^"), ("2", "<"), ("A", "v")],
    "4": [("7", "^"), ("1", "v"), ("5", ">")],
    "5": [("8", "^"), ("4", "<"), ("2", "v"), ("6", ">")],
    "6": [("9", "^"), ("5", "<"), ("3", "v")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("7", "<"), ("5", "v"), ("9", ">")],
    "9": [("8", "<"), ("6", "v")],
    "A": [("3", "^"), ("0", "<")],
}

# יצירת גרף מכוון
G = nx.DiGraph()

# הוספת הצמתים והקשתות
for node, edges in numeric_keypad.items():
    for edge, label in edges:
        G.add_edge(node, edge, label=label)

# הגדרת פריסת הצמתים
pos = nx.spring_layout(G)

# ציור הצמתים והקשתות
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    edge_color="black",
    font_weight="bold",
)
labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# הצגת הגרף
plt.show()
