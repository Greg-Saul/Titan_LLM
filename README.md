# Titan_LLM

### Dependencies
- youtube-transcript-api: https://pypi.org/project/youtube-transcript-api/

### Environment Setup
To contribute to this project or clone it using SSH, follow these steps:

1. **Generate SSH Key**
    - Open your terminal (connect to your remote server if applicable)
    - Generate a new SSH key pair using the following command:
      ```bash
      ssh-keygen -t ed25519 -C "your_email@example.com"
      ```
        - `ssh-keygen` → Starts the SSH key generation process  
        - `-t ed25519` → Encryption algorithm  
        - `-C` → Identifying comment
    - When prompted, press **ENTER** to accept the default file location
    - (Optional) Enter a passphrase (can be left blank)

2. **Add Public Key to GitHub**
    - Display your public key using:
      ```bash
      cat ~/.ssh/id_ed25519.pub
      ```
    - Copy the entire line (starts with `ssh-ed25519` and ends with your email address) and paste it in GitHub:
        - **GitHub → Settings → SSH and GPG Keys → New SSH key → Paste it there**

3. **Clone the Repository via SSH**
    - On your GitHub repository page, click the **CODE** button
    - Select the **SSH** option and copy the provided URL
    - In your terminal, run:
      ```bash
      git clone <repository_SSH_URL>
      ```

4. Freely access and work with the repository.
