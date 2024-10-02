'''
    Simple time decorator for benchmarking
'''
import time


def time_decorator(fn): 
    '''
        time_decorator
        Simple decorator to track the time of a function call
    '''
    def _wrap(*args, **kwargs):
        start_time = time.time() 
        result = fn(*args, **kwargs)
        end_time = time.time() 
        return result, end_time - start_time
    return _wrap

