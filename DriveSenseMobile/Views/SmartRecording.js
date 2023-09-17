import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
} from "react-native";
import { useEffect, useState } from "react";
import axios from "axios";
const SmartRecording = () => {
  const [script, setScript] = useState(
    "Citizen (John): Good afternoon, Officer Smith. Police Officer (Smith): Good afternoon, John. How can I assist you today? John: I wanted to let you know that I've noticed some unusual activity in the neighborhood lately, like some strangers loitering around the park at night. Officer Smith: Thank you for letting us know, John. We always appreciate when citizens like you keep an eye out for their community's safety. Can you provide any descriptions or license plate numbers? John: I didn't get their license plate, but I remember one of them had a distinctive red backpack and another was wearing a baseball cap. Officer Smith: That's helpful information, John. We'll increase patrols in the area, especially during nighttime, and be on the lookout for individuals matching those descriptions. If you notice anything else, please don't hesitate to call us. John: Will do, Officer Smith. I just want our neighborhood to remain safe for everyone. Officer Smith: Your concern is appreciated, and we're here to ensure the safety of our community. If you have any more questions or need assistance with anything else, feel free to reach out. Have a great day, John. John: Thank you, Officer Smith. You too!"
  );
  const [recording, setRecording] = useState(false);
  const [feedbackAI, setFeedbackAI] = useState("");

  onPressRecord = async () => {
    setRecording(!recording);
    if (recording) {
    } else {
    }
  };
  const onPressFeedback = () => {
    if (script.length > 0) {
      const options = {
        method: "POST",
        url: "https://api.cohere.ai/v1/generate",
        headers: {
          accept: "application/json",
          "content-type": "application/json",
          authorization: "Bearer iENOH7qq8sRzEe8H02niUSrc5m5RCjKMJLT5GIRi",
        },
        data: {
          num_generations: 1,
          max_tokens: 500,
          //   truncate: "END",
          return_likelihoods: "NONE",
          prompt: `Is this a nice conversation between the police officer and the citizen or does it involve brutality: ${script}`,
          stream: false,
        },
      };

      axios
        .request(options)
        .then(function (response) {
          console.log(response.data);
          console.log(response.data.generations[0].text);
          setFeedbackAI(response.data.generations[0].text);
        })
        .catch(function (error) {
          console.error(error);
          setFeedbackAI(error);
        });
      setFeedbackAI("Loading...");
      return;
    }
    setFeedbackAI("");
    return;
  };
  return (
    <ScrollView
      contentContainerStyle={{
        backgroundColor: "white",
        alignItems: "center",
      }}
    >
      <View>
        <TouchableOpacity
          onPress={onPressRecord}
          style={{
            backgroundColor: "#121212",
            padding: 20,
            borderRadius: 10,
            marginTop: 50,
          }}
        >
          <Text style={{ color: "white", fontWeight: "bold" }}>
            {!recording ? "Start Recording" : "Stop"}
          </Text>
        </TouchableOpacity>
      </View>
      <View>
        <TextInput
          editable={false}
          multiline
          value={script}
          placeholder="Voice Script"
          textAlign={"left"}
          style={{
            backgroundColor: "#dbdbd9",
            margin: 20,
            fontSize: 18,
            width: 340,
            borderRadius: 10,
            padding: 20,
            minHeight: 200,
          }}
        />
        <View>
          <TouchableOpacity
            onPress={onPressFeedback}
            style={{
              backgroundColor: "#5A4AE3",
              padding: 20,
              margin: 10,
              borderRadius: 10,
              marginTop: 50,
              alignItems: "center",
            }}
          >
            <Text style={{ color: "white", fontSize: 20 }}>
              Feedback from AI
            </Text>
          </TouchableOpacity>
          <View style={{ padding: 20, marginBottom: 200 }}>
            <Text style={{ fontSize: 20, textAlign: "justify", padding: 5 }}>
              <Text style={{ fontWeight: "bold" }}>
                {feedbackAI.length ? "AI RESPONSE: " : ""}
              </Text>
              {feedbackAI}
            </Text>
            <Text
              style={{
                color: "green",
                fontWeight: "bold",
                padding: 30,
                fontSize: 30,
                textAlign: "center",
              }}
            >
              {feedbackAI.length && feedbackAI !== "Loading..."
                ? "No issue here!"
                : ""}
            </Text>
          </View>
        </View>
      </View>
    </ScrollView>
  );
};

export default SmartRecording;
