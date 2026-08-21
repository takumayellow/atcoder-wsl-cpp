#include <stdio.h>

int main(void){
    int h,w;
    scanf("%d %d", &h, &w);

    if(w * 10000 >= 25 * h * h) {
        printf("Yes\n");}
    else{
        printf("No\n");
    }

    return 0;
}
