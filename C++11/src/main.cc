#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include "bfs.h"


using std::vector;
using std::unordered_map;
using std::string;
using std::cout;
using std::endl;


int main() {
    unordered_map<string, vector<string> > graph = {{"a", {"b", "g", "d"}},
                                                    {"b", {"e", "a", "f"}},
                                                    {"d", {"a", "f"}},
                                                    {"g", {"e", "a"}},
                                                    {"f", {"b", "d", "c"}},
                                                    {"e", {"b", "g"}},
                                                    {"c", {"f", "h"}},
                                                    {"h", {"c"}}};
    auto result = BFS::bfs_traverse<string>(graph, string("a"));

    for (auto i : result) {
        cout << i << endl;
    } 
} 
