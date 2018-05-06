var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var PythonShell = require('python-shell');

// create a pyshell object to run your script, im not sure if this takes inputs tho, still looking
var pyshell = new PythonShell('mat_to_image.py'); 


app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');;
});


io.on('connection', function(socket){
  console.log('device connected');
  socket.on('disconnect', function(){
    console.log('device disconnected');
  });
});
    
pyshell.on('message', function (message) {  
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message); // prints to server shell whatever would have been printed on idle shell
});

io.on('connection', function(socket){

  socket.on('sendMatrix', function(obj) {

    PythonShell.run('mat_to_image.py', {args: [obj]}, function (err, results) {

      if (err) throw err;
    });
    
    PythonShell.run('recognizer.py', {}, function (err, results) {

      if (err) throw err;

      console.log(results);
    });
  });
});


http.listen(8888, function(){
  console.log('listening on *:8888');
});