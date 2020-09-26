# CS-Unit1-Build

https://medium.com/decision-tree-learning

### Algorithm Explanation:
- Find unique values for a column.
- Counts the number of each type of example.
  - Check if value is numeric
- Compare the feature value in an example to the feature value in question.
  - Print the question in a readable format.
- Keep track of the best information gain.
- Split dataset.
  - Skip this split if it doesn't divide the dataset.
  - Calculate information gain from split.
- Decide whether to follow the true-branch or the false-branch.
  - Compare the feature / value stored in the node, to the example we're considering.
- Call function recursively on the true branch.
- Call function recursively on the false branch.

To run decision tree example:
``` python decision-tree.py ```