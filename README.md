# WebMail-less-Mailing-and-Designing-IITK-Flix

This project demonstrates various network programming functionalities using Python socket programming, email sending, and video streaming. It is divided into two main sections: **End Term Projects** and **Mid Term Projects**.

---

## End Term Projects

### IITK-Webmail
A Python script that sends an email (with optional CC, BCC, and file attachments) using the IITK SMTP server.

- **Configuration:**  
  Update your `sender_email` and `sender_password` in [End_Term/IITK-Webmail.py](End_Term/IITK-Webmail.py). Set the recipient and attachment details as needed.
- **Usage:**
    ```sh
    python End_Term/IITK-Webmail.py
    ```

### Chat Box
A UDP-based chat application to communicate between your PC and a phone.

- **Configuration:**  
  Modify the `phone_ip` and `phone_port` in [End_Term/Chat Box.py](End_Term/Chat Box.py) to match your phone's settings. Ensure the PC's IP and port are correctly set.
- **Usage:**
    ```sh
    python "End_Term/Chat Box.py"
    ```

---

## Mid Term Projects

### UDP Server & Client

- **UDP Server:**  
  [Mid_Term/UDP_SERVER.py](Mid_Term/UDP_SERVER.py) receives a message, converts it to uppercase, and sends it back.
- **UDP Client:**  
  [Mid_Term/UDP_CLIENT.py](Mid_Term/UDP_CLIENT.py) sends a lowercase string to the server and prints the uppercase response.
- **Usage:**
    1. Start the server:
        ```sh
        python Mid_Term/UDP_SERVER.py
        ```
    2. In another terminal, run the client:
        ```sh
        python Mid_Term/UDP_CLIENT.py
        ```

### TCP Server & Client

- **TCP Server:**  
  [Mid_Term/TCP_SERVER.py](Mid_Term/TCP_SERVER.py) listens for connections, converts received messages to uppercase, and sends them back.
- **TCP Client:**  
  [Mid_Term/TCP_CLIENT.py](Mid_Term/TCP_CLIENT.py) connects to the server, sends a lowercase string, and prints the uppercase message received.
- **Usage:**
    1. Start the server:
        ```sh
        python Mid_Term/TCP_SERVER.py
        ```
    2. In another terminal, run the client:
        ```sh
        python Mid_Term/TCP_CLIENT.py
        ```

### FLIX Video Streaming

- **FLIX Server:**  
  [Mid_Term/FLIX_SERVER.py](Mid_Term/FLIX_SERVER.py) captures webcam video, pickles each frame, and streams it over TCP.
- **FLIX Client:**  
  [Mid_Term/FLIX_CLIENT.py](Mid_Term/FLIX_CLIENT.py) connects to the server, receives the video frames, unpickles them, and displays the video.
- **Usage:**
    1. Run the server:
        ```sh
        python Mid_Term/FLIX_SERVER.py
        ```
    2. In another terminal or on a client machine, run:
        ```sh
        python Mid_Term/FLIX_CLIENT.py
        ```
- **Requirements:**  
  Make sure you have OpenCV installed:
    ```sh
    pip install opencv-python
    ```

---

## General Notes

- **Python Version:** All scripts are written in Python.
- **Network Settings:** Update IP addresses and port numbers as necessary.
- **Email Credentials:** For the email script, update the sender credentials in [End_Term/IITK-Webmail.py](End_Term/IITK-Webmail.py) with valid details.