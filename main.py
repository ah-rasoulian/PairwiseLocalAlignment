import math

# A dictionary representing PAM250 cores
PAM250 = {
    'A': {'A': 2, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N': 0, 'P': 1,
          'Q': 0, 'R': -2, 'S': 1, 'T': 1, 'V': 0, 'W': -6, 'Y': -3},
    'C': {'A': -2, 'C': 12, 'D': -5, 'E': -5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4,
          'P': -3, 'Q': -5, 'R': -4, 'S': 0, 'T': -2, 'V': -2, 'W': -8, 'Y': 0},
    'D': {'A': 0, 'C': -5, 'D': 4, 'E': 3, 'F': -6, 'G': 1, 'H': 1, 'I': -2, 'K': 0, 'L': -4, 'M': -3, 'N': 2, 'P': -1,
          'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
    'E': {'A': 0, 'C': -5, 'D': 3, 'E': 4, 'F': -5, 'G': 0, 'H': 1, 'I': -2, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': -1,
          'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
    'F': {'A': -3, 'C': -4, 'D': -6, 'E': -5, 'F': 9, 'G': -5, 'H': -2, 'I': 1, 'K': -5, 'L': 2, 'M': 0, 'N': -3,
          'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W': 0, 'Y': 7},
    'G': {'A': 1, 'C': -3, 'D': 1, 'E': 0, 'F': -5, 'G': 5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N': 0, 'P': 0,
          'Q': -1, 'R': -3, 'S': 1, 'T': 0, 'V': -1, 'W': -7, 'Y': -5},
    'H': {'A': -1, 'C': -3, 'D': 1, 'E': 1, 'F': -2, 'G': -2, 'H': 6, 'I': -2, 'K': 0, 'L': -2, 'M': -2, 'N': 2, 'P': 0,
          'Q': 3, 'R': 2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y': 0},
    'I': {'A': -1, 'C': -2, 'D': -2, 'E': -2, 'F': 1, 'G': -3, 'H': -2, 'I': 5, 'K': -2, 'L': 2, 'M': 2, 'N': -2,
          'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -5, 'Y': -1},
    'K': {'A': -1, 'C': -5, 'D': 0, 'E': 0, 'F': -5, 'G': -2, 'H': 0, 'I': -2, 'K': 5, 'L': -3, 'M': 0, 'N': 1, 'P': -1,
          'Q': 1, 'R': 3, 'S': 0, 'T': 0, 'V': -2, 'W': -3, 'Y': -4},
    'L': {'A': -2, 'C': -6, 'D': -4, 'E': -3, 'F': 2, 'G': -4, 'H': -2, 'I': 2, 'K': -3, 'L': 6, 'M': 4, 'N': -3,
          'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': 2, 'W': -2, 'Y': -1},
    'M': {'A': -1, 'C': -5, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 2, 'K': 0, 'L': 4, 'M': 6, 'N': -2,
          'P': -2, 'Q': -1, 'R': 0, 'S': -2, 'T': -1, 'V': 2, 'W': -4, 'Y': -2},
    'N': {'A': 0, 'C': -4, 'D': 2, 'E': 1, 'F': -3, 'G': 0, 'H': 2, 'I': -2, 'K': 1, 'L': -3, 'M': -2, 'N': 2, 'P': 0,
          'Q': 1, 'R': 0, 'S': 1, 'T': 0, 'V': -2, 'W': -4, 'Y': -2},
    'P': {'A': 1, 'C': -3, 'D': -1, 'E': -1, 'F': -5, 'G': 0, 'H': 0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N': 0,
          'P': 6, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -1, 'W': -6, 'Y': -5},
    'Q': {'A': 0, 'C': -5, 'D': 2, 'E': 2, 'F': -5, 'G': -1, 'H': 3, 'I': -2, 'K': 1, 'L': -2, 'M': -1, 'N': 1, 'P': 0,
          'Q': 4, 'R': 1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
    'R': {'A': -2, 'C': -4, 'D': -1, 'E': -1, 'F': -4, 'G': -3, 'H': 2, 'I': -2, 'K': 3, 'L': -3, 'M': 0, 'N': 0,
          'P': 0, 'Q': 1, 'R': 6, 'S': 0, 'T': -1, 'V': -2, 'W': 2, 'Y': -4},
    'S': {'A': 1, 'C': 0, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': 1,
          'Q': -1, 'R': 0, 'S': 2, 'T': 1, 'V': -1, 'W': -2, 'Y': -3},
    'T': {'A': 1, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 0, 'H': -1, 'I': 0, 'K': 0, 'L': -2, 'M': -1, 'N': 0, 'P': 0,
          'Q': -1, 'R': -1, 'S': 1, 'T': 3, 'V': 0, 'W': -5, 'Y': -3},
    'V': {'A': 0, 'C': -2, 'D': -2, 'E': -2, 'F': -1, 'G': -1, 'H': -2, 'I': 4, 'K': -2, 'L': 2, 'M': 2, 'N': -2,
          'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -6, 'Y': -2},
    'W': {'A': -6, 'C': -8, 'D': -7, 'E': -7, 'F': 0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4,
          'P': -6, 'Q': -5, 'R': 2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y': 0},
    'Y': {'A': -3, 'C': 0, 'D': -4, 'E': -4, 'F': 7, 'G': -5, 'H': 0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2,
          'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W': 0, 'Y': 10}
}


class AlignmentMatrixCell:
    def __init__(self):
        self.value = 0
        self.parent = None

    def set_value(self, value):
        self.value = value

    def set_parent(self, parent):
        self.parent = parent


# Gap penalty is considered as 5
GAP_SCORE = -5


def get_gap_penalty(cell1, cell2):
    if cell1[0] == cell2[0]:
        return GAP_SCORE * math.fabs(cell1[1] - cell2[1])
    elif cell1[1] == cell2[1]:
        return GAP_SCORE * math.fabs(cell1[0] - cell2[0])
    else:
        return 0


# printing the matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(int(matrix[i][j].value), end="\t")
        print()
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j].parent, end="\t")
        print()


def main():
    # getting 2 protein sequences
    first_protein = input().upper()
    second_protein = input().upper()

    x = len(first_protein)
    y = len(second_protein)

    # creating the alignment matrix
    alignment_matrix = []
    for i in range(x + 1):
        matrix_row = []
        for j in range(y + 1):
            matrix_row.append(AlignmentMatrixCell())
        alignment_matrix.append(matrix_row)

    maximum_cell_location = None

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            # print("i, j", i, j)  # --------------------------
            match_score = PAM250.get(first_protein[i - 1]).get(second_protein[j - 1]) + alignment_matrix[i - 1][j - 1] \
                .value
            # print("match-score: ", match_score)  # ---------------------
            potential_parent_left = None
            max_value_left = -math.inf
            for column in range(j):
                if alignment_matrix[i][column].value + get_gap_penalty((i, column), (i, j)) >= max_value_left:
                    max_value_left = alignment_matrix[i][column].value + get_gap_penalty((i, column), (i, j))
                    potential_parent_left = (i, column)
            # print("left: ", max_value_left, " p: ", potential_parent_left)  # --------------------
            potential_parent_top = None
            max_value_top = -math.inf
            for row in range(i):
                if alignment_matrix[row][j].value + get_gap_penalty((row, j), (i, j)) >= max_value_top:
                    max_value_top = alignment_matrix[row][j].value + get_gap_penalty((row, j), (i, j))
                    potential_parent_top = (row, j)
            # print("top: ", max_value_top, " p: ", potential_parent_top)  # -----------------------
            # desired order is handled here
            if max_value_left >= max(match_score, max_value_top, 0):
                alignment_matrix[i][j].set_value(max_value_left)
                alignment_matrix[i][j].set_parent(potential_parent_left)
            elif max_value_top >= max(match_score, max_value_left, 0):
                alignment_matrix[i][j].set_value(max_value_top)
                alignment_matrix[i][j].set_parent(potential_parent_top)
            elif match_score >= max(max_value_left, max_value_top, 0):
                alignment_matrix[i][j].set_value(match_score)
                alignment_matrix[i][j].set_parent((i - 1, j - 1))
            # maximum is zero -> no parent will be set
            else:
                alignment_matrix[i][j].set_value(0)

            # now set maximum cell to find it in O(1)
            if maximum_cell_location is None:
                maximum_cell_location = (i, j)
            else:
                if alignment_matrix[i][j].value >= alignment_matrix[maximum_cell_location[0]][maximum_cell_location[1]] \
                        .value:
                    maximum_cell_location = (i, j)

    # print_matrix(alignment_matrix)  # -----------------------------

    # print maximum alignment score
    print(int(alignment_matrix[maximum_cell_location[0]][maximum_cell_location[1]].value))
    # now trace back to find alignment
    first_protein_alignment = ""
    second_protein_alignment = ""

    traced_cell = alignment_matrix[maximum_cell_location[0]][maximum_cell_location[1]]
    current_location = maximum_cell_location
    while traced_cell.parent is not None:
        # stop traceback when it reached a score 0 in matrix
        if alignment_matrix[current_location[0]][current_location[1]].value == 0:
            break

        if traced_cell.parent[0] == current_location[0]:  # they are in the same row
            for k in range(current_location[1] - traced_cell.parent[1]):
                first_protein_alignment = "-" + first_protein_alignment
                second_protein_alignment = second_protein[current_location[1] - k - 1] + second_protein_alignment
        elif traced_cell.parent[1] == current_location[1]:  # they are in the same column
            for k in range(current_location[0] - traced_cell.parent[0]):
                second_protein_alignment = "-" + second_protein_alignment
                first_protein_alignment = first_protein[current_location[0] - k - 1] + first_protein_alignment
        else:  # match or miss-match has happened
            first_protein_alignment = first_protein[current_location[0] - 1] + first_protein_alignment
            second_protein_alignment = second_protein[current_location[1] - 1] + second_protein_alignment

        current_location = traced_cell.parent
        traced_cell = alignment_matrix[traced_cell.parent[0]][traced_cell.parent[1]]

    # printing alignments
    # we have to reverse to sequences cause we fill that from end
    print(first_protein_alignment)
    print(second_protein_alignment)


if __name__ == '__main__':
    main()
