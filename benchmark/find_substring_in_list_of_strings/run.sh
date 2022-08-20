fastero "file: method_0.py" -n "any()" \
        "file: method_1.py" -n "find() w/ for-loop" \
        "file: method_1a.py" -n "find() w/ comprehension" \
        "file: method_2.py" -n "join()" \
        "file: method_3.py" -n "for-loop conditional check" \
        "file: method_4.py" -n "list-comprehension conditional check" \
        --setup "file: setup.py" --runs 25
