document.getElementsByName('q')[0].focus();
document.getElementsByName('q')[0].value='people at university at buffalo';
var ev = document.createEvent('KeyboardEvent'); 
ev.initKeyEvent( 'keydown', true, true, window, false, false, false, false, 13, 0); 
document.body.dispatchEvent(ev);