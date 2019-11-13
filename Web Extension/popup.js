

function transfer(){	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
	   	tablink = tab.url;
		$("#p1").text("The URL being tested is - "+tablink);

		var xhr=new XMLHttpRequest();
		params="url="+tablink;
        // alert(params);
		var markup = "url="+tablink+"&html="+document.documentElement.innerHTML;
		xhr.open('POST','http://localhost/extension/clientserver.php',false );
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhr.send(markup);
		$("#div1").text(xhr.responseText);
		return xhr.responseText;
	});
}


$(document).ready(function(){
    $("button").click(function(){	
		var url = transfer();
    });
});

chrome.tabs.getSelected(null,function(tab) {
   	var tablink = tab.url;
	$("#p1").text("The URL being tested is - "+tablink);
});
