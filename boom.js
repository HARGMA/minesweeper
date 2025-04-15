let counter;
let bombs;
let cel;
let m = [];
let score = 0;
let lvl;
let flags = lvl;
let end = false;
let table;
table = document.getElementById("table");
let msg = document.getElementById("msg");
let submit = document.getElementById("submit");

function clear(x, y) {
  for (let i = x - 1; i < x + 2; i++) {
    for (let j = y - 1; j < y + 2; j++) {
      if (
        0 <= i &&
        i < 10 &&
        0 <= j && 
        j < 10
      ) {
        cel = table.rows[i].cells[j].querySelector("button");
        if(cel.style.backgroundImage === 'url("none.jpg")'){
          cel.style.backgroundImage = `url(${m[i][j]}.jpg)`;
        
        
        if (m[i][j] == "0" ) {
          // m[i][j]="x"
          clear(i, j);
        }}
      }
    }
  }
}

function choose(i,j){
  //table = document.getElementById("table");
  if (end) return;
  cel=table.rows[i].cells[j].querySelector("button");
  let x= document.getElementById("bomb").checked;
  let y=document.getElementById("flag").checked;
  if(x){
    bomb(i,j);
    return;
  }
  else if (y) {
    flag(i,j);
    return;
  }
}
function bomb(i, j) {
  cel = table.rows[i].cells[j].querySelector("button");
  if (cel.style.backgroundImage === 'url("🚩.jpg")') {return ;}
  cel.style.backgroundImage = `url(${m[i][j]}.jpg)`;
  if (m[i][j] == "💣") {
    end=true;
    show();
    msg.innerHTML ="sorry u lost :(<br> u found " + score + " bombs!";
    //replay();
    return
  } 
  if(m[i][j]==="0") clear(i, j);
}

function flag(i,j){
  if (cel.style.backgroundImage === 'url("none.jpg")'){
    if(flags>=maxFlags){
      document.getElementById("msg").innerHTML="u used all of your flags<br>(u should unflag)";
      return;
    }else{
      document.getElementById("msg").innerHTML="";
    }
    if(m[i][j]=="💣"){
      score++;
      if (score==lvl){
        cel.style.backgroundImage = "url('🚩.jpg')";
        end=true;
        win()
      }
    }
    cel.style.backgroundImage = "url('🚩.jpg')";
    flags++
    document.getElementById("flags").innerHTML = lvl-flags;
  }else if(cel.style.backgroundImage==='url("🚩.jpg")'){
  if(m[i][j]=="💣"){
      score--;
    }
    flags--;
    document.getElementById("flags").innerHTML = lvl-flags;
    cel.style.backgroundImage = "url('none.jpg')";
  }
}
function win(){
  msg.innerHTML="gongrats u won 🥳🐠<br> refrech to replay";
  // replay();
}
// function replay(){

//   showPrompt("wnna retry","yes",true);
//   inp=document.getElementById("userInput").value.toUpperCase();
//   console.log(inp);
//   //}while(inp!="YES" && inp!="NO")
//   if(inp=="YES") {
//     initial(10);
//   }
//   else {
//     msg.innerHTML ="good by :)";
//   }
// }

// async function showPrompt(ch,preWrote,tst) {
//   ok=submit.checked
//   document.getElementById("userInput").value = preWrote;
//   const input = document.getElementById("userInput");

//   document.getElementById("prompt").innerHTML=ch;
//   document.getElementById("customPrompt").style.display = "block";
//   document.getElementById("overlay").style.display = "block";
  
//   document.getElementById("userInput").focus();
//    //Add event listener for Enter key
//    input.addEventListener("keydown", function handler(e) {
//     if (e.key === "Enter" || submit) {
//       // Remove listener to avoid duplicates
//       input.removeEventListener("keydown", handler);
//       //console.log(input);
//       idkAnyMore =document.getElementById("userInput").value;
//       submitPrompt();
//       console.log(idkAnyMore+submit);
//       return idkAnyMore
//     }
//   });
//}

// function submitPrompt() {
//   document.getElementById("customPrompt").style.display = "none";
//   document.getElementById("overlay").style.display = "none";
// }
async function show(){
  for(let i=0;i<10;i++){
    for(let j=0;j<10;j++){
      cel=table.rows[i].cells[j].querySelector("button")
      if(m[i][j]=="💣"){
        await sleep(300);
        cel.style.backgroundImage = "url('💣.jpg')";
      }
    }
  }
}
function add(m, x, y, top) {
  for (let i = x - 1; i < x + 2; i++) {
    for (let j = y - 1; j < y + 2; j++) {
      if (i >= 0 && i < top && j >= 0 && j < top && m[i][j] != "💣") {
        m[i][j]= String(Number(m[i][j])+1);
      }
    }
  }

}
function initial(top) {
  for (let i = 0; i < top; i++) {
    m[i] = [];
    for (let j = 0; j < top; j++) {
      m[i][j] = "0";
      cel= table.rows[i].cells[j].querySelector("button");
      cel.style.backgroundImage = "url(none.jpg)"
    }
  }
  do {
    lvl = Number(prompt("choose how many bombs u want(1-99):", "10"));
  } while (lvl < 1 || lvl > 99);
  //lvl =showPrompt("choose how many bombs u want(1-99):", "20",lvl < 1 || lvl > 99)
  score = 0;
  maxFlags = lvl;
  document.getElementById("flags").innerHTML=maxFlags;
  flags=0
  lose = false;
  bombs = 0;
  
  do {
    let x= Math.trunc(Math.random() * 10);
    let y = Math.trunc(Math.random() * 10);
    cel = table.rows[x].cells[y].querySelector("button");
    if (m[x][y] !== "💣") {
      //cel.style.backgroundImage = "url(💣.jpg)";
      m[x][y] = "💣";
      bombs++;
    }
  } while (bombs < lvl);
  for (let i = 0; i < top; i++) {
    for (let j = 0; j < top; j++) {
      if (m[i][j] === "💣") {
       add(m, i, j, top);
      }
    }
  }
  for (let i = 0; i < top; i++) {
    for (let j = 0; j < top; j++) {
      //console.log(m +" i :"+j);
     
      cel = table.rows[i].cells[j].querySelector("button");
      //cel.innerHTML = m[i][j];
    }
  }
}

initial(10);

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}