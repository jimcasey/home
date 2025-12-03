# Advent of Code 2025 - Knowledge Base

## Project Structure

### Directory Layout
```
2025/
├── README.md           # Links to AOC 2025
├── template.py         # Boilerplate for daily solutions
├── new.py             # Script to generate day folders
├── KNOWLEDGE.md       # This file
└── XX/                # Day-specific folders
    ├── part1.py       # Part 1 solution
    ├── part2.py       # Part 2 solution (copied from part1)
    ├── test.txt       # Test input data
    └── input.txt      # Actual puzzle input
```

### Creating New Days
```bash
python3 new.py 01
```
This creates a folder with `part1.py`, `test.txt`, and `input.txt`.

## Development Workflow

### 1. Initial Development Pattern
1. Start with `test.txt` for development
2. Develop and debug `part1.py` using test data
3. Switch to `input.txt` when ready for final answer
4. Copy `part1.py` to `part2.py` for part 2
5. Update `part2.py` to read from `test.txt` for development
6. Repeat cycle for part 2

### 2. Git Workflow
- Commit after each significant change
- Push to branch: `claude/advent-of-code-2025-<sessionId>`
- Branch must start with `claude/` and end with session ID
- Always push with `-u` flag for tracking

### 3. Testing Approach
- Use small test datasets in `test.txt` first
- Verify logic with known outputs
- Add debug output temporarily when needed
- Remove debug output before final commit
- Switch to `input.txt` only after test passes

## Code Patterns

### Template Structure
```python
from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'  # or '/input.txt'


def main():
  lines = readInput()
  # Solution logic here


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
```

### Common Parsing Pattern
```python
for line in lines:
  direction = line[0]        # First character
  value = int(line[1:])      # Rest as integer
```

## Mathematical Constraints & Patterns

### Day 01: Circular Index Navigation

#### Key Constraints
- **Index Range**: 0-99 (100 values)
- **Wrap-Around**: Use modulo 100
- **Starting Index**: 50 (problem-specific)

#### Wrapping Rules
```python
# Right movement (forward)
index = (index + value) % 100

# Left movement (backward)
index = (index - value) % 100
```

Examples:
- `R99` from 0 → 99
- `R100` from 0 → 0
- `R101` from 0 → 1
- `L5` from 0 → 95 (wraps to 99-4)

#### Part 1: Landing on Zero
Count when index equals 0 after each move:
```python
if index == 0:
  zero_count += 1
```

#### Part 2: Passing Through Zero
Count ALL crossings of 0 (including landing on it):

```python
# Right moves: count multiples of 100 crossed
zero_count += (index + value) // 100 - index // 100

# Left moves: count multiples of 100 crossed going down
zero_count += (index - 1) // 100 - (index - value - 1) // 100
```

**Key Insight**: Crossing detection uses integer division to count how many times we cross the 0/100 boundary.

Examples:
- R10 from 90 → crosses 100, reaches 0 → count +1
- R25 from 90 → crosses 100, reaches 15 → count +1
- R125 from 90 → crosses 100 twice → count +2

## Debugging Techniques

### Temporary Debug Output
```python
print(f"{index} {line}")  # Show state after each step
```

### Debug-to-Final Transition
1. Add debug output to verify logic
2. Test with known results
3. Remove debug output
4. Keep only final answer output
5. Commit clean version

## Learned Constraints

### Modulo Arithmetic
- **DO**: Use `% 100` for range 0-99
- **DON'T**: Use conditional checks like `if index > 99: index = 0`
- **WHY**: Modulo handles values > 100 correctly (e.g., R111 → 11)

### Problem-Specific Parameters
- Initial state (e.g., starting index) is often provided in problem
- Don't assume index starts at 0 unless specified
- Test data helps identify these parameters

### Edge Cases
- Values larger than range (handled by modulo)
- Negative wrapping (Python's modulo handles correctly)
- Multiple crossings in single move

## Common Pitfalls

### 1. Wrong Initial State
❌ Starting at index 0 when problem specifies 50
✅ Read problem carefully for initial conditions

### 2. Landing vs. Passing
❌ Only counting when landing on target
✅ Understanding "passes through" vs "lands on"

### 3. Modulo Range
❌ Using modulo 101 for range 0-100
✅ Using modulo 100 for range 0-99

### 4. Debug Output Left In
❌ Committing code with debug prints
✅ Clean up before final commit

## Results Summary

### Day 01
- **Part 1**: 1145 (counting lands on 0)
- **Part 2**: 6561 (counting passes through 0)
- **Test Results**: 3 and 6 respectively

## Tips for Future Days

1. **Start Simple**: Use test data to understand the problem
2. **Iterate**: Build complexity gradually
3. **Verify**: Check edge cases with test data
4. **Document**: Note any problem-specific constraints
5. **Clean**: Remove debug code before committing
6. **Track**: Use git commits to track progress
7. **Reuse**: Copy patterns from previous days when applicable

## File Management

### When to Use Each File
- `test.txt`: Development, debugging, verification
- `input.txt`: Final solution, actual answer
- `part1.py`: First part solution
- `part2.py`: Second part solution (often extends part1)

### Switching Between Files
Update the `inputPath` variable:
```python
inputPath = scriptPath + '/test.txt'  # Development
inputPath = scriptPath + '/input.txt'  # Production
```
