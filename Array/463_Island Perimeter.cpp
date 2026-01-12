#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class Solution {
public:
    bool visit[105][105];
    int n, m;
    int cnt;
    vector<pair<int, int>> v = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    bool valid(int i, int j) {
        if (i < 0 || i >= n || j < 0 || j >= m) {
            return false;
        }
        return true;
    }

    void dfs(int si, int sj, vector<vector<int>>& grid) {
        visit[si][sj] = true;
        for (int i = 0; i < 4; i++) {
            int ci = si + v[i].first;
            int cj = sj + v[i].second;
            
            if (valid(ci, cj) == false)
                cnt++; 
            else if (valid(ci, cj) == true && grid[ci][cj] == 0)
                cnt++; 
            else if (valid(ci, cj) && !visit[ci][cj] && grid[ci][cj] == 1) {
                dfs(ci, cj, grid);
            }
        }
    }

    int islandPerimeter(vector<vector<int>>& grid) {
        cnt = 0;
        n = grid.size();
        m = grid[0].size();
        memset(visit, false, sizeof(visit));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visit[i][j] && grid[i][j] == 1) {
                    dfs(i, j, grid);
                }
            }
        }
        return cnt;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> grid = {
        {0, 1, 0, 0},
        {1, 1, 1, 0},
        {0, 1, 0, 0},
        {1, 1, 0, 0}
    };

    int result = sol.islandPerimeter(grid);
    cout << "Island Perimeter: " << result << endl;

    return 0;
}