"""
In abstract algebra, the symmetric group defined over any set is the group whose elements are all the bijections from the set to itself.
The group operation is the composition of functions.

The elements of the symmetric group on a set X are the permutations of X.

Notation: id = ()

Author: Raphael Senn
License: MIT License
"""
import copy

class Permutation:
    def __init__(self, *args: int) -> None:
        """
        *args = (n_1, n_2, n_3, ..., n_x) with n_i Element in {1, 2, ..., max(n_1, ..., n_x)}
        and i Element in {1, 2, 3, ..., x}
        1 -> n_1,
        2 -> n_2,
        3 -> n_3,
        ...
        x -> n_x

        For example:
        p = Permutaion(5, 3, 4, 1, 2)
        1 -> 5 <=> p(1) = 5,
        2 -> 3 <=> p(2) = 3,
        3 -> 4 <=> p(3) = 4,
        4 -> 1 <=> p(4) = 1,
        5 -> 2 <=> p(5) = 2
        """
        self.permutation = []
        for m in args:
            assert m > 0, f'{m} is not a natural Number'
            assert isinstance(m, int), f'{m} is not a natural Number'
            assert m not in self.permutation, 'Permutation is not bijektiv'
            assert m <= len(args), f'{m} is not a natural Number between 1 and {len(args)}'
            self.permutation.append(m)

    def __call__(self, m: int) -> int:
        """
        For example:
        p = Permutation(3, 2, 1)
        p(1) = 3
        p(2) = 2
        p(3) = 1
        """
        assert m > 0, f'{m} is not a natural Number'
        assert isinstance(m, int), f'{m} is not a natural Number'
        assert m <= len(self.permutation), f'{m} is not a natural Number between 1 and {len(args)}'
        return self.permutation[m - 1]

    def is_abelian(self) -> bool:
        """
        Return True or False if the Permutation is abelian or not.

        For example:
        p = Permutation(1)
        p.is_abelian = True
        because:
        (p o p)(1) = p(p(1)) = p(1) = 1 = p(1) = p(p(1)) = (p o p)(1)

        """

        if 0 < len(self.permutation) < 3:
            return True
        return False

    def to_cycle(self) -> list[tuple[int]]:
        """
        Permutations are also often written in cycle notation (cyclic form) so that given the set M = {1, 2, 3, 4},
        a permutation p of M with p(1) = 2, p(2) = 4, p(4) = 1 and p(3) = 3 <=> p = Permutation(2, 4, 3, 1),
        will be written as (1, 2, 4)(3), or more commonly, (1, 2, 4) since 3 is left unchanged.
        This method will return [(1, 2, 4)].

        Returns the cycle notation of the Permutation as a list of tuples.
        
        For example:
        p = Permutation(5, 4, 1, 2, 6, 3, 7)
        p.to_cycle = [(1, 5, 6, 3), (2, 4)]

        p = Permutation(1, 2, 3, 4, 5)
        p.to_cycle = [()]

        """
        cycles = []
        visited = set()

        for i in range(1, len(self.permutation) + 1):
            cycle = ()
            current = i
            while current not in visited:
                visited.add(current)
                cycle = cycle + (current,)
                current = self.permutation[current - 1]
            if len(cycle) > 1:
                cycles.append(cycle)
        return cycles
    
    def list_to_cycle(self, A: list[int]) -> list[tuple[int]]:
        """
        """
        cycles = []
        visited = set()

        for i in range(1, len(A) + 1):
            cycle = ()
            current = i
            while current not in visited:
                visited.add(current)
                cycle = cycle + (current,)
                current = A[current - 1]
            if len(cycle) > 1:
                cycles.append(cycle)
        return cycles

    def cycle(self, cycle: list) -> None:
        """
        Creates a Permutation from Cycle Notation.
        
        For example:
        """
        pass

    def order(self) -> int:
        """
        The order (number of elements) of the symmetric group S_n is n!.

        Runtime: O(len(self.permutation))

        For example:
        S_1 has order 1 = 1!
        S_2 has order 2 = 2!
        S_3 has order 6 = 3!
        S_4 has order 24 = 4!
        S_5 has order 120 = 5!
        S_6 has order 720 = 6!
        """
        n = len(self.permutation)
        if n == 0:
            return 1
        for i in range(n - 1, 1, -1): # from (n - 1) to 1, with 1 step downwards.
            n *= i
        return n

    def get_group(self) -> list[list[tuple[int]]]:
        """
        
        For example: 
        p = Permutation(1)
        p.get_group() returns all elements from S_1

        p = Permutation(1, 2)
        p.get_group() returns all elements from S_2

        p = Permutation(1, 2, 3)
        p.get_group() returns all elements from S_3
        ...

        We use the Heap-Algorithm.
        
        """
        # Shi*ty code, but it works for now
        A = self.permutation
        group_elements = [[()]]
        # group_elements = [()] + self.list_to_cycle(copy.deepcopy(A))
        B = [0 for i in range(len(self.permutation))]
        i = 1
        # Heap-algorithm form robert sedgewick
        while i < len(A):
            if B[i] < i:
                if i % 2 == 0:
                    A[0], A[i] = A[i], A[0]
                else:
                    A[B[i]], A[i] = A[i], A[B[i]]
                group_elements.append(self.list_to_cycle(copy.deepcopy(A)))
                # group_elements += self.list_to_cycle(copy.deepcopy(A))
                B[i] += 1
                i = 1
            else:
                B[i] = 0
                i += 1
        return group_elements

    def group(self, n: int) -> list[list[tuple[int]]]:
        """
        Returns all Elements from S_n with n Element in netural Numbers.
        """
        pass

    def __repr__(self) -> str:
        """
        Print method, prints cycle Notation of the Permutation.
        """
        permutation_to_string = ""
        cycle_notation = self.to_cycle()
        for cycle in cycle_notation:
            permutation_to_string += "("
            for n in cycle:
                if n != cycle[-1]:
                    permutation_to_string += str(n) + " "
                else: 
                    permutation_to_string += str(n)
            permutation_to_string += ")"
        return permutation_to_string
