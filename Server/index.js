var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////// NEW STUFF ////////////////////////////////////////////////////////
var PythonShell = require('python-shell'); // need to require this package
var pyshell = new PythonShell('script.py'); // create a pyshell object to run your script, im not sure if this takes inputs tho, still looking
// into it
pyshell.send('2');

pyshell.on('message', function (message) {  
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message); // prints to server shell whatever would have been printed on idle shell
});
///////////////////////////////////////////////////////////////////////////////////////////////////


app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');;
});

// app.get('/script', run_python())


io.on('connection', function(socket){
  console.log('device connected');
  socket.on('disconnect', function(){
    console.log('device disconnected');
  });
});
    
io.on('connection', function(socket){

  socket.on('sendMatrix', function(obj) {
    //io.emit('add', obj);

    console.log(obj)
  });
});



http.listen(3000, function(){
  console.log('listening on *:3000');
});