```markdown
# 🔍 Advanced OSINT Tool

A powerful Python-based OSINT (Open Source Intelligence) tool for extracting comprehensive contact information and personal details
from websites. This CLI tool helps you find domain ownership details, contact information, social media profiles, and more.

## 🌟 Features

- **Domain WHOIS Information** - Get registrar details, creation date, expiration date
- **Contact Extraction** - Extract emails and phone numbers from websites
- **Social Media Discovery** - Find linked social media profiles
- **DNS Record Analysis** - View A, MX, NS, and TXT records
- **Comprehensive Scraping** - Deep scan of contact, about, and team pages
- **Dual Export Formats** - Save results in both TXT and CSV formats
- **Batch Processing** - Analyze multiple websites from a text file

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/advanced-osint-tool.git
cd advanced-osint-tool
```

2. **Create virtual environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

1. **Run the tool**
```bash
python advanced_osint.py
```

2. **Choose an option from the menu**
   - Option 1: Analyze websites from a text file
   - Option 2: Analyze a single website
   - Option 3: Exit

### Analyzing Multiple Websites

1. **Create a text file with website URLs**
```bash
echo "example.com
google.com
github.com" > websites.txt
```

2. **Run the tool and select option 1**

### Analyzing Single Website

1. **Run the tool and select option 2**
2. **Enter the website URL when prompted**

## 🛠️ Commands Reference

### Setup Commands
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Linux/Mac)
source venv/bin/activate

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Deactivate virtual environment
deactivate
```

### Tool Usage Commands
```bash
# Run the OSINT tool
python advanced_osint.py

# Run with basic version
python osint_simple.py
```

## 📊 Output Examples

### Sample Results Display
```
🎯 COMPLETE OSINT REPORT FOR: https://example.com
================================================================================

📋 DOMAIN REGISTRATION INFORMATION:
--------------------------------------------------
   👤 Registrant Name: John Doe
   🏢 Organization: Example Inc.
   📧 Contact Emails: admin@example.com, john@example.com

📞 CONTACT INFORMATION:
--------------------------------------------------
   📧 Email Addresses Found:
      • contact@example.com
      • support@example.com

🌐 SOCIAL MEDIA PROFILES:
--------------------------------------------------
   🔗 Facebook:
      • facebook.com/examplepage
```

## 🔧 Dependencies

- `requests` - HTTP requests for web scraping
- `beautifulsoup4` - HTML parsing and data extraction
- `whois` - Domain WHOIS information lookup
- `dnspython` - DNS record analysis

## ⚠️ Legal Disclaimer

This tool is intended for:
- Security research and penetration testing
- Investigating your own websites
- Educational purposes
- Legitimate OSINT activities

**Please use responsibly and ethically:**
- Only scan websites you own or have permission to test
- Respect robots.txt files and terms of service
- Comply with local laws and regulations
- Do not use for malicious purposes

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

2. **WHOIS lookup fails**
   - Some domains have restricted WHOIS information
   - Tool will continue with other data extraction

### Virtual Environment Issues

```bash
# If virtual environment doesn't activate
python -m venv venv --copies
source venv/bin/activate

# If packages aren't installing
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

## 📄 License

This project is licensed under the MIT License.

---

**⭐ If you find this tool useful, please give it a star on GitHub!**
```
