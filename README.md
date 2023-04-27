# Pomodoro GUI App
Welcome to the Pomodoro GUI App! This app is designed to help you manage your time more effectively using the Pomodoro Technique. The idea behind the Pomodoro Technique is that by breaking work into shorter intervals of 25 minutes, you can improve focus and productivity, and reduce the likelihood of burnout. It is a simple yet effective technique that can be used for a wide range of tasks, from studying and writing to programming and project management. This app provides a simple and easy-to-use interface for implementing the Pomodoro Technique on your computer. It's written completely in Python using the _tkinter_ library.

## Prerequisites
Before you can use the Pomodoro GUI App, you will need to have Python 3.6 or higher installed on your computer. If you don't have Python installed, you can download it from the official website: _https://www.python.org/downloads/_

## Installation
### First way
To install the app, simply clone the repository to your local machine:

`git clone https://github.com/harisbikovic/pomodoro-gui-app.git`

Navigate to your project directory. To run the app, simply run the **_main.py_** file:

`python main.py`

### Second way
If the previous is not your preferred way then do this:
1. Click on the green "Code" button, then select "Download ZIP"
2. Extract the ZIP file to a location of your choice on your computer
3. Navigate to the extracted ZIP file on your computer
4. Double-click the **_main.py_** file


## Using the App
Both of the previous two ways will launch the app window, which displays a timer and controls for starting and stopping the Pomodoro intervals. The default interval length is 25 minutes, with a short break of 5 minutes in between. After 4 Pomodoro intervals, a longer break of 15 minutes is taken.

![image](https://user-images.githubusercontent.com/108518278/233389549-aa961063-1f4a-4b36-8efc-7c9b43222036.png)


![image](https://user-images.githubusercontent.com/108518278/234800479-3d2a7086-f2d8-42ec-bf09-6070347edf23.png)


## Customize the App

If you would like to change the duration of any of the mentioned intervals you
can do so by changing the values in **_main.py_** file: WORK_MIN, 
SHORT_BREAK_MIN and 
LONG_BREAK_MIN.
