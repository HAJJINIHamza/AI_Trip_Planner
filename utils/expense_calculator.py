class Calculator:
    @staticmethod
    def multiply(a:int, b:int):
        """
        Mutliply two integers
        
        Args :
            a : int
            b : int
        Return :
            int: The product of a and b
        """
        return a*b
    
    @staticmethod
    def calculate_total(*x: float) -> float:
        """
        Calculate the sum of the given list of numbers 

        Args:
            x : lits[float]

        Returns : 
            float : The sum of number in the list x
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total:float, days: int) -> float:
        """
        Calculate daily budget

        Args: 
            total : float
            days : int
        
        returns float: Expense for a single day
        """
        return total / days if days > 0 else 0