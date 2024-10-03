# **Enfilei**

### Desenvolvido por **Chef Soluções**

---

## **Sobre a Empresa: Chef Soluções**

A **Chef Soluções** foi fundada em 2020 com o objetivo de trazer inovação para o setor de alimentação, oferecendo soluções tecnológicas que aprimoram a experiência dos clientes e otimizam o gerenciamento de restaurantes. Nossa missão é ajudar estabelecimentos de todos os tamanhos a melhorar sua eficiência operacional, reduzindo o tempo de espera dos clientes e automatizando processos internos. Através de um portfólio de produtos robustos e escaláveis, garantimos que restaurantes possam oferecer um atendimento ágil, integrado e de alta qualidade.

---

## **Descrição do Projeto**

**Enfilei** é um sistema de gerenciamento de pedidos e organização de filas de espera, desenvolvido especialmente para restaurantes que buscam otimizar seu fluxo de trabalho, aumentar a eficiência e proporcionar uma experiência agradável aos clientes. Usando tecnologias de ponta como Django REST Framework, Celery, RabbitMQ e Redis, o sistema garante a distribuição organizada dos pedidos, o monitoramento em tempo real e a redução do tempo de espera.

### **Principais Funcionalidades:**

1. **Gestão de Pedidos**: O sistema permite que os pedidos dos clientes sejam feitos digitalmente e processados em uma fila ordenada, priorizando automaticamente pedidos de delivery ou retirada.
   
2. **Fila de Espera**: Caso o restaurante esteja cheio, os clientes podem ser colocados em uma fila de espera organizada, com notificações automáticas informando quando a mesa está disponível.
   
3. **Notificações em Tempo Real**: Clientes são notificados automaticamente via SMS ou aplicativo quando o pedido está pronto ou quando uma mesa é liberada.

4. **Automação do Inventário**: O sistema atualiza o estoque de ingredientes automaticamente, com base nos pedidos feitos, garantindo uma gestão eficiente dos insumos.

---

## **Tecnologias Utilizadas:**

- **Django REST Framework**: Para criar a API que permite interagir com o sistema.
- **Celery**: Biblioteca de tarefas assíncronas para gerenciamento de fila e execução de tarefas em segundo plano.
- **RabbitMQ**: Message broker usado para enfileirar e distribuir as tarefas para os workers do Celery.
- **Redis**: Utilizado como backend opcional para armazenar temporariamente o status dos pedidos e otimizar a velocidade de recuperação de dados.

---

## **Como Funciona o Sistema:**

1. **Recebimento e Enfileiramento de Pedidos**:

- Quando um cliente faz um pedido via aplicativo ou com o garçom, o pedido é adicionado a uma fila gerenciada por RabbitMQ.
- Celery distribui as tarefas para diferentes seções do restaurante (cozinha, bar, etc.), processando os pedidos em paralelo, de acordo com a ordem recebida e priorizando quando necessário.

2. **Fila de Espera para Mesas**:

- Se o restaurante estiver cheio, os clientes podem ser colocados em uma fila de espera. O sistema gerencia essa fila e, assim que uma mesa fica disponível, o cliente recebe uma notificação informando que a mesa está pronta.
- O sistema pode fazer isso automaticamente através de Celery e RabbitMQ para processar as notificações em tempo real.

3. **Notificações Automáticas**:

- O cliente é notificado em diferentes estágios, como quando o pedido está pronto para ser servido ou quando a mesa fica disponível. Essas notificações são enviadas automaticamente via SMS ou através do aplicativo do restaurante.

4. **Automação do Inventário**:

- Cada vez que um pedido é feito, o sistema subtrai automaticamente os ingredientes utilizados do estoque. Se algum insumo atingir um nível crítico, um alerta pode ser enviado ao gerente para reabastecimento.

---

## **Instalação e Execução**

### **Pré-requisitos**:

- Python 3.8+
- Django 5.1.1
- Celery 5.x
- RabbitMQ
- Redis (opcional, pode ser usado como backend para resultados do Celery)

### **Passos para rodar o sistema**:

1. Clone o repositório:
   ```bash
   git clone https://github.com/MathewsDantas/enfilei-backend.git

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






