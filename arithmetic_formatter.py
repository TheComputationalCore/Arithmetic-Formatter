def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Initialize lists to store formatted lines
    top_row = []
    bottom_row = []
    dash_row = []
    answer_row = []
    
    for problem in problems:
        # Split the problem into components
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'
        
        num1, operator, num2 = parts
        
        # Check for valid operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if numbers contain only digits
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check if numbers are not more than four digits
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Calculate the width needed for this problem
        width = max(len(num1), len(num2)) + 2
        
        # Format the numbers and operator
        top_row.append(num1.rjust(width))
        bottom_row.append(operator + num2.rjust(width - 1))
        dash_row.append('-' * width)
        
        # Calculate answer if needed
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_row.append(answer.rjust(width))
    
    # Combine rows with proper spacing
    result = '    '.join(top_row) + '\n' + \
             '    '.join(bottom_row) + '\n' + \
             '    '.join(dash_row)
    
    if show_answers:
        result += '\n' + '    '.join(answer_row)
    
    return result
