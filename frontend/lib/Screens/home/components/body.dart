import 'package:flutter/material.dart';
import 'package:frontend/Screens/Welcome/welcome_screen.dart';


class Body extends StatelessWidget {
  const Body({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery
        .of(context)
        .size;
    return Scaffold(
      appBar: AppBar(title: Text('Welocome')),
      body: Center(
        child: Text('My Page!')),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            DrawerHeader(
              child: Text('Drawe Header'),
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
            ),
            ListTile(
              title: Text('logout'),
              onTap:() {
                Navigator.push(context, MaterialPageRoute(
                  builder: (context){
                    return WelcomeScreen();

                  } )
                  );
              },
            ),
          ],


      ),

      ),

    );
  }
}