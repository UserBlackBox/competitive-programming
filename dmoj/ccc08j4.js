// https://dmoj.ca/problem/ccc08j4
// https://dmoj.ca/submission/2621387
// should be run with v8dmoj

var line;
var postfix;
var i;
var a;
var b;
while(true){
    line = gets()
    if(line === '0'){
        break;
    }
    line = line.split(' ');
    line.reverse();
    postfix = [];
    for(i=0;i<line.length;i++){
        if(line[i] === '+' || line[i] === '-'){
            a = postfix.pop();
            b = postfix.pop();
            postfix.push(a+" "+b+" "+line[i]);
        }
        else{
            postfix.push(line[i]);
        }
    }
    print(postfix.join(" "));
}
