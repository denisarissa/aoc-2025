import time

start = time.time()

input = open("day10_input.txt").read().strip().split('\n')

total_presses = 0

for line in input:
    if not line.strip():
        continue
    
    # Parse button configurations from (0,2,3) format
    # Numbers indicate which counters the button increments
    buttons = []
    pos = 0
    while pos < len(line):
        if line[pos] == '(':
            close = pos + 1
            while close < len(line) and line[close] != ')':
                close += 1
            nums = line[pos+1:close]
            if nums.strip():
                affected = tuple(int(x.strip()) for x in nums.split(','))
                buttons.append(affected)
            pos = close
        pos += 1
    
    # Parse target counter values from {3,5,4,7} format
    curly_start = line.find('{')
    curly_end = line.find('}')
    targets = [int(x.strip()) for x in line[curly_start+1:curly_end].split(',')]
    
    num_counters = len(targets)
    num_buttons = len(buttons)
    
    # Build equation matrix: rows = counters, columns = buttons
    # equations[i][j] = 1 if button j increments counter i
    # Last column is target value for that counter
    equations = []
    for counter_idx in range(num_counters):
        equation = []
        for button in buttons:
            affects = 1 if counter_idx in button else 0
            equation.append(float(affects))
        equation.append(float(targets[counter_idx]))
        equations.append(equation)
    
    # Gaussian elimination to reduced row echelon form
    # Goal: determine which buttons are locked vs free
    # Locked: press count determined by equation
    # Free: can press any number of times
    locked_buttons = []
    current_row = 0
    
    for btn_col in range(num_buttons):
        # Find equation that uses this button (non-zero coefficient)
        found_row = None
        for row in range(current_row, num_counters):
            if abs(equations[row][btn_col]) > 1e-9:
                found_row = row
                break
        
        if found_row is None:
            continue  # Button is free
        
        # Move equation to current row
        equations[current_row], equations[found_row] = equations[found_row], equations[current_row]
        
        # Scale equation so button coefficient becomes 1
        coeff = equations[current_row][btn_col]
        for col in range(num_buttons + 1):
            equations[current_row][col] /= coeff
        
        locked_buttons.append(btn_col)
        
        # Eliminate button from all other equations
        for row in range(num_counters):
            if row != current_row and abs(equations[row][btn_col]) > 1e-9:
                factor = equations[row][btn_col]
                for col in range(num_buttons + 1):
                    equations[row][col] -= factor * equations[current_row][col]
        
        current_row += 1
    
    free_buttons = [col for col in range(num_buttons) if col not in locked_buttons]
    
    # No free buttons: solution is determined
    if not free_buttons:
        counts = [equations[r][-1] for r in range(len(locked_buttons))]
        if all(abs(c - round(c)) < 1e-9 and round(c) >= 0 for c in counts):
            total_presses += sum(round(c) for c in counts)
        continue
    
    # Try different free button press counts to find minimum
    min_presses = float('inf')
    max_search = max(targets) * 2
    
    # Iterate by total free button presses: 0, 1, 2, ...
    for total_free in range(max_search):
        # Generate all ways to split total among free buttons
        splits = []
        
        def make_splits(remaining, num_left, current):
            if num_left == 1:
                splits.append(current + [remaining])
                return
            for amount in range(remaining + 1):
                make_splits(remaining - amount, num_left - 1, current + [amount])
        
        if len(free_buttons) == 1:
            splits = [[total_free]]
        else:
            make_splits(total_free, len(free_buttons), [])
        
        # Test each split
        for split in splits:
            plan = [0.0] * num_buttons
            
            # Set free button press counts
            for i, free_btn in enumerate(free_buttons):
                plan[free_btn] = float(split[i])
            
            # Calculate locked button press counts from equations
            for row in range(len(locked_buttons)):
                locked_btn = locked_buttons[row]
                needs = equations[row][-1]
                
                # Subtract free button contributions
                for free_btn in free_buttons:
                    needs -= equations[row][free_btn] * plan[free_btn]
                
                plan[locked_btn] = needs
            
            # Valid if all counts are non-negative integers
            if all(abs(c - round(c)) < 1e-9 and round(c) >= 0 for c in plan):
                min_presses = min(min_presses, sum(round(c) for c in plan))
        
        # Stop if searched past the best solution
        if min_presses != float('inf') and total_free > min_presses:
            break
    
    total_presses += min_presses

print(total_presses)
print(time.time() - start)