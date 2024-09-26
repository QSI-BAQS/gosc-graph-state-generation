''' Constructs a greedy schedule
'''
import copy
import bisect
from graph_state_generation.schedulers import scheduler


class GreedyCZScheduler(scheduler.Scheduler):
    '''
        Constructs a greedy schedule
        This scheduler assumes a linear bus layout
    '''
    left = 0
    right = -1
    graph_node = 1
    mapped_graph = 0

    def greedy_schedule(self, *args, **kwargs):
        '''
            Constructs a greedy schedule
        '''

        # We will be changing the associated adjacency matrix
        self.graph = copy.deepcopy(self.graph)

        # Copy the segments and sort by their leftmost value
        segments = list(zip(map(self.apply_mapper, self.graph), self.graph))
        segments.sort(
                key=lambda x: x[0][self.left]
            )

        # Map from nodes to mapped segments
        segment_dict = {segment[self.graph_node]: segment for segment in segments}

        curr_right = 0

        # Initial layer
        self.schedule_layers.append([])

        # Greedily consume segments until all segments have been scheduled
        while len(segments) > 0:
            # Reached end of layer
            if segments[-1][0][self.left] < curr_right:
                curr_right = 0
                self.schedule_layers.append([])
                continue

            # Extract element
            next_segment_idx = bisect.bisect_left(
                segments,
                curr_right,
                key=lambda x: x[0][self.left])
            mapped_node, graph_node = segments.pop(next_segment_idx)

            # Remove reciprocal edges
            for neighbour in graph_node:
                neighbouring_node = self.graph[neighbour]

                neighbouring_node.remove(graph_node.qubit_idx)
                segments.remove(segment_dict[neighbouring_node])

                # Only re-add node if it still has edges
                if len(self.graph[neighbour]) > 0:
                    segment = (self.apply_mapper(neighbouring_node), neighbouring_node)
                    segment_dict[segment[self.graph_node]] = segment   
                    bisect.insort(segments, segment, key=lambda x: x[0][self.left])

            # Append consumed node to schedule
            self.schedule_layers[-1].append(graph_node)
            curr_right = mapped_node[self.right] + 1

    def schedule(self, *args, **kwargs):
        return self.greedy_schedule(*args, **kwargs)
