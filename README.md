# mini-soc-wazuh-swarm
# Mini SOC with Wazuh on Docker Swarm

A miniature Security Operations Center (SOC) environment built with Wazuh SIEM deployed on a Docker Swarm cluster. This project demonstrates infrastructure automation with Ansible, container orchestration, and security monitoring capabilities.

##  Features

- **Containerized Wazuh Stack**: Deploys Wazuh Indexer, Manager, and Dashboard using Docker
- **Docker Swarm Orchestration**: Utilizes swarm mode for high availability
- **Automated Deployment**: Ansible playbooks for provisioning and teardown
- **Reverse Proxy & SSL**: Traefik with SSL termination for secure access
- **Custom Detection Rules**: Implemented SSH brute force detection logic
- **CI/CD Ready**: GitHub repository structure supports automation

##  Architecture

The solution consists of a Docker Swarm cluster running:

- Wazuh Indexer (OpenSearch)
- Wazuh Manager
- Wazuh Dashboard
- Traefik (reverse proxy with SSL)
- Automated with Ansible playbooks

##  Installation

### Prerequisites
- Docker Engine
- Ansible
- Python 3.x
1. Clone the repository:
```bash
git clone https://github.com/Auaub/mini-soc-wazuh-final.git
cd mini-soc-wazuh-final
Run the deployment playbook:

bash

ansible-playbook ansible/playbooks/deploy.yml -i ansible/inventories/hosts.ini
📊 Project Status
✅ Completed:

Docker Swarm cluster setup

Wazuh stack deployment automation

SSL certificate configuration

Custom SSH detection rules

⚠️ Known Issues:

Wazuh Dashboard initialization fails due to OpenSearch security index issue

Custom rules not validated in UI

🔜 Future Enhancements:

Resolve OpenSearch security initialization

Add Trivy vulnerability scanning

Implement additional detection rules

Enhance CI/CD pipeline

📄 Report
A detailed project report is available in docs/report.pdf which includes:

Executive summary

Architecture overview

Technical implementation details

Issues faced and solutions

Future work recommendations


