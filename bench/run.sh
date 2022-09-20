RUNS=1000

fastero "file: bench_find_substring_in_list_of_strings/method_0.py" -n "any()" \
	"file: bench_find_substring_in_list_of_strings/method_1.py" -n "find() w/ for-loop" \
	"file: bench_find_substring_in_list_of_strings/method_2.py" -n "find() w/ comprehension" \
	"file: bench_find_substring_in_list_of_strings/method_3.py" -n "join()" \
	"file: bench_find_substring_in_list_of_strings/method_4.py" -n "for-loop conditional check" \
	"file: bench_find_substring_in_list_of_strings/method_5.py" -n "list-comprehension conditional check" \
	--setup "file: bench_find_substring_in_list_of_strings/setup.py" --runs $RUNS

fastero "file: bench_find_unique_keys_from_list_of_dicts/method_0.py" -n "Using Chain itertools" \
	"file: bench_find_unique_keys_from_list_of_dicts/method_1.py" -n "Using list/dict Comprehension" \
	"file: bench_find_unique_keys_from_list_of_dicts/method_2.py" -n "Using keys(),extend(),list() and set() methods" \
	--setup "file: bench_find_unique_keys_from_list_of_dicts/setup.py" --runs $RUNS
