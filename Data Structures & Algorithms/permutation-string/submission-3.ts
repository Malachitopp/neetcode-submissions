class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1: string, s2: string): boolean {
        const hash = new Map<string, number>();

        for (const c of s1) {
            hash.set(c, (hash.get(c) ?? 0) + 1);
        }

        const need = hash.size 

        for ( let i = 0; i < s2.length ; i ++){
            const count2 = new Map<string, number>();
            let curr = 0 
            for (let j = i; j < s2.length; j ++) {
                count2.set(s2[j], (count2.get(s2[j]) ?? 0)+1);
                const have = count2.get(s2[j])!;
                const want = hash.get(s2[j]) ?? 0 ;

                if (want < have) break
                if (want === have) {
                    curr += 1
                };
                if (curr === need) return true;
            }

        }
        return false 
    }
}
