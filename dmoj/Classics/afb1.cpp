//https://dmoj.ca/problem/a4b1
//https://dmoj.ca/submission/3312488

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int nums[n];
    for(int i=0;i<n;i++){
      cin >> nums[i];
    }
    sort(nums,nums+n);
    for(int i=0;i<n;i++){
      cout << nums[i] << endl;
    }
    return 0;
}

