#include <stdio.h>

int main(){

    int number1,number2;
    int math;

    printf("Enter Number1 :> ");
    scanf("%d", &number1);

    printf("Enter Number2 :> ");
    scanf("%d", &number2);

    printf("math | 1:+ | 2:- | 3:/ | 4:* | :> ");
    scanf("%d", &math);

    while(1){
        if (math == 1){
        printf("number1:%d + Number2:%d = %d", number1, number2, number1 + number2);
        break;
        }

        if (math == 2){
        printf("number1:%d - Number2:%d = %d", number1, number2, number1 - number2);
        break;
        }
    
        if (math == 3){
        printf("number1:%d / Number2:%d = %d", number1, number2, number1 / number2);
        break;
        }

        if (math == 4){
        printf("number1:%d * Number2:%d = %d", number1, number2, number1 * number2);
        break;
        }
    }
   
   
    return 0;
}
