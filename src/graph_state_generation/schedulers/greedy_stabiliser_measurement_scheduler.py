'''
    Constructs a greedy schedule
'''
import bisect
from graph_state_generation.schedulers import scheduler
from graph_state_generation.graph_state import graph_node


class GreedyStabiliserMeasurementSchedulerLeft(scheduler.Scheduler):
    '''
        Constructs a greedy schedule
        This scheduler assumes a linear bus layout
    '''
    left = 0
    right = 1

    def greedy_schedule(self, *args, **kwargs):
        '''
            Constructs a greedy schedule
        '''

        # Copy the segments
        lr_segments = list(zip(map(self.get_lr, self.graph), self.graph))
        lr_segments.sort(key=lambda x: x[0][self.left])  # Gets the self.left value

        curr_right = 0
        curr_layer = 0

        self.schedule_layers.append([])

        # Greedily consume segments until all segments have been scheduled
        while len(lr_segments) > 0:
            # Reached end of layer
            if lr_segments[-1][0][self.left] < curr_right:
                curr_layer += 1
                curr_right = 0
                self.schedule_layers.append([])
                continue

            # Extract element
            next_segment_idx = bisect.bisect_left(
                lr_segments,
                curr_right,
                key=lambda x: x[0][self.left])
            lr, node = lr_segments.pop(next_segment_idx)
            self.schedule_layers[-1].append(node)
            curr_right = lr[self.right] + 1

    def _schedule(self, *args, **kwargs):
        return self.greedy_schedule(*args, **kwargs)

    def get_lr(self, node: graph_node.GraphNode):
        '''
           Maps a node to its leftmost and right most elements
        '''
        mapped_node = self.apply_mapper(node)
        return (min(mapped_node), max(mapped_node))
