import clingo


def print_answer_sets(program):
    control = clingo.Control()
    control.add("base", [], program)
    control.ground([("base", [])])
    control.configuration.solve.models = 0
    for model in control.solve(yield_=True):
        sorted_model = [str(atom) for atom in model.symbols(shown=True)]
        sorted_model.sort()
        print("Answer set: {{{}}}".format(", ".join(sorted_model)))


def main():
    program = """
    
        var(1..3).
        print(X) :- var(X).
        #show print/1.
        
    """

    print_answer_sets(program)


if __name__ == '__main__':
    main()
