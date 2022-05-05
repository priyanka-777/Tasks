 let list1 = [];
    let list2 = [];
    let list3 = [];
    let list4 = [];
    let list5 = [];

    let n = 1;
    let x = 0;
    function AddRow(){
        let AddRown = document.getElementById("show");
        let  NewRow = AddRown.insertRow(n);

        list1[x] = document.getElementById("fname").value;
        list2[x] = document.getElementById("lname").value;
        list3[x] = document.getElementById("aadhar").value;
        list4[x] = document.getElementById("mail").value;
        list5[x] = document.getElementById("phone").value;
	  if(!list1[x] || !list2[x] || !list3[x] || !list4[x] || !list5[x]){
        alert("please fill all fields");
        return;
    }

        let cell1 = NewRow.insertCell(0);
        let cell2 = NewRow.insertCell(1);
        let cell3 = NewRow.insertCell(2);
        let cell4 = NewRow.insertCell(3);
        let cell5 = NewRow.insertCell(4);

        cell1.innerHTML = list1[x];
        cell2.innerHTML = list2[x];
        cell3.innerHTML = list3[x];
        cell4.innerHTML = list4[x];
        cell5.innerHTML = list5[x];

        n++;
        x++;
    }
