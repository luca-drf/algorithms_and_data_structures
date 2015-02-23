#ifndef BFS_H
#define BFS_H

#include <vector>
#include <unordered_map>
#include <algorithm>
#include "light_queue.h"

using std::vector;
using std::unordered_map;

namespace BFS {
    template <typename T>
    void initialize(unordered_map<T, vector<T> > graph,
                    unordered_map<T, bool> visited);

    template <typename T>
    vector<T> bfs_traverse(unordered_map<T, vector<T> > graph, T start);
}

template <typename T>
void BFS::initialize(unordered_map<T, vector<T> > graph,
                unordered_map<T, bool> visited) {
    for (auto i : graph) {
        visited.emplace(i.first, false);
    }
}

template <typename T>
vector<T> BFS::bfs_traverse(unordered_map<T, vector<T> > graph, T start) {
    lightQueue<T> queue;
    unordered_map<T, bool> visited;
    vector<T> result;
    result.reserve(graph.size());
    initialize<T>(graph, visited);
    
    queue.enqueue(start);
    visited[start] = true;
    result.push_back(start);

    while (!queue.is_empty()) {
        auto cur_node = queue.dequeue();
        auto neighbours = graph[cur_node];
        vector<T> to_sort;
        to_sort.reserve(neighbours.size());

        for (auto node : neighbours) {
            if (!visited[node]) {
                to_sort.push_back(node);
                visited[node] = true;
            }
        }
        std::sort(to_sort.begin(), to_sort.end());
        queue.enqueue(to_sort);
        result.insert(result.end(), to_sort.begin(), to_sort.end());
    }
    return result;
}
#endif
