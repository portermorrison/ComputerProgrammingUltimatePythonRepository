import importlib

problems = """
extremes
powers
tip_calculator
volume_functions
"""

def make_problem_title(filenameSansExtension):
    return filenameSansExtension.replace("_", " ").title().replace(" ", "")

def print_problem_banner(title):
    print("".center(80, "-"))
    print("|" + title.center(78, " ") + "|")
    print("".center(80, "-"))

for (idx, name) in enumerate(problems.strip().split("\n")):
    run_again = "y"
    print_problem_banner(str(idx + 1) + ". " + make_problem_title(name))
    the_module = importlib.import_module(name)
    print("Run again? (y/n): ", end="")
    run_again = input()
    while run_again != "n":
        importlib.reload(the_module)
        print("Run again? (y/n): ", end="")
        run_again = input()

