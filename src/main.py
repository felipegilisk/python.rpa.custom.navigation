""" Arquivo base do projeto """
import time
from funcs import functions, logs, notify, secrets


def main():
    # try:
        secrets.load_settings()
        logs.log()
        logs.print_and_log('--------------- Automação iniciada! ---------------')

        browser = functions.start_chrome()
        logs.print_and_log('Navegador Chrome iniciado')

        functions.acme_login(browser)
        logs.print_and_log('Login no sistema ACME efetuado')
        time.sleep(2)

        collected_data = functions.acme_get_work_items_data(browser)
        logs.print_and_log('Dados coletados do sistema ACME')
        print(collected_data)

        functions.acme_logout(browser)
        logs.print_and_log('Logout no sistema ACME concluído')

        browser.close()
        logs.print_and_log('Navegador Chrome finalizado')

        
        logs.print_and_log('--------------- Processo finalizado ---------------')


    # except Exception as error:
    #     logs.print_and_log(f'{error}', warning=True)


if __name__ == '__main__':
    main()
