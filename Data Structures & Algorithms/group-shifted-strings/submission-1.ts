class Solution {
    /**
     * @param {string[]} strings
     * @return {string[][]}
     */
    groupStrings(strings: string[]): string[][] {
        const mapHashmap: Map<string, string[]> = new Map();

        for (let s of strings){
            const gaps:number[] = [] 
            for (let i = 1;i<s.length; i ++){
                const diff = s.charCodeAt(i) - s.charCodeAt(i - 1);
                gaps.push((diff + 26) % 26);
            }
            let key = gaps.join(',')
            if (!mapHashmap.has(key)) {
            mapHashmap.set(key, []);
            }
            mapHashmap.get(key)!.push(s) 
        }
        return Array.from(mapHashmap.values());
    }
}
