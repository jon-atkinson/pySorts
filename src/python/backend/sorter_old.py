import timeit

class Sorter:

    def __init__():
        print("creating new sorter")

    def compute_algo_comparisons(algos, in_strs, n, arr_type, num_reps, verbose):
        """ compares the average runtimes of different algorithms on on type of input
        algos: list of refs to algorithms to compare
        in_strs: list of strings corresponding to the algos being compared
        n: size of array being sorted
        arr_type: string representing the sortedness of the array
        num_reps: number of reps (with newly gen arrs per rep) to be avged
        """
        results = dict()
        for i, elem in enumerate(in_strs):
            results.update({in_strs[i]: 0.0})

        for i in range(num_reps):
            # new input array since repeating one allows python memory cache optimisations
            arr = get_arr(arr_type)(n, "python")

            if arr is None:
                print('error in input array type')
                return None

            if not verbose:
                for j, elem in enumerate(in_strs):
                    if (elem[-1] == "C"):
                        results[elem] += timeit.timeit(lambda: algos[j](create_arrays.to_c_arr(deep_array_copy(arr), n), n), number=1)
                    else:
                        results[elem] += timeit.timeit(lambda: algos[j](deep_array_copy(arr), n), number=1)
            else: # TODO refactor eventually, this is quite an inelegant and inefficient soln. to this problem
                print('(running in verbose mode)')
                for j, elem in enumerate(in_strs):
                    if (elem[-1] == "C"):
                        inArray = create_arrays.to_c_arr(deep_array_copy(arr), n)
                        sortedArray = algos[j](inArray, n)
                    else:
                        sortedArray = algos[j](deep_array_copy(arr), n)

                    print("\n\n(" + elem + ")\nInitial: " + str(arr[0:n]) + "\nFinal: " + str(sortedArray[0:n]), end="")

                    if (elem[-1] == "C"):
                        results[elem] += timeit.timeit(lambda: algos[j](create_arrays.to_c_arr(deep_array_copy(arr), n), n), number=1)
                    else:
                        results[elem] += timeit.timeit(lambda: algos[j](deep_array_copy(arr), n), number=1)


        # meaningless for comparison since #reps introduces a constant scale factor but for semantic sakes
        # also helps when considering rough runtimes over tests with different number of repeat tests
        for i, elem in enumerate(in_strs):
            results[elem] /= num_reps
        return results
