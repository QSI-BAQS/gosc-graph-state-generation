'''
 Constructs a greedy schedule
'''
import bisect
from graph_state_generation.schedulers.scheduler import Scheduler, MappedNode


class GreedyCZScheduler(Scheduler):
    '''
        Constructs a greedy schedule
        This scheduler assumes a linear bus layout
    '''
    left = 0
    right = -1
    graph_node = 1
    mapped_graph = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, mapped_node=CZMappedNode, **kwargs)

    def greedy_schedule(self, *args, **kwargs):
        '''
            Constructs a greedy schedule
        '''

        # Copy the segments and sort by their leftmost value
        curr_right = 0

        # Initial layer
        self.schedule_layers.append([])

        segments = list(self.mapped_segments)
        segments.sort(key=lambda x: x.left)

        # Greedily consume segments until all segments have been scheduled
        while len(segments) > 0:
            # Reached end of layer
            if segments[-1].left < curr_right:
                curr_right = 0
                self.schedule_layers.append([])
                continue

            # Extract element
            next_segment_idx = bisect.bisect_left(
                segments,
                curr_right,
                key=lambda x: x.left)
            mapped_node = segments.pop(next_segment_idx)

            # Remove reciprocal edges
            for neighbouring_node in mapped_node.references:
                if len(neighbouring_node) <= 1:
                    # Remove node
                    # Segments is sorted on left most element, hence multiple objects
                    # may share the same index
                    index = bisect.bisect_left(
                            segments,
                            neighbouring_node.left,
                            key=lambda x: x.left
                        )
                    while segments[index].qubit_idx != neighbouring_node.qubit_idx:
                        index += 1
                    segments.pop(index)

                    index = bisect.bisect_left(
                        self.graph.vertices,
                        neighbouring_node.qubit_idx,
                        key=lambda x: x.qubit_idx
                    )
                    self.graph.pop(index)
                    self.mapped_segments.pop(index)
                    continue

                position_update = neighbouring_node.remove_edge(mapped_node.graph_node.qubit_idx)
                # Only re-add node if it still has edges
                if position_update is not None:
                    # Re-sort node
                    index = bisect.bisect_left(segments, position_update, key=lambda x: x.left)
                    while segments[index].qubit_idx != neighbouring_node.qubit_idx:
                        index += 1
                    segments.pop(index)
                    bisect.insort(segments, neighbouring_node, key=lambda x: x.left)

            # Append consumed node to schedule
            if len(mapped_node) > 0:
                self.schedule_layers[-1].append(mapped_node)
                curr_right = mapped_node.right + 1

        # If the last layer was purely decorative  
        if len(self.schedule_layers[-1]) == 0:
            self.schedule_layers.pop(-1)

    def schedule(self, *args, **kwargs):
        '''
            schedule
            Dispatch method for greedy_schedule
        '''
        return self.greedy_schedule(*args, **kwargs)


class CZMappedNode(MappedNode):
    '''
        Mapped node for CZ stabilisers
    '''
    def __init__(self, graph_node, scheduler):
        super().__init__(graph_node, scheduler)

        self.left = min(self.mapped_values)
        self.right = max(self.mapped_values)

    def remove_edge(self, idx):
        '''
            Removes an edge from the node
        '''
        edge_idx = self.graph_node.index(idx)

        update_left = None
        update_right = None
        if self.mapped_values[edge_idx] == self.left:
            update_left = self.left

        if self.mapped_values[edge_idx] == self.right:
            update_right = self.left

        super().remove_edge(idx)

        if update_right is not None:
            self.right = max(self.mapped_values)

        if update_left is not None:
            self.left = min(self.mapped_values)
            return update_left

        return None
