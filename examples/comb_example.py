from graph_state_generation.mappers import weight_sort_mapper 
from graph_state_generation.schedulers import greedy_cz_scheduler
from graph_state_generation.graph_state import example_graphs

height = 10
width = 3
spacing = 1

n_vertices = 10
gs = example_graphs.graph_binary_tree(n_vertices)

mapped_gs = weight_sort_mapper.CombWeightSortMapper(gs, height, width, n_passes=100)
schedule = greedy_cz_scheduler.GreedyCZScheduler(gs, mapped_gs) 
