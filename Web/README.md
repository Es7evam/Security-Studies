# Web Security

Web is usually the entry point at security in general. <br>

Here I'll be mainly covering some tools that can help you when you do things related to web pentesting. <br>

In the future I plan to write a guide on what you should usually do in each situation, but remember that's not a rule.

## Table of Contents
1. [Enumerating](#enumerating)
2. [Payloads and Reverse Shells](#payloads)
3. [Scripts](#scripts)
4. [Cheat Sheets](#cheatsheets)

### Initial Enumerating <a name="enumerating"></a>

 - [nmap](https://nmap.org/) - Nmap is an utility for network discovery and security auditing
 - [dirb](http://dirb.sourceforge.net/),  [dirsearch](https://github.com/maurosoria/dirsearch) and [Gobuster](https://github.com/OJ/gobuster) are file and directories bruteforcers. Gobuster also scans for DNS subdomains.
 - [WPScan](https://wpscan.org/) - A black box WordPress vulnerability scanner.

### Payloads and Reverse Shells <a name="payloads"></a>
 - [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - A list of useful payloads and bypass for Web Application Security and Pentest/CTF.
 - [PHP Web Shells](https://github.com/JohnTroony/php-webshells) - Common PHP shells.

### Scripts <a name="scripts"></a>
 - [LinuxPrivChecker](/Scripts/linuxprivchecker.py) - Script made to enumerate basic system info and search for common privilege escalation vectors such as world writable files, misconfigurations, clear-text passwords and applicable exploits.
 - [LinEnum](https://github.com/rebootuser/LinEnum) - Scripted Local Linux Enumeration & Privilege Escalation Checks

### Cheat Sheets <a name="cheatsheets"></a>
 - [Local Linux Enumeration & Privilege Escalation](https://www.rebootuser.com/?p=1623)
