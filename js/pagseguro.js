function spoilerBtt(typeBtt) {

	spoiler = document.getElementsByClassName('spoiler');

		for (i = 0; i < spoiler.length; i++) {

		if (spoiler[i].id == typeBtt) {
			spoiler[i].style.display = 'inline';
		} 
		else { 
			spoiler[i].style.display = 'none';
		}

		if (document.getElementsByClassName('typeBtt')[i].id == 'btt'+typeBtt){
				document.getElementById('btt'+typeBtt).disabled = true;
			}
			else{
				document.getElementsByClassName('typeBtt')[i].disabled = false;
			}
	}

}

function goToNewPage(dropdownlist)
 {
 var url = dropdownlist.options[dropdownlist.selectedIndex].value;
 if (url != "")
 {
 window.open(url);
 }
 }

 document.getElementById("submit").onclick = goToNewPage(document.dropdown[1].list);
 document.getElementById("submit").setAttribute("onclick'","goToNewPage(document.dropdown[1].list);");
 document.getElementById("bttSUB").onclick = spoilerBtt('SUB');
 document.getElementById("bttSUB").setAttribute("onclick","spoilerBtt('SUB');");
 document.getElementById("bttPUB").onclick = spoilerBtt('PUB');
 document.getElementById("bttPUB").setAttribute("onclick","spoilerBtt('PUB');");