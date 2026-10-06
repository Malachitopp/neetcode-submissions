class Solution {
    /**
     * @param {number} m
     * @param {number} n
     * @return {number}
     */
    uniquePaths(m: number, n: number): number {
        const bottom = Array.from({length:m}, () => Array(n).fill(-1))

        function dfs(i,j) {
            if ( i >= m || j >= n ){
                return 0
            }
            if ( i === m -1 && j === n-1) {
                return 1
            }   
            if (bottom[i][j] != -1) {
                return bottom[i][j]

            }
            bottom[i][j] = dfs(i + 1, j) + dfs(i, j+1) 
            return bottom[i][j]
        }
        return dfs(0,0)
    }
}
