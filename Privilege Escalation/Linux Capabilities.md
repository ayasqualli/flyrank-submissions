1- Check GTFOBins

#### Enumerating Capabilities

```bash
find /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -type f -exec getcap {} \;
```

### Exploitation
![../Attachements/Pasted image 20260109194206.png](<../Attachements/Pasted image 20260109194206.png>)

Linux capabilities are a security feature in the Linux operating system that allows specific privileges to be granted to processes, allowing them to perform specific actions that would otherwise be restricted. This allows for more fine-grained control over which processes have access to certain privileges, making it more secure than the traditional Unix model of granting privileges to users and groups.

However, like any security feature, Linux capabilities are not invulnerable and can be exploited by attackers. One common vulnerability is using capabilities to grant privileges to processes that are not adequately sandboxed or isolated from other processes, allowing us to escalate their privileges and gain access to sensitive information or perform unauthorized actions.

Another potential vulnerability is the misuse or overuse of capabilities, which can result in processes having more privileges than they need. This can create unnecessary security risks, as we could exploit these privileges to gain access to sensitive information or perform unauthorized actions.

Overall, Linux capabilities can be a practical security feature, but they must be used carefully and correctly to avoid vulnerabilities and potential exploits.

Setting capabilities involves using the appropriate tools and commands to assign specific capabilities to executables or programs. In Ubuntu, for example, we can use the `setcap` command to set capabilities for specific executables. This command allows us to specify the capability we want to set and the value we want to assign.

When capabilities are set for a binary, it means that the binary will be able to perform specific actions that it would not be able to perform without the capabilities. For example, if the `cap_net_bind_service` capability is set for a binary, the binary will be able to bind to network ports, which is a privilege usually restricted.

Some capabilities, such as `cap_sys_admin`, which allows an executable to perform actions with administrative privileges, can be dangerous if they are not used properly. For example, we could exploit them to escalate their privileges, gain access to sensitive information, or perform unauthorized actions. Therefore, it is crucial to set these types of capabilities for properly sandboxed and isolated executables and avoid granting them unnecessarily.

![../Attachements/Pasted image 20260109193924.png](<../Attachements/Pasted image 20260109193924.png>)


### Privilege Escalation: 
![../Attachements/Pasted image 20260109194019.png](<../Attachements/Pasted image 20260109194019.png>)

When a binary is executed with capabilities, it can perform the actions that the capabilities allow. However, it will not be able to perform any actions not allowed by the capabilities. This allows for more fine-grained control over the binary's privileges and can help prevent security vulnerabilities and unauthorized access to sensitive information.

When using the `setcap` command to set capabilities for an executable in Linux, we need to specify the capability we want to set and the value we want to assign. The values we use will depend on the specific capability we are setting and the privileges we want to grant to the executable.

Here are some examples of values that we can use with the `setcap` command, along with a brief description of what they do:![](../Attachements/Pasted%20image%2020260620124612.png)

Several Linux capabilities can be used to escalate a user's privileges to `root`, including:
![](../Attachements/Pasted%20image%2020260620124638.png)