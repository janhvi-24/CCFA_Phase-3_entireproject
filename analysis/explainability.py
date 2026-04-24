import pandas as pd
import networkx as nx


def build_graph():
    nodes_df = pd.read_csv("nodes.csv")
    edges_df = pd.read_csv("edges.csv")

    G = nx.Graph()

    for node in nodes_df.iloc[:, 0]:
        G.add_node(int(node))

    for _, row in edges_df.iterrows():
        G.add_edge(int(row[0]), int(row[1]))

    return G


def explain_risk(account_id):

    G = build_graph()

    if account_id not in G:
        return ["Account not found in graph"]

    neighbors = list(G.neighbors(account_id))
    degree = len(neighbors)

    explanations = []

    # Rule 1: Many connections
    if degree > 5:
        explanations.append(f"Connected to many accounts ({degree}) → possible mule network")

    # Rule 2: Few connections
    elif degree == 0:
        explanations.append("No transaction connections → low activity")

    else:
        explanations.append(f"Connected to {degree} accounts")

    # Rule 3: Check risky neighbors
    try:
        risk_df = pd.read_csv("risk_scores.csv")
        risk_map = dict(zip(risk_df["node_id"], risk_df["risk_score"]))

        risky_neighbors = [
            n for n in neighbors if risk_map.get(n, 0) > 0.5
        ]

        if risky_neighbors:
            explanations.append(
                f"Connected to high-risk accounts: {risky_neighbors}"
            )

    except:
        explanations.append("Risk neighbor data unavailable")

    return explanations