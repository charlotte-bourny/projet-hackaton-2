import osmnx as ox
import networkx as nx
import vrpy
from shapely.geometry import Point
import geopandas as gpd

# Fonction pour calculer la consommation énergétique en Joules
def calculate_energy_consumption(route, graph, speed_kmh=20, efficiency_kwh_per_km=0.17):
    total_distance = sum(graph[u][v]['length'] for u, v in zip(route[:-1], route[1:]))
    total_distance_km = total_distance / 1000
    energy_consumption = total_distance_km * efficiency_kwh_per_km
    return energy_consumption

# Fonction pour optimiser la tournée de livraison
def optimize_delivery_route(depot, destinations):
    # Créer le graphe routier avec OSMnx
    G = ox.graph_from_point(depot, distance=500, network_type='drive')

    # Ajouter le dépôt au graphe
    G.add_node('depot', x=depot.x, y=depot.y)

    # Ajouter les destinations au graphe
    for i, dest in enumerate(destinations):
        G.add_node(f'dest_{i}', x=dest.x, y=dest.y)

    # Créer une demande pour chaque destination
    demands = [1] * len(destinations)

    # Initialiser le problème de routage avec VRPy
    problem = vrpy.VRPy()

    # Ajouter les nœuds (dépôt et destinations) au problème
    for node in G.nodes:
        x, y = G.nodes[node]['x'], G.nodes[node]['y']
        problem.add_node(node, x=x, y=y)

    # Ajouter les arcs au problème
    for edge in G.edges:
        problem.add_arc(edge[0], edge[1], distance=G[edge[0]][edge[1]]['length'])

    # Ajouter la demande à chaque destination
    for i, dest in enumerate(destinations):
        problem.add_demand(f'dest_{i}', demands[i])

    # Résoudre le problème d'optimisation
    problem.solve()

    # Obtenir la meilleure tournée
    best_route = problem.get_routes()[0]

    # Afficher la tournée optimisée
    print("Tournée optimisée:", best_route)

    # Calculer la consommation énergétique
    energy_consumption = calculate_energy_consumption(best_route, G)

    print("Consommation énergétique estimée:", energy_consumption, "Joules")

# Coordonnées du dépôt
depot_coords = Point(2.3522, 48.8566)  # Exemple: Paris

# Coordonnées des destinataires
dest_coords = [Point(2.3697, 48.8530),  # Exemple: Proche du dépôt à Paris
               Point(2.2945, 48.8588),  # Exemple: Centre-ville à Paris
               Point(2.3522, 48.8636)]  # Exemple: Autre endroit à Paris

# Appel de la fonction pour optimiser la tournée de livraison
optimize_delivery_route(depot_coords, dest_coords)
