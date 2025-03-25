import os
from typing import List
import matplotlib.pyplot as plt


def process_latex_equation(latex_list: List[str], env: str = "aligned"):
    """
    Process a list of LaTeX equations into a properly formatted string with the specified environment.

    Args:
        latex_list (List[str]): List of LaTeX equations to process
        env (str, optional): LaTeX environment to use. Defaults to "aligned".

    Returns:
        str: Processed LaTeX string with proper environment formatting

    Raises:
        ValueError: If the specified environment is not supported
    """

    import re

    text = "\\\[25pt] \n".join(latex_list)  # Leave some space between equations

    if env == "aligned":
        text = rf"""$$
        \begin{{{env}}}
            {text}
        \end{{{env}}}
        $$"""

    elif env == "align":
        text = rf"""
        \begin{{{env}*}}
            {text}
        \end{{{env}*}}
        """

    elif env == "alignat":
        text = rf"""
        \begin{{{env}*}}{{{2}}}
            {text}
        \end{{{env}*}}
        """

    else:
        raise ValueError(f"Environment {env} not supported")

    text = text.replace("\n", "")  # Remove newlines otherwise it does not compile
    text = re.sub(r"\s+", ' ', text)  # Remove extra spaces

    return text


def generate_latex_equation(latex_list,
                            env: str = "aligned",
                            format: str = "svg",
                            save_path: str = "./"):
    """
    Generate and save a list of LaTeX equations as an image file.

    This function creates a matplotlib figure with the rendered LaTeX equation and saves it
    in the specified format. The output is optimized for vector graphics editing in tools
    like Adobe Illustrator.

    Args:
        latex_list (Union[str, List[str]]): Single LaTeX equation or list of equations
        env (str, optional): LaTeX environment to use. Defaults to "aligned".
        format (str, optional): Output format. Must be one of ["svg", "pdf", "png"]. Defaults to "svg".
        save_path (str, optional): Directory to save the output file. Defaults to "./".
    """

    assert env in ["aligned", "align", "alignat"], "Environment must be either aligned, align or alignat"
    assert format in ["svg", "pdf", "png"], "Format must be either svg, pdf or png"

    if isinstance(latex_list, str):
        latex_list = [latex_list]

    text = process_latex_equation(latex_list, env=env)

    fig, ax = plt.subplots(figsize=(5, 1))
    ax.text(0, 0, text, fontsize=45, ha='left', va='center')
    ax.axis('off')

    # Save the figure as a SVG file
    filename = os.path.join(save_path, f"latex_equation.{format}")
    plt.savefig(filename,
                dpi=300,
                transparent=True,
                bbox_inches='tight',
                format=format)


def generate_algorithm(latex_alg,
                       format: str = "svg",
                       save_path: str = "./"):
    """
    Generate and save a LaTeX algorithm as an image file.

    This function creates a matplotlib figure with the rendered LaTeX algorithm and saves it
    in the specified format. The algorithm is rendered with a border and is optimized for
    vector graphics editing in tools like Adobe Illustrator.

    Args:
        latex_alg (str): LaTeX code for the algorithm
        format (str, optional): Output format. Must be one of ["svg", "pdf", "png"].
                              Defaults to "svg".
        save_path (str, optional): Directory to save the output file. Defaults to "./".
    """

    latex_alg = latex_alg.replace("\n", "")

    plt.text(0, 1, latex_alg, fontsize=18, ha='left', va='center', bbox=dict(facecolor='none', edgecolor='black', linewidth=1))
    plt.axis('off')

    filename = os.path.join(save_path, f"latex_algorithm.{format}")
    plt.tight_layout()
    plt.savefig(filename,
                transparent=True,
                dpi=300,
                bbox_inches='tight',
                format=format)
