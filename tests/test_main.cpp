#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE Main

// The boost unit tests have some unused variables, so suppress the warnings about that.
#pragma GCC diagnostic ignored "-Wunused-variable"

#include <boost/test/included/unit_test.hpp>

//JAZ Nothing needs to go here - the test module definitions above create a main function.
