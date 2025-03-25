# LaTeX to Illustrator Converter

A Python tool that converts LaTeX equations and algorithms into high-quality vector graphics (SVG, PDF) that can be easily imported into Adobe Illustrator or other design tools for editing.

## Required

- For Mac, download AMS fonts in the OTF format from https://github.com/Happypig375/AMSFonts-Ttf-Otf
 and paste it into Library/Fonts

- List desired Latex preambles as:

    ```python
    sty_path = os.getcwd() + "/custom-definitions"
    latex_preamble = [
        rf'\usepackage{{{sty_path}}}', # Custom style files
        r'\usepackage{{amsmath}}',
        r'\usepackage[OT1]{fontenc}',
        r"\usepackage{algpseudocode}",
    ]
    ```

- Pass the following rcParams
    ```python
    plt.rcParams.update({
        "text.usetex": True,
        'pdf.fonttype': 42, # This enables editing text in Illustrator
        'ps.fonttype': 42,  # This enables editing text in Illustrator
        'text.latex.preamble': '\n'.join(latex_preamble), # Parse the preambles
        'font.size': 18,
    })
    ```

- Save it either in 
    - ```.svg``` format: editable as vector graphics
    - ```.pdf``` format: editable also as a text when available

- It is essential to use ```\usepackage[OT1]{fontenc}``` encoding instead of ```[T1]```.

- For additional details: https://jonathansoma.com/lede/data-studio/matplotlib/exporting-from-matplotlib-to-open-in-adobe-illustrator/

## Usage

### Converting Equations

```python
from latex_to_illustrator import generate_latex_equation

# Single equation
equation = "x^2 + y^2 = r^2"
generate_latex_equation(equation, env="aligned", format="svg", save_path="./")

# Multiple equations line-by-line
equations = [
    "x^2 + y^2 = r^2",
    "y = mx + b"
]
generate_latex_equation(equations, env="align", format="pdf", save_path="./")

# Multiple equations at once
equations = r"""
    x^2 + y^2 = r^2 \\
    y = mx + b
"""
generate_latex_equation(equations, env="align", format="pdf", save_path="./")
```

### Converting Algorithms

```python
from latex_to_illustrator import generate_algorithm

algorithm= r"""
\begin{algorithmic}[1]
    \Procedure{Euclid}{$a,b$} 
        \State $r\gets a \bmod b$
        \While{$r\not=0$}
            \State $a \gets b$
            \State $b \gets r$
            \State $r \gets a \bmod b$
        \EndWhile\label{euclidendwhile}
        \State \textbf{return} $b$
    \EndProcedure
\end{algorithmic}
"""

generate_algorithm(algorithm, format="svg", save_path="./")
```

## Parameters

### `generate_latex_equation()`
- `latex_list`: String or list of strings containing LaTeX equations
- `env`: Equation environment ("aligned", "align", or "alignat")
- `format`: Output format ("svg", "pdf", or "png")
- `save_path`: Directory to save the output file

### `generate_algorithm()`
- `latex_alg`: String containing LaTeX algorithm code
- `format`: Output format ("svg", "pdf", or "png")
- `save_path`: Directory to save the output file