# Rank calculation 

I've had some fun;

In this project, I've wanted to implement an efficient way of calculating the rank of the matrix;

There are several ways to find a matrix rank. However, the simplest yet effective one is Gauss elimination (i.e., row echelon form); 

If the matrix is singular, then the sum of nun-null rows equals rank;

Because the computational efficiency of the algorithm is O(n^3), I've decided to implement it by using C;
