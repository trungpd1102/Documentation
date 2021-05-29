1. Elevate provileges user with a user pseudo privileges :
- `usermod -aG sudo <user_name>`
- Check this out: `grep -Po '^sudo.+:K.*$' /etc/group
2. Generate ssh-key
- `ssh-keygen -t ed25519`
- Copy to server: `ssh-copy-id -i /root/.ssh/id_ed25519.pub <user_name>@<IP_address>`
