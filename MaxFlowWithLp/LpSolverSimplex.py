def simplex(c, A, b):

    num_vars = len(c)
    num_constraints = len(b)

    tableau = []

    # Step 1: 
    for coefficients, rhs_value in zip(A, b):
        slack_variables = [0] * num_constraints
        tableau_row = coefficients + slack_variables + [rhs_value]
        tableau.append(tableau_row)

    # Step 2: 
    negated_objective_coefficients = []
    for coeff in c:
        negated_coeff = -coeff
        negated_objective_coefficients.append(negated_coeff)
    objective_function_row = negated_objective_coefficients + [0] * (num_constraints + 1)
    tableau.append(objective_function_row)

    # Adding the identity matrix to form slack variables
    for i in range(num_constraints):
        tableau[i][num_vars + i] = 1

    def pivot(pivot_row_index, pivot_col_index):
        pivot_element = tableau[pivot_row_index][pivot_col_index]        
        if pivot_element == 0:
            raise ValueError("Pivot element is zero, which is not allowed.")

        # Step 1: Normalize the pivot row
        normalized_pivot_row = []
        for element in tableau[pivot_row_index]:
            normalized_element = element / pivot_element
            normalized_pivot_row.append(normalized_element)
        tableau[pivot_row_index] = normalized_pivot_row

        # Step 2: Eliminate the pivot column in all other rows
        for row_index in range(len(tableau)):
            if row_index != pivot_row_index:
                pivot_col_value = tableau[row_index][pivot_col_index]
                updated_row = []
                for col_index, current_row_element in enumerate(tableau[row_index]):
                    updated_element = current_row_element - (pivot_col_value * normalized_pivot_row[col_index])
                    updated_row.append(updated_element)
                tableau[row_index] = updated_row

    # Simplex iterations
    while True:
        # Find the pivot column (most negative value in the last row)
        num_decision_vars = len(tableau[0]) - 1
        pivot_col = 0
        for col_index in range(1, num_decision_vars):
            current_coefficient = tableau[-1][col_index]
            if current_coefficient < tableau[-1][pivot_col]:
                pivot_col = col_index

        # Optimal reached checking
        if tableau[-1][pivot_col] >= 0:
            break

        # Find the pivot row
        ratios = []
        for r in range(num_constraints):
            if tableau[r][pivot_col] > 0:
                ratio = tableau[r][-1] / tableau[r][pivot_col]
                ratios.append((ratio, r))
        if not ratios:
            raise ValueError("The problem is unbounded.")

        # Find the row with the smallest ratio, which is the pivot row
        pivot_row = min(ratios)[1]

        # Perform the pivot operation
        pivot(pivot_row, pivot_col)

    # Extract solution
    solution = [0] * num_vars
    for i in range(num_vars):
        col = [row[i] for row in tableau[:-1]]
        if col.count(1) == 1 and col.count(0) == num_constraints - 1:
            solution[i] = tableau[col.index(1)][-1]

    optimal_value = tableau[-1][-1]
    return solution, optimal_value

def main():
    # Example usage
    A = [
        [1, 1],
        [5, 2]
        ]
    c = [40, 30]
    b = [11, 40]
    solution, optimal_value = simplex(c, A, b)
    print(f"Optimal solution: x1 = {solution[0]:.1f}, x2 = {solution[1]:.1f}")
    print(f"Optimal value: {optimal_value:.1f}")

if __name__ == "__main__":
    main()
