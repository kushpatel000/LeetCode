#!/bin/python3

import argparse
from pathlib import Path
from get_today import download_and_export_problem as daep


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Utilities to interface with Leetcode."
    )
    parser.add_argument(
        "action",
        type=str,
        choices=["get", "clean"],
        help='Action to perform: "get" or "clean".',
    )
    parser.add_argument(
        "target",
        nargs='?',
        type=str,
        help='If action is "get", then this should be either "today" or a number.',
    )

    args = parser.parse_args()

    if args.action == "get":
        if args.target is None:
            args.target = "today"
    elif args.target is not None:
        parser.error('argument target: not allowed when action is "clean"')

    return args

def clean():
    completed = Path.cwd().glob('p[0-9][0-9][0-9][0-9].py')
    completed_path = Path.cwd() / 'Complete'
    for src in completed:
        dst = completed_path / src.name
        src.rename(dst)
        print(f'  Moving {src.name}')
        
    print('Finished.')


def main(action: str, target: str) -> None:
    if action == 'clean':
        clean()
        return

    if action == 'get':
        daep(target)
        return

    raise ValueError(f'Bad action: "{action}"')
        

    # Replace with your core logic
    print(f"First argument: {action} {type(action)}")
    print(f"Second argument: {target} {type(target)}")


if __name__ == "__main__":
    args = parse_args()
    main(args.action, args.target)