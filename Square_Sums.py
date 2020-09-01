def sub_prog(num, req_dict, out_list, flag_dict, perf_sqrs):
    flag_dict[num] = False
    if len(out_list) == 0:
        out_list.append(num)
    if num + out_list[-1] in perf_sqrs and num != out_list[-1]:
        out_list.append(num)
    for x in req_dict[num]:
        if flag_dict[x]:
            sub_prog(x, req_dict, out_list, flag_dict, perf_sqrs)
            if len(out_list) == len(req_dict):
                return out_list
            popped = out_list.pop()
            flag_dict[popped] = True


def square_sums(org):
    nums_sqs = [n for n in range(2 * org)]
    nums = [x for x in range(1, org + 1)]
    perf_sqrs = [x for x in nums_sqs if x ** .5 % 1 == 0]  # x**.5 % 1 == 0
    req_dict = {}
    out_list = []
    flag_dict = {}

    # making mapped dict
    for n in nums:
        req_dict[n] = [x for x in nums if n != x and x + n in perf_sqrs]

    # making flag dictionary
    for num in nums:
        flag_dict[num] = True

    for num in nums:
        if sub_prog(num, req_dict, out_list, flag_dict, perf_sqrs):
            return out_list
        else:
            for number in nums:
                flag_dict[number] = True
            out_list = []
    return False
