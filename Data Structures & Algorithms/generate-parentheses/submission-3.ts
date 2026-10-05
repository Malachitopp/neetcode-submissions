class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n: number): string[] {
        let stack:string[] = [] 
        let output = [] 

        function dfs(openN:number, closedN:number) {
            if (openN === n && closedN === n) {
                output.push(stack.join(''))
                return 
            }

            if ( openN < n ) { 
                stack.push('(')
                dfs(openN + 1, closedN) 
                stack.pop()
            }
            if (closedN < openN ) {
                stack.push(')')
                dfs(openN, closedN + 1 ) 
                stack.pop() 
            }

        }
        dfs(0,0) 
        return output 
    }
}
