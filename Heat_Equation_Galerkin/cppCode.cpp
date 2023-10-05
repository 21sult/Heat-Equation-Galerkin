#include <iostream>
#include <vector>
#include <fstream>
#include "sparselib/sparselib.hh"

using namespace ::std;
using namespace ::sparselib_load;
using ::sparselib::index_type ;
using ::sparselib_fun::maxval ;
using ::sparselib_fun::minval ;
using ::sparselib_fun::absval ;

void solve(double dx, double L, string filename)
{
    // CONFIG
    // > variáveis gerais
    double N = L / dx; // Número de passos / Dimensão da matriz A
    double nulos = 3*N - 2;

    // > matriz A
    CCoorMatrix<double> A; // matriz A
    A.new_dim(N-1, N-1, nulos);
    for (int i = 0; i<N-1; i++)
    {
        for (int j = 0; j<N-1; j++)
        {
            if (i == j) A.insert(i,j) = (2.0/dx) + (2.0*dx/3.0);
            else if (i == j+1 || i == j-1) A.insert(i,j) = (dx/6.0) - (1.0/dx);
        }
    }

    // > vetor x
    Vector<double> x;
    x.new_dim(N-1);
    x = 0; // definir todos os valores de x como 0

    // > vetor b
    Vector<double> b;
    b.new_dim(N-1);
    b = 0; // definir todos os valores de b como 0
    b[0] = 1/dx - dx/6;

    // RESOLUÇÃO
    IdPreco<int> P;
    P.build(A);
    int iter, max_iter = 100000;;
    double epsilon = 0.00001; // precisão
    double sol = bicgstab(A, b, x, P, epsilon, max_iter, iter); // resolver

    // FICHEIRO
    vector<double> vec_a(N);
    vec_a[0] = 1;
    vec_a[N] = 0;
    vector<double> vec_x(N);
    vec_x[0] = 0;
    vec_x[N] = N*dx;
    for (int i = 1; i < N; i++)
    {
        vec_x[i] = i*dx;
        vec_a[i] = x[i-1];
    }

    ofstream data(filename);
    for (int i = 0; i < N+1; i++) data << i*dx << "\t" << vec_a[i] << endl;
    data.close();
}

int main()
{
    solve(1.0 , 10, "data1.txt");
    solve(0.5 , 10, "data2.txt");
    solve(0.1 , 10, "data3.txt");
    solve(0.01, 10, "data4.txt");
    solve(0.001, 10, "data5.txt");

    return 0;
}
