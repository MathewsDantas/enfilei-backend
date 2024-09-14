# **Clinico Queue Manager**

### Desenvolvido por **Medsis Soluções**

---

## **Sobre a Empresa: Medsis Soluçõess**

A **Medsis Soluções** foi fundada em 2015 por um grupo de profissionais da área de tecnologia e saúde, com a missão de otimizar o atendimento nas clínicas médicas e hospitais por meio da inovação tecnológica. Nosso foco é reduzir o tempo de espera dos pacientes e melhorar a eficiência dos processos de gestão de atendimento, garantindo uma experiência mais ágil e satisfatória para os usuários. Desde sua fundação, a Medisys Solutions tem se destacado por fornecer soluções robustas e escaláveis, ajudando clínicas a digitalizarem seus processos e melhorarem sua operação.

---

## **Descrição do Projeto**

**Clinico Queue Manager** é um sistema de gerenciamento de fila de atendimento e cadastro de pacientes. Ele foi desenvolvido com foco em clínicas e hospitais que desejam melhorar o fluxo de pacientes e reduzir o tempo de espera, proporcionando uma experiência mais organizada e eficiente. O sistema usa uma arquitetura robusta com **Django REST Framework**, **Celery** e **RabbitMQ** para processar as tarefas de forma assíncrona e garantir que os pacientes sejam atendidos em ordem e sem falhas.

### **Principais Funcionalidades:**

1. **Cadastro de Pacientes**: O sistema permite o cadastro de novos pacientes e identifica se o paciente já possui um registro na clínica por meio do CPF.
   
2. **Fila de Atendimento**: Pacientes identificados como já cadastrados são automaticamente colocados na fila de atendimento.
   
3. **Processamento Assíncrono**: O sistema utiliza **Celery** e **RabbitMQ** para gerenciar as tarefas de forma assíncrona, garantindo que o registro e a fila sejam processados de maneira eficiente.

4. **Reset Diário da Fila**: A fila de atendimento é resetada diariamente, garantindo que cada dia tenha um novo fluxo de pacientes.

---

## **Tecnologias Utilizadas:**

- **Django REST Framework**: Para criar a API que permite interagir com o sistema.
- **Celery**: Biblioteca de tarefas assíncronas para gerenciamento de fila e execução de tarefas em segundo plano.
- **RabbitMQ**: Message broker usado para enfileirar e distribuir as tarefas para os workers do Celery.

---

## **Como Funciona o Sistema:**

1. **Cadastro/Identificação do Paciente**:
   - O usuário (funcionário da clínica) insere o CPF do paciente.
   - O sistema verifica se o paciente já está cadastrado.
   - Se o paciente não estiver cadastrado, ele é registrado e automaticamente colocado na fila.

2. **Adicionando o Paciente à Fila**:
   - Se o paciente já estiver registrado, ele é adicionado à fila de atendimento por meio de uma tarefa Celery.
   - RabbitMQ gerencia a fila de mensagens para garantir que as tarefas sejam entregues e processadas corretamente.

3. **Reset Diário da Fila**:
   - A fila de pacientes é automaticamente resetada todos os dias, garantindo que o fluxo do dia anterior não interfira no novo dia de atendimento.

---

## **Instalação e Execução**

### **Pré-requisitos**:

- Python 3.8+
- Django 4.x
- Celery 5.x
- RabbitMQ
- Redis (opcional, pode ser usado como backend para resultados do Celery)

### **Passos para rodar o sistema**:

1. Clone o repositório:
   ```bash
   git clone https://github.com/MathewsDantas/medsis-fila-backend.git

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt

3. Configure as variáveis de ambiente para RabbitMQ e Celery.
   
4. Rode as migrações do banco de dados:
   ```bash
   python manage.py migrate

5. Inicie o servidor Django:
   ```bash
   python manage.py runserver

6. Inicie o worker do Celery:
   ```bash
   celery -A clinico_queue_manager worker --loglevel=info

5. Inicie o RabbitMQ:
   ```bash
   sudo rabbitmq-server
   ```






