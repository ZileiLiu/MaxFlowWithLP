def create_lp_matrices(net_flow, source=0, sink=None):
    n = len(net_flow)  # Number of nodes
    if sink is None:
        sink = n - 1  # Default sink is the last node
    
    # Objective function coefficients (c)
    c = [0] * (n * n)
    
    # For maximizing flow from source to sink
    for j in range(n):
        if source != j:
            c[source * n + j] = 1  # Maximize flow from source
    
    # Constraints matrix (A)
    A = []
    b = []
    
    # Flow conservation constraints (for each node except for source and sink)
    for i in range(1, n-1):
        row = [0] * (n * n)
        # Outflow from node i
        for j in range(n):
            if i != j:
                row[i * n + j] = 1
        # Inflow to node i
        for j in range(n):
            if i != j:
                row[j * n + i] = -1
        A.append(row)
        b.append(0) 

        # add the same constraints in the opposite way
        row_opposite = [-x for x in row]
        A.append(row_opposite)
        b.append(0)
    
    # Capacity constraints for each edge
    for i in range(n):
        for j in range(n):
            if i != j:
                row = [0] * (n * n)
                row[i * n + j] = 1
                A.append(row)
                b.append(net_flow[i][j])
    
    return c, A, b

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
    c, A, b = create_lp_matrices(net_flow_1)
    print("Objective function coefficients (c):")
    print(c)

    print("\nConstraints matrix (A):")
    for i, row in enumerate(A):
        print(f"Row {i + 1}: {row}")

    print("\nRight-hand side vector (b):")
    print(b)

if __name__ == "__main__":
    main()
