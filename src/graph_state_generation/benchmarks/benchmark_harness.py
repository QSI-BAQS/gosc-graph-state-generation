'''
    Benchmark
    Simple benchmark harness
'''
from typing import Callable, Iterable, Type
from graph_state_generation.utility.time_decorator import time_decorator 

Mapper = Type['Mapper']
Scheduler = Type['Scheduler']


class Benchmark:
    '''
        Benchmark
        Simple benchmark harness
    '''
    def __init__(self,
         graph_constructor : Callable,
         mapper_constructor : Callable,
         scheduler_constructor : Callable
        ):
        self.graph_constructor = graph_constructor
        self.mapper_constructor = mapper_constructor
        self.scheduler_constructor = scheduler_constructor
        self.results = None

    def benchmark(
            graph_param_iterable : Iterable,
            mapper_param_iterable : Iterable,
            scheduler_param_iterable : Iterable,
            results_lambda : Callable =lambda x: x.scheduler_layers):
        '''
            Runs a set of benchmarks
            :: graph_param_iterable : Iterable :: Collection of scheduler params  
            :: mapper_param_iterable : Iterable :: Collection of mapper params 
            :: scheduler_param_iterable : Iterable :: Collection of scheduler params 
            ::  
        '''
        result_obj = {'results': [], 'runtimes': []}  
    
        for params in zip(
                    graph_param_iterable,
                    mapper_param_iterable,
                    scheduler_param_iterable
                ): 
            result, runtime = self.run_benchmark_instance(*params)
            result_obj['results'].append(result)
            result_obj['runtimes'].append(runtime)

        return result_obj  

    @time_decorator
    def run_benchmark_instance(
        self,
        graph_params,
        mapper_params,
        scheduler_params
    ):
        '''
            run_benchmark_instance
            ::
        '''
        graph = self.graph_constructor(**graph_params) 
        mapper = self.mapper_constructor(graph, **mapper_params)
        scheduler = self.scheduler_constructor(graph, mapper, **scheduler_params)
        if not scheduler.called:
            scheduler()

        return scheduler



