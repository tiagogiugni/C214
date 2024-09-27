# Interface para o serviço de envio de e-mails
class EmailServiceInterface:
    def enviar_email(self, destinatario, assunto, mensagem):
        raise NotImplementedError("Este método deve ser implementado por uma classe concreta")

# Implementação concreta do serviço de envio de e-mails
class EmailServiceSMTP(EmailServiceInterface):
    def enviar_email(self, destinatario, assunto, mensagem):
        print(f"Enviando e-mail para {destinatario} com o assunto '{assunto}' e a mensagem:\n{mensagem}\n")

# Classe Lead representando um cliente potencial
class Lead:
    def __init__(self, nome, email): 
        self.nome = nome
        self.email = email

# Gerenciador de Oportunidades que utiliza o serviço de e-mails
class OportunidadeManager:
    def __init__(self, email_service):  
        self.email_service = email_service

    def criar_oportunidade(self, lead, descricao):
        # Simula a criação de uma nova oportunidade para o lead
        print(f"Oportunidade criada para {lead.nome}: {descricao}")
        # Enviando e-mail para o lead sobre a nova oportunidade
        assunto = "Nova Oportunidade"
        mensagem = f"Olá {lead.nome}, temos uma nova oportunidade para você: {descricao}"
        self.email_service.enviar_email(lead.email, assunto, mensagem)

if __name__ == "__main__": 
    # Criando uma instância do serviço de envio de e-mails
    email_service = EmailServiceSMTP()

    # Criando uma instância do gerenciador de oportunidades com a injeção de dependência do serviço de e-mails
    oportunidade_manager = OportunidadeManager(email_service)

    # Criando um lead e uma nova oportunidade
    lead = Lead("Tiago", "tiago.goncalves@ges.inatel.br")
    oportunidade_manager.criar_oportunidade(lead, "Parceria exclusiva com condições especiais")
