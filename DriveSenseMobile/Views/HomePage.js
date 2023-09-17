import { View, Text, Image, TouchableOpacity } from "react-native";
import { useState, useEffect, useContext } from "react";
import { UserContext } from "../App";
import Logo from "../assets/DriveSense-logos/DriveSense-logos_transparent.png";
//Start btn, Welcome NAME, Overall score (with visuals), cohere thing
function HomeScreen({ navigation }) {
  const [user] = useContext(UserContext);
  return (
    <View
      style={{
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "white",
      }}
    >
      <Text style={{ fontWeight: "bold", fontSize: 30 }}>
        Welcome {user.name} 👋
      </Text>
      <Image source={Logo} style={{ width: 400, height: 300 }} />
      <View style={{ alignSelf: "left" }}></View>
      <View>
        <TouchableOpacity
          onPress={() => {
            navigation.navigate("MapLocation");
          }}
          style={{
            backgroundColor: "#9453f5",
            padding: 20,
            margin: 20,
            borderRadius: 20,
          }}
        >
          <Text style={{ fontWeight: "bold", color: "#fffceb", fontSize: 20 }}>
            Start Drive
          </Text>
        </TouchableOpacity>
      </View>
      <View>
        <TouchableOpacity
          onPress={() => {
            navigation.navigate("SmartRecording");
          }}
          style={{
            padding: 20,
            margin: 30,
            borderRadius: 20,
            justifyContent: "center",
            alignItems: "center",
            backgroundColor: "#fff4d1",
          }}
        >
          <Text style={{ fontWeight: "bold", color: "#9453f5", fontSize: 20 }}>
            Smart Record
          </Text>
        </TouchableOpacity>
      </View>
      <View>
        <Text style={{ fontWeight: 600, fontSize: 20 }}>
          Current Driving Score:{" "}
          <Text
            style={{
              color:
                user.previous_score > 70
                  ? "#57d984"
                  : user.previous_score > 45
                  ? "#f0ca43"
                  : "#d93114",
              fontSize: 24,
            }}
          >
            {user.previous_score}
          </Text>
        </Text>
      </View>
    </View>
  );
}

export default HomeScreen;
