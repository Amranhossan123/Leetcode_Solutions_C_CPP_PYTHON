#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class Solution {
public:
    bool visit[305][305];
    vector<pair<int,int>> v = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    int m, n;

    bool valid(int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n) {
            return false;
        }
        return true;
    }

    void dfs(int si, int sj, vector<vector<char>>& grid) {
        visit[si][sj] = true;
        for (int i = 0; i < 4; i++) {
            int ci = si + v[i].first;
            int cj = sj + v[i].second;
            if (valid(ci, cj) && !visit[ci][cj] && grid[ci][cj] == '1') {
                dfs(ci, cj, grid);
            }
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        m = grid.size();
        if (m == 0) return 0;
        n = grid[0].size();
        memset(visit, false, sizeof(visit));
        int cnt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visit[i][j] && grid[i][j] == '1') {
                    dfs(i, j, grid);
                    cnt++;
                }
            }
        }
        return cnt;
    }
};

int main() {
    Solution sol;
    vector<vector<char>> grid = {
        {'1', '1', '0', '0', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '1', '0', '0'},
        {'0', '0', '0', '1', '1'}
    };

    int result = sol.numIslands(grid);
    cout << "Number of Islands: " << result << endl;

    return 0;
}