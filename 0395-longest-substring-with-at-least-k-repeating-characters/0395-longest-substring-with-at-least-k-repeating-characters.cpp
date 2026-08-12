class Solution {
public:
    int longestSubstring(string s, int k) {
        int n =s.length();
        int ans=0;

        for (int i=0; i<n ; i++){
            unordered_map<char,int> mymap;
            int count=0;
            for (int j=i; j<n ; j++){
                mymap[s[j]]++;

                if (mymap[s[j]]==k){
                    count++;
                }

                if (count==mymap.size()) ans=max(ans,j-i+1);
                
            }
        }

        return ans;
    }
};