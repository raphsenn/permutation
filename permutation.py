
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
        Permutaion p(5, 3, 4, 1, 2) 
        1 -> 5,
        2 -> 3,
        3 -> 4,
        4 -> 1,
        5 -> 2
        """
        self.permutation = []
        for m in args:
            assert m > 0, f'{m} is not a natural Number'
            assert isinstance(m, int), f'{m} is not a natural Number'
            assert m not in self.permutation, 'Permutation is not bijektiv'
            assert m <= len(args), f'{m} is not a natural Number between 1 and {len(args)}' 
            self.permutation.append(m)
    
    def is_abelian(self) -> bool:
        """
        Return True or False if the Permutation is abelian or not.
        
        For example:
        p = Permutation(1) is abelian, because:
        (p o p)(1) = p(p(1)) = p(1) = 1 = p(1) = p(p(1)) = (p o p)(1)
        
        """
    
        if 0 < len(self.permutation) < 3:
            return True
        return False
     
    def to_cycle(self) -> list:
        """
        Returns the cycle notation of the Permutation as a list of tuples.

        Notation () = id

        For example:
        p = Permutation(5, 4, 1, 2, 6, 3, 7)
        p.to_cycle = [(1 5 6 3), (2 4)] 

        p = Permutation(1, 2, 3, 4, 5)
        p.to_cycle = [()]

        """
        pass 
