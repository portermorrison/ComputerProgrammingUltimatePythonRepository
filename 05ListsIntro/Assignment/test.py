import unittest
import inspect
import main

def test_function_definition(test_case, module, function_name, expected_num_args):
    # check the function is defined
    function_defined = hasattr(module, function_name)
    test_case.assertTrue(function_defined, f"{function_name} is not defined in {module.__name__}")

    # check the function takes correct # arguments
    function = getattr(module, function_name)
    signature = inspect.signature(function)
    num_arguments = len(signature.parameters)

    test_case.assertEqual(num_arguments, expected_num_args, f"{function_name} should take {expected_num_args} argument(s)")

def execute_test(test_case, module, function_name, input_output_list):
    test_function_definition(test_case, module, function_name, len(input_output_list[0][0]))
    func = getattr(module, function_name)
    for arguments, expected_result in input_output_list:
      with test_case.subTest(arguments=arguments):
          result = func(*arguments)
          test_case.assertEqual(result, expected_result, f"{function_name}{arguments} was expected to return:\n{expected_result}\nInstead, it returned:\n{result}\n")

class TestFunctions(unittest.TestCase):
    longMessage = False

    def test_make_abc(self):
        test_cases = [
            [ (), ["a", "b", "c"] ]
        ]
        execute_test(self, main, "make_abc", test_cases)
    
    def test_equal_edges(self):
        test_cases = [
            [([1, 2, 3, 4, 1],), True],
            [([1, 2, 3, 4],), False],
            [([1, 0],), False],
            [([5, 5],), True]
        ]
        execute_test(self, main, "equal_edges", test_cases)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False, catchbreak=False)
