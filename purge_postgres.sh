#!/bin/bash

echo "Parando o serviço PostgreSQL..."
sudo systemctl stop postgresql

echo "Removendo pacotes PostgreSQL..."
sudo apt-get --purge remove postgresql\* -y

echo "Removendo dependências não utilizadas..."
sudo apt-get autoremove -y

echo "Removendo arquivos de configuração..."
sudo rm -rf /etc/postgresql/
sudo rm -rf /etc/postgresql-common/
sudo rm -rf /var/lib/postgresql/
sudo rm -rf /var/log/postgresql/

echo "Removendo usuário e grupo PostgreSQL..."
sudo deluser postgres
sudo delgroup postgres

echo "Atualizando a lista de pacotes..."
sudo apt-get update

echo "PostgreSQL removido completamente do sistema."