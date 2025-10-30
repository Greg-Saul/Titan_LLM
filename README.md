# Titan_LLM

### Dependencies
- youtube-transcript-api: https://pypi.org/project/youtube-transcript-api/

### Environment Setup
To contribute to this project or clone it using ssh, follow these steps:

1. Generate SSH Key
    - Open your terminal (connect to your remote server if applicable)
    - Generate a new SSH key pair using the following command:
        ssh-keygen -t ed25519 -C "your_email@example.com"
            *ssh-keygen -> Starts the SSH key generation process
            *-t ed25519 -> encryption algorithm
            *-c -> Identifying comment
    - When promted, press ENTER to accept the defualt file location
    - Optional, enter a passphrase (can be left blank)

2. Add Public Key to Github
    - Display public key using:
        cat ~/.ssh/id_ed25519.pub
    - Copy the entire line (starts with ssh-ed25519 and ends with 
      your email address) and paste in Github
        GitHub → Settings → SSH and GPG Keys → New SSH key → Paste it there

3. Clone the Repository via SSH
    - On your Github repository page, click the CODE button
    - Select the SSH option and copy the provided URL
    - In terminal run: 
        git clone <repository_SSH_URL>

4. Freely access and work with the repository

