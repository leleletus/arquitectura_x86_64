extern int moda_asm_int(int *arreglo, int N);
int moda_c( int *arreglo, int N)
{
    int cont_max = 0;
    int cont_int;
    int moda_value;
    for (int i = 0; i<N; i++)
    {    cont_int = 0;
        for(int j = 0;j<N;j++)
        {if (arreglo[i] == arreglo[j])
            {cont_int = cont_int + 1;}
        }
        if (cont_int>cont_max)
            {cont_max = cont_int;
            moda_value = arreglo[i];}
    }
    return moda_value;   
}