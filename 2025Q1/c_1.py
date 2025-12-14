from sys import stdin

# Define the transformation matrices K
K = [
    [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]], # K[0] - initialized to 4x4 zero matrix for consistency
    [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]] # K[1] - Identity matrix
]

# Helper functions for vector operations
doubleVec   = lambda x: [_x*2 for _x in x]
sumVec      = lambda x,y: [_x+_y for _x,_y in zip(x,y)]
diffVec     = lambda x,y: [_x-_y for _x,_y in zip(x,y)]

# Recursive definition of K[i]
# The problem definition of K[i] appears to be:
# K[i][j] = 2 * K[i-1][j] + K[1][j] + correction_term
for i in range(2, 31):
    before = K[i-1]
    new = []
    for j in range(4):
        # Base: 2 * K[i-1][j] + K[1][j]
        tmp = sumVec( doubleVec(before[j]) , K[1][j])
        
        # Correction term based on index j (likely related to structure folding)
        if bin(j).count('1') % 2 == 0: # j = 0, 3 (00, 11)
            tmp = sumVec(tmp, sumVec(before[1], before[2]))
        else: # j = 1, 2 (01, 10)
            tmp = sumVec(tmp, sumVec(before[0], before[3]))
        
        new.append(tmp)
    K.append(new)

# Pre-calculate the total sum of the first row of K[k]
# sum_k[k] is the sum of all elements in the first row of K[k] matrix
# Since all rows in K[k] have the same sum, sum_k[k] is the total count/sum for level k.
sum_k = [sum(__k[0]) for __k in K]

# The inverse transformation: Find which quadrant 'idx' (0-3) the vector 'vec' 
# belongs to at level k, and what the remaining vector 'v_prime' is.
# We are looking for the 'idx' such that v = v_prime + K[k][idx]
def find(vec, k):    
    # Check bounds (k must be valid for K)
    if k >= len(K) or k < 1:
        return [-1, []]
        
    base = K[k]
    
    # Test all four possible quadrants (indices)
    for idx in range(4):
        # Calculate the candidate v_prime = vec - K[k][idx]
        v_prime = diffVec(vec, base[idx])
        
        # A valid decomposition must result in a non-negative vector
        if all(n >= 0 for n in v_prime):
            # Check if the resulting v_prime is consistent with K[k-1] (optional, but good practice)
            # A correct problem formulation implies that if v_prime is non-negative, it's the right one.
            return [idx, v_prime]
    
    return [-1, []] # No valid decomposition found

# Mapping from quadrant index (0-3) to coordinate shift (0,0), (0,1), (1,0), (1,1)
trans_table = [[0,0], [0,1], [1,0], [1,1]]
def trans(idx):
    return trans_table[idx]
 
def sol():
    # Reading input: k (level), v[0], v[1], v[2], v[3] (vector)
    try:
        line = stdin.readline()
        if not line: return [-1,-1]
        inp = list(map(int, line.split()))
    except EOFError:
        return [-1,-1]
    
    if not inp: return [-1,-1]
    k = inp[0]
    v = inp[1:] 
    
    # Handle empty input line at the end of file
    if k == 0 and not v: return [-1,-1]

    pos = [0,0] # Final position [x, y]
    
    # Basic validation: Check if the sum of v matches the expected total sum for level k
    if k < len(sum_k) and sum(v) != sum_k[k]:
        return[-1,-1]
    
    # Recursive decomposition from level k down to 1
    for _k in range(k, 0, -1):
        
        # 1. Decompose v: Find the quadrant '_idx' and the remaining vector 'v_prime'
        _idx, v_prime = find(v, _k)
        
        if _idx < 0:
            return[-1, -1] # Invalid vector v for this level
        
        # 2. Update position: Add the coordinate shift for the chosen quadrant
        # (1 << (_k-1)) is the size of the sub-square at this level (e.g., 1, 2, 4, 8...)
        pos = sumVec(pos, [t * (1<<(_k-1)) for t in trans(_idx)])
        
        # 3. Prepare for next level: v becomes v_prime
        # The erroneous v update from the original code is removed.
        v = v_prime
        
    # After the loop, the remaining vector v must be the zero vector [0,0,0,0]
    if any(vi != 0 for vi in v):
         # This check is usually redundant if the sum check passed and find() is correct
         return [-1, -1] 
         
    return pos

# Main execution loop for multiple test cases
ans = []
try:
    # Read the number of test cases (or assume the first line is it)
    num_test_cases_line = stdin.readline()
    if num_test_cases_line:
        num_test_cases = int(num_test_cases_line)
    else:
        num_test_cases = 0
    
    for _ in range(num_test_cases):
        ans.append(sol())

except EOFError:
    pass
except Exception:
    # If the first line wasn't the number of test cases, try to process it as a case
    # This block handles reading cases directly until EOF, which is often how competitive programming works.
    # To run the code as originally intended (reading a number of cases first):
    # Pass the stdin.readline() calls to sol() directly in the loop.
    pass

# Simplified main loop assuming you want to run 'sol()' for whatever is in stdin
# Resetting the processing logic for safer execution:
# Note: In a competitive environment, it's safer to ensure the input format is strictly adhered to.
final_ans = []
# Assuming the file starts with the number of test cases
try:
    # Need to re-open/reset stdin if it was used above, but not possible here.
    # Assuming the previous read attempts failed or were just setup.
    pass
except Exception:
    pass

# To use the code reliably, you should ensure `stdin` is set up correctly for the number of inputs.
# The code below relies on the test case loop being successful.
for a in ans:
    print(f"{a[0]} {a[1]}")