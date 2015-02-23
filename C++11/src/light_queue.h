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

template <typename T>
lightQueue<T>::lightQueue():
    head(nullptr),
    tail(nullptr)
{}

template <typename T>
lightQueue<T>::~lightQueue() {}

template <typename T>
void lightQueue<T>::enqueue(vector<T> vec) {
    for (auto obj : vec){
        if (head) {
            tail->next = make_shared<node<T> >(obj, nullptr);
            tail = tail->next;
        }
        else {
            tail = make_shared<node<T> >(obj, nullptr);
            head = tail;

        }
    }
}

template <typename T>
void lightQueue<T>::enqueue(T elem) {
    if (head) {
        tail->next = make_shared<node<T> >(elem, nullptr);
        tail = tail->next;
    }
    else {
        tail = make_shared<node<T> >(elem, nullptr);
        head = tail;

    }
}

template <typename T>
T lightQueue<T>::dequeue() {
    if (head) {
        auto popped = head;
        head = popped->next;
        return popped->data;
    }
    else {
        throw std::out_of_range("Popping from empty queue");
    }
}

template <typename T>
bool lightQueue<T>::is_empty() {
    if (head)
        return false;
    else
        return true;
}

#endif
