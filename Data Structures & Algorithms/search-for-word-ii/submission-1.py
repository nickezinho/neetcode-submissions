class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Armazena a palavra completa no nó final

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Construir a Trie com todas as palavras
        root = TrieNode()
        for w in words:
            node = root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w  # Marca o final da palavra
        
        ROWS, COLS = len(board), len(board[0])
        res = []
        
        # 2. Função de Backtracking usando o Tabuleiro e a Trie simultaneamente
        def dfs(r, c, node):
            char = board[r][c]
            curr_node = node.children[char]
            
            # Se encontramos uma palavra, adicionamos ao resultado
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # Evita duplicados no resultado
            
            # Marca a célula atual como visitada alterando o caractere
            board[r][c] = "#"
            
            # Explora as 4 direções adjacentes (Cima, Baixo, Esquerda, Direita)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    board[nr][nc] in curr_node.children):
                    dfs(nr, nc, curr_node)
            
            # Backtracking: restaura o caractere original da célula
            board[r][c] = char
            
            # Otimização (Pruning): remove nós folhas vazios para acelerar a busca
            if not curr_node.children:
                node.children.pop(char)

        # 3. Iniciar a busca a partir de cada célula do tabuleiro
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)
                    
        return res

        
        # This one i get it... kinda
        # words = set(words)
        # ret_words = []

        # m, n = len(board), len(board[0])

        # def dfs(i, j, st):
        #     letter = board[i][j]
        #     st += letter
        #     if st in words: 
        #         ret_words.append(st)
        #         words.remove(st)
            
        #     board[i][j] = '#'

        #     for i_off, j_off in [(-1,0), (0,1), (1,0), (0,-1)]:
        #         r, c = i + i_off, j + j_off
        #         if 0 <= r < m and 0 <= c < n and board[r][c] != '#':
        #             dfs(r, c, st)
            
        #     board[i][j] = letter
        # for i in range(m):
        #     for j in range(n):
        #         dfs(i, j, '')
        # return ret_words
