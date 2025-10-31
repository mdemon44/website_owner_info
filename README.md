<body>
  <div class="wrap">
    <div class="badges" aria-hidden="true">
      <img src="https://img.shields.io/badge/Team-Pentadex-blue?style=for-the-badge" alt="Team Pentadex" class="badge">
      <img src="https://img.shields.io/badge/Version-1.0-green?style=for-the-badge" alt="Version 1.0" class="badge">
      <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge" alt="Python 3.8+" class="badge">
      <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License MIT" class="badge">
    </div>
  </body>
## 🚀 Overview Enterprise OSINT Intelligence Platform is a comprehensive, professional-grade open source intelligence tool designed for security researchers, penetration testers, and digital forensics experts. This tool provides advanced capabilities for gathering intelligence from various online sources with a user-friendly command-line interface. ## ✨ Features ### 🔍 Core Intelligence - **Single Target Analysis** - Deep analysis of individual targets - **Batch Processing** - Analyze multiple targets simultaneously - **Domain Intelligence** - WHOIS lookup and domain information - **Website Scraping** - Automated data extraction from websites - **Email & Phone Extraction** - Automated contact information gathering ### 🛠️ Advanced Capabilities - **Multi-API Integration** - Support for 8+ intelligence APIs - **Real-time Monitoring** - Live data processing and analysis - **Threat Assessment** - Security risk evaluation - **Data Verification** - Automated data validation - **Report Generation** - Professional intelligence reports ### 🎯 Supported Targets - 🌐 Websites & Domains - 📧 Email Addresses - 📞 Phone Numbers - 🏢 Organizations - 🔗 Social Media Profiles - 📍 IP Addresses ## 📋 Requirements ### System Requirements - **OS**: Windows 10/11, Linux, macOS - **Python**: 3.8 or higher - **RAM**: 4GB minimum (8GB recommended) - **Storage**: 500MB free space ### Python Dependencies
txt
requests>=2.31.0
whois>=0.9.3
beautifulsoup4>=4.12.2
dnspython>=2.4.2
urllib3>=2.0.4
cryptography>=41.0.4
colorama>=0.4.6
python-whois>=0.8.0
## 🛠️ Installation ### Method 1: Quick Install (Recommended) 1. **Clone the Repository**
bash
git clone https://github.com/mdemon44/website_owner_info/tree/main
cd website_owner_info
2. **Create Virtual Environment**
bash
python -m venv venv
3. **Activate Virtual Environment** - **Windows:**
bash
venv\Scripts\activate
- **Linux/macOS:**
bash
source venv/bin/activate
4. **Install Dependencies**
bash
pip install -r requirements.txt
### Method 2: Manual Installation 1. **Install Python Dependencies**
bash
pip install requests whois beautifulsoup4 dnspython cryptography colorama
2. **Run the Tool**
bash
python info.py
## 🎮 Usage ### First Time Setup When you run the tool for the first time, it will automatically: - ✅ Check system dependencies - ⚙️ Run setup wizard - 🔑 Guide you through API configuration - 💾 Save configuration for future use ### Main Menu Options
┌──────────────────────────────────────────────────┐
│                 MAIN OPERATIONS                  │
├──────────────────────────────────────────────────┤
│  1. 🚀 Single Target Analysis                   │
│  2. 📁 Batch Analysis                           │
│  3. ⚙️  System Configuration                    │
│  4. 📊 View Results                             │
│  5. 🛡️  System Health Check                     │
│  0. Exit System                                 │
└──────────────────────────────────────────────────┘
### 1. Single Target Analysis - Enter target URL, domain, or IP address - Choose analysis mode (Quick/Standard/Deep) - View comprehensive intelligence report ### 2. Batch Analysis - Load multiple targets from text file - Process targets in parallel - Generate consolidated reports ### 3. System Configuration - API key management - System settings - Performance tuning ## 🔑 API Configuration ### Supported APIs | API Service | Category | Usage | |-------------|----------|-------| | NumVerify | 📞 Phone Intelligence | Phone number validation | | AbstractAPI | 📞 Phone Intelligence | Phone number lookup | | IPInfo | 🌐 Network Analysis | IP geolocation | | WhoisXMLAPI | 🔍 Domain Intelligence | Domain whois data | | Shodan | 🌐 Network Analysis | Device intelligence | | Hunter.io | 🔍 Domain Intelligence | Email discovery | | SerpAPI | 🤖 Web Automation | Search engine data | | Apify | 🤖 Web Automation | Web scraping | ### API Setup Instructions 1. **Access API Configuration** - Navigate to System Configuration → API Management - Select Configure API Keys 2. **Enter API Keys** - Obtain API keys from respective services - Enter keys in the interactive setup - Test API connectivity 3. **Verification** - Tool validates each API key - Shows active/inactive status - Monitors API usage ## 📊 Output Examples ### Intelligence Report Sample
==================================================
ENTERPRISE OSINT INTELLIGENCE REPORT
Generated: 2024-01-15 14:30:25
Total Results: 1
==================================================

RESULT 1:
Target: https://example.com
Domain: example.com
Time: 2024-01-15T14:30:25

WHOIS Information:
  Registrar: Example Registrar, Inc.
  Created: 2020-01-15
  Organization: Example Organization

Website Data:
  Title: Example Domain
  Status: 200
  Emails: admin@example.com, contact@example.com
  Phones: +1-555-0123, +1-555-0124
## ⚙️ Configuration ### Configuration File The tool automatically creates a configuration file at: - **Linux/macOS**: ~/.professional_osint_config.json - **Windows**: C:\Users\[Username]\.professional_osint_config.json ### Custom Settings - API rate limiting - Output formatting - Data retention policies - Security settings ## 🐛 Troubleshooting ### Common Issues 1. **Dependency Errors**
bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
2. **API Connection Issues** - Verify internet connectivity - Check API key validity - Review rate limits 3. **Permission Errors**
bash
# Run with appropriate permissions
chmod +x info.py
### Logs and Debugging - Check system logs in configuration directory - Enable verbose mode for detailed output - Review API response codes ## 🤝 Contributing We welcome contributions from the security community! ### How to Contribute 1. Fork the repository 2. Create a feature branch 3. Make your changes 4. Submit a pull request ### Development Setup
bash
git clone https://github.com/mdemon44/website_owner_info/tree/main
cd website_owner_info
python -m venv venv
source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
## 📄 License This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. ## 🛡️ Disclaimer This tool is intended for: - ✅ Security research - ✅ Penetration testing (with permission) - ✅ Digital forensics - ✅ Educational purposes **⚠️ Important**: Only use this tool on systems you own or have explicit permission to test. The developers are not responsible for any misuse. ## 📞 Support ### Documentation - 📚 [Full Documentation](docs/) - 🎥 [Video Tutorials](tutorials/) - ❓ [FAQ](docs/FAQ.md) ### Community Support - 💬 [Discord Community](https://discord.gg/pentadex) - 📱 [Telegram Channel](https://t.me/pentadexx) - 🐛 [Issue Tracker](https://github.com/mdemon44) ### Professional Support For enterprise support and custom implementations, contact our team. ## 🙏 Acknowledgments - **Team Pentadex** - Development and maintenance - **Open Source Community** - Libraries and tools - **Security Researchers** - Testing and feedback --- <div align="center"> **Made with ❤️ by Team Pentadex** [![Telegram](https://img.shields.io/badge/Telegram-Join%20Channel-blue?style=for-the-badge&logo=telegram)](https://t.me/pentadexx) [![Website](https://img.shields.io/badge/Website-Visit%20Us-green?style=for-the-badge)](https://emonsec.page.gd) *Stay Secure! 🔒* </div>
## 📁 Additional Files

আপনার GitHub repository এর জন্য নিচের additional files ও create করতে পারেন:

### 1. `requirements.txt`
txt requests>=2.31.0 whois>=0.9.3 beautifulsoup4>=4.12.2 dnspython>=2.4.2 urllib3>=2.0.4 cryptography>=41.0.4 colorama>=0.4.6 python-whois>=0.8.0
### 2. `.gitignore`
gitignore # Virtual environment venv/ .env/ .venv/ # Configuration files *.json *.config # Logs *.log logs/ # Output files *.txt reports/ output/ # OS generated files .DS_Store Thumbs.db # Python cache __pycache__/ *.pyc
### 3. `LICENSE`
text MIT License Copyright (c) 2024 Team Pentadex Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Only for Educational puposses and If this tools used for bad Purpose i'm not responsible for that. 
Thank You 
