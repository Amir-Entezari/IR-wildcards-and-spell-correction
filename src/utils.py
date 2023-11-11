def get_all_permutations(input_str: str):
    """
    this function will generate all circular permutation of a string
    """
    perm_list = []
    n = len(input_str)
    for i in range(n):
        permuterm = input_str[i:n] + input_str[0:i]
        perm_list.append(permuterm)
    return perm_list