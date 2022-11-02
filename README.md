<a name="readme-top"></a>

<br />
<div align="center">
<img src="https://user-images.githubusercontent.com/102517425/194453496-931c1941-ac55-4c3a-a1b0-e1c740b39f45.png" alt="Logo" width="300" height="330">
<!--   <img src="https://user-images.githubusercontent.com/102517425/193991032-0dcdb5fe-1d5d-459a-b9fa-a673cbda4133.png" alt="Logo" width="300" height="330"> -->
</a>

<h2 align="center">chime</h2>

  <p align="center">
    A wind controlled IoT electronic chime device that connects to the internet <br> allowing users to remotely select alternate musical scales.
    <br />
    <br />
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li>
            <a href="#prerequisites">Prerequisites</a>
            <ul>
                <li><a href="#environment">Environment</a></li>
            </ul>
        </li>
        <li><a href="#installation">Installation and Setup</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
<!--     <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



## About The Project

### Built With

[![Python][Python]][Python-url]  
[![Arduino][Arduino]][Arduino-url]
[![Javascript][Javascript]][Javascript-url]
[![React][React]][React-url]
[![Visual studio code][Visual studio code]][Visual studio code-url]  

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

### Prerequisites

#### Environment

- Install pip
- Install npm

### Installation and Setup

1. Clone the repo
   ```sh
   git clone https://github.com/joe-sacco/chime
   ```
2. Install libraries
   ```sh
   pip install
   npm install
   ```
3. Run Python server
   ```sh
   cd python
   uvicorn main:app --reload
   ```
4. Run React Server
    ```sh
    cd client
    npm start
    ```

5. Create Your Own Scales (scales are proprietary)

    ```sh
    cd python
    touch scales.py    
    ```
    Add scales to scale.py.  Syntax:
    
     ```sh
    scale_calm = { 
      "Note Name": number (MIDI value), 
      "Note Name": number (MIDI value) ...
    }
    ```
    Example:
    
    ```sh
    scale_calm = { 
       "A4": 69, 
       "C4": 60 ...
    }
    ```
5. Setup Hardware
    ```sh
    cd arduino    
    ```
    - BEFORE powering the Arduino:
      - Connect wind sensor ground to Arduino ground
      - Connect wind sensor data line to Arduino pin A0
      - Connect wind sensor power to Arduino power
    - Power the Arduino
      - Connect the Arduino to your computer using a USB cable
    - Flash the Arduino
      - Use [Arduino IDE](https://www.arduino.cc/en/software) to run AnalogReadSerial.ino
      
7.  Route computer MIDI output to your choice of sound generator
8.  Connect sound generator to speakers
9.  Place wind sensor outside
10. Run code and enjoy!
    ```sh
    cd python
    python instrument.py
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Roadmap

See the [open issues](https://github.com/joe-sacco/chime/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Developer: [https://github.com/joe-sacco](https://github.com/joe-sacco)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Arduino]: https://user-images.githubusercontent.com/102517425/193999702-341470ee-af1f-435f-91ce-d5de7f1f7695.png
[Arduino-url]: https://www.arduino.cc/
[Javascript]: https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E
[Javascript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[React]: https://img.shields.io/badge/-ReactJs-61DAFB?logo=react&logoColor=white&style=for-the-badge
[React-url]: https://reactjs.org/
[Visual Studio Code]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[Visual Studio Code-url]:https://code.visualstudio.com/
