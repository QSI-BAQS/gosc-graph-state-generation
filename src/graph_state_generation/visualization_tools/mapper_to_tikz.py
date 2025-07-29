'''
    Provides a tikz representation of the graph
'''

header = r'''
%!TEX options=--shell-escape
\documentclass[tikz]{standalone}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{xcolor}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{hyperref}
\usepackage{accsupp}    
\usepackage{graphicx}
\usepackage{mathtools}
\usepackage{pagecolor}
\usepackage{amsmath} % for \dfrac
\usepackage{tikz}
\tikzset{>=latex} % for LaTeX arrow head
\usepackage{braket}
\usepackage{pgfplots} 
\usepackage[edges]{forest}
\usetikzlibrary{patterns, backgrounds, arrows.meta}
\setlength{\parindent}{0cm}
\setlength{\parskip}{1em}

\usetikzlibrary{patterns}

\begin{document}
\begin{tikzpicture}[]
'''


tail = r"""
\end{tikzpicture}
\end{document} 
"""

def mapper_to_tikz(mapper, canvas = 3.5):
    '''
        Provides a tikz representation of the graph
    '''

    tikz_str = header + f"\n\\draw (-{canvas}, -{canvas}) rectangle ({canvas}, {canvas});\n"

    tikz_str += draw_polygon(len(graph))
    tikz_str += draw_edges(graph)
    tikz_str += tail
    return tikz_str    

def draw_nodes(mapper, row_sep: float=2.85, col_sep: float 2.85: graph_fill="red!45", graph_draw="red!35"
, map_fill="blue!45", map_draw="blue!35") -> str:
   graph_nodes = f'''
\\foreach \\x in {{0, ..., {mapper.n_elements - 1}}}{{
    \\node[shape=circle, draw={graph_draw} ,fill={graph_fill}, inner sep=0em, minimum width = 0.5cm](g_\\x) at (\\x * {col_sep}, {row_sep}) {{\\x}};
}}
    ''' 
    mapped_nodes = ""
    
    for graph_idx, mapped_idx in enumerate(mapper):   
        mapped_nodes = f'''
    \\node[shape=circle, draw={graph_draw} ,fill={graph_fill}, inner sep=0em, minimum width = 0.5cm](\\x) at (\\x * {col_sep}, {row_sep}) {{\\x}};
}}
    ''' 

def draw_graph_edges(mapper) -> str:
    edges = ""
    for node in graph:
        for edge in node:  
            lower, upper = min(edge, node.qubit_idx), max(edge, node.qubit_idx)
            edges += f"\\draw[draw=gray!95] (g_{lower}) to[bend right=45] (g_{upper});\n";
    return edges


def draw_mapped_edges(mapper) -> str:
    edges = ""
    for node in graph:
        mapped_node = (mapper[node.qubit_idx], node.qubit_idx) 
        for edge in node:  
            mapped_edge = (mapper[edge], edge)
            lower, upper = min(mapped_node, mapped_edge), max(mapped_node, mapped_edge) 
            edges += f"\\draw[draw=gray!95] (m_{lower[1]}) to[bend right=45] (m_{upper[1]});\n";
    return edges
