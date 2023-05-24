def func_executor(*func):
    fumction_name = []
    function_result = []
    for i in func:
        fumction_name.append()
        function_result.append(i[0](*i[1]))
    return fumction_name, function_result

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor( (sum_numbers, (1, 2)), (multiply_numbers, (2, 4)) ))