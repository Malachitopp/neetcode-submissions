class Solution {
private:
    static constexpr std::array<std::array<int,2>, 4> directions = {{{1,0}, {-1,0}, {0,1}, {0,-1}}};
    int output{};
    int ROWS {}, COLS{} ;


public:
    int numIslands(vector<vector<char>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size(); 
       
        for (int r{}; r < grid.size(); r ++ )
        {
            for (int c{}; c < grid[0].size(); c++)
            {
                if (grid[r][c] == '1')
                {

                    output ++; 
                    dfs(grid, r,c);
                }

            }

        }
        return output; 
       


    }

    void dfs(vector<vector<char>>& grid, int r, int c)
    {
        grid[r][c] = '0';

        for (auto [dr,dc] : directions )
        {
            int nr = dr + r, nc = dc + c ;
            if (nr < 0 || nc < 0 || nr >= ROWS || nc >= COLS || grid[nr][nc]=='0'){
                continue;
            }
            dfs(grid, nr, nc);
        }
    }
};
