import React, { useEffect, useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  Image,
  TouchableOpacity,
  KeyboardAvoidingView,
  ScrollView,
} from "react-native";
import Logo from "../assets/DriveSense-logos/DriveSense-logos_transparent.png";

const AuthPage = ({ navigation }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {});

  return (
    <KeyboardAvoidingView behavior={"padding"} style={styles.container}>
      <ScrollView alwaysBounceHorizontal={false} alwaysBounceVertical={true}>
        <Image
          source={Logo}
          style={{
            width: 400,
            height: 300,
            padding: 20,

            alignSelf: "center",
          }}
        />
        <View>
          <View>
            <Text
              style={{
                fontSize: 30,
                fontWeight: 200,
                padding: 50,
                alignSelf: "center",
              }}
            >
              Login to DriveSense
            </Text>
          </View>
          <View style={{ flex: 1, alignItems: "center" }}>
            <TextInput
              style={styles.input}
              placeholder="Email"
              value={email}
              onChangeText={setEmail}
            />
            <TextInput
              style={styles.input}
              type="password"
              placeholder="Password"
              value={password}
              onChangeText={setPassword}
              secureTextEntry={true}
            />
            <TouchableOpacity
              onPress={() => {
                navigation.navigate("DriveSense");
              }}
              style={{
                backgroundColor: "#121212",
                padding: 20,
                borderRadius: 10,
                marginTop: 50,
              }}
            >
              <Text style={{ color: "white", fontWeight: "bold" }}>LOGIN</Text>
            </TouchableOpacity>
          </View>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
};

export default AuthPage;

const styles = StyleSheet.create({
  input: {
    width: 300,
    height: 50,
    borderRadius: 10,
    backgroundColor: "#d0d3d9",
    padding: 10,
    margin: 20,
    fontSize: 18,
    // fontFamily: "Roboto",
    // fontWeight: "bold",
    // fontStyle: "normal",
    // textAlign: "left",
  },
  container: {
    flex: 1,
  },
});
