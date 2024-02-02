import osmnx
G2 = osmnx.graph_from_address(
 address="60 boulevard Saint-Michel, Paris, France",
 dist=2000,
 dist_type="network",
 network_type="drive",
)
fig, ax = osmnx.plot_graph(osmnx.project_graph(G2))
origine = osmnx.distance.nearest_nodes(G2, X=2.34017, Y=48.84635)
destination = osmnx.distance.nearest_nodes(G2, X=2.35036, Y=48.8413)
route = osmnx.shortest_path(G2, origine, destination)
fig, ax = osmnx.plot_graph_route(G2, route, node_size=0)
print(osmnx.utils_graph.route_to_gdf(G2, route))