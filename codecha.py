
import networkx as nx
import matplotlib.pyplot as plt
from geopy.distance import geodesic
def charlotte(x):
    # Coordonnées du dépôt
    z=x
    depot_coords = (2.36815, 48.74991)

    # Coordonnées des destinataires
    destinations = {
        'Mines Paris': (2.33969, 48.84563),
        'Observatoire de Paris': (2.33650, 48.83730),
        'Marie du 14e': (2.32698, 48.83320),
        'Gare Montparnasse TGV': (2.32159, 48.84117),
        'Mairie du 15e': (2.29991, 48.84126)
    }


    G = nx.Graph()
    G.add_node('Depot', pos=depot_coords)

    for lieu, coord in destinations.items():
        G.add_node(lieu, pos=coord)


    for lieu,coord in destinations.items():
        distance = geodesic(depot_coords, coord).meters
        G.add_edge('Depot', lieu, weight=distance)


    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos)
    nx.draw_networkx_labels(G, pos)

    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(G, pos, labels)


    plt.title('Graph Simplifié à Vol d\'Oiseaux')
    plt.show()

    import requests


    G1 = nx.Graph()
    G1.add_node('Depot', pos=depot_coords)

    for lieu, coord in destinations.items():
        response = requests.get(
            f'https:',
            params={
                'start': f'{depot_coords[0]},{depot_coords[1]}',
                'end': f'{coord[0]},{coord[1]}'
            }
        )
        distance = response.json()['properties']['distance']
        G.add_node(lieu, pos=coord)
        G.add_edge('Depot', lieu, weight=distance)

    pos = nx.get_node_attributes(G1, 'pos')

    nx.draw(G1, pos)
    nx.draw_networkx_labels(G1, pos)

    labels = nx.get_edge_attributes(G1, 'weight')
    nx.draw_networkx_edge_labels(G1, pos, edge_labels=labels)

    plt.title('Graph avec Distances Réelles')
    a = plt.savefig('graph.png')
    return a