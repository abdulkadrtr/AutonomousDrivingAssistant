# AutonomousDrivingAssistant
The vehicle assistant is capable of engaging in verbal communication with you, comprehending your dialogue, and establishing goals for the vehicle.
![People (1)](https://user-images.githubusercontent.com/87595266/226173442-ccfb2b4a-7c36-44e5-9443-59911ba8064b.png)

# About the project

This is an autonomous driving assistant project created using a Turkish natural language model. The project utilizes Google Speech-to-Text service to recognize your speech and Google Text-to-Speech service to communicate with you verbally. Your conversations are processed and comprehended by a natural language model we designed, allowing the autonomous vehicle assistant to understand where you want to go.

We are using the ROS2 system to implement the project, and utilizing the Webots Tesla model for the simulation environment. Additionally, our own KNN artificial intelligence model is employed in the project to enable an autonomous vehicle to exit a narrow parallel parking space.

To see the project details and demo video, please watch the Youtube video.

# Youtube Project Introduction & Demo

https://youtu.be/kXKoH2fnbSc

# How to Create a Project Environment ?

To run the project, you will need the ROS2 Humble and webots_ros2 packages, as well as the webots simulation environment. 
Please follow the instructions below. These instructions assume that you have installed ROS2 Humble and the Webots simulation environment.

- Create a ros2_ws folder and create an src folder inside the directory. Then, follow the instructions under the 'Install webots_ros2 from sources' section in the link below.

    [Install webots_ros2 from sources](https://github.com/cyberbotics/webots_ros2/wiki/Linux-Installation-Guide#install-webots_ros2-from-sources)
   
- Move the `tesla_voice_control` package to the `ros2_ws/src/webots_ros2/` directory. This package will enable you to launch the simulation environment.

- Afterwards, move the `voice_control` package to the `ros2_ws/src/` directory, as it is necessary for launching your autonomous driving assistant.

## Getting Started

1. In your working directory, compile the project using `colcon build` within the `ros2_ws` directory.
2. Launch the robot by running the command `ros2 launch tesla_voice_control robot_launch.py` in one terminal.
3. In another terminal, run `ros2 run voice_control voice_control` to start the driving assistant.
4. Test the demo by saying "I want to go home" aloud. The autonomous vehicle will exit the parking space and drive towards your home, eventually coming to a stop.

The 'data.csv' file contains the dataset created for using the Turkish natural language model.
