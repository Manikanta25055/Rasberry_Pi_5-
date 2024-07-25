# Object detection from Hailo Ai Module

- How to detect sample objects from Raspberry pi 5, using raspberry camera module 3 and Hailo Ai 8L entry level Accelerator

### Ingredients
1. Raspberry pi 5
2. Raspberry pi camera module 3
3. Hailo ai accelarator 8L
4. OfficiaL power supply
5. SSD of min 128Gb

To setup the hailo repo to get started
### Clone the Repository
```bash
git clone https://github.com/hailo-ai/hailo-rpi5-examples.git
```
Enter the repository directory:
```bash
cd hailo-rpi5-examples
```

### Environment Configuration
To run the examples, you should ensure your environment is set up correctly. We use the hailo-tappas-core pkgconfig file to get Hailo dependencies.

You can set it all up by sourcing the following script. This script will set the required environment variables and activate Hailo virtual environment (if it doesn't exist, it will create it).
```bash
source setup_env.sh
```

### Requirements Installation
Make sure you are in the virtual environment and run the following command:
```bash
pip install -r requirements.txt
```

### Resources Download
```bash
./download_resources.sh
```
# Detection Example

![detection](https://github.com/user-attachments/assets/e1369279-8dd5-4c93-a4c4-e30885a2e28e)

This is the one of the basic model demonstrated here, it uses YOLOv6n model as default. 

#### To run the example use:
```bash
python basic_pipelines/detection.py --input resources/detection0.mp4
```
- If you want to use your Camera module 3 fro the input
   ```bash
   python basic_pipelines/detection.py --input rpi
   ```
   - The rpi command takes the input from the camera module 3, make sure that the hardware is correctly set up otherwise you may encounter an error for the camera usage.
   
##### To close the application press 'Ctrl+C'.

For additional options run:
```bash
python basic_pipelines/detection.py --help
```

# Connect to the pi

1. You can use the official Raspberry pi connect to connect to the pi, you can read the documentation here
```
https://www.raspberrypi.com/documentation/services/connect.html

```
2. You can connect it via a HDMI cable to the external monitor (suggested way to get the best output)
3. You can use SSH to connect to the pi from your terminal(macOS) or powershell(windows)
   - command is
     ```bash
     ssh <username>@<hostname>
     ```
     to connect with the ssh, you must have edited the settings from the imager when you were downloading the os to the pi, youcan watch the detailed video in here

      ```
      https://youtu.be/VFlZ7Twkkmg?feature=shared

      ```
      









