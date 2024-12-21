#ifndef TRIE_H
#define TRIE_H

#include <iostream>
#include <unordered_map>
#include <string>

class TrieNode {
public:
    std::unordered_map<char, TrieNode*> children;
    bool isEndOfWord;

    TrieNode() : isEndOfWord(false) {}
};

class Trie {
private:
    TrieNode* root;

    void displayHelper(TrieNode* node, const std::string& prefix) const {
        if (node->isEndOfWord) {
            std::cout << prefix << std::endl;
        }
        for (const auto& child : node->children) {
            displayHelper(child.second, prefix + child.first);
        }
    }

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(const std::string& word) {
        TrieNode* current = root;
        for (char c : word) {
            if (current->children.find(c) == current->children.end()) {
                current->children[c] = new TrieNode();
            }
            current = current->children[c];
        }
        current->isEndOfWord = true;
    }

    bool search(const std::string& word) const {
        TrieNode* current = root;
        for (char c : word) {
            if (current->children.find(c) == current->children.end()) {
                return false;
            }
            current = current->children[c];
        }
        return current->isEndOfWord;
    }

    void display() const {
        displayHelper(root, "");
    }

    ~Trie() {
        // Implementar la lógica de liberación de memoria si es necesario
    }
};

#endif // TRIE_H
