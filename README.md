Binary Search Visualizer

Why I chose Binary Search:
Binary Search is significantly faster than Linear Search because it repeatedly divides the list in half. It also clearly demonstrates decomposition, abstraction, and algorithmic thinking, making it ideal for this assignment.

Problem Breakdown and Computational Thinking

Decomposition
- Receive user input: list of numbers and a target number  
- Convert the input string into a list of integers  
- Sort the list using Python’s built-in `sort()`  
- Apply Binary Search:
  - Initialize `low` and `high` indexes  
  - Compute middle index  
  - Compare target with middle value  
  - Narrow search to left or right half  
- Display step-by-step process and final result  

Pattern Recognition
- Binary Search repeatedly divides the list in half  
- Compares target to the midpoint value  
- Eliminates half of remaining elements each step  

Abstraction
- Users only see the list, target, and search steps  
- Internal logic, indexes, and calculations are hidden  
- Focus is on understanding the process, not the code  

Algorithm Design
**Input:** list of integers, target number  
**Process:** sort → binary search → record steps  
**Output:** result (found/not found) + step-by-step explanation  

Steps to Run
1. Open the Hugging Face link
https://huggingface.co/spaces/25rj/binary-search-visualizer

2. Enter a list of numbers (comma-separated) in the first box.
3. Enter the number to search in the second box.
4. Click Run Binary Search.
5. View the Result and the Step-by-step process below.

Author and Acknowledgment
Justin Chen
CISC 121

Resources I used were:
- Python
- Gradio
- Hugging Face
- GitHub