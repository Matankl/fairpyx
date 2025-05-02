"""
An implementation of the algorithms in:

"Efficient Nearly-Fair Division with Capacity Constraints", by A. Hila Shoshan,  Noam Hazon,  Erel Segal-Halevi
(2023), https://arxiv.org/abs/2205.07779

Programmer: Matan Ziv.
Date: 2025-04-27.
"""

# The end-users of the algorithm feed the input into an "Instance" variable, which tracks the original input (agents, items and their capacities).
# But the algorithm implementation uses an "AllocationBuilder" variable, which tracks both the ongoing allocation and the remaining input (the remaining capacities of agents and items).
# The function `divide` is an adaptor - it converts an Instance to an AllocationBuilder with an empty allocation.
from fairpyx import Instance, AllocationBuilder, divide


# The end-users of the algorithm feed the input into an "Instance" variable, which tracks the original input (agents, items and their capacities).
# The input of the algorithm is:
# a dict of a dict witch tells the valuations of the items for each player
# a dict of a sets, dict of category each category is a set contains the items in the category
# a dict of categories and the capacities

# the returned value of the algorithem is


# The `logging` facility is used both for debugging and for illustrating the steps of the algorithm.
# It can be used to automatically generate running examples or explanations.
import logging

logger = logging.getLogger(__name__)

# This example instance is used in doctests throughout this file:
example_instance = Instance(
    valuations={"Alice": {"c1": 8, "c2": 6, "c3": 10}, "Bob": {"c1": 8, "c2": 10, "c3": 6},
                "Chana": {"c1": 6, "c2": 8, "c3": 10}, "Dana": {"c1": 6, "c2": 8, "c3": 10}},
    agent_capacities={"Alice": 2, "Bob": 3, "Chana": 2, "Dana": 3},
    item_capacities={"c1": 2, "c2": 3, "c3": 4},
)


def algorithm1(alloc: AllocationBuilder):
    """
    This dummy algorithm gives one item to the first agent, and all items to the second agent.
    This algorithm ignores agent and item conflicts.

    >>> divide(algorithm1, example_instance)
    {'Alice': ['c1'], 'Bob': ['c1', 'c2', 'c3'], 'Chana': [], 'Dana': []}
    """
    logger.info("\nAlgorithm 1 starts. items %s , agents %s", alloc.remaining_item_capacities,
                alloc.remaining_agent_capacities)
    remaining_agents = list(
        alloc.remaining_agents())  # `remaining_agents` returns the list of agents with remaining capacities.
    remaining_items = list(alloc.remaining_items())
    alloc.give(remaining_agents[0],
               remaining_items[0])  # `give` gives the specified agent the specified item, and updates the capacities.
    alloc.give_bundle(remaining_agents[1],
                      remaining_items)  # `give_bundle` gives the specified agent the specified set of items, and updates the capacities.
    # No need to return a value. The `divide` function returns the output.


### MAIN PROGRAM

if __name__ == "__main__":
    # 1. Run the doctests:
    import doctest, sys

    print("\n", doctest.testmod(), "\n")

    # 2. Run the algorithm on random instances, with logging:
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.INFO)

    from fairpyx.adaptors import divide_random_instance

    divide_random_instance(algorithm=algorithm3,
                           num_of_agents=30, num_of_items=10, agent_capacity_bounds=[2, 5],
                           item_capacity_bounds=[3, 12],
                           item_base_value_bounds=[1, 100], item_subjective_ratio_bounds=[0.5, 1.5],
                           normalized_sum_of_values=100,
                           random_seed=1)
