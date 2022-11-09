import networkx as nx
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 导入数据
data = np.loadtxt("./assets/PageRank_Dataset.csv",
                  skiprows=1,
                  delimiter=",",
                  dtype=np.int16)

# 创建图
Graph = nx.DiGraph()
Graph.add_nodes_from(range(data.min(), data.max()))
for link in data:
    node1, node2 = link
    Graph.add_edge(node1, node2)

# 画图
# nx.draw(Graph, with_labels=True)
# plt.show()

pr = nx.pagerank(Graph, max_iter=500, alpha=0.01)
sortedPage = sorted(pr.items(), key=lambda x: x[1], reverse=True)
topPages = sortedPage[:20]  # 前20个
print(topPages)
pd.DataFrame(topPages).to_csv('output/topPages.csv')
pd.DataFrame(sortedPage).to_csv('output/sortedPage.csv')
