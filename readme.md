- Made project structure
- Wrote requirements.txt
- Enter venv
- Pip install
- Code
- Add SECRET_KEY and DATABASE_URL in env
- Run uvicorn app.main:app --reload
- Write Dockerfile and docker-compose
- Launch ec2 (ubuntu) and ssh into it
- Run sudo apt update && sudo apt install docker.io -y && sudo systemctl start docker
- Copy project to ubuntu machine
- Run docker-compose up --build -d
- If prev command not work, Run these - 
    <!-- - sudo apt remove docker docker-engine docker.io containerd runc -y
    - sudo apt update
    - udo apt install ca-certificates curl gnupg -y
    - sudo install -m 0755 -d /etc/apt/keyrings
    - curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    - sudo chmod a+r /etc/apt/keyrings/docker.gpg
    - echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  noble stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    - sudo apt update
    - sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
    - Verify 
        - docker --version
        - docker compose version
    - Re-run prev command -->

    - Run sudo apt install docker-compose
    - Run docker sudo systemctl start docker
    - Run sudo docker compose up --build -d
- Add inbound rule to open port 8000 in instance's security group









