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

class EnhancedOSINTTool:
    def __init__(self):
        self.results = []
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def banner(self):
        print("""
        🕵️‍♂️ ENHANCED OSINT TOOL
        ======================
        Get Complete Owner Information
        """)

    def load_websites_from_file(self, filename):
        """Load websites from text file"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                websites = [line.strip() for line in file if line.strip()]
            return websites
        except FileNotFoundError:
            print(f"❌ Error: File '{filename}' not found!")
            return []

    def extract_emails(self, text):
        """Extract email addresses from text"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return list(set(emails))

    def extract_phones(self, text):
        """Extract phone numbers from text"""
        phone_patterns = [
            r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            r'\b\(\d{3}\)\s*\d{3}[-.]?\d{4}\b',
            r'\b\d{2}[-.]?\d{4}[-.]?\d{4}\b',
            r'\+\d{1,3}[-.\s]?\d{1,14}[-.\s]?\d{1,14}'
        ]
        phones = []
        for pattern in phone_patterns:
            phones.extend(re.findall(pattern, text))
        return list(set(phones))

    def extract_social_media(self, text, html_content):
        """Extract social media profiles"""
        social_patterns = {
            'facebook': [r'facebook\.com/[^\s"\']+', r'fb\.com/[^\s"\']+'],
            'twitter': [r'twitter\.com/[^\s"\']+', r'x\.com/[^\s"\']+'],
            'linkedin': [r'linkedin\.com/(in|company)/[^\s"\']+'],
            'instagram': [r'instagram\.com/[^\s"\']+'],
            'youtube': [r'youtube\.com/(user|channel)/[^\s"\']+'],
            'github': [r'github\.com/[^\s"\']+'],
            'pinterest': [r'pinterest\.com/[^\s"\']+'],
            'tiktok': [r'tiktok\.com/@[^\s"\']+']
        }
        
        social_media = {}
        
        # Extract from text
        for platform, patterns in social_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, text.lower())
                if matches:
                    social_media[platform] = list(set(matches))
        
        # Also extract from href attributes
        soup = BeautifulSoup(html_content, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href'].lower()
            for platform, patterns in social_patterns.items():
                for pattern in patterns:
                    if re.search(pattern, href):
                        if platform not in social_media:
                            social_media[platform] = []
                        social_media[platform].append(href)
        
        return social_media

    def get_whois_info(self, domain):
        """Get WHOIS information using the better whois package"""
        try:
            w = whois.whois(domain)
            return {
                'registrar': w.registrar,
                'creation_date': str(w.creation_date) if w.creation_date else 'N/A',
                'expiration_date': str(w.expiration_date) if w.expiration_date else 'N/A',
                'updated_date': str(w.updated_date) if w.updated_date else 'N/A',
                'name': w.name,
                'org': w.org,
                'address': w.address,
                'city': w.city,
                'state': w.state,
                'country': w.country,
                'zipcode': w.zipcode,
                'emails': w.emails,
                'phone': w.phone,
                'name_servers': w.name_servers,
                'status': w.status
            }
        except Exception as e:
            return {'error': str(e)}

    def deep_scrape_website(self, url):
        """Deep scrape website for comprehensive information"""
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            
            # Extract basic contact info
            emails = self.extract_emails(text)
            phones = self.extract_phones(text)
            
            # Extract social media
            social_media = self.extract_social_media(text, response.text)
            
            # Look for about pages, team pages, contact pages
            important_pages = self.find_important_pages(soup, url)
            
            # Extract meta information
            meta_info = self.extract_meta_info(soup)
            
            # Look for address information
            addresses = self.extract_addresses(text)
            
            return {
                'emails': emails,
                'phones': phones,
                'social_media': social_media,
                'important_pages': important_pages,
                'meta_info': meta_info,
                'addresses': addresses,
                'title': soup.title.string if soup.title else 'No title',
                'description': meta_info.get('description', ''),
                'keywords': meta_info.get('keywords', '')
            }
        except Exception as e:
            return {'error': str(e)}

    def find_important_pages(self, soup, base_url):
        """Find important pages like about, contact, team"""
        important_keywords = ['about', 'contact', 'team', 'staff', 'people', 'company', 'info', 'help', 'support']
        important_pages = {}
        
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            link_text = link.get_text().lower()
            
            for keyword in important_keywords:
                if keyword in href.lower() or keyword in link_text:
                    full_url = urljoin(base_url, href)
                    if keyword not in important_pages:
                        important_pages[keyword] = []
                    if full_url not in important_pages[keyword]:
                        important_pages[keyword].append(full_url)
        
        return important_pages

    def extract_meta_info(self, soup):
        """Extract meta information from page"""
        meta_info = {}
        
        # Description
        desc_tag = soup.find('meta', attrs={'name': 'description'})
        if desc_tag:
            meta_info['description'] = desc_tag.get('content', '')
        
        # Keywords
        keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
        if keywords_tag:
            meta_info['keywords'] = keywords_tag.get('content', '')
        
        # Author
        author_tag = soup.find('meta', attrs={'name': 'author'})
        if author_tag:
            meta_info['author'] = author_tag.get('content', '')
        
        return meta_info

    def extract_addresses(self, text):
        """Extract potential addresses from text"""
        # Simple address pattern (can be improved)
        address_patterns = [
            r'\d+\s+[\w\s]+\s+(?:street|st|avenue|ave|road|rd|boulevard|blvd|drive|dr|lane|ln)\s*,\s*[\w\s]+\s*,\s*[A-Z]{2}\s*\d{5}',
            r'[\w\s]+\s*,\s*[\w\s]+\s*,\s*[A-Z]{2}\s*\d{5}'
        ]
        
        addresses = []
        for pattern in address_patterns:
            addresses.extend(re.findall(pattern, text, re.IGNORECASE))
        
        return list(set(addresses))

    def analyze_website(self, website):
        """Comprehensive website analysis"""
        print(f"\n🔍 Analyzing: {website}")
        
        # Ensure website has protocol
        if not website.startswith(('http://', 'https://')):
            website = 'https://' + website
        
        parsed_url = urlparse(website)
        domain = parsed_url.netloc
        
        result = {
            'website': website,
            'domain': domain,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Get WHOIS information
        print("   📋 Getting WHOIS information...")
        whois_info = self.get_whois_info(domain)
        result['whois'] = whois_info
        
        # Deep scrape website
        print("   🕸️  Deep scraping website...")
        scrape_info = self.deep_scrape_website(website)
        result['scraped_data'] = scrape_info
        
        # Scrape important pages found
        print("   🔍 Scanning important pages...")
        page_details = {}
        important_pages = scrape_info.get('important_pages', {})
        
        for page_type, urls in important_pages.items():
            page_details[page_type] = []
            for page_url in urls[:2]:  # Limit to first 2 pages of each type
                try:
                    page_data = self.deep_scrape_website(page_url)
                    page_details[page_type].append({
                        'url': page_url,
                        'data': page_data
                    })
                    time.sleep(1)  # Be polite
                except:
                    pass
        
        result['page_details'] = page_details
        
        return result

    def display_results(self, result):
        """Display comprehensive results"""
        print(f"\n{'='*80}")
        print(f"🎯 COMPLETE OSINT REPORT FOR: {result['website']}")
        print(f"{'='*80}")
        
        # WHOIS Information
        print("\n📋 DOMAIN REGISTRATION INFORMATION:")
        print("-" * 50)
        whois_info = result['whois']
        if 'error' not in whois_info:
            print(f"   👤 Registrant Name: {whois_info.get('name', 'N/A')}")
            print(f"   🏢 Organization: {whois_info.get('org', 'N/A')}")
            print(f"   📧 Contact Emails: {', '.join(whois_info.get('emails', [])) if whois_info.get('emails') else 'N/A'}")
            print(f"   📞 Contact Phone: {whois_info.get('phone', 'N/A')}")
            print(f"   📍 Address: {whois_info.get('address', 'N/A')}")
            print(f"   🏙️ City: {whois_info.get('city', 'N/A')}")
            print(f"   🗺️ Country: {whois_info.get('country', 'N/A')}")
            print(f"   📅 Created: {whois_info.get('creation_date', 'N/A')}")
            print(f"   ⏰ Expires: {whois_info.get('expiration_date', 'N/A')}")
            print(f"   🏢 Registrar: {whois_info.get('registrar', 'N/A')}")
        else:
            print(f"   ❌ WHOIS Error: {whois_info['error']}")
        
        # Contact Information
        print("\n📞 CONTACT INFORMATION:")
        print("-" * 50)
        scraped = result['scraped_data']
        if 'error' not in scraped:
            if scraped.get('emails'):
                print(f"   📧 Email Addresses Found:")
                for email in scraped['emails']:
                    print(f"      • {email}")
            else:
                print("   📧 No email addresses found")
            
            if scraped.get('phones'):
                print(f"   📞 Phone Numbers Found:")
                for phone in scraped['phones']:
                    print(f"      • {phone}")
            else:
                print("   📞 No phone numbers found")
            
            if scraped.get('addresses'):
                print(f"   📍 Possible Addresses:")
                for address in scraped['addresses']:
                    print(f"      • {address}")
        
        # Social Media
        print("\n🌐 SOCIAL MEDIA PROFILES:")
        print("-" * 50)
        social_media = scraped.get('social_media', {})
        if social_media:
            for platform, profiles in social_media.items():
                print(f"   🔗 {platform.capitalize()}:")
                for profile in profiles[:3]:  # Show first 3 profiles
                    print(f"      • {profile}")
        else:
            print("   No social media profiles found")
        
        # Important Pages
        print("\n📄 IMPORTANT PAGES FOUND:")
        print("-" * 50)
        important_pages = scraped.get('important_pages', {})
        for page_type, urls in important_pages.items():
            print(f"   📁 {page_type.capitalize()} pages:")
            for url in urls[:3]:
                print(f"      • {url}")

    def save_comprehensive_report(self, filename):
        """Save comprehensive report to text file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("COMPREHENSIVE OSINT TOOL - DETAILED REPORT\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*100 + "\n\n")
                
                for result in self.results:
                    f.write(f"TARGET: {result['website']}\n")
                    f.write(f"Domain: {result['domain']}\n")
                    f.write(f"Analysis Time: {result['timestamp']}\n")
                    f.write("="*80 + "\n")
                    
                    # WHOIS Information
                    f.write("\nDOMAIN REGISTRATION INFORMATION:\n")
                    f.write("-"*50 + "\n")
                    whois_info = result['whois']
                    if 'error' not in whois_info:
                        for key, value in whois_info.items():
                            if value and key != 'error':
                                f.write(f"{key}: {value}\n")
                    else:
                        f.write(f"WHOIS Error: {whois_info['error']}\n")
                    
                    # Contact Information
                    scraped = result['scraped_data']
                    if 'error' not in scraped:
                        f.write("\nCONTACT INFORMATION:\n")
                        f.write("-"*50 + "\n")
                        f.write(f"Emails: {', '.join(scraped.get('emails', []))}\n")
                        f.write(f"Phones: {', '.join(scraped.get('phones', []))}\n")
                        f.write(f"Addresses: {', '.join(scraped.get('addresses', []))}\n")
                        
                        # Social Media
                        f.write("\nSOCIAL MEDIA PROFILES:\n")
                        f.write("-"*50 + "\n")
                        social_media = scraped.get('social_media', {})
                        for platform, profiles in social_media.items():
                            f.write(f"{platform.upper()}: {', '.join(profiles)}\n")
                    
                    f.write("\n" + "="*100 + "\n\n")
            
            print(f"✅ Comprehensive report saved to: {filename}")
        except Exception as e:
            print(f"❌ Error saving report: {e}")

    def main(self):
        """Main CLI interface"""
        self.banner()
        
        while True:
            print("\nOptions:")
            print("1. Analyze websites from file")
            print("2. Analyze single website")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                filename = input("Enter the filename with websites: ").strip()
                websites = self.load_websites_from_file(filename)
                
                if websites:
                    print(f"\n🚀 Starting comprehensive analysis of {len(websites)} websites...")
                    for website in websites:
                        result = self.analyze_website(website)
                        self.results.append(result)
                        self.display_results(result)
                    
                    save_choice = input("\n💾 Do you want to save the comprehensive report? (y/n): ").strip().lower()
                    if save_choice == 'y':
                        base_name = input("Enter base filename (without extension): ").strip()
                        if base_name:
                            self.save_comprehensive_report(f"{base_name}_full_report.txt")
                        else:
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            self.save_comprehensive_report(f"full_osint_report_{timestamp}.txt")
                
            elif choice == '2':
                website = input("Enter website URL: ").strip()
                if website:
                    print(f"\n🚀 Starting comprehensive analysis...")
                    result = self.analyze_website(website)
                    self.results.append(result)
                    self.display_results(result)
                    
                    save_choice = input("\n💾 Do you want to save the report? (y/n): ").strip().lower()
                    if save_choice == 'y':
                        base_name = input("Enter base filename (without extension): ").strip()
                        if base_name:
                            self.save_comprehensive_report(f"{base_name}_full_report.txt")
                        else:
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            self.save_comprehensive_report(f"full_osint_report_{timestamp}.txt")
                
            elif choice == '3':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice!")

if __name__ == "__main__":
    tool = EnhancedOSINTTool()
    tool.main()
