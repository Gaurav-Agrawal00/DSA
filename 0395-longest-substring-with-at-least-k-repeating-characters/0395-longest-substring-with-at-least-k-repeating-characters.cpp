class Solution {
public:
    int longestSubstring(string s, int k) {
        int n =s.length();
        int i=0;
        // unordered_map<char,int> mymap;
        int ans=0;

        for (i=0; i<n ; i++){
            unordered_map<char,int> mymap;
            for (int j=i; j<n ; j++){
                mymap[s[j]]++;

                bool ok=true;
                for (auto [key,val]:mymap){
                    if (!(val>=k)){
                        ok=false;
                    }
                }

                if (ok){
                    ans=max(ans,j-i+1);
                }
                
            }
        }

        return ans;
    }
};