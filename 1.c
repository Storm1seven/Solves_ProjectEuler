#include<stdio.h>
#include<math.h>
int main()
{
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {   
        long int a, b, c, d;
        scanf("%ld", &a);
        b= (a/3)*((a/3)+1)/2;
        c= (a/5)*((a/5)+1)/2;
        d= (a/15)*((a/15)+1)/2;
        long int f;
        if(a%3==0||a%5==0)
            f=(3*b)+(5*c)-(15*d)-a;
        else
            f=(3*b)+(5*c)-(15*d);

        printf("%ld\n", f);

    }
    return 0;
    
}