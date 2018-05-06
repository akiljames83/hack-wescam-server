var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var PythonShell = require('python-shell');


app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');;
});


io.on('connection', function(socket){
  console.log('device connected');
  socket.on('disconnect', function(){
    console.log('device disconnected');
  });
});

var count = 0;
io.on('connection', function(socket){
  
  socket.on('sendMatrix', function(obj) {

    count++;
    //console.log(count);
    
    if (count == 30) {
      
      PythonShell.run('mat_to_image.py', {args: [obj]}, function (err, results) {

        if (err) throw err;
      });
      
      PythonShell.run('recognizer.py', {}, function (err, results) {
  
        if (err) throw err;
  
        io.emit("identity", results);
        console.log(results);
      });

      count = 0;
    }
  });
});


http.listen(8888, function(){
  console.log('listening on *:8888');
});