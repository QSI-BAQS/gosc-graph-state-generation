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

def graph_to_tikz(graph, canvas = 3.5):
    '''
        Provides a tikz representation of the graph
    '''

    tikz_str = header + f"\n\\draw (-{canvas}, -{canvas}) rectangle ({canvas}, {canvas});\n"

    tikz_str += draw_polygon(len(graph))
    tikz_str += draw_edges(graph)
    tikz_str += tail
    return tikz_str    

def draw_polygon(n_points: int, radius: float=2.85, fill="red!45", draw="red!35") -> str:
   return f'''
\\foreach \\x in {{0, ..., {n_points - 1}}}{{
    \\node[shape=circle, draw={draw} ,fill={fill}, inner sep=0em, minimum width = 0.5cm](\\x) at (\\x * 360 / {n_points} : {radius}cm) {{\\x}};
}}
    ''' 

def draw_edges(graph) -> str:
    edges = ""
    for node in graph:
        for edge in node:  
            lower, upper = min(edge, node.qubit_idx), max(edge, node.qubit_idx)
            if abs(upper - lower) > len(graph) // 2: 
                edges += f"\\draw[draw=gray!95] ({lower}) to[bend right=45] ({upper});\n";
            else:
                edges += f"\\draw[draw=gray!95] ({lower}) to[bend left=45] ({upper});\n";

    return edges
