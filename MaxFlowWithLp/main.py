from MaxFlowModelling import create_lp_matrices
from LpSolverSimplex import simplex

def list_to_matrix(flat_list):
    import math
    
    n = int(math.sqrt(len(flat_list)))  # Determine the size of the matrix
    matrix = []

    for i in range(n):
        row = flat_list[i*n:(i+1)*n]
        matrix.append(row)
    
    return matrix

def print_matrix_1(matrix):
    n = len(matrix)
    print("   " + " ".join(f"{j:>6}" for j in range(n)))
    for i, row in enumerate(matrix):
        formatted_row = " ".join(f"{value:>6.1f}" if isinstance(value, float) else f"{value:>6}" for value in row)
        print(f"{i:>2} [{formatted_row}]")

def print_matrix_2(matrix):
    n = len(matrix)
    print("   " + " ".join(f"{j+1:>6}" for j in range(n)))  # Column indices start from 1
    for i, row in enumerate(matrix):
        formatted_row = " ".join(f"{value:>6.1f}" if isinstance(value, float) else f"{value:>6}" for value in row)
        print(f"{i+1:>2} [{formatted_row}]")  # Row indices start from 1

def test(net_flow):
    c, A, b = create_lp_matrices(net_flow)
    solution, objective_value = simplex(c, A, b)
    print("Solution:")
    solution_matrix = list_to_matrix(solution)  
    if (len(solution) > 40):
        print_matrix_2(solution_matrix)
    else:
        print_matrix_1(solution_matrix)
    print(f"Objective Value: {objective_value}")
    return solution, objective_value


def main():
    # Example usage
    net_flow_1 = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 0, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0],
        ]
    net_flow_2 = [
        [0, 2000, 1600, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 250, 3000, 1000, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1000, 400, 0, 0],
        [0, 0, 0, 0, 2000, 2000, 3000, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2000, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2000, 0, 0, 0, 1500],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1200],
        [0, 0, 0, 0, 0, 0, 0, 0, 1000, 1600, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 500, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 500],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    print("Test 1:")
    test(net_flow_1)
    print("\nTest 2:")
    test(net_flow_2)

if __name__ == "__main__":
    main()
