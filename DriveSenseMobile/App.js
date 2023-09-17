import React, { useEffect, useState, createContext } from "react";
import { StyleSheet, Text, View } from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import HomeScreen from "./Views/HomePage";
import MapLocation from "./Views/MapLocation";
import AuthPage from "./Views/Auth";
import SmartRecording from "./Views/SmartRecording";
const Stack = createNativeStackNavigator();
export const UserContext = createContext();

export default function App() {
  const [user, setUser] = useState({ name: "Krish", previous_score: 100 });

  return (
    <UserContext.Provider value={[user, setUser]}>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="AuthPage">
          <Stack.Screen
            name="AuthPage"
            component={AuthPage}
            options={{ headerShown: false }}
          />
          <Stack.Screen name="DriveSense" component={HomeScreen} />
          <Stack.Screen name="MapLocation" component={MapLocation} />
          <Stack.Screen name="SmartRecording" component={SmartRecording} />
        </Stack.Navigator>
      </NavigationContainer>
    </UserContext.Provider>
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
    fontSize: 30,
    fontWeight: "bold",
  },
});
