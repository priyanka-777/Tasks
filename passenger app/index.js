let count = 0
let saveEl = document.getElementById("save-el")
let countEl = document.getElementById("count-el")
function increment() {
    count += 1
    countEl.textContent = count
}
function incrementby5() {
    count += 5
    countEl.textContent = count
}
function decrement(){
	count-=1
	countEl.textContent=count
}
function save() {
    if(count!=0){
        let countStr = count + " - "
        saveEl.textContent=saveEl.textContent+countStr
        countEl.textContent = 0
        count = 0
    }
}
function reset(){
    countEl.textContent = 0
    count = 0
    saveEl.textContent="PREVIOUS ENTRIES:"
}

function input(){
    let value=document.getElementById("values").value
    if(value==parseInt(value)){
     count=parseInt(count)+parseInt(value)   
     countEl.textContent=count
    }
    else{
        alert("u entered a wrong type of input!\nplease give correct input type!");
    }
     value=0;
}
console.log("Let's count people on the subway!")
