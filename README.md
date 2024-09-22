# AIKeyboard 🖐💻

Happy typing without a keyboard! 😄

AI-powered virtual keyboard using hand gesture detection, built with Python and OpenCV.

## Overview

AIKeyboard is a virtual keyboard that uses a webcam to detect hand gestures for typing. It leverages computer vision techniques to track hand movements and allows users to type without a physical keyboard.

## Features

- **Hand Gesture Detection**: Uses OpenCV and `cvzone.HandTrackingModule` to detect hands and fingertips.
- **Virtual Typing**: Simulates keypresses based on finger positioning and gestures.
- **Customizable Keys**: Includes common alphabetic characters, space, and backspace keys.

## Tech Stack

- **Python**: Core programming language used.
- **OpenCV**: For webcam access and hand tracking.
- **cvzone**: For additional hand tracking and utilities.
- **pynput**: To simulate actual keyboard presses.

## How It Works

1. The webcam captures hand movements.
2. The `HandDetector` module identifies fingertips and positions.
3. You have to just pinch on the keyboard with your thumb and index finger, the corresponding key is pressed.
4. The result is displayed in real-time on the screen.

This is the current layout of the keyboard:

Q W E R T Y U I O P
A S D F G H J K L ;
Z X C V B N M , . /
[SPACE] [BACKSPACE]

## Requirements

Install the required Python packages:

```bash
pip install opencv-python
pip install cvzone
pip install pynput

