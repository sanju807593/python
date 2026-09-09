# a=12
# b=24
# print(a+b)
# a=12
# b=24
# print(a-b)
# a=12
# b=24
# print(a*b)
# a=12
# b=24
# print(a/b)
# a=12
# b=24
# print(a**b)
# a=12
# b=24
# print(a//b)
# a=10
# b=20
# a+=b
# print(a)
# a=20
# b=18
# a-=b
# print(a)
# a=12
# b=24
# a*=b
# print(a)
# a=12
# b=24
# a/=b
# print(a)
# a=12
# b=24
# a**=b
# print(a)
# a=12
# b=24
# a//=b
# print(a)
# a=12
# b=24
# print(a<b)
# a=12
# b=24
# print(a>b)
# a=12
# b=24
# print(a<=b)
# a=12
# b=24
# print(a>=b)

# a=10
# b=20
# print(a)
# print(a>0 and b>0)
# print(a<0 or b<0)
# print (a is int)
# print(type(a))
# print(a is not int)
# print(10 in range(a))
# l=[1,2,3,4]
# print(4 not in l)

# z=int(input("enter the number:"))
# y=int(input("enter your second number:"))
# x=int(input("enter your third number:"))
# if(z>y):
#     if(z>x):
#         print(z, "is greater")
#     else:
#         print(x, "is greater")
# else:
#     if(y>x):
#         print(y, "is greater")
#     else:
#         print(x,"is greater")

# 1. write a programe to check if number +ve -ve or zero...

# 2. write a programe tocheck wheather a number odd or even... 

# 3. write a programe to check eligible to vote...

# 4. write a programe to find larger of 2 number...

# 5. write a programe to find smalest of three number...

# 6. write a programe to check if a number is divisible by both 3 and 5...


# ans 2
# num=int(input("enter the number"))
# if num & 2==0:
#     print("even")
# else:
#     print("odd")


# ans 3
# age=int(input("enter the number"))
# if age >=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")

# # ans 1
# num=int(input("enter the number"))
# if num>0:
#     print("positive number")
# elif num<0:
#     print("negative number")
# else:
#     print("zero")

# ans 5
# num1=int (input("enter the number:"))
# num2=int (input("enter the number:"))
# num3=int (input("enter the number:"))
# if num1<num2<num3:
#     print("num1 is smallest")
# elif ("num2 is smallest"):

#     print("num3 is smallest")


#include <stdio.h>

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num % 3 == 0 && num % 5 == 0) {
        printf("%d is divisible by both 3 and 5.\n", num);
    } else {
        printf("%d is not divisible by both 3 and 5.\n", num);
    }

    return 0;
}

