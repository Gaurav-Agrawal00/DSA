class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int n=nums.size();
        unordered_map<int,int> mymap;
        int i=0,j=0;
        int ans=0;
        while (j<n){
            mymap[nums[j]]++;
            
            
            while (mymap[nums[j]]>k){
                mymap[nums[i]]--;
                i++;

            }
            ans=max(ans,j-i+1);
            j++;
        }
        return ans;
        
    }
};