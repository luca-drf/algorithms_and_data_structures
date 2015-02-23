#include <vector>
#include <string>
#include <unordered_map>

#include "gtest/gtest.h"

#include "bfs.h"

using std::vector;
using std::unordered_map;
using std::string;


class BFSTest : public ::testing::Test
{
protected:
    // You can remove any or all of the following functions if its body
    // is empty.

    BFSTest() {
        // You can do set-up work for each test here.
    }

    virtual ~BFSTest() {
        // You can do clean-up work that doesn't throw exceptions here.
    }

    // If the constructor and destructor are not enough for setting up
    // and cleaning up each test, you can define the following methods:

    virtual void SetUp() {
        // Code here will be called immediately after the constructor (right
        // before each test).
        graph = {{"a", {"b", "g", "d"}},
                 {"b", {"e", "a", "f"}},
                 {"d", {"a", "f"}},
                 {"g", {"e", "a"}},
                 {"f", {"b", "d", "c"}},
                 {"e", {"b", "g"}},
                 {"c", {"f", "h"}},
                 {"h", {"c"}}};

    }

    virtual void TearDown() {
        // Code here will be called immediately after each test (right
        // before the destructor).
    }

    // Objects declared here can be used by all tests in the test case.
    unordered_map<string, vector<string> > graph;
};


TEST_F(BFSTest, UnitTest) 
{
    auto result = BFS::bfs_traverse<string>(graph, string("a"));
    vector<string> expected = {"a", "b", "d", "g", "e", "f", "c", "h"};
    ASSERT_EQ( expected, result );
}

