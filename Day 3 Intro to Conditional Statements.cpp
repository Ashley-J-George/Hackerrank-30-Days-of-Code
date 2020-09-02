#include<iostream>

using namespace std;



int main()
{
    int n;
    cin>>n;
    if((n%2!=0) || (n%2==0 && n>5 && n<21))
        cout<<"Weird";
    if((n%2==0 && n>20)||(n%2==0 && n>1 && n<6))
        cout<<"Not Weird";

    return 0;
}
