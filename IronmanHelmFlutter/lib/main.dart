import 'dart:convert';
import 'package:flutter/material.dart';
import 'dart:ui';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import 'StudentModel.dart';

var paddingScreen =17;
var one= 10;
var url = "http://10.0.0.5/";

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp])
      .then((value) => runApp(MaterialApp(home: ToDo())));
}

class ToDo extends StatefulWidget {
  @override
  _CounterState createState() => _CounterState();
}

class _CounterState extends State<ToDo> {

  void sendStatus(){
    url = "http://182.0.0.188/SB?Data="+one.toString();
    getStudent();
  }
  void change1()
  {
    one=1;
    sendStatus();
  }
  void change2()
  {
    one=2;
    sendStatus();
  }
  void change3()
  {
    one=3;
    sendStatus();
  }
  void change4()
  {
    one=4;
    sendStatus();
  }
  void change5()
  {
    one=5;
    sendStatus();
  }
  void change6()
  {
    one=6;
    sendStatus();
  }
  void change7()
  {
    one=7;
    sendStatus();
  }
  void change8()
  {
    one=8;
    sendStatus();
  }
  void change9()
  {
    one=9;
    sendStatus();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      appBar: AppBar(
        backgroundColor: Colors.grey,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'images/Logo.png',
              scale: 10,
            ),
            Container(
                padding: const EdgeInsets.all(8.0), child: Text('Ironman'))
          ],
        ),
      ),
      body: SingleChildScrollView(

        child: Column(

            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: <Widget>[
          Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: Padding(
                    padding: const EdgeInsets.only(bottom:60.0),
                    child: FlatButton(
                      child: Text('LiveBild'),
                      color:Colors.orange,
                      onPressed: () {change1();},
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: Padding(
                    padding: const EdgeInsets.only(bottom:60.0),
                    child: FlatButton(
                      child: Text('Servo'),
                      color: Colors.orange,
                      onPressed: () {change2();},
                    ),
                  ),
                ),

                Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: Padding(
                    padding: const EdgeInsets.only(bottom:60.0),
                    child: FlatButton(
                      child: Text('Sprache'),
                      color: Colors.orange,
                      onPressed: () {change3();},
                    ),
                  ),
                ),
              ]),
              Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: <Widget>[
                    Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Padding(
                        padding: const EdgeInsets.only(bottom:10.0),
                        child: FlatButton(
                          child: Text('   T.Servo zu    '),
                          color:Colors.red,
                          onPressed: () {change4();},
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Padding(
                        padding: const EdgeInsets.only(bottom:10.0),
                        child: FlatButton(
                          child: Text('   T.Servo auf   '),
                          color: Colors.red,
                          onPressed: () {change5();},
                        ),
                      ),
                    ),
                  ]),
              Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: <Widget>[
                    Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Padding(
                        padding: const EdgeInsets.only(bottom:30.0),
                        child: FlatButton(
                          child: Text('   T.Livebild an '),
                          color:Colors.red,
                          onPressed: () {change6();},
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Padding(
                        padding: const EdgeInsets.only(bottom:30.0),
                        child: FlatButton(
                          child: Text('   T.Livebild aus'),
                          color: Colors.red,
                          onPressed: () {change7();},
                        ),
                      ),
                    ),
                  ]),
              Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: <Widget>[
                    Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Padding(
                        padding: const EdgeInsets.only(bottom:10.0),
                        child: FlatButton(
                          child: Text('   D. kompilieren  '),
                          color:Colors.yellow,
                          onPressed: () {change8();},
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Padding(
                        padding: const EdgeInsets.only(bottom:10.0),
                        child: FlatButton(
                          child: Text('    Dic. löschen    '),
                          color: Colors.yellow,
                          onPressed: () {change9();},
                        ),
                      ),
                    ),
                  ]),
        ]),
      )
    );
  }
}
Future<StudentModel> getStudent()async{
  final response = await http.get(url);
  }