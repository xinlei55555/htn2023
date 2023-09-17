import * as Location from "expo-location";
import { useState, useEffect } from "react";
import {
  View,
  StyleSheet,
  Text,
  Touchable,
  TouchableOpacity,
  Image,
} from "react-native";
import MapPicture from "../assets/maps.png";

export default function MapLocation({ navigation }) {
  const [location, setLocation] = useState(null);
  const [errorMsg, setErrorMsg] = useState(null);

  useEffect(() => {
    let { status } = Location.requestForegroundPermissionsAsync();
    if (status === "refused") {
      setErrorMsg("Permission to access location was denied");
      return;
    }
    let interval = setInterval(async () => {
      let location = await Location.getCurrentPositionAsync({});
      setLocation(location);
      try {
        let res = await fetch("192.168.140.5:8000/gps", {
          headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
          },
          method: "POST",
          body: JSON.stringify({
            longitude: location.coords?.longitude,
            latitude: location.coords?.latitude,
          }),
        });
      } catch (err) {
        console.log(err);
      }
    }, 500);
    return () => {
      clearInterval(interval);
    };
  }, []);

  let text = "Waiting..";

  if (errorMsg) {
    text = errorMsg;
  } else if (location) {
    text = location;
    text.timestamp = new Date(text.timestamp).toLocaleString();
  }
  return (
    <View style={styles.container}>
      <Image
        source={MapPicture}
        style={{ height: 300, marginBottom: 50 }}
        resizeMode={"contain"}
      />
      <Text style={{ fontWeight: "300", fontSize: 25 }}>
        Time: {text.timestamp}
      </Text>
      <Text style={styles.coord}>Longitude: {text.coords?.longitude}</Text>
      <Text style={styles.coord}>Latitude: {text.coords?.latitude}</Text>
      <Text style={{ fontSize: 20, padding: 30 }}>Tracking...</Text>
      <TouchableOpacity
        style={{
          borderRadius: 15,
          marginTop: 20,
          backgroundColor: "#fc032c",
          padding: 15,
        }}
        onPress={() => {
          navigation.navigate("DriveSense");
        }}
      >
        <Text
          style={{
            fontSize: 25,
            color: "white",
            fontWeight: "bold",
            color: "#fffceb",
          }}
        >
          STOP
        </Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  coord: {
    fontSize: 22,
    fontWeight: "bold",
  },
});
