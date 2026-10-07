class Solution {
    longestPalindromeSubseq(s: string): number {
        const n = s.length;
        const cache = new Map<number, number>();

        function dfs(l: number, r: number): number {
            if (l > r) return 0;
            if (l === r) return 1;

            const key = l * n + r;
            if (cache.has(key)) return cache.get(key)!;

            let result: number;
            if (s[l] === s[r]) {
                result = 2 + dfs(l + 1, r - 1);
            } else {
                result = Math.max(dfs(l + 1, r), dfs(l, r - 1));
            }

            cache.set(key, result);
            return result;
        }

        return dfs(0, n - 1);
    }
}
