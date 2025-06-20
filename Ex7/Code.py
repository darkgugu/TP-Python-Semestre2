import json

def load_sat(filepath="./Ex7/config.json"):
    with open(filepath, "r") as f:
        return json.load(f)["SAT"]

def evaluate_clause(clause, assignment):
    for literal in clause:
        var = literal.strip("-")
        is_neg = literal.startswith("-")
        value = assignment.get(var, False)
        if (value and not is_neg) or (not value and is_neg):
            return True
    return False

def verify_sat(clauses, assignment):
    return all(evaluate_clause(clause, assignment) for clause in clauses)

if __name__ == "__main__":
    data = load_sat()
    clauses = data["clauses"]
    assignment = {
        "A": True,
        "B": False,
        "C": True,
        "D": True
    }

    result = verify_sat(clauses, assignment)
    print("L'affectation satisfait la formule SAT ?" , result)
