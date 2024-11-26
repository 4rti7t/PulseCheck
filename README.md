# **NetPulse**: Advanced IP Status Checker 🚀


**NetPulse** is your go-to tool for efficiently checking the status of multiple IP addresses. Whether you're troubleshooting network issues or performing a security audit, this advanced Python tool provides a real-time, interactive experience to help you categorize **Live** and **Dead** IPs in style.

---

## 🌟 **Features**  
- **Real-Time Progress**: See the ping process live with a stylish progress spinner.
- **Elegant Output**: Beautifully formatted results using the `rich` library, showing IPs in **Live** and **Dead** tables.
- **Cross-Platform**: Supports Windows, macOS, and Linux systems.
- **Error Handling**: Gracefully handles file errors and ping issues with user-friendly messages.
- **Sleek Branding**: Interactive console with a modern ASCII logo.

---

## 🛠️ **Installation**  

**### 1. Clone or Download the Repository**
```
git clone https://github.com/4rti7t/PulseCheck.git
cd CheckPulse
```
**REQUIREMENTS:**
```
pip install rich
```
⚡ Usage
```
Create a file with a list of IP addresses (one per line) and name it ips.txt
```

**Run the script:**

```
python3 PulseCheck.py
```

Watch as NetPulse pings the IPs and categorizes them into Live or Dead based on their response.

**🎨 Example Output**

After running the script, you will see a neatly formatted output like this:

**RESULTS:**
```
Live IPs:
+------------------+
|   IP Address     |
+------------------+
| 192.168.1.1      |
| 10.0.0.5         |
+------------------+

Dead IPs:
+------------------+
|   IP Address     |
+------------------+
| 192.168.1.100    |
+------------------+
```
![Screenshot_2024-11-27_00_19_28](https://github.com/user-attachments/assets/adab82bc-3172-4806-9027-502a5fd828aa)



**💡 Contributing**

We welcome contributions! Feel free to fork the repo, create a new branch, and submit a pull request. Any improvements, bug fixes, or feature requests are highly appreciated.

**📄 License**

```This project is licensed under the MIT License. See the LICENSE file for details.```

**🤝 Credits**
Logo: Custom ASCII art (coming soon).
Technology Stack: Python, rich library for interactive output, and subprocess for system commands.

**🆘 Support**

If you encounter any issues, don't hesitate to open an issue. We're happy to help!

Thanks for using NetPulse! 🌍
Stay efficient, stay connected. 😎
