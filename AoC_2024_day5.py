from aocd import get_data
from typing import List, Tuple
import networkx as nx


def data_process() -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    """
    Process the input data from Advent of Code.
    
    Returns:
        Tuple containing processed rules and sequences.
    """
    try:
        data = get_data(year=2024, day=5).split('\n\n')
        if len(data) < 2:
            raise ValueError("Invalid input data format")
            
        rules = [tuple(map(int, rule.split('|'))) for rule in data[0].split('\n')]
        seqs = [list(map(int, x.split(','))) for x in data[1].split('\n')]
        return rules, seqs
    except Exception as e:
        raise ValueError(f"Error processing data: {e}")


def is_valid_seq(rules: List[Tuple[int, int]], seq: List[int]) -> bool:
    """
    Check if a sequence is valid according to the rules.
    
    Args:
        rules: List of (before, after) pairs representing rules
        seq: Sequence to validate
        
    Returns:
        bool: True if sequence is valid, False otherwise
    """
    # Create position mapping for O(1) lookup
    pos_map = {num: idx for idx, num in enumerate(seq)}
    
    for before, after in rules:
        if before in pos_map and after in pos_map:
            if pos_map[before] > pos_map[after]:
                return False
    return True


def get_middle_number(seq: List[int]) -> int:
    """
    Get the middle number from a sequence.
    
    Args:
        seq: Input sequence
        
    Returns:
        int: Middle number in the sequence
    """
    return seq[len(seq) // 2]


def part1(rules: List[Tuple[int, int]], seqs: List[List[int]]) -> int:
    """
    Solve part 1 of the puzzle.
    
    Args:
        rules: List of rules
        seqs: List of sequences to check
        
    Returns:
        int: Sum of middle numbers from valid sequences
    """
    return sum(get_middle_number(seq) for seq in seqs if is_valid_seq(rules, seq))


"""part 2"""
def build_graph(rules: List[Tuple[int, int]], seq: List[int]) -> nx.DiGraph:
    """
    Build a directed graph from rules and sequence.
    
    Args:
        rules: List of (before, after) pairs representing rules
        seq: Input sequence
        
    Returns:
        nx.DiGraph: Directed graph representing the sequence order
    """
    G = nx.DiGraph()
    # Add all nodes first to ensure isolated nodes are included
    G.add_nodes_from(seq)
    seq_set = set(seq)
    G.add_edges_from((before, after) for before, after in rules 
                    if before in seq_set and after in seq_set)
    return G

def get_sorted_sequence(rules: List[Tuple[int, int]], seq: List[int]) -> List[int]:
    """
    Get topologically sorted sequence using graph-based approach.
    
    Args:
        rules: List of rules
        seq: Sequence to sort
        
    Returns:
        List[int]: Topologically sorted sequence
    """
    G = build_graph(rules, seq)
    return list(nx.lexicographical_topological_sort(G))

def part2(rules: List[Tuple[int, int]], seqs: List[List[int]]) -> int:
    """
    Solve part 2 of the puzzle.
    
    Args:
        rules: List of rules
        seqs: List of invalid sequences to process
        
    Returns:
        int: Sum of middle numbers from sorted sequences
    """
    return sum(get_middle_number(get_sorted_sequence(rules, seq)) for seq in seqs)


if __name__ == "__main__":
    rules, seqs = data_process()
    result_part1 = part1(rules, seqs)
    print(f"Part 1 result: {result_part1}")
    # part 2
    invalid_sequences = [seq for seq in seqs if not is_valid_seq(rules, seq)]
    result_part2 = part2(rules, invalid_sequences)
    print(f"Part 2 result: {result_part2}")
