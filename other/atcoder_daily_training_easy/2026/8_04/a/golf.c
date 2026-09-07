#include<stdio.h>
int a[3],i,m=1<<30;char c;
int main(){scanf("%d%d%d %c",a+1,a+2,a,&c);a[c%3]=m;for(;i<3;i++)m=m<a[i]?m:a[i];printf("%d",m);}
