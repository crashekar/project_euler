total_sum = 0
result_set = set()
for multiplicand in range(1,100):
    for multiplier in range(100, 10000):
        result = multiplier * multiplicand
        concat_result = "%s%s%s" % (result, multiplier, multiplicand) 
        sorted_concat_result = list(concat_result)
        sorted_concat_result.sort()
        if sorted_concat_result == ['1','2','3','4','5','6','7','8','9']:
            ss = "%s*%s=%s" % (  multiplier, multiplicand,result)
            result_set.add(result)

print sum(list(result_set))

