"""
In abstract algebra, the symmetric group defined over any set is the group whose elements are all the bijections from the set to itself.
The group operation is the composition of functions.

The elements of the symmetric group on a set X are the permutations of X.

Notation: id = ()
"""
import copy


class Permutation:
    def __init__(self, *args: int) -> None:
        """
        Initializes a permutation object.

        Args:
            *args (int): Integers representing the permutation mapping.
                         Each integer i represents that i is mapped to args[i-1].

        Raises:
            AssertionError: If the input conditions for a valid permutation are not met.

        For example:
            p = Permutation(5, 3, 4, 1, 2)
            - 1 is mapped to 5 (p(1) = 5)
            - 2 is mapped to 3 (p(2) = 3)
            - 3 is mapped to 4 (p(3) = 4)
            - 4 is mapped to 1 (p(4) = 1)
            - 5 is mapped to 2 (p(5) = 2)
        """ 
        self.permutation = dict()
        i = 1
        for m in args:
            assert m > 0, f'{m} is not a natural Number'
            assert isinstance(m, int), f'{m} is not a natural Number'
            assert m not in self.permutation.values(), 'Permutation is not bijektiv'
            assert m <= len(args), f'{m} is not a natural Number between 1 and {len(args)}'
            self.permutation[i] = m
            i += 1

    def __call__(self, m: int) -> int:
        """
        Applies the permutation to the given element.

        Args:
            m (int): The element to be permuted.

        Returns:
            int: The result of applying the permutation to the input element.

        Raises:
            AssertionError: If the input conditions for a valid element are not met.

        Example:
            p = Permutation(3, 2, 1)
            - p(1) returns 3
            - p(2) returns 2
            - p(3) returns 1
        """ 
        assert m > 0, f'{m} is not a natural Number'
        assert isinstance(m, int), f'{m} is not a natural Number'
        assert m <= len(self.permutation), f'{m} is not a natural Number between 1 and {len(args)}'
        return self.permutation[m]

    def is_abelian(self) -> bool:
        """
        Checks if the permutation is an abelian permutation.

        Returns:
            bool: True if the permutation is abelian, False otherwise.

        Example:
            p = Permutation(1)
            - p.is_abelian() returns True
              because (p o p)(1) = p(p(1)) = p(1) = 1 = p(1) = p(p(1)) = (p o p)(1)
        """
        if 0 < len(self.permutation) < 3:
            return True
        return False

    def to_cycle(self) -> list[tuple[int]]:
        """
        Returns the cycle notation of the Permutation as a list of tuples.

        Permutations are often written in cycle notation (cyclic form), where each cycle
        represents a set of elements that are permuted among themselves. This method
        returns the cycle notation of the Permutation.

        Returns:
            list[tuple[int]]: A list of tuples representing the cycles of the Permutation.

        Example:
            p = Permutation(5, 4, 1, 2, 6, 3, 7)
            p.to_cycle() returns [(1, 5, 6, 3), (2, 4)]

            p = Permutation(1, 2, 3, 4, 5)
            p.to_cycle() returns [()]
        """        
        cycles = []
        visited = set()

        for i in range(1, len(self.permutation) + 1):
            cycle = ()
            current = i
            while current not in visited:
                visited.add(current)
                cycle = cycle + (current,)
                current = self.permutation[current]
            if len(cycle) > 1:
                cycles.append(cycle)
        return cycles
    
    def list_to_cycle(self, A: list[int]) -> list[tuple[int]]:
        """
        Converts a list representation of a permutation to cycle notation.

        Args:
            A (list[int]): A list representing a permutation.

        Returns:
            list[tuple[int]]: A list of tuples representing the cycles of the permutation.

        Example:
            p = Permutation()
            p.list_to_cycle([2, 4, 3, 1]) returns [(1, 2, 4)]
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

        Args:
            cycle (list): A list representing the cycle notation of a permutation.

        Example:
            p = Permutation()
            p.cycle([(1, 2, 4)]) creates the permutation corresponding to (1, 2, 4).
        """ 
        numb_of_elements = 0
        for cyc in cycle:
            i = 0 
            while i < len(cyc):
                if cyc[i] not in self.permutation:
                    if i < len(cyc) - 1:
                        self.permutation[cyc[i]] = cyc[i+1]
                    else:
                        self.permutation[cyc[i]] = cyc[0] 
                i += 1
            if numb_of_elements < max(cyc):
                numb_of_elements += max(cyc)
        if len(self.permutation) < numb_of_elements:
            for i in range(1, numb_of_elements + 1):
                if i not in self.permutation:
                    self.permutation[i] = i
        self.permutation = dict(sorted(self.permutation.items())) 

    def order(self) -> int:
        """
        Returns the order (number of elements) of the symmetric group S_n.

        The order of the symmetric group S_n is n!, where n is the length of the permutation.

        Returns:
            int: The order of the symmetric group S_n.

        Example:
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
        Generates all elements of the symmetric group S_n in which our permutation is in,  using Heap's algorithm.

        Returns:
            list[list[tuple[int]]]: A list of lists, where each inner list represents
                                     the cycle notation of a permutation in S_n.

        Examples:
            p = Permutation(1)
            p.get_group() returns [[()]]  # All elements from S_1

            p = Permutation(1, 2)
            p.get_group() returns [[()], [(1, 2)]]  # All elements from S_2

            p = Permutation(1, 2, 3)
            p.get_group() returns [[()], [(1, 2)], [(1, 2, 3)], [(1, 3, 2)], [(2, 1)]...]  # All elements from S_3
        """ 
        # Shi*ty code, but it works for now
        A = list(self.permutation.values())
        B = [0 for i in range(len(self.permutation))]
        group_elements = [[()]]
        # Heap-algorithm from robert sedgewick
        i = 1
        while i < len(A):
            if B[i] < i:
                if i % 2 == 0:
                    A[0], A[i] = A[i], A[0]
                else:
                    A[B[i]], A[i] = A[i], A[B[i]]
                group_elements.append(self.list_to_cycle(copy.deepcopy(A)))
                B[i] += 1
                i = 1
            else:
                B[i] = 0
                i += 1
        return group_elements
   
    @classmethod
    def group(cls, n: int) -> list[list[tuple[int]]]:
        """
        Generates all elements of the symmetric group S_n.

        Args:
            n (int): The order of the symmetric group.

        Returns:
            list[list[tuple[int]]]: A list of lists, where each inner list represents
                                     the cycle notation of a permutation in S_n.

        Examples:
            Permutation.group(2) returns [[()], [(1, 2)]]  # All elements from S_2

            Permutation.group(3) returns [[()], [(1, 2)], [(1, 2, 3)], [(1, 3, 2)], [(2, 1)]...]  # All elements from S_3

            Permutation.group(4) returns [[()], [(1, 2)], [(1, 2, 3)], [(1, 3, 2)], [(2, 1)], ...]  # All elements from S_4
        """ 
        # Shi*ty code, but it works for now
        A = [i for i in range(1, n + 1)]
        B = [0 for i in range(1, n + 1)]
        group_elements = [[()]]
        
        # Heap-algorithm from robert sedgewick
        i = 1
        while i < len(A):
            if B[i] < i:
                if i % 2 == 0:
                    A[0], A[i] = A[i], A[0]
                else:
                    A[B[i]], A[i] = A[i], A[B[i]]
                group_elements.append(Permutation().list_to_cycle(copy.deepcopy(A)))
                B[i] += 1
                i = 1
            else:
                B[i] = 0
                i += 1
        return group_elements

    def inverse(self):
        """
        Returns the inverse Element of the current permutation.
        
        Returns:
            Permutation: A new permutation representing the inverse of the current permutation.
  
        Examples:
            p = Permutation(1, 2, 3)
            p_inverse = p.inverse()
            such that p * p_inverse = id = p_inverse * p
 
        Note:
            The inverse permutation undoes the effect of the original permutation.
            The inverse of the identity permutation is the identity itself. 
        """
        new_permutation = dict()
        for i in range(1, len(self.permutation) + 1):
            new_permutation[self.permutation[i]] = i
        new_permutation = dict(sorted(new_permutation.items()))
        args = tuple(new_permutation.values())
        return Permutation(*args)

    def __mul__(self, other):
        """
        Compose two permutations.

        Args:
            other (Permutation): Another permutation to compose with.

        Returns:
            Permutation: A new permutation resulting from the composition of self and other.

        Examples:
            p1 = Permutation(1, 2, 3)
            p2 = Permutation(2, 3, 1)
            result = p1 * p2
            repr(result) returns "(1 3 2)"
        
            q1 = Permutation(2, 3, 1)
            q2 = Permutation(3, 1, 2)
            result = q1 * q2
            repr(result) returns (1 2 3) 
            
            result2 = q2 * q1
            repr(result2) returns (1 3 2)

         Note:
            The composition of permutations is not commutative. In general, p1 * p2 is not necessarily equal to p2 * p1.
            However, for permutations in S_n where 1 <= n < 3, it is commutative.
        """ 
        new_permutation = ()
        for i in other.permutation:
            new_permutation = new_permutation + (self.permutation[other.permutation[i]], )
        return Permutation(*new_permutation)

    def __eq__(self, other) -> bool:
        """

        """
        if self.permutation == other.permutation:
            return True
        return False

    def __repr__(self) -> str:
        """
        Returns a string representation of the permutation in cycle notation.

        Returns:
            str: A string representing the cycle notation of the permutation.

        Example:
            p = Permutation(1, 2, 3)
            repr(p) returns "(1 2 3)"
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
