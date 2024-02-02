""" Arquivo para notificações e templates de notificações """
import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_mail(mail_to: str, mail_subject: str, mail_body: str, mail_attachment: str):
    """
    Envio de e-mail
     - mail_to: destinatário
     - mail_subject: assunto
     - mail_body: corpo da mensagem
     - mail_attachment: arquivo a ser anexado, contendo o caminho completo
    """
    SENDER = os.environ.get("MAIL_LOGIN")
    SENDER_PWORD = os.environ.get("MAIL_PWORD")

    html_message = MIMEMultipart()
    html_message['Subject'] = mail_subject
    html_message['From'] = SENDER
    html_message['To'] = mail_to
    html_message.attach(MIMEText(mail_body, 'html'))

    with open(mail_attachment, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(mail_attachment)}",
    )

    html_message.attach(part)

    context = ssl.create_default_context()

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls(context=context)
        server.login(SENDER, SENDER_PWORD)
        server.sendmail(SENDER, mail_to, html_message.as_string().encode("UTF-8"))


def html_body(data_count: dict):
    """
    Converte os dados coletados em html para envio do e-mail
    """
    html = """
    <h3>Prezado colaborador,</h3>
    <p>Segue em anexo o arquivo com os dados vinculados a categoria "Work Items" para análise.</p>
    <p>Abaixo também segue o resumo dos registros agrupados por tipo.</p>
    <table style="width: 300px; text-align: center">
        <thead style="background-color:#8dafff">
            <tr style="border: 2px solid #00000000">
                <th style="width: 30%">Tipo</th>
                <th>Quantidade de registros</th>
            </tr>
        </thead>
        <tbody>"""
    
    for item in data_count:
        html += f"""
            <tr style="border: 2px solid #00000000; background-color: #ddd; color: #000">
                <td>{item}</td>
                <td>{data_count[item]}</td>
            </tr>"""
    html += """
        </tbody>
    </table>
"""
    return html
