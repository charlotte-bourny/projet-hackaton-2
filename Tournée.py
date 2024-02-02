import numpy
import matplotlib.pyplot
from itertools import combinations
from networkx import DiGraph
from vrpy import VehicleRoutingProblem
X = numpy.random.random(size = 6)
print(X)
Y = numpy.random.random(size = 6)
print(Y)
def distance_cartesienne(x1, x2, y1, y2):
    return numpy.sqrt(numpy.square(x1-x2)+numpy.square(y1-y2))

G3 = DiGraph()
for (i, (xval, yval)) in enumerate(zip(X, Y)):
    G3.add_edge("Source", i, cost = distance_cartesienne(xval, 0, yval, 0))
    G3.add_edge(i, "Sink", cost = distance_cartesienne(xval, 0, yval, 0))
    G3.nodes[i]["demand"] = 1
for ((i, (x1, y1)), (j, (x2, y2))) in combinations(list(enumerate(zip(X, Y))), 2):
    G3.add_edge(i, j, cost = distance_cartesienne(x1, x2, y1, y2))
    G3.add_edge(j, i, cost = distance_cartesienne(x1, x2, y1, y2))

probleme_optimisation = VehicleRoutingProblem(G3, load_capacity = 9999)
probleme_optimisation.solve()
print(probleme_optimisation.best_value)
print(probleme_optimisation.best_routes)

matplotlib.pyplot.figure(figsize=(10,10))
matplotlib.pyplot.scatter(X, Y, color = 'red', marker = 'x')
for route in probleme_optimisation.best_routes.values():
    itineraire_X = [0] + [X[p] for p in route[1:-1]] + [0]
    itineraire_Y = [0] + [Y[p] for p in route[1:-1]] + [0]
    for (a, b, c, d) in zip(itineraire_X[:-1], itineraire_Y[:-1], [x2-x1 for (x1, x2) in zip(itineraire_X[:-
1], itineraire_X[1:])], [y2-y1 for (y1, y2) in zip(itineraire_Y[:-1], itineraire_Y[1:])]):
        matplotlib.pyplot.arrow(a, b, c, d, width = 0.001, color = 'black', length_includes_head =
True, head_width = 0.01)
matplotlib.pyplot.title("Routage d'une tournée de 6 destinations aléatoires au départ de (0, 0)")
matplotlib.pyplot.show()
