from graphviz import Digraph

def create_erd():
    erd = Digraph(engine='neato')
    erd.attr(rankdir='TB', nodesep='0.5', ranksep='0.5')  # Reduced node and rank separation
    erd.attr('node', shape='rect', style='filled', fillcolor='lightblue', fontsize='10', width='0.5', height='0.3')  # Set explicit size for nodes
    erd.attr('edge', dir='none')  # No arrowheads on edges

    # Key node for PK and FK
    erd.node('K', 'Key\nPK = Primary Key\nFK = Foreign Key', shape='rect', fontsize='10', style='filled', fillcolor='lightgrey', width='0.5', height='0.3')  # Set explicit size

    # Add nodes for tables (Entities)
    add_entity(erd, 'Authors', 'A')
    add_entity(erd, 'Books', 'B')
    add_entity(erd, 'Customers', 'C')
    add_entity(erd, 'Transactions', 'T')

    # Add attributes in subgraphs for better control
    with erd.subgraph(name='cluster_A'):
        add_attribute(erd, 'Author_ID\n(PK)', 'A')
        add_attribute(erd, 'Name', 'A')
        add_attribute(erd, 'Bio', 'A')

    with erd.subgraph(name='cluster_B'):
        add_attribute(erd, 'Book_ID\n(PK)', 'B')
        add_attribute(erd, 'Title', 'B')
        add_attribute(erd, 'Genre', 'B')
        add_attribute(erd, 'Price', 'B')
        add_attribute(erd, 'Author_ID\n(FK)', 'B')

    with erd.subgraph(name='cluster_C'):
        add_attribute(erd, 'Customer_ID\n(PK)', 'C')
        add_attribute(erd, 'Name', 'C')
        add_attribute(erd, 'Email', 'C')
        add_attribute(erd, 'Phone_Number', 'C')

    with erd.subgraph(name='cluster_T'):
        add_attribute(erd, 'Transaction_ID\n(PK)', 'T')
        add_attribute(erd, 'Customer_ID\n(FK)', 'T')
        add_attribute(erd, 'Book_ID\n(FK)', 'T')
        add_attribute(erd, 'Transaction_Date', 'T')


    # Add relationships
    add_relationship(erd, 'writes', 'A', 'B')
    add_relationship(erd, 'makes', 'C', 'T')
    add_relationship(erd, 'is part of', 'B', 'T')

    # Output the ERD to a file
    erd.render('bookhaven_erd', format='png', cleanup=True)
    print("ERD created and saved as bookhaven_erd.png")

def add_entity(erd, label, node_id):
    erd.node(node_id, label, shape='rect', fontsize='10', style='filled', fillcolor='lightblue', width='0.5', height='0.3')  # Set explicit size

def add_attribute(erd, label, parent_id):
    attr_id = f'{parent_id}_{label.replace(" ", "_")}'
    erd.node(attr_id, label, shape='ellipse', fontsize='8', style='filled', fillcolor='lightyellow', width='0.5', height='0.3')  # Set explicit size
    erd.edge(parent_id, attr_id)

def add_relationship(erd, label, from_node, to_node):
    rel_id = f'rel_{from_node}_{to_node}'
    erd.node(rel_id, label, shape='diamond', fontsize='10', style='filled', fillcolor='lightgreen', width='0.5', height='0.3')  # Set explicit size
    erd.edge(from_node, rel_id)  # Edge from from_node to relationship
    erd.edge(to_node, rel_id)    # Edge from to_node to relationship

if __name__ == "__main__":
    create_erd()
