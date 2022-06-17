""" 
Trie based autocomplete

Input: python autocomplete.py '<query>' 'term1' 'term2' ... 
Output: prints out relevant terms to the query

Future improvements:
> Create a maximum length for the output terms
> Use a corpus of terms instead of a list of terms. 
    >This perhaps: https://github.com/first20hours/google-10000-english
        >no curse words :^)
    >Depending on query length, use different corpus
    >Return n most similar terms to the query
> Implement a visualisation

"""

import sys

from dataclasses import dataclass

@dataclass
class Node():
    def __init__(self):
        self.leaves = {}
        self.last: bool = False

class Trie():
    def __init__(self):
        self.root = Node()
    
    def create_trie(self, terms):
        for i in terms:
            self.add_term(i)
    
    def add_term(self, term):
        node = self.root
        for a in term:
            if a not in node.leaves:
                node.leaves[a] = Node()
            node = node.leaves[a]
        node.last = True
    
    def predict(self, node, term):
        if node.last:
            print(term)
        
        for a, n in node.leaves.items():
            self.predict(n, term + a)
    
    def autopredict(self, query):
        node = self.root
        
        for i in query:
            if not node.leaves.get(i):
                return
            node = node.leaves[i]
        
        if not node.leaves:
            return
    
        self.predict(node, query)
        return
        
def main():
    terms = []
    for i in sys.argv[2:]:
        terms.append(i)
        
    predictor = Trie()
    predictor.create_trie(terms)
    
    predictor.autopredict(sys.argv[1])

if __name__ == "__main__":
    main()