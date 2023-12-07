# Beanstalkd

## Breve Explicação

O **beanstalkd** é um servidor de **filas** leve e escalável, projetado para ser simples e eficiente. Ele é **usado para gerenciar filas de mensagens assíncronas**, permitindo que os aplicativos enviem e recebam mensagens de forma eficiente e desacoplada. Foi escrito em C por Keith Rarick e é distribuído como software de código aberto.

## Conceito

O beanstalkd fornece uma fila de tarefas onde os **_producers_** (produtores) colocam mensagens e os **_consumers_** (consumidores) retiram essas mensagens para processamento. As mensagens na fila são chamadas de **_"jobs"_**, e cada _job_ é associado a uma tarefa específica no qual um aplicativo precisa realizar.

## Características

- **Leveza:** O beanstalkd é projetado para ser eficiente em termos de recursos, tornando-o uma escolha atraente para situações em que a eficiência é crítica.

- **Protocolo Simples:** Ele usa um protocolo de comunicação simples baseado em texto, facilitando a integração com uma variedade de linguagens de programação.

- **Prioridades e Atrasos:** Jobs podem ser priorizados e configurados com atrasos, permitindo que os desenvolvedores controlem a ordem e o momento em que as tarefas são processadas.

- **Escalabilidade:** O beanstalkd é projetado para ser distribuído e escalável, permitindo que você dimensione sua infraestrutura de fila conforme necessário.

- **APIs para Diversas Linguagens:** Existem bibliotecas e APIs disponíveis para várias linguagens de programação, facilitando a integração do beanstalkd em diferentes ambientes de desenvolvimento.

## Linguagens Suportadas

- C/C++
- Go
- Java
- Javascript
- Node.JS
- PHP
- Python
- Ruby
- Rust
- .NET/C#

> _Essas são as linguagens mais comuns utilizadas, mas além destas existem outras._

## Utilidade do Beanstalkd

Os desenvolvedores costumam **utilizar** o beanstalkd em **cenários onde é necessário desacoplar processos assíncronos**, como processamento de trabalhos em segundo plano, **balanceamento de carga**, entre outros. Ele oferece uma solução eficiente para lidar com fluxos de trabalho que envolvem tarefas assíncronas e distribuídas.

## Configuração de Ambiente - Beanstalkd e Beanstalkd Console

### Requisitos

- Linux (Recomendado usar Ubuntu 20.04+)
- Python 3.6+

```
$ sudo apt-get install python3.12
```

### Usando Ubuntu 20.04 ou superior

```
Instale o Python
$ sudo apt-get install python3.12

Instale o beanstalkd
$ sudo apt-get update
$ sudo apt-get install beanstalkd

Por fim, instale a biblioteca pystalk
$ pip install pystalk
```

- Comandos para _iniciar, parar, reiniciar ou checar status do serviço Beanstalkd_

```
$ sudo systemctl {start|status|restart|stop} beanstalkd
ou
$ sudo service beanstalkd {start|status|restart|stop}
```

- Como instalar a interface Web para o Beanstalkd

```
$ curl -s http://getcomposer.org/installer | php
$ composer create-project ptrofimov/beanstalk_console -s dev /var/www/html/beanstalk_console
$ cd /var/www/html/beanstalk_console
```

- Como verificar o _hostname_ no beanstalkd

```
$ hostname -I
```

> _O resultado retornado deve ser algo como: 192.168.1.104 172.18.0.1 172.17.0.1_

```
$ php -S 192.168.1.104:7654 -t public
```

- Em seguida, acesse o navegador usando o hostname e a porta especificada no comando acima.

- Após acessar o navegador, adicione um novo servidor com _localhost:11300_

## Executando o Projeto

Acesse o diretório onde está os arquivos do consumer.py e do producer.py e em seguida execute o seguinte comando no terminal:

```
python3 <nome_do_arquivo>.py
```
