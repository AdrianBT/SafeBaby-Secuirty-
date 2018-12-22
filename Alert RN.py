import React, { Component } from "react";
import { Text, TouchableOpacity, View } from "react-native";
import Dialog from "react-native-dialog";
 
export default class DialogTester extends Component {
  state = {
    dialogVisible: false
  };
 
  showDialog = () => {
    this.setState({ dialogVisible: true });
  };
 
  handleNo = () => {
    this.setState({ dialogVisible: false });
  };

  if (handleCancel == onPress)
    {
      return <h1> Okay <h1>
    }

  handleYes = () => {
    this.setState({ dialogVisible: false });
  };

  if (handleCancel == onPress)
    {
      return <h1> We will notify you again in a few minites <h1>
    }


render() {
  const blurComponentIOS = (
    <BlurView
      style={StyleSheet.absoluteFill}
      blurType="xlight"
      blurAmount={50}
    />
  )
  return (
    <View style={styles.container}>
      <Dialog.Container
        visible={this.state.dialogVisible}
        blurComponentIOS={blurComponentIOS}
      >
        <Dialog.Title>Baby in the car</Dialog.Title>
        <Dialog.Description>
          Did you leave your baby in the car?.
        </Dialog.Description>
        <Dialog.Button label="Yes" onPress={this.handleYes} />
        <Dialog.Button label="No" onPress={this.handleNo} />
      </Dialog.Container>
    </View>
  );
}
