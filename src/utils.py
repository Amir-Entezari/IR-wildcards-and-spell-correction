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


def edit_distance(word1: str, word2: str):
    """
    this function will calculate the distance of between two word. The distance means the total number of operation
    that we need to convert each word to other
    :param word1: str
        first word you want to calculate distance of with another
    :param word2:
        second word you want to calculate distance of with another
    :return:
        the edit distance of between word1 and word2
    """
    dp = [[0 for j in range(len(word2))] for i in range(len(word1))]
    for i in range(1, len(word1)):
        dp[i][0] = i
    for j in range(1, len(word2)):
        dp[0][j] = j
    for i in range(1, len(word1)):
        for j in range(1, len(word2)):
            dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i] == word2[j] else 1),
                           dp[i - 1][j] + 1,
                           dp[i][j - 1] + 1)
    return dp[-1][-1]
