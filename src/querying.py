from src.utils import get_all_permutations


class TrieNode:
    """
    This class is the main class of nodes that are used in Trie class
    ...
    Attributes:
    ----------
    char: str
        character that is in node
    is_end: bool
        this attribute determines if the current node is the end of a word or not.
    children: dict
        this attribute contains the children nodes of a node.

    Methods:
    -------
    Methods defined here:
        __init__(self, char):
            Constructor will set initial attribute, char.
            :parameter
            ---------
            char:str
                the character which is in current node.
            :return
                None
        __repr__(self):
            represents the instance of node as the char attribute.
        __str__(self):
            print the instance of node as the char attribute.
    """

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}

    def __repr__(self):
        return self.char

    def __str__(self):
        return self.char


class Trie(object):
    """
    This class is the prefix tree, Or Trie. This tree contains nodes that each is a character and have children as the
    next character. In this tree, words are the nodes that their is_end attributes are True.
    ...
    Attributes:
    ----------
    root: TrieNode
        Root of the whole tree.

    Methods:
    -------
    Methods defined here:
        __init__(self):
            Constructor will create the root by TrieNode object.
            :parameter
                None
            :return
                None
        insert(self, word):
            This function insert a word into the tree. It first sets the current node to root of the tree,
            then loop over the characters of the word, and if the current char exists in children of the current node,
            sets the current node to that child, and else, it create a new_node by the current char and add it to the
            children of the current node. And after the loop, the is_end attribute of the last node will set to True.
            :parameter
                - word:str
                    the word you want to insert into the tree.
            :return
                The last node which is the end of the word.
        _dfs(self, node, prefix, result=[]):
            This function get a node(root of a tree or subtree) and a prefix, then return all words that contain the
            given prefix in the result argument.

            :parameter
                - node:TrieNode
                    the node to start with
                - prefix:str
                    the current prefix, for tracing a
                    word while traversing the trie
                - result:list
                    the list that the function will add all words into it.
            :return
                return all words that contain the given prefix in the given tree.

        dfs_helper(self, node, prefix):
            this function is a helper function for _dfs, because the _dfs function store results in its parameter.
            :parameter
                - node:TrieNode
                    the node to start with
                - prefix:str
                    the current prefix, for tracing a
                    word while traversing the trie
            :return
                return all words that contain the given prefix in the given tree.

        print_all_words(self):
            this function will print all words of a Trie.
            :parameter
                None
            :return
                None
        query(self, x:str):
            This function is as same as the dfs_helper function, but first check if the given word is in trie or not, then
            call the the dfs_helper with the root node and return all words contain x as prefix(include x if there exist).
            :parameter
                - x:str
                    the given word or prefix
            :return
                return all words contain x as prefix(include x if there exist).
    """

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")

    def insert(self, word):
        """
        This function insert a word into the tree. It first sets the current node to root of the tree,
        then loop over the characters of the word, and if the current char exists in children of the current node,
        sets the current node to that child, and else, it create a new_node by the current char and add it to the
        children of the current node. And after the loop, the is_end attribute of the last node will set to True.
            :parameter
                - word:str
                    the word you want to insert into the tree.
            :return
                The last node which is the end of the word.
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        return node

    def _dfs(self, node, prefix, result=[]):
        """
        This function get a node(root of a tree or subtree) and a prefix, then return all words that contain the
        given prefix in the result argument.
            :parameter
                - node:TrieNode
                    the node to start with
                - prefix:str
                    the current prefix, for tracing a
                    word while traversing the trie
                - result:list
                    the list that the function will add all words into it.
            :return
                 return all words that contain the given prefix in the given tree.
        """
        if node.is_end:
            # result.append(node)
            result.append(prefix + node.char)

        for child in node.children.values():
            self._dfs(child, prefix + node.char, result)

    def dfs_helper(self, node, prefix):
        """
        this function is a helper function for _dfs, because the _dfs function store results in its parameter.
            :parameter
                - node:TrieNode
                    the node to start with
                - prefix:str
                    the current prefix, for tracing a
                    word while traversing the trie
            :return
                return all words that contain the given prefix in the given tree.
        """
        result = []
        self._dfs(node, prefix, result=result)
        return result

    def print_all_words(self):
        """
        print_all_words(self):
            this function will print all words of a Trie.
            :parameter
                None
            :return
                None
        """
        for word in sorted(self.dfs_helper(self.root, '')):
            print(word)

    def query(self, x: str):
        """
        This function is as same as the dfs_helper function, but first check if the given word is in trie or not, then
        call the the dfs_helper with the root node and return all words contain x as prefix(include x if there exist).
        :parameter
            - x:str
                the given word or prefix
        :return
            return all words contain x as prefix(include x if there exist).
        """
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        result = self.dfs_helper(node, x[:-1])
        return sorted(result)


class QueryProcessor:
    """
    In this class, I implement an information retrieval system which can search a query among documents.
    ...
    Attributes:
    -----------
    indexing_model: InvertedIndex
        an instance of InvertedIndex class which has been created by indexing documents.
    Methods
    -------
    Methods defined here:
        get_word_docs(self, word: str):
                this simple function gets a token and will return all index of documents that this token is appeared in.
                :param word:
                    a word that you want to search.
                :return:
                    list of indexes of documents.
        intersect(self, first_word, second_word):
                this function get two words, and find documents that both of these word has been occurred.
                :parameter
                first_word: str
                    first word you want to search
                second_word: str
                    second word you want to search
                :return
                    list of indexes of documents.
            union(self, first_word, second_word):
                this function get two words, and find documents that either each of these word has been occurred.
                :parameter
                first_word: str
                    first word you want to search
                second_word: str
                    second word you want to search
                :return
                    list of indexes of documents.
            not_in(self, word):
                this function get one word, and find documents that this word has been not occurred.
                :parameter
                word: str
                    the word you want to search
                :return
                    list of indexes of documents.
            near(self, first_word, second_word, length):
                this function get two words, and find documents that either each of these word has been occurred near by at most 3 words on left or right.
                :parameter
                first_word: str
                    first word you want to search
                second_word: str
                    second word you want to search
                :return
                    list of indexes of documents.
            search(self, query):
                this function get a query and recognize what kind of query is; then search the query.
                :parameter
                    query: str
                        the query that user wants to search
                :return
                    print list of indexes of documents in a pretty way.
    """

    def __init__(self, indexing_model):
        self.indexing_model = indexing_model
        self.prefix_trie: Trie = Trie()

    def get_word_docs(self, word):
        t = self.indexing_model.get_token(word)
        result = set()
        for doc in t.docs:
            result.add(doc['doc_idx'])
        return result

    def create_prefix_trie(self):
        """
        This functions should run after create_posting_list to add all words to prefix_trie to create it.
        :return:
            None
        """
        if self.indexing_model.posting_list:
            for token in self.indexing_model.posting_list:
                # Add permuterms
                permuterms = get_all_permutations(token.word + '$')
                for term in permuterms:
                    node = self.prefix_trie.insert(term)
        else:
            raise Exception("You should first create posting list")

    def wildcard_query(self, token: str):
        """
        This function gets a token that contain * and return matched word.
        If there is just one *, it will add a '$' at the end of the word, and then permutate it such that the * pose on
        the end of the string, and then search it in prefix_trie and will return the all match tokens.
        If there are two *, it convert two * and the characters between these two into one *. Then do the same thing for
        having one *. And from resulted matched, it search if they have the sequence characters of between two * in the
        input token.
        :param token:
            the token that has * and you wants to get all matches.
        :return:
            return all matches
        """
        if token.count('*') == 1:
            star_idx = token.index('*')
            result_tokens = self.prefix_trie.query(token[star_idx + 1:] + token[0:star_idx])
            for i, word in enumerate(result_tokens):
                dollar_idx = word.index('$')
                result_tokens[i] = word[dollar_idx + 1:] + word[0:dollar_idx]
            return result_tokens

        elif token.count('*') == 2:
            star1_idx = token.index('*')
            star2_idx = token.index('*', star1_idx + 1)
            result_tokens = self.prefix_trie.query(token[star2_idx + 1:] + token[0:star1_idx])
            for i, word in enumerate(result_tokens):
                dollar_idx = word.index('$')
                result_tokens[i] = word[dollar_idx + 1:] + word[0:dollar_idx]
            # print(result_tokens)
            result = []
            for word in result_tokens:
                if token[star1_idx + 1:star2_idx] in word:
                    result.append(word)
            return result
        else:
            raise Exception("Query is not valid")

    def intersect(self, first_word, second_word):
        docs1 = self.get_word_docs(first_word)
        docs2 = self.get_word_docs(second_word)
        return set(docs1 & docs2)

    def union(self, first_word, second_word):
        docs1 = self.get_word_docs(first_word)
        docs2 = self.get_word_docs(second_word)
        return set(docs1 | docs2)

    def not_in(self, word):
        all_docs = set(range(len(self.indexing_model.documents)))
        word_docs = self.get_word_docs(word)
        return set(all_docs - word_docs)

    def near(self, first_word, second_word, distance):
        result = set()
        t1 = self.indexing_model.get_token(first_word)
        t2 = self.indexing_model.get_token(second_word)
        for t in (t1, t2):
            for doc in t.docs:
                for idx in doc['indexes']:
                    if second_word in self.indexing_model.documents[doc["doc_idx"]][idx + 1:idx + 1 + distance]:
                        result.add(doc['doc_idx'])
        return set(result)

    def search(self, query):
        query_parts = query.lower().split()
        if len(query_parts) > 2:
            if '*' not in query_parts[0]:
                query_parts[0] = [query_parts[0]]
            if '*' not in query_parts[2]:
                query_parts[2] = [query_parts[2]]
            if '*' in query_parts[0]:
                query_parts[0] = self.wildcard_query(query_parts[0] + '$')
            if '*' in query_parts[2]:
                query_parts[2] = self.wildcard_query(query_parts[1] + '$')
        if len(query_parts) == 1:
            if '*' in query_parts[0]:
                query_parts[0] = self.wildcard_query(query_parts[0] + '$')
            else:
                query_parts[0] = [query_parts[0]]
            result = self.get_word_docs(query_parts[0][0])
            for token1 in query_parts[0]:
                result = result.union(self.get_word_docs(token1))
            return result
        elif 'and' in query_parts:
            result = set()
            for token1 in query_parts[0]:
                for token2 in query_parts[2]:
                    result = result.union(self.intersect(token1, token2))
            return result
        elif 'or' in query_parts:
            result = set()
            for token1 in query_parts[0]:
                for token2 in query_parts[2]:
                    result = result.union(self.union(token1, token2))
            return result
        elif 'not' in query_parts:
            if '*' in query_parts[0]:
                query_parts[1] = self.wildcard_query(query_parts[1] + '$')
            else:
                query_parts[1] = [query_parts[1]]
            result = self.not_in(query_parts[1][0])
            for token1 in query_parts[1]:
                result = result.intersection(self.not_in(token1))
            return result
        elif 'near' in query:
            distance = int(query_parts[1].split('/')[1])
            result = set()
            for token1 in query_parts[0]:
                for token2 in query_parts[2]:
                    result = result.union(self.near(token1, token2, distance=distance))
            return self.near(query_parts[0], query_parts[2], distance)
        else:
            return list(self.get_word_docs(query_parts[0]))
