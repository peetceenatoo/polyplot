# Explanation

## Formal proof incoming

Since I found out about this algorithm, I have been so busy that I could not work on it at all.
I estimate that I will upload it to the repository by the end of February, and not within the first half of such month.
Although, until a formal proof is published, I suggest that no one use it.

## The idea

Let $p1(x)$ be a first-degree polynomial: it must be a straight line.
Every straight line - except the vertical one, which is not a polynomial - shows a steady increment as x grows, as its derivative is steady.<br/>
Let now $x1$ and $x2$ be a couple of values of $x$.
It means that, if $p1(x1)$ and $p1(x2)$ are known, then, let $d$ be $x2-x1$, $p1(x2+d)$ is also known and it equals $p1(x2)+(p1(x2)-p1(x1))$, because the increment of the straight line must be the same as the previous, as the distance on the x-axis between $x2+d$ and $x2$ is the same as the one between $x2$ and $x1$.<br/><br/>

Let now $p2(x)$ be a second-degree polynomial: it must be a vertical parabola.
The derivative of every proper vertical parabola is a straight line.<br/>
Let now $x1$ and $x2$ be a couple of values of $x$.
It means that, fixed a certain distance $d = x1-x2$ on the x-axis, the increment that the parabola shows between two points $x$ and $x+d$, keeps increasing steadily.
Thus, if $p2(x1)$, $p2(x2)$ and $p2(x2+d)$ are known, then $p2(x2+2d)$ is also known and it equals $p2(x2+d)+{(p2(x2)-p2(x1))+[(p2(x2+d)-p2(x2))-p2(x1)]}$, because the increment of the vertical parabola must be increased the same as it did previously, as the distance on the x-axis between $x2+2d$ and $x2+d$is the same as the one between $x2+d$ and $x2$ and the one between $x2$ and $x1$.<br/><br/>

It is noticeable that, given an n-degree polynomial $p(x)$, knowing the value of the polynomial for n+1 values of $x$ which are all distant $d$ from the previous one, then it is possible to evaluate the polynomial for the value of $x$ which is distant $d$ from the last one of the previous n+1 ones.<br/><br/>

## The algorithm

The algorithm basically evaluates the polynomial for n+1 values of $x$ which are all distant $d$ from the next one, and then it initializes n variables as it follows:<br/>
- the first variable $t1$ with the increment from the first one to the second one;<br/>
- the second variable $t2$ with the increment of the previous to get the increment from the second one to the third one;<br/>
- [...]<br/>
- until it gets to the variable $tn$, initialized to the $nth$ increment, which is steady.<br/><br/>

Then, $p(x2) = p(x1) + t1$, because that $t1$ was initialized to the increment from $p(x1)$ to $p(x2)$.<br/>
Next - since $t2$ was initialized to the increment that $t1$ needs during the second iteration of the loop to become the increment from $p(x2)$ to $p(x3)$, and since any variable $ti$ will be updated as $ti+t(i+1)$ (see the algorithm), which means that $t1$ will be updated to $t1+t2$ -, then $p(x3) = p(x2)+t1$.<br/>
Next - since $t3$ was initialized to the increment that $t2$ needs during the second iteration to become the increment that $t1$ will need during the third iteration to become the increment from $p(x3)$ to $p(x4)$, and due to update of the variables $t1, ..., tn$ -, then $p(x4) = p(x3)+t1$.<br/>
And so on.

## Wrap-up

The algorithm initializes the variables $t1, ..., tn$ so that they are what they are needed to be for the algorithm itself to work.<br/>
The proof will need to show that such variables exist and that they are $n$.




