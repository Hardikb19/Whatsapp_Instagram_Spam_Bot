function FunctionDispatch(element, eventid) 
{ 
	var mouseEvent = document.createEvent('MouseEvents'); 
	mouseEvent.initEvent(eventid, true, true); 
	element.dispatchEvent(mouseEvent); 
} 

function startTimer() 
{ 
	setTimeout(MessageTrigger, 3000); 
} 

function MessageTrigger() 
{ 

	messageBox = document.querySelectorAll("[contenteditable='true']")[0]; 

	message = "Enter Your Message Body Here";//Your message needs to be placed here, for spaces try using &nbsp eg.. Hardik&nbspBharunt which gives "Hardik Bharunt" as the message

	counter = 10;

    for (i = 0; i < counter; i++) 
    { 
		event = document.createEvent("UIEvents"); 
		messageBox.innerHTML = message.replace(/ /gm, '');
		event.initUIEvent("input", true, true, window, 1); 
		messageBox.dispatchEvent(event); 

		EventExecute(document.querySelector('span[data-icon="send"]'), 'click'); 
	} 
}

var EventExecute = (element, type) => { 
	var event = document.createEvent("MouseEvents"); 
	event.initMouseEvent 
	(type, true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null); 
	element.dispatchEvent(event); 
}; 

contact = "Contact Name"//Add contact name or name of the group as it is

FunctionDispatch(document.querySelector('[title="' + contact + '"]'), 'mousedown'); 

startTimer(); 