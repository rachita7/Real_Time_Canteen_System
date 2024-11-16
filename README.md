# 🍴 Real-Time Canteen Information System  

Academic Project for CE1003 Introduction to Computational Thinking (NTU)

**For NTU North Spine Food Court**  

This project involves the development of a real-time information system for the NTU North Spine Food Court, designed to help users access important details about the food stalls in the canteen. Built using Python and the **PyQt5** GUI toolkit, the system provides real-time information about stall availability, opening and closing times, menus, and estimated waiting times based on user input.

---

## 📋 Features
- **Stall Information**: Displays information such as the **opening and closing times** of each food stall in the NTU North Spine Food Court.
- **Availability Check**: Allows users to check if a stall is available at a specific, user-defined **date and time**.
- **Menu Display**: Shows the **menu** of the selected stall.
- **Estimated Waiting Time**: Calculates the estimated **waiting time** for a stall based on the **number of people** in the queue, input by the user.
- **User-Friendly GUI**: Designed with **PyQt5** for an intuitive and responsive interface.

---

## ⚙️ Requirements

To run the project, ensure you have the following libraries installed:

- **Python 3.x**
- `PyQt5` (for GUI development)
- `datetime` (for handling date and time)

You can install the necessary libraries using pip:

```bash
pip install PyQt5
```

---

## 🚀 How to Use

1. **Clone the Repository**  
   Clone this repository to your local machine:  
   ```bash
   git clone <repository_url>
   ```

2. **Run the Program**  
   Navigate to the project folder and run the application:  
   ```bash
   python canteen_system.py
   ```

3. **Interact with the System**  
   - **Stall Selection**: Choose a food stall from the list.
   - **Check Availability**: Select the date and time you plan to visit, and the program will tell you whether the stall is available.
   - **Menu**: View the menu of the selected stall.
   - **Waiting Time**: Input the number of people in the queue to get an estimated waiting time.

---

## 💡 Project Details

- **GUI Framework**: The application is built using **PyQt5**, a popular Python binding for the Qt application framework, known for its ease of use and structured framework.
- **Estimated Waiting Time**: The system calculates waiting time based on an estimated number of people in the queue, helping users plan their visits accordingly.
