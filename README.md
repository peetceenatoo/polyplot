# Polynomial plotting

## Straightforward method

Let $p(x)$ be a polynomial of grade n with real coefficients. Let k be the discrete number of points which is intended to be plotted.
A straightforward approximated evaluation at such points has got time complexity $O(k*n^2)$.
The approximation is due to the impossibility of representing real numbers.

## This algorithm

Let's initially consider a restriction of the problem.
Let $p(x)$ be a polynomial of grade n with integer coefficients.
One may want to plot the polynomial for k consecutive integer positive values of x, or to plot it for some integer positive values such that the largest one is k.
This algorithm seems to be working, through a phase of initialization with time complexity $O(n^2)$ and a phase of actual evaluation with time complexity $O(k*n)$.
As k is reasonably much larger than n in - kind of - every realistic context, it just works better.

## Soon

Completely aware that it's still almost useless, I'm working on a formal proof that it actually works, to then generalize its functionality.<br/>

Next features hopefully available soon in this repository:<br/>
    1. Formal proof;<br/>
    2. Extension of the domain of applicability [from positive integers to integers];<br/>
    3. Extension of the domain of the polynomial coefficients;<br/>
    4. Further extension of the domain of applicability [the k values of x to be evaluated will anyway have to be consecutive].


