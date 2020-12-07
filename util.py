from typing import List

def get_file_contents(file: str) -> List[List[str]]:
    """
    Process the input file

    Some of AoC puzzles formats the input file to use a blank line to designate a group.
    :param file: the name of the file
    :return:
    """
    with open(file) as fh:
        content = fh.read()
        return [block.strip().split('\n') for block in content.strip().split('\n\n')]
