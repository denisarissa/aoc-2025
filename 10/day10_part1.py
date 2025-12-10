input = open("day10_input.txt").read().strip().split('\n')

total_presses = 0

for line in input:
    if not line.strip():
        continue
    
    # Parse target light pattern from [.##.] format
    # . = off (0), # = on (1)
    start = line.find('[')
    end = line.find(']')
    target_lights = [1 if char == '#' else 0 for char in line[start+1:end]]
    
    # Parse button configurations from (0,2,3) format
    # Numbers indicate which lights the button toggles
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
    
    num_lights = len(target_lights)
    num_buttons = len(buttons)
    
    # Build equation matrix: rows = lights, columns = buttons
    # equations[i][j] = 1 if button j affects light i
    # Last column is target state for that light
    equations = []
    for light_idx in range(num_lights):
        equation = []
        for button in buttons:
            affects = 1 if light_idx in button else 0
            equation.append(affects)
        equation.append(target_lights[light_idx])
        equations.append(equation)
    
    # Gaussian elimination over GF(2) (binary field with XOR)
    # Goal: determine which buttons are locked vs free
    # Locked: must press/not press to satisfy constraints
    # Free: can choose either way
    locked_buttons = []
    current_row = 0
    
    for btn_col in range(num_buttons):
        # Find equation that uses this button
        found_row = None
        for row in range(current_row, num_lights):
            if equations[row][btn_col] == 1:
                found_row = row
                break
        
        if found_row is None:
            continue  # Button is free
        
        # Move equation to current row
        equations[current_row], equations[found_row] = equations[found_row], equations[current_row]
        locked_buttons.append(btn_col)
        
        # Eliminate button from other equations using XOR
        # If another row has this button, XOR with current row
        for row in range(num_lights):
            if row != current_row and equations[row][btn_col] == 1:
                for col in range(num_buttons + 1):
                    equations[row][col] ^= equations[current_row][col]
        
        current_row += 1
    
    free_buttons = [col for col in range(num_buttons) if col not in locked_buttons]
    
    # No free buttons: solution is determined
    if not free_buttons:
        presses = sum(equations[r][-1] for r in range(len(locked_buttons)))
        total_presses += presses
        continue
    
    # Try all combinations of free button presses to find minimum
    min_presses = float('inf')
    
    for combo in range(1 << len(free_buttons)):
        plan = [0] * num_buttons
        
        # Set free button values from combination
        for i, free_btn in enumerate(free_buttons):
            plan[free_btn] = (combo >> i) & 1
        
        # Back substitution: calculate locked button values
        for row in range(len(locked_buttons) - 1, -1, -1):
            locked_btn = locked_buttons[row]
            needs = equations[row][-1]
            
            # XOR out contributions from already-decided buttons
            for btn_idx in range(locked_btn + 1, num_buttons):
                needs ^= (equations[row][btn_idx] * plan[btn_idx])
            
            plan[locked_btn] = needs
        
        min_presses = min(min_presses, sum(plan))
    
    total_presses += min_presses

print(total_presses)