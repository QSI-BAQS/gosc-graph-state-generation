from graph_state_generation.mappers import linear_mapper
from graph_state_generation.schedulers import  greedy_cz_scheduler
from graph_state_generation.graph_state import example_graphs


n_vertices = 100
gs = example_graphs.graph_binary_tree(n_vertices)

mapped_gs = linear_mapper.LinearMapper(gs)
schedule = greedy_cz_scheduler.GreedyCZScheduler(gs, mapped_gs) 
