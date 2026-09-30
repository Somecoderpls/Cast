import argparse, ast, rules

def parse_args():
    parser = argparse.ArgumentParser(prog="Cast", description="Code AST")
    parser.add_argument('filename')
    return parser.parse_args()

if __name__ == "__main__":
    parser = parse_args()
    list_of_classes = rules.get_all_classes()
    with open(parser.filename) as f:
        source = f.read()
    mast = ast.parse(source)
    for my_class in list_of_classes:
        sec = my_class
        print(f"Checking file {parser.filename}")
        sec.visit(mast)
