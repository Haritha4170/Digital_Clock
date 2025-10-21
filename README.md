# 🕒 Digital Clock using Python  

## 📖 Overview  
This project is a **Digital Clock** built using Python’s **Tkinter GUI library**.  
It displays the **current system time** in hours, minutes, and seconds — updating every second automatically.  
This project demonstrates how real-time GUI applications can be developed using **event-driven programming** in Python.  

---

## 🚀 Features  
✅ Real-time digital clock that updates every second  
✅ Displays time in **12-hour format with AM/PM**  
✅ Beautiful **Tkinter GUI design**  
✅ Lightweight, responsive, and easy to customize  
✅ Beginner-friendly Python mini-project  

---

## 🧠 Concepts Learned  
- GUI Programming using **Tkinter**  
- Working with **time.strftime()** for formatted time  
- Scheduling tasks using **Tkinter’s `after()` method**  
- Event-driven programming  
- Styling GUI widgets (fonts, colors, layouts)  

---

## 🧰 Technologies Used  

| Component | Description |
|------------|-------------|
| 🐍 **Python** | Programming language |
| 🧱 **Tkinter** | GUI library used to build the interface |
| ⏲️ **time module** | Used to get and format the system time |

---

## ⚙️ How to Run  

Follow these simple steps to run the project on your system 👇  

### 1️⃣ Prerequisites  
- Install [Python 3](https://www.python.org/downloads/)  
- Install VS Code or any Python IDE  

### 2️⃣ Clone the Repository  
git clone https://github.com/Haritha4170/Digital_Clock.git
### Navigate to the Project Folder
cd Digital_Clock
### 4️⃣ Run the Script
bash
python digital_clock.py
## 🎉 You’ll see a digital clock window appear showing the live system time.
  
### 🪄 Code Explanation (Simplified)
Import modules — tkinter for GUI, time for fetching current time

Create window — Using Tk() to initialize the main GUI window

Add label — A Label() widget to display time with custom font & color

Define function — A function updates the label every second using strftime()

Use after() method — Schedules the function to refresh every 1000ms

Run loop — root.mainloop() keeps the GUI window active

### 🌟 Future Enhancements
💡 Add date display (Day, Month, Year)
💡 Add alarm functionality
💡 Add stopwatch or timer mode
💡 Include light/dark theme switch
