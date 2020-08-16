// https://dmoj.ca/problem/grind
// https://dmoj.ca/submission/2946270
// should be run with v8dmoj

let n = Number(gets());
let schedule = [];
let temp;

let max = 0;
for(let i=0;i<n;i++){
    temp = gets();
    temp = temp.split(' ');
    temp[0] = Number(temp[0]);
    temp[1] = Number(temp[1]);
    if(schedule[temp[0]] == undefined) schedule[temp[0]] = 1;
    else schedule[temp[0]] += 1;
    if(schedule[temp[1]] == undefined) schedule[temp[1]] = -1;
    else schedule[temp[1]] -= 1;

    if(temp[1] > max) max = temp[1];
}
let machines = 0;
if(schedule[0] == undefined){
    schedule[0] = 0;
}
for(let i=1;i<=max;i++){
    if(schedule[i] == undefined){
        schedule[i] = schedule[i-1];
    }
    else schedule[i] += schedule[i-1];

    if(schedule[i] > machines){
        machines = schedule[i];
    } 
}
print(machines);
