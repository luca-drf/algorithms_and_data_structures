#ifndef LIGHT_QUEUE_H
#define LIGHT_QUEUE_H

#include <vector>
#include <memory>
#include <stdexcept>


using std::vector;
using std::shared_ptr;
using std::make_shared;


template <typename T>
struct node {
    T data;
    shared_ptr<node> next;

    node(T data, shared_ptr<node> next):
        data(data), next(next){}
};


template <typename T>
class lightQueue {
    public:
        shared_ptr<node<T> > head;
        shared_ptr<node<T> > tail;

        lightQueue ();
        ~lightQueue ();

        void enqueue (vector<T> vec);
        void enqueue (T elem);
        
        T dequeue ();
        bool is_empty ();
};

#include "light_queue.cpp"

#endif
