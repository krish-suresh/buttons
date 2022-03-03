import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
// import 'firebase_options.dart';
// import 'package:cloud_firestore/cloud_firestore.dart';

void main() {
  // WidgetsFlutterBinding.ensureInitialized();
  // await Firebase.initializeApp(
  //   options: DefaultFirebaseOptions.currentPlatform,
  // );
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              StatusBox(
                color: Colors.green,
                text: "Open",
              ),
              StatusBox(
                color: Colors.red,
                text: "Busy",
              ),
              StatusBox(
                color: Colors.orange,
                text: "Waiting",
              )
            ],
          ),
          // StreamBuilder(
          //     stream: FirebaseFirestore.instance
          //         .collection('machines')
          //         .doc('DUQrTjlWeTT2DAdupQzp')
          //         .snapshots(),
          //     builder: (BuildContext context,
          //         AsyncSnapshot<DocumentSnapshot> snapshot) {
          //       if (snapshot.hasError) {
          //         return Text('Something went wrong');
          //       }

          //       if (snapshot.connectionState == ConnectionState.waiting) {
          //         return Scaffold(
          //           body: Center(child: CircularProgressIndicator()),
          //         );
          //       }
          //       Map<String, dynamic> data =
          //           snapshot.data!.data() as Map<String, dynamic>;
          //       return Column(
          //         mainAxisAlignment: MainAxisAlignment.center,
          //         children: [
          //           DefaultTextStyle(
          //             style: TextStyle(color: Colors.black, fontSize: 12),
          //             child: Text(data['room'] +
          //                 " " +
          //                 data['machine_type'] +
          //                 " " +
          //                 data['machine_id'].toString()),
          //           ),
          //           StatusBox(
          //             color: data['status'] == "open"
          //                 ? Colors.green
          //                 : (data['status'] == "busy"
          //                     ? Colors.red
          //                     : Colors.orange),
          //           ),
          //         ],
          //       );
          //     })
        ],
      ),
    );
  }
}

class StatusBox extends StatelessWidget {
  const StatusBox({Key? key, this.color = Colors.red, this.text = ""})
      : super(
          key: key,
        );
  final Color color;
  final String text;
  @override
  Widget build(BuildContext context) {
    return DecoratedBox(
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        border: Border.all(width: 5.0, color: Colors.white),
      ),
      child: Padding(
        padding: EdgeInsets.all(32.0),
        child: Container(
          width: 50.0,
          height: 50.0,
          child: Container(
            decoration: new BoxDecoration(
              color: color,
              shape: BoxShape.rectangle,
              borderRadius: BorderRadius.all(Radius.circular(8.0)),
            ),
            child: Center(
              child: DefaultTextStyle(
                style: TextStyle(color: Colors.white, fontSize: 12),
                child: Text(
                  text,
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
