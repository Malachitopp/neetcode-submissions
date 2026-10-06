class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    combinationSum2(candidates: number[], target: number): number[][] {
        const output = [];
        candidates.sort((a, b) => a - b)

        function dfs(i:number, curr:number[]) {
            let sum = curr.reduce((s,c) => s + c, 0)
            if (sum === target){
                output.push([...curr]) 
                return 
            }
            if (i >= candidates.length) {
                return 
            }
            if (sum > target) {
                return 
            }

            curr.push(candidates[i]) 
            dfs(i+1, curr) 
            curr.pop() 
            while ( i+1 < candidates.length && candidates[i] === candidates[i+1] ){
                i++
            }
            dfs(i + 1, curr)

        }
        dfs(0,[]) 
        return output 
    }
}
