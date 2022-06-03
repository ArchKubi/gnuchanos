#include <stdio.h>

int main(){
    int numberInt = 10;
    float numberFloat = 10.50;
    double numberDouble = 10.500;
    char string[2] = "10"; // Nope
    printf("%f %d %d", (float)numberInt, (int)numberFloat, (int)numberFloat);
    return 0;
}