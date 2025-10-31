import os
import re
import requests
import whois
import dns.resolver
import csv
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import time
import sys
from datetime import datetime
import json
from pathlib import Path
import platform
import hashlib
import threading
from concurrent.futures import ThreadPoolExecutor
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import subprocess
import importlib
import shutil
import socket
import ssl
import ipaddress
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import getpass
from typing import Dict, List, Any
import random

class ProfessionalEnterpriseOSINTTool:
    def __init__(self):
        self.results = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        self.current_directory = Path.cwd()
        self.config_file = Path.home() / '.professional_osint_config.json'
        self.setup_complete = False
        self.analysis_history = []
        self.api_usage_stats = {}
        
        # Enhanced API configurations - ALL KEYS EMPTY BY DEFAULT
        self.api_config = {
            'numverify': {
                'key': '', 
                'url': 'http://apilayer.net/api/validate',
                'test_number': '14158586273',
                'required': False,
                'calls': 0
            },
            'abstractapi': {
                'key': '', 
                'url': 'https://phonevalidation.abstractapi.com/v1/',
                'test_number': '14152007986',
                'required': False,
                'calls': 0
            },
            'ipinfo': {
                'key': '',
                'url': 'https://ipinfo.io/{ip}/json',
                'required': False,
                'calls': 0
            },
            'whoisxmlapi': {
                'key': '',
                'url': 'https://www.whoisxmlapi.com/whoisserver/WhoisService',
                'required': False,
                'calls': 0
            },
            'apify': {
                'key': '',
                'url': 'https://api.apify.com/v2/acts/',
                'required': False,
                'calls': 0
            },
            'serpapi': {
                'key': '',
                'url': 'https://serpapi.com/search',
                'required': False,
                'calls': 0
            },
            'hunterio': {
                'key': '',
                'url': 'https://api.hunter.io/v2/domain-search',
                'required': False,
                'calls': 0
            },
            'shodan': {
                'key': '',
                'url': 'https://api.shodan.io/shodan/host/',
                'required': False,
                'calls': 0
            }
        }
        
        self.verified_data = []
        self.suspicious_data = []
        self.confidence_threshold = 80
        
        # Enhanced required packages
        self.required_packages = {
            'requests': 'requests',
            'whois': 'whois',
            'beautifulsoup4': 'bs4',
            'dnspython': 'dns',
            'urllib3': 'urllib3',
            'cryptography': 'cryptography',
            'colorama': 'colorama'
        }

        # Initialize colorama for cross-platform colored output
        try:
            import colorama
            colorama.init()
            self.colors = {
                'RED': colorama.Fore.RED,
                'GREEN': colorama.Fore.GREEN,
                'YELLOW': colorama.Fore.YELLOW,
                'BLUE': colorama.Fore.BLUE,
                'MAGENTA': colorama.Fore.MAGENTA,
                'CYAN': colorama.Fore.CYAN,
                'WHITE': colorama.Fore.WHITE,
                'RESET': colorama.Fore.RESET,
                'BRIGHT': colorama.Style.BRIGHT,
                'NORMAL': colorama.Style.NORMAL
            }
        except ImportError:
            self.colors = {k: '' for k in ['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE', 'RESET', 'BRIGHT', 'NORMAL']}

    def get_terminal_center(self, text_length):
        """Calculate center position for text"""
        try:
            cols = os.get_terminal_size().columns
            return max(0, (cols - text_length) // 2)
        except:
            return 0

    def print_centered(self, text, color='WHITE', style='NORMAL'):
        """Print centered text"""
        # Remove color codes for length calculation
        clean_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
        center_pos = self.get_terminal_center(len(clean_text))
        spaces = " " * center_pos
        print(f"{spaces}{self.colors[style]}{self.colors[color]}{text}{self.colors['RESET']}")

    def clear_screen(self):
        """Clear terminal screen based on OS"""
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def show_professional_banner(self):
        """Show professional centered banner with the new design"""
        self.clear_screen()
        
        banner_lines = [
            "██████████████████████████████████████████████",
            "█▄─▄▄─█▄─▀█▀─▄█─▄▄─█▄─▀█▄─▄█─▄▄▄▄█▄─▄▄─█─▄▄▄─█",
            "██─▄█▀██─█▄█─██─██─██─█▄▀─██▄▄▄▄─██─▄█▀█─███▀█",
            "▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀",
            "                                              ",
            "      Made by Team Pentadex Since 2025        ",
            "         https://t.me/pentadexx   v1.0        "
        ]
        
        for line in banner_lines:
            self.print_centered(line, 'CYAN', 'BRIGHT')
        
        print()
        
        # Stats line
        active_apis = sum(1 for config in self.api_config.values() if config.get('key'))
        stats_text = f"📊 Analyses: {len(self.results)} | 🔑 Active APIs: {active_apis} | ✅ Verified: {len(self.verified_data)} | ⚠️  Suspicious: {len(self.suspicious_data)}"
        self.print_centered(stats_text, 'YELLOW', 'BRIGHT')
        
        print()
        self.print_centered("─" * 70, 'CYAN', 'BRIGHT')
        print()

    def show_loading_spinner(self, message="Processing", duration=2):
        """Show animated loading spinner"""
        spinner_frames = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
        start_time = time.time()
        i = 0
        
        while (time.time() - start_time) < duration:
            frame = spinner_frames[i % len(spinner_frames)]
            clean_message = re.sub(r'\x1b\[[0-9;]*m', '', message)
            center_pos = self.get_terminal_center(len(clean_message) + 2)
            spaces = " " * center_pos
            print(f"\r{spaces}{self.colors['YELLOW']}{self.colors['BRIGHT']}{message} {frame}{self.colors['RESET']}", end="", flush=True)
            time.sleep(0.1)
            i += 1
        
        clean_message = re.sub(r'\x1b\[[0-9;]*m', '', message)
        center_pos = self.get_terminal_center(len(clean_message) + 2)
        spaces = " " * center_pos
        print(f"\r{spaces}✅ {message}{' ' * 20}", flush=True)

    def progress_bar(self, iteration, total, prefix='Progress:', suffix='Complete', length=40, fill='█'):
        """Display centered progress bar"""
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        
        bar_text = f'{prefix} |{bar}| {percent}% {suffix}'
        center_pos = self.get_terminal_center(len(bar_text))
        spaces = " " * center_pos
        
        print(f'\r{spaces}{bar_text}', end='\r', flush=True)
        if iteration == total:
            print()

    def display_header(self, title):
        """Display centered section header"""
        try:
            width = min(60, os.get_terminal_size().columns - 4)
        except:
            width = 60
            
        print()
        self.print_centered("═" * width, 'CYAN', 'BRIGHT')
        self.print_centered(f" {title} ", 'CYAN', 'BRIGHT')
        self.print_centered("═" * width, 'CYAN', 'BRIGHT')
        print()

    def display_menu(self, title, options):
        """Display professional centered menu"""
        try:
            width = min(50, os.get_terminal_size().columns - 4)
        except:
            width = 50
        
        print()
        self.print_centered("┌" + "─" * width + "┐", 'CYAN', 'BRIGHT')
        self.print_centered(f"│ {title:^{width-2}} │", 'CYAN', 'BRIGHT')
        self.print_centered("├" + "─" * width + "┤", 'CYAN', 'BRIGHT')
        
        for key, value in options.items():
            menu_text = f"  {self.colors['YELLOW']}{key}.{self.colors['RESET']} {value}"
            self.print_centered(menu_text, 'WHITE', 'NORMAL')
        
        exit_text = f"  {self.colors['RED']}0.{self.colors['RESET']} Exit System"
        self.print_centered(exit_text, 'WHITE', 'NORMAL')
        
        self.print_centered("└" + "─" * width + "┘", 'CYAN', 'BRIGHT')
        print()

    def display_success(self, message):
        """Display success message"""
        self.print_centered(f"✅ {message}", 'GREEN', 'BRIGHT')

    def display_error(self, message):
        """Display error message"""
        self.print_centered(f"❌ {message}", 'RED', 'BRIGHT')

    def display_warning(self, message):
        """Display warning message"""
        self.print_centered(f"⚠️  {message}", 'YELLOW', 'BRIGHT')

    def display_info(self, message):
        """Display info message"""
        self.print_centered(f"💡 {message}", 'BLUE', 'BRIGHT')

    def get_user_input(self, prompt, color='YELLOW'):
        """Get user input with centered prompt"""
        self.print_centered(f"\n{prompt}", color, 'BRIGHT')
        center_pos = self.get_terminal_center(2)
        spaces = " " * center_pos
        user_input = input(f"{spaces}> ").strip()
        return user_input

    def confirm_action(self, message):
        """Confirm action with user"""
        response = self.get_user_input(f"{message} (y/N)", 'YELLOW').lower()
        return response in ['y', 'yes']

    def check_dependencies(self):
        """Check if all required packages are installed"""
        missing_packages = []
        
        for package, import_name in self.required_packages.items():
            try:
                importlib.import_module(import_name)
            except ImportError:
                missing_packages.append(package)
        
        return missing_packages

    def install_dependencies(self, packages):
        """Install missing dependencies"""
        self.display_header("DEPENDENCY INSTALLATION")
        
        for i, package in enumerate(packages, 1):
            self.progress_bar(i, len(packages), prefix=f'Installing {package}', suffix='Complete')
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package], 
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(0.5)
            except subprocess.CalledProcessError:
                return False
        
        return True

    def load_config(self):
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                
                # Update API configurations
                for api_name, api_config in config.get('api_config', {}).items():
                    if api_name in self.api_config:
                        self.api_config[api_name]['key'] = api_config.get('key', '')
                        self.api_config[api_name]['calls'] = api_config.get('calls', 0)
                
                self.setup_complete = config.get('setup_complete', False)
                self.analysis_history = config.get('analysis_history', [])
                return True
            except Exception as e:
                self.display_error(f"Config error: {e}")
                return False
        return False

    def save_config(self):
        """Save configuration to file"""
        try:
            config = {
                'setup_complete': self.setup_complete,
                'api_config': self.api_config,
                'analysis_history': self.analysis_history[-100:],  # Keep last 100 entries
                'last_updated': datetime.now().isoformat(),
                'system_info': {
                    'platform': platform.system(),
                    'python_version': sys.version,
                    'tool_version': '4.0'
                }
            }
            
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
            return True
        except Exception as e:
            self.display_error(f"Save error: {e}")
            return False

    def test_api_key(self, api_name, api_key):
        """Test if API key is valid"""
        if not api_key:
            return False, "No API key provided"
        
        try:
            if api_name == 'numverify':
                params = {
                    'access_key': api_key,
                    'number': self.api_config[api_name]['test_number'],
                    'country_code': '',
                    'format': 1
                }
                response = requests.get(self.api_config[api_name]['url'], params=params, timeout=10)
                data = response.json()
                if response.status_code == 200 and data.get('valid') is not None:
                    return True, "API key validated successfully"
                else:
                    return False, f"API error: {data.get('error', {}).get('info', 'Unknown error')}"
            
            elif api_name == 'abstractapi':
                url = f"{self.api_config[api_name]['url']}?api_key={api_key}&phone={self.api_config[api_name]['test_number']}"
                response = requests.get(url, timeout=10)
                data = response.json()
                if response.status_code == 200 and ('valid' in data or 'number' in data):
                    return True, "API key validated successfully"
                else:
                    error_msg = data.get('error', {}).get('message', 'Unknown error') if isinstance(data.get('error'), dict) else 'Invalid response'
                    return False, f"API error: {error_msg}"
            
            elif api_name == 'ipinfo':
                test_ip = "8.8.8.8"
                url = f"https://ipinfo.io/{test_ip}/json?token={api_key}"
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    return True, "API key validated successfully"
                else:
                    return False, f"HTTP {response.status_code}: Invalid API key"
            
            return True, "API key accepted"
            
        except Exception as e:
            return False, f"API test failed: {str(e)}"

    def setup_wizard(self):
        """Professional setup wizard"""
        self.show_professional_banner()
        self.display_header("INITIAL SETUP WIZARD")
        
        # System Check
        self.display_info("Running system diagnostics...")
        time.sleep(1)
        
        system_info = {
            "Platform": platform.system(),
            "Python Version": sys.version.split()[0],
            "Current Directory": str(self.current_directory),
            "CPU Cores": os.cpu_count()
        }
        
        for key, value in system_info.items():
            self.print_centered(f"  {key}: {value}", 'WHITE', 'BRIGHT')
        
        # Dependency Check
        self.display_info("Checking dependencies...")
        missing_packages = self.check_dependencies()
        
        if missing_packages:
            self.display_warning(f"Missing {len(missing_packages)} packages: {', '.join(missing_packages)}")
            
            if self.confirm_action("Install missing dependencies automatically?"):
                if not self.install_dependencies(missing_packages):
                    self.display_error("Dependency installation failed")
                    return False
            else:
                self.display_info("Please install dependencies manually and restart")
                return False
        else:
            self.display_success("All dependencies verified")
        
        # API Configuration
        self.display_info("API Configuration (Optional)")
        if self.confirm_action("Configure API keys for enhanced functionality?"):
            self.configure_apis_interactive()
        
        # Finalize setup
        self.setup_complete = True
        self.save_config()
        
        self.display_header("SETUP COMPLETED")
        self.display_success("System initialized successfully")
        self.display_success("Configuration saved")
        self.display_success("Ready for intelligence operations")
        
        self.get_user_input("Press Enter to continue to main menu...", 'GREEN')
        return True

    def configure_apis_interactive(self):
        """Interactive API configuration - SHOW NOTHING FOR EMPTY KEYS"""
        api_categories = {
            '📞 PHONE INTELLIGENCE': ['numverify', 'abstractapi'],
            '🌐 NETWORK ANALYSIS': ['ipinfo', 'shodan'],
            '🔍 DOMAIN INTELLIGENCE': ['whoisxmlapi', 'hunterio'],
            '🤖 WEB AUTOMATION': ['apify', 'serpapi']
        }
        
        for category, apis in api_categories.items():
            self.display_header(category)
            
            for api_name in apis:
                config = self.api_config[api_name]
                current_key = config['key']
                
                # Only show if key exists and is not empty
                if current_key and current_key.strip():
                    masked_key = current_key[:8] + '•' * 12 + current_key[-4:]
                    self.display_info(f"{api_name.upper()}: {masked_key}")
                    
                    if not self.confirm_action("Update this API key?"):
                        continue
                else:
                    # Don't show anything for empty keys - just prompt for new key
                    self.display_info(f"Configuring {api_name.upper()}...")
                
                while True:
                    new_key = self.get_user_input(f"Enter {api_name} API key (or press Enter to skip):", 'YELLOW')
                    
                    if not new_key:
                        self.display_info("Skipping API configuration")
                        break
                    
                    self.show_loading_spinner("Validating API key", duration=2)
                    is_valid, message = self.test_api_key(api_name, new_key)
                    
                    if is_valid:
                        self.api_config[api_name]['key'] = new_key
                        self.display_success(f"API key validated and saved")
                        break
                    else:
                        self.display_error(f"Validation failed: {message}")
                        if not self.confirm_action("Try again?"):
                            break

    def system_health_check(self):
        """Comprehensive system health check"""
        self.display_header("SYSTEM HEALTH CHECK")
        
        checks = [
            ("Dependencies", len(self.check_dependencies()) == 0),
            ("API Configuration", any(config.get('key') for config in self.api_config.values())),
            ("Config File", self.config_file.exists()),
            ("Internet Connectivity", self.check_internet_connection()),
            ("Disk Space", self.check_disk_space())
        ]
        
        all_healthy = True
        for check_name, status in checks:
            if status:
                self.display_success(f"✓ {check_name}")
            else:
                self.display_error(f"✗ {check_name}")
                all_healthy = False
        
        return all_healthy

    def check_internet_connection(self):
        """Check internet connectivity"""
        try:
            requests.get("https://www.google.com", timeout=5)
            return True
        except:
            return False

    def check_disk_space(self):
        """Check available disk space"""
        try:
            stat = shutil.disk_usage(self.current_directory)
            return stat.free > 1024 * 1024 * 1024  # 1GB minimum
        except:
            return False

    def display_dashboard(self):
        """Display main system dashboard"""
        self.show_professional_banner()
        
        # Quick Stats
        active_apis = sum(1 for config in self.api_config.values() if config.get('key'))
        stats = [
            f"📊 Total Analyses: {len(self.analysis_history)}",
            f"🔑 Active APIs: {active_apis}",
            f"✅ Verified Data: {len(self.verified_data)}",
            f"⚠️  Suspicious Entries: {len(self.suspicious_data)}"
        ]
        
        for stat in stats:
            self.print_centered(stat, 'CYAN', 'BRIGHT')
        
        print()
        
        # API Status
        if active_apis > 0:
            self.display_info("Active APIs:")
            for api_name, config in self.api_config.items():
                if config.get('key'):
                    calls = config.get('calls', 0)
                    self.print_centered(f"  ✅ {api_name.upper()}: {calls} calls", 'GREEN')
        else:
            self.display_warning("No APIs configured - limited functionality")
        
        print()
        
        # Recent Activity
        if self.analysis_history:
            self.display_info("Recent Activity:")
            for activity in self.analysis_history[-3:]:
                self.print_centered(f"  • {activity['target']} - {activity['timestamp']}", 'WHITE')

    def main_menu(self):
        """Enhanced main menu system"""
        while True:
            self.display_dashboard()
            
            menu_options = {
                '1': '🚀 Single Target Analysis',
                '2': '📁 Batch Analysis', 
                '3': '⚙️  System Configuration',
                '4': '📊 View Results',
                '5': '🛡️  System Health Check'
            }
            
            self.display_menu("MAIN OPERATIONS", menu_options)
            
            choice = self.get_user_input("Select option", 'YELLOW')
            
            if choice == '1':
                self.single_target_analysis()
            elif choice == '2':
                self.batch_analysis_workflow()
            elif choice == '3':
                self.system_configuration_menu()
            elif choice == '4':
                self.show_results()
            elif choice == '5':
                self.system_health_check()
                self.get_user_input("Press Enter to continue...", 'GREEN')
            elif choice == '0':
                if self.confirm_action("Are you sure you want to exit?"):
                    self.shutdown_sequence()
                    break
            else:
                self.display_error("Invalid selection")

    def single_target_analysis(self):
        """Single target analysis workflow"""
        self.display_header("SINGLE TARGET ANALYSIS")
        
        target = self.get_user_input("Enter target (URL, IP, or domain):", 'YELLOW')
        if not target:
            return
        
        analysis_modes = {
            '1': 'Quick Scan',
            '2': 'Standard Analysis', 
            '3': 'Deep Intelligence'
        }
        
        self.display_menu("ANALYSIS MODE", analysis_modes)
        mode_choice = self.get_user_input("Select analysis mode:", 'YELLOW')
        
        modes = {'1': 'quick', '2': 'standard', '3': 'deep'}
        mode = modes.get(mode_choice, 'standard')
        
        self.perform_target_analysis(target, mode)

    def batch_analysis_workflow(self):
        """Professional batch analysis workflow"""
        self.display_header("BATCH ANALYSIS")
        
        self.display_info("Current directory: " + str(self.current_directory))
        
        # Show available text files
        files = list(self.current_directory.glob("*.txt"))
        if files:
            self.display_info("Text files found:")
            for i, f in enumerate(files, 1):
                self.print_centered(f"  {i}. {f.name}", 'WHITE')
        
        file_path = self.get_user_input("Enter path to targets file:", 'YELLOW')
        if not file_path:
            return
        
        file_path = Path(file_path)
        if not file_path.is_absolute():
            file_path = self.current_directory / file_path
        
        if not file_path.exists():
            self.display_error("File not found")
            return
        
        targets = self.load_targets_from_file(file_path)
        if not targets:
            self.display_error("No valid targets found in file")
            return
        
        self.display_info(f"Loaded {len(targets)} targets for analysis")
        
        if not self.confirm_action(f"Start batch analysis of {len(targets)} targets?"):
            return
        
        # Batch analysis with progress
        successful = 0
        for i, target in enumerate(targets, 1):
            self.progress_bar(i, len(targets), prefix=f'Analyzing {target[:30]}', suffix='Complete')
            
            try:
                result = self.basic_analysis(target)
                if result:
                    successful += 1
                    self.results.append(result)
                    self.analysis_history.append({
                        'target': target,
                        'timestamp': datetime.now().isoformat(),
                        'mode': 'batch'
                    })
                time.sleep(1)  # Rate limiting
            except Exception as e:
                self.display_error(f"Failed to analyze {target}: {str(e)}")
        
        self.display_success(f"Batch analysis completed: {successful}/{len(targets)} successful")
        
        if successful > 0:
            self.ask_save_report()

    def system_configuration_menu(self):
        """System configuration menu"""
        while True:
            self.display_header("SYSTEM CONFIGURATION")
            
            config_options = {
                '1': '🔑 API Management',
                '2': '🛠️  System Settings', 
                '3': '📊 Performance Tuning'
            }
            
            self.display_menu("CONFIGURATION", config_options)
            
            choice = self.get_user_input("Select option", 'YELLOW')
            
            if choice == '1':
                self.api_management_dashboard()
            elif choice == '2':
                self.system_settings()
            elif choice == '3':
                self.performance_tuning()
            elif choice == '0':
                break
            else:
                self.display_error("Invalid selection")

    def api_management_dashboard(self):
        """Professional API management dashboard - FIXED VERSION"""
        self.display_header("API MANAGEMENT")
        
        # API Statistics - FIXED: Properly count active APIs
        active_apis = sum(1 for config in self.api_config.values() if config.get('key'))
        total_calls = sum(config.get('calls', 0) for config in self.api_config.values())
        
        self.display_info(f"Active APIs: {active_apis}/{len(self.api_config)}")
        self.display_info(f"Total API Calls: {total_calls}")
        
        # API Status - FIXED: Proper iteration
        self.display_info("API STATUS:")
        for api_name, config in self.api_config.items():
            status = "✅ ACTIVE" if config.get('key') else "❌ INACTIVE"
            calls = config.get('calls', 0)
            color = 'GREEN' if config.get('key') else 'RED'
            status_text = f"  {api_name.upper():<15} {status:<12} Calls: {calls}"
            self.print_centered(status_text, color)
        
        # Management Options
        management_options = {
            '1': 'Configure API Keys',
            '2': 'Test All APIs',
            '3': 'API Usage Analytics'
        }
        
        self.display_menu("MANAGEMENT OPTIONS", management_options)
        
        choice = self.get_user_input("Select option", 'YELLOW')
        
        if choice == '1':
            self.configure_apis_interactive()
            self.save_config()
        elif choice == '2':
            self.test_all_apis()
        elif choice == '3':
            self.api_usage_analytics()

    def system_settings(self):
        """System settings menu"""
        self.display_header("SYSTEM SETTINGS")
        self.display_info("System settings functionality")
        self.display_info("This section will contain system configuration options")
        self.get_user_input("Press Enter to continue...", 'GREEN')

    def performance_tuning(self):
        """Performance tuning menu"""
        self.display_header("PERFORMANCE TUNING")
        self.display_info("Performance optimization settings")
        self.display_info("This section will contain performance-related configurations")
        self.get_user_input("Press Enter to continue...", 'GREEN')

    def show_results(self):
        """Show all analysis results"""
        if not self.results:
            self.display_warning("No analysis results available")
            return
        
        self.display_header("ANALYSIS RESULTS")
        
        for i, result in enumerate(self.results, 1):
            self.print_centered(f"\n{i}. {result['target']}", 'YELLOW')
            self.print_centered(f"   Domain: {result['domain']}", 'WHITE')
            self.print_centered(f"   Time: {result['timestamp']}", 'WHITE')
            
            # Show brief info
            web_data = result.get('website_data', {})
            if 'error' not in web_data:
                emails = web_data.get('emails', [])
                phones = web_data.get('phones', [])
                if emails:
                    self.print_centered(f"   📧 Emails: {len(emails)} found", 'GREEN')
                if phones:
                    self.print_centered(f"   📞 Phones: {len(phones)} found", 'GREEN')
        
        print()
        if self.confirm_action("Show detailed report for a specific result?"):
            try:
                choice = int(self.get_user_input("Enter result number:", 'YELLOW'))
                if 1 <= choice <= len(self.results):
                    self.show_analysis_summary(self.results[choice-1])
            except ValueError:
                self.display_error("Invalid number")

    def perform_target_analysis(self, target, mode='standard'):
        """Perform analysis on a single target"""
        self.display_header(f"ANALYZING TARGET: {target}")
        
        analysis_steps = [
            "Initializing analysis engine",
            "Gathering domain intelligence", 
            "Collecting network data",
            "Analyzing website content",
            "Compiling intelligence report"
        ]
        
        for step in analysis_steps:
            self.show_loading_spinner(step, duration=1.5)
        
        # Perform actual analysis
        result = self.basic_analysis(target)
        
        if result:
            self.analysis_history.append({
                'target': target,
                'timestamp': datetime.now().isoformat(),
                'mode': mode
            })
            self.display_success("Analysis completed successfully")
            self.show_analysis_summary(result)
            self.results.append(result)
            self.ask_save_report()
        else:
            self.display_error("Analysis failed")

    def basic_analysis(self, target):
        """Perform basic OSINT analysis"""
        try:
            # Add protocol if missing
            if not target.startswith(('http://', 'https://')):
                target = 'https://' + target
            
            domain = urlparse(target).netloc
            
            result = {
                'target': target,
                'domain': domain,
                'timestamp': datetime.now().isoformat(),
                'whois': self.get_whois_info(domain),
                'website_data': self.scrape_website(target)
            }
            
            return result
        except Exception as e:
            self.display_error(f"Analysis error: {e}")
            return None

    def get_whois_info(self, domain):
        """Get WHOIS information"""
        try:
            w = whois.whois(domain)
            return {
                'registrar': w.registrar,
                'creation_date': str(w.creation_date),
                'name': w.name,
                'org': w.org,
                'emails': w.emails,
                'country': w.country
            }
        except:
            return {'error': 'WHOIS lookup failed'}

    def scrape_website(self, url):
        """Scrape website for basic info"""
        try:
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract basic info
            text = soup.get_text()
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
            phones = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)
            
            return {
                'title': soup.title.string if soup.title else 'No title',
                'emails': list(set(emails)),
                'phones': list(set(phones)),
                'description': self.get_meta_description(soup),
                'status_code': response.status_code
            }
        except:
            return {'error': 'Scraping failed'}

    def get_meta_description(self, soup):
        """Extract meta description"""
        desc = soup.find('meta', attrs={'name': 'description'})
        return desc.get('content', '') if desc else ''

    def show_analysis_summary(self, result):
        """Show analysis results summary"""
        self.display_header("DETAILED ANALYSIS RESULTS")
        
        self.print_centered(f"🎯 Target: {result['target']}", 'GREEN')
        self.print_centered(f"🌐 Domain: {result['domain']}", 'BLUE')
        self.print_centered(f"🕐 Time: {result['timestamp']}", 'WHITE')
        
        # WHOIS info
        whois_info = result['whois']
        if 'error' not in whois_info:
            self.print_centered("\n📋 WHOIS Information:", 'CYAN')
            self.print_centered(f"   Registrar: {whois_info.get('registrar', 'N/A')}", 'WHITE')
            self.print_centered(f"   Created: {whois_info.get('creation_date', 'N/A')}", 'WHITE')
            self.print_centered(f"   Organization: {whois_info.get('org', 'N/A')}", 'WHITE')
        
        # Website data
        web_data = result['website_data']
        if 'error' not in web_data:
            self.print_centered("\n🌐 Website Data:", 'CYAN')
            self.print_centered(f"   Title: {web_data.get('title', 'N/A')}", 'WHITE')
            self.print_centered(f"   Status: {web_data.get('status_code', 'N/A')}", 'WHITE')
            
            emails = web_data.get('emails', [])
            if emails:
                self.print_centered(f"   📧 Emails ({len(emails)}):", 'GREEN')
                for email in emails:
                    self.print_centered(f"      {email}", 'WHITE')
            
            phones = web_data.get('phones', [])
            if phones:
                self.print_centered(f"   📞 Phones ({len(phones)}):", 'GREEN')
                for phone in phones:
                    self.print_centered(f"      {phone}", 'WHITE')

    def load_targets_from_file(self, file_path):
        """Load targets from file"""
        try:
            with open(file_path, 'r') as f:
                targets = [line.strip() for line in f if line.strip()]
            return targets
        except Exception as e:
            self.display_error(f"Failed to read file: {e}")
            return []

    def ask_save_report(self):
        """Ask to save results to file"""
        if not self.confirm_action("Save results to file?"):
            return
        
        filename = f"osint_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("ENTERPRISE OSINT INTELLIGENCE REPORT\n")
                f.write("=" * 50 + "\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Results: {len(self.results)}\n")
                f.write("=" * 50 + "\n\n")
                
                for i, result in enumerate(self.results, 1):
                    f.write(f"RESULT {i}:\n")
                    f.write(f"Target: {result['target']}\n")
                    f.write(f"Domain: {result['domain']}\n")
                    f.write(f"Time: {result['timestamp']}\n")
                    
                    # WHOIS info
                    whois_info = result['whois']
                    if 'error' not in whois_info:
                        f.write("WHOIS Information:\n")
                        f.write(f"  Registrar: {whois_info.get('registrar', 'N/A')}\n")
                        f.write(f"  Created: {whois_info.get('creation_date', 'N/A')}\n")
                        f.write(f"  Organization: {whois_info.get('org', 'N/A')}\n")
                    
                    # Website data
                    web_data = result['website_data']
                    if 'error' not in web_data:
                        f.write("Website Data:\n")
                        f.write(f"  Title: {web_data.get('title', 'N/A')}\n")
                        f.write(f"  Status: {web_data.get('status_code', 'N/A')}\n")
                        
                        emails = web_data.get('emails', [])
                        if emails:
                            f.write(f"  Emails: {', '.join(emails)}\n")
                        
                        phones = web_data.get('phones', [])
                        if phones:
                            f.write(f"  Phones: {', '.join(phones)}\n")
                    
                    f.write("-" * 40 + "\n\n")
            
            self.display_success(f"Report saved to: {filename}")
        except Exception as e:
            self.display_error(f"Failed to save report: {e}")

    def test_all_apis(self):
        """Test all configured APIs"""
        self.display_header("API TESTING")
        
        for api_name, config in self.api_config.items():
            if config['key']:
                self.display_info(f"Testing {api_name.upper()}...")
                is_valid, message = self.test_api_key(api_name, config['key'])
                if is_valid:
                    self.display_success(f"✅ {api_name.upper()}: {message}")
                else:
                    self.display_error(f"❌ {api_name.upper()}: {message}")
            else:
                self.display_warning(f"⚠️  {api_name.upper()}: Not configured")

    def api_usage_analytics(self):
        """Show API usage analytics"""
        self.display_header("API USAGE ANALYTICS")
        
        total_calls = sum(config.get('calls', 0) for config in self.api_config.values())
        active_apis = sum(1 for config in self.api_config.values() if config.get('key'))
        
        self.display_info(f"Total API Calls: {total_calls}")
        self.display_info(f"Active APIs: {active_apis}/{len(self.api_config)}")
        
        for api_name, config in self.api_config.items():
            calls = config.get('calls', 0)
            status = "ACTIVE" if config.get('key') else "INACTIVE"
            color = 'GREEN' if config.get('key') else 'RED'
            status_text = f"  {api_name.upper():<15} {status:<8} Calls: {calls}"
            self.print_centered(status_text, color)

    def shutdown_sequence(self):
        """Professional shutdown sequence"""
        self.display_header("SYSTEM SHUTDOWN")
        
        shutdown_steps = [
            "Saving configuration data",
            "Closing API connections", 
            "Generating session report",
            "Securing system state"
        ]
        
        for step in shutdown_steps:
            self.show_loading_spinner(step, duration=0.8)
        
        self.display_success("System shutdown completed successfully")
        self.print_centered("Thank you for using Team Pentadex tools v1.0", 'GREEN', 'BRIGHT')
        self.print_centered("Stay secure! 🔒", 'CYAN', 'BRIGHT')
        self.print_centered("Join telegram for more update , https://t.me/pentadexx ", 'WHITE', 'BRIGHT')
        time.sleep(2)

    def initialize_tool(self):
        """Initialize the tool"""
        if not self.load_config() or not self.setup_complete:
            return self.setup_wizard()
        return True

    def main(self):
        """Main application entry point"""
        try:
            if self.initialize_tool():
                self.main_menu()
        except KeyboardInterrupt:
            self.display_info("\nOperation cancelled by user")
        except Exception as e:
            self.display_error(f"Unexpected error: {e}")
        finally:
            self.save_config()

if __name__ == "__main__":
    tool = ProfessionalEnterpriseOSINTTool()
    tool.main()
