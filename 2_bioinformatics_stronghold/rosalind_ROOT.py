#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Counting Rooted Binary Trees
URL: http://rosalind.info/problems/root/

Given: A positive integer n (n≤1000).
Return: The value of B(n) modulo 1,000,000.
'''
    
if __name__ == '__main__':
    # A quick function to calculate the double factorial of a given number
    doublefactorial = lambda n: n * doublefactorial(n-2) if n > 1 else 1 
    
    # Read the number of leaves, n.
    n = int(open('problem_datasets/rosalind_root.txt', 'r').read())
    
    # The number of trees on n leaves is the double factorial, (2n-3)!!
    print(doublefactorial(2*n-3) % 1000000)
