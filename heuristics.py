# -*- coding: utf-8 -*-


#
#
def mostOftenVariable(var_range, litclauses):
    """
    mostOftenVariable(var_range, litclauses) -> variable

        - var_range: An Iterable that which returns all the possible variables
        
        - litclauses: A dictionary with all the clauses per literal in var_range
    
    Returns the variable that apears more times on the formula
    """
    
    best = -1
    var = 0
    
    for v in var_range:
        times = 0
        
        try:
            times += len(litclauses[v])
        except KeyError:
            pass
        
        try:
            times += len(litclauses[-v])
        except KeyError:
            pass
        
        if times > best:
            best = times            
            var = v
            
    return var
        
        
#
#
def mostEqulibratedVariable(var_range, litclauses):
    """
    mostEqulibratedVariable(var_range, litclauses) -> variable

        - var_range: An Iterable that which returns all the possible variables
        
        - litclauses: A dictionary with all the clauses per literal in var_range
    
    Returns the most equilibrated variable [ (len(var) * len(-var)) ]
    """
    
    var = 0
    best = -1
    
    for v in var_range:
        pvlen = nvlen = 0
    
        try:
            pvlen = len(litclauses[v]) 
        except KeyError:
            pass
        
        try:
            nvlen = len(litclauses[-v])
        except KeyError:
            pass

        eq_value = pvlen * nvlen * 1024 + pvlen + nvlen
            
        if eq_value > best:
            best = eq_value
            var = v

    return var        