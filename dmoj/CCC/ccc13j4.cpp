//https://dmoj.ca/problem/ccc13j4
//https://dmoj.ca/submission/3315039

#include <bits/stdc++.h>

using namespace std;

int main() {
    int t;
    cin >> t;
    int n;
    cin >> n;
    unsigned int nums[n];
    for(int i=0;i<n;i++){
      cin >> nums[i];
    }
    sort(nums,nums+n);
    unsigned int tasks = 0;
    unsigned long total = 0;
    for(int i=0;i<n;i++){
      total += nums[i];
      if(total<=t){
          tasks += 1;
      }else{
          break;
      }
    }
    cout << tasks << endl;
    return 0;
}

