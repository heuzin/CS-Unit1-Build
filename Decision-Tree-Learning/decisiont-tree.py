class DecisionNode:
    # Decision Node asks a question
    # Hold reference to the question and to the two child nodes.

    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
    
def build_decsion_tree(rows):
    # Calculate the information gain and return the question that produces the highest gain
    gain, question = find_best_split(rows)

    # Base case: no further questions, return a leaf
    # Create Leaf class
    if gain == 0:
        return Leaf(rows)

    # Partition
    # Create Partition function
    true_rows, false_rows = partition(rows, question)

    # True branch
    true_branch = build_decsion_tree(true_rows)

    # False branch
    false_branch = build_decsion_tree(false_rows)

    return DecisionNode(question, true_branch, false_branch)