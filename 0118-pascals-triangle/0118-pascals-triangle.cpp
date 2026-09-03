class Solution {
public:
vector<vector<int>> generate(int numRows) {
    int n = numRows;
    vector<vector<int>> ans;

    for (int i = 1; i <= n; i++) {
        vector<int> res;

        for (int j = 1; j <= i; j++) {
            if (j == 1 || j == i) {
                res.push_back(1);
            }
            else {
                res.push_back(ans[i-2][j-2] + ans[i-2][j-1]);
            }
        }

        ans.push_back(res);
    }

    return ans;
}};