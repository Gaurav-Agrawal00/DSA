class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> myset;
        int n =nums.size();
        vector<vector<int>> final;
        sort(nums.begin(),nums.end());
        for (int i=0; i<n ; i++){
            int low=i+1, high=n-1;
            while (low<high){
                int sum=nums[low]+nums[high]+nums[i];
                if (sum==0){
                    myset.insert({nums[i],nums[low],nums[high]});
                    low++,high--;
                }
                else if(sum<0){
                    low++;
                }else high--;
            }
        }

        vector<vector<int>> ans(myset.begin(),myset.end());
        return ans;
        
    }
};