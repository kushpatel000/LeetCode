#!/usr/bin/zsh

set -euo pipefail

if (( $# != 1 )); then
    print -u2 "Error: Missing argument."
    print -u2 "Usage: $0 <number>"
    exit 1
fi

INPUT="$1"

if [[ ! "$INPUT" =~ ^[0-9]{1,4}$ ]]; then
    print -u2 "Error: Input must be a number with less than 5 digits."
    exit 1
fi


PADDED_NUM="${(l:4::0:)INPUT}"

SUBDIR="Test_Cases"
PY_FILE="p${PADDED_NUM}.py"
JSON_FILE="${SUBDIR}/p${PADDED_NUM}.json"

if [[ -e "$PY_FILE" ]]; then
    print -u2 "Error: File '${PY_FILE}' already exists. Aborting."
    exit 1
fi

if [[ -e "$JSON_FILE" ]]; then
    print -u2 "Error: File '${JSON_FILE}' already exists. Aborting."
    exit 1
fi



cat <<EOF > "$PY_FILE"
# ${PADDED_NUM}. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    pass



if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.xxxx
    ]
    
    test_cases = ts.load_test_cases(__file__)

    # ts.test_all(
    #     test_cases,
    #     test_funcs,
    #     # check_thresh = 1e-5,
    #     display = True,
    #     test_only = True
    # )

EOF



cat <<EOF > "$JSON_FILE"
[
    [

    ],
    [
        
    ]
]
EOF