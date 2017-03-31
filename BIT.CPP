#include<bits/stdc++.h>
using namespace std;
void update_BIT(int input_array[],int n,int binary_indexed_tree[],int val,int i){
        binary_indexed_tree[i]= binary_indexed_tree[i]-input_array[i-1]+val;
        int temp1 = i + (i & (-i));
        while(temp1<=n){
            binary_indexed_tree[temp1]= binary_indexed_tree[temp1]-input_array[i-1]+val;
            int temp2 = temp1;
            temp1 = temp2 + (temp2 & (-temp2));
        }
}
int main()
{
    int n,v;
    cin>>n;
    int input_array[n+1]={0},binary_indexed_tree[n+1]={0};
    for(int i=0;i<n;i++){
        cin>>v;
        update_BIT(input_array,n,binary_indexed_tree,v,i+1);
        input_array[i]=v;
    }
    for(int i=1;i<=n;i++)
        cout<<binary_indexed_tree[i]<< " ";
    return 0;
}