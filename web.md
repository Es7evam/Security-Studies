# Web

Web is usually the entry point at security in general.   


Here I'll be mainly covering some tools that can help you when you do things related to web pentesting.   


In the future I plan to write a guide on what you should usually do in each situation, but remember that's not a rule.

## Table of Contents

1. [Enumerating](web.md#enumerating)
2. [Payloads and Reverse Shells](web.md#payloads)
3. [Scripts](web.md#scripts)
4. [Cheat Sheets](web.md#cheatsheets)

### Initial Enumerating 

* [nmap](https://nmap.org/) - Nmap is an utility for network discovery and security auditing
* [dirb](http://dirb.sourceforge.net/),  [dirsearch](https://github.com/maurosoria/dirsearch) and [Gobuster](https://github.com/OJ/gobuster) are file and directories bruteforcers. Gobuster also scans for DNS subdomains.
* [WPScan](https://wpscan.org/) - A black box WordPress vulnerability scanner.

### Payloads and Reverse Shells 

* [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - A list of useful payloads and bypass for Web Application Security and Pentest/CTF.
* [PHP Web Shells](https://github.com/JohnTroony/php-webshells) - Common PHP shells.

### Scripts 

* [LinuxPrivChecker](https://github.com/Es7evam/Security-Studies/tree/c2582d3cae736dd0a22e16cdc167c8db55dc1352/Scripts/linuxprivchecker.py) - Script made to enumerate basic system info and search for common privilege escalation vectors such as world writable files, misconfigurations, clear-text passwords and applicable exploits.
* [LinEnum](https://github.com/rebootuser/LinEnum) - Scripted Local Linux Enumeration & Privilege Escalation Checks

### Cheat Sheets 

* [Local Linux Enumeration & Privilege Escalation](https://www.rebootuser.com/?p=1623)
* [Pentest Monkey Reverse Shell Cheat Sheet](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
* [SQL Injection Cheat Sheet - Netsparker](https://the-eye.eu/public/Books/qt.vidyagam.es/library/SQL/SQL%20Injection%20Cheat%20Sheet/SQL%20Injection%20Cheat%20Sheet%20-%20Netsparker.pdf)

