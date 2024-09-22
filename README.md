# Hack the North 2023 Winner: Drive Sense

## Inspiration:
Our inspiration for this app comes from the critical need to improve road safety and assess driver competence, especially under various road conditions. The alarming statistics on road accidents and fatalities, including those caused by distracted driving and poor road conditions, highlight the urgency of addressing this issue. We were inspired to create a solution that leverages technology to enhance driver competence and reduce accidents.

## What it does
Our app has a frontend, which connects to a GPS signal and tracks a given car's acceleration and speed. Such a React frontend also encompasses a Map, as well as a record feature, which, through the implementation of an LLM by Cohere, is capable of detecting and alerting police, in the event of any speech that may be violent, or hateful, given road conditions. We have numerous algorithms and computer vision on the backend that were fine-tuned upon YOLOv5 and YOLOv8. These models take in an image through a camera feed, surrounding cars, the color of the surrounding traffic lights, and the size of the car plates in front of the drivers. By detecting car plates, we can infer the acceleration of a car (based on the change in the size of the car plates) and can assess the driver's habits. By checking for red lights, correlated with the GPS data, we can determine a driver's reaction time and give a rating for a driver's capacities. Finally, an eye-tracking model can determine a driver's concentration and focus on the road. All this paired with its interactive mobile app makes our app the ultimate replacement for any classic dashcam and protects the driver from the road's hazards.

https://www.youtube.com/watch?v=G3tUnQWzXzw

https://devpost.com/software/drive-sense

![Processed Image](processed.png)

