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
