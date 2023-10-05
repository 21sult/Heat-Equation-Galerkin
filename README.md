# Heat-Equation-Galerkin
Solving the Heat Equation using the method of linear finite elements in conjunction with the Galerkin method to reduce residuals, developed at the University of Lisbon. The computational part is done in C++, and the data analysis is done in Python with Matplotlib. It is highly suggested that one read the research paper .PDF's if they wish to understand the context behind the code, as the following descriptions only give brief outlines. The .PDF and images are in Portuguese according to the university's language.

## Description
This study covers the resolution of the heat equation, i) analytically; and ii) employing the method of linear finite elements in conjunction with the Galerkin method to reduce residuals.
A comparison of i) and ii) allowed us to investigate the effectiveness of the aforementioned methods.

Consider a metal bar of dimension $L$ with thermal diffusion coefficient $\alpha$ in contact with a heat reservoir at temperature $T_R$. I considered the ambient temperature $T_A$ and $T(x)$ the temperature of the bar
at a distance $x$ from the reservoir; thus the equation for the temperature variation is,

![image](https://github.com/21sult/Heat-Equation-Galerkin/assets/145617965/8a6cb554-2b54-4910-9556-276c9788d742)

In the stationary state we get

![image](https://github.com/21sult/Heat-Equation-Galerkin/assets/145617965/9fd63d5b-c22e-4964-b1a6-08c9fb36683c)

Where $k=\mu / \alpha$.

Using linear finite elements, I solved the equation for the steady state when $T_R = 2 T_A$, $L = 10$ and $k=1$. I solved the matrix problem using _SparseLib++_. Then, plotted a graph of $u(x) = T(x)$ and compared with the analytical solution.

![fig1](https://github.com/21sult/Heat-Equation-Galerkin/assets/145617965/99fabba2-400d-44fc-92b7-c1ba8b0539ac)
![fig2](https://github.com/21sult/Heat-Equation-Galerkin/assets/145617965/718d2d17-7e9f-4b00-9322-10a37cdc2655)

See the research paper for more details.
