"""
Generates a random Permutation.
"""
import random


def generate_random_permutation(size):
    return random.sample(range(1, size + 1), size)
