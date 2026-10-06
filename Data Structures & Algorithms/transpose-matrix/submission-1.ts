class Solution {
    /**
     * @param {number[][]} matrix
     * @return {number[][]}
     */
    transpose(matrix: number[][]): number[][] {
        const row = matrix.length 
        const col = matrix[0].length 

        const temp = Array.from({length: col}, () => Array(row).fill(0) )

        for (let r = 0; r < row; r++) {
            for (let c = 0; c<col; c++){
                temp[c][r] = matrix[r][c]
            }
        }
        return temp 
    }
}
