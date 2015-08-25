#include <vector>
#include <string>
#include <stdexcept>

#include "gtest/gtest.h"

#include "light_queue.h"

using std::vector;
using std::string;


class LQTest : public ::testing::Test
{
protected:
    // You can remove any or all of the following functions if its body
    // is empty.

    LQTest() {
        // You can do set-up work for each test here.
    }

    virtual ~LQTest() {
        // You can do clean-up work that doesn't throw exceptions here.
    }

    // If the constructor and destructor are not enough for setting up
    // and cleaning up each test, you can define the following methods:

    virtual void SetUp() {
        // Code here will be called immediately after the constructor (right
        // before each test).

    }

    virtual void TearDown() {
        // Code here will be called immediately after each test (right
        // before the destructor).
    }

    // Objects declared here can be used by all tests in the test case.
};

TEST_F(LQTest, isEmpty) 
{
    lightQueue<string> empty;
    ASSERT_EQ( empty.is_empty(), true );
}

TEST_F(LQTest, queueTest) 
{
    lightQueue<string> queue; 
    queue.enqueue("a");
    ASSERT_EQ( queue.is_empty(), false );    
    ASSERT_EQ( queue.dequeue(), "a" );
    ASSERT_EQ( queue.is_empty(), true );

    vector<string> vec = {"c", "d", "e"};
    queue.enqueue(vec);
    ASSERT_EQ( queue.is_empty(), false );    
    for (auto s : vec) {
        ASSERT_EQ( queue.dequeue(), s );
    }
    ASSERT_EQ( queue.is_empty(), true );
}

TEST_F(LQTest, popEmpty) 
{
    lightQueue<string> empty;
    ASSERT_THROW( empty.dequeue(), std::out_of_range );
}
