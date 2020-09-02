// Day 6: Let's Review

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    string s[10],a;
    int t,i;
    cin>>t;
    for(i=0;i<t;i++)
        cin>>s[i];

    for(i=0;i<t;i++)
    {
        a=s[i];

        for(int j=0;j<a.size();j++)
        {
            if(j%2==0)
                cout<<a[j];
        }

        cout<<" ";

        for(int j=0;j<a.size();j++)
        {
            if(j%2!=0)
                cout<<a[j];
        }
        cout<<endl;

    }

    return 0;
}
