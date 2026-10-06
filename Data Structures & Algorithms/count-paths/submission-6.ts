class Solution {
    /**
     * @param {number} m
     * @param {number} n
     * @return {number}
     */
    uniquePaths(m: number, n: number): number {
        let bottom = Array(n).fill(1) 

        for (let i = m-1 ; i > 0 ; i -- ){
            const newRow = Array(n).fill(1) 
            for (let j = n-2; j >= 0; j --) { 
                newRow[j] = newRow[j+1] + bottom[j]
                
            }
            bottom = newRow 
        }
        return bottom[0]
    }
}
