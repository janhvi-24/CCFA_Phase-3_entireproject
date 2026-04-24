import pandas as pd
import networkx as nx
from pyvis.network import Network


def create_transaction_graph():
    nodes_df = pd.read_csv("nodes.csv")
    edges_df = pd.read_csv("edges.csv")

    G = nx.Graph()

    for node in nodes_df.iloc[:, 0]:
        G.add_node(int(node))

    for _, row in edges_df.iterrows():
        G.add_edge(int(row[0]), int(row[1]))

    return G


def visualize_graph(account_id):

    G = create_transaction_graph()

    net = Network(height="500px", width="100%", bgcolor="#111111", font_color="white")

    for node in G.nodes():
        if node == account_id:
            net.add_node(node, label=f"🔴 {node}", color="red", size=30)
        else:
            net.add_node(node, label=str(node), color="blue", size=15)

    for edge in G.edges():
        net.add_edge(edge[0], edge[1])

    net.save_graph("graph.html")

    return "graph.html"