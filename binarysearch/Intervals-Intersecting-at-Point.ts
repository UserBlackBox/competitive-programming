// https://binarysearch.com/problems/Intervals-Intersecting-at-Point

class Solution {
    solve(intervals: Array<Array<number>>, point: number): number {
        let count:number = 0;
        for(let i:number=0;i<intervals.length;i++){
            if(intervals[i][0]<=point && intervals[i][1]>=point) count += 1;
        }
        return count;
    }
}
