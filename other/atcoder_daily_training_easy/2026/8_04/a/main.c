#include <stdio.h>
#include <string.h>

int min(int x, int y) {
    int ans;
    if (x < y) { ans = x; }
    else { ans = y; }
    return ans;
}

int main(void) {
    int r, g, b;
    char c[8];

    if (scanf("%d%d%d", &r, &g, &b) != 3) { return 1; }
    if (scanf("%7s", c) != 1) { return 1; }
    
    if (strcmp(c, "Red")==0) { printf("%d", min(g,b)); }
    else if (strcmp(c, "Green")==0) { printf("%d", min(r,b)); }
    else { printf("%d", min(r,g)); }
}
