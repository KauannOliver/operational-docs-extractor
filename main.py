import os
import json
from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

lista = json.loads(Path(os.environ.get("DOCS_PAGES_FILE", "pages.local.json")).read_text(encoding="utf-8"))

# Inicializar o WebDriver
for required in ("DOCS_LOGIN_URL", "DOCS_USERNAME", "DOCS_PASSWORD"):
    if not os.environ.get(required):
        raise SystemExit(f"Missing required configuration: {required}")
driver = webdriver.Chrome()

# URL da página de login
url = os.environ["DOCS_LOGIN_URL"]
driver.get(url)

try:
    # Esperar e preencher o campo de login
    campo_login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/ft-core-login/div/div/div/wac-input/div/div/input"))
    )
    campo_login.send_keys(os.environ["DOCS_USERNAME"])

    # Esperar e preencher o campo de senha
    campo_senha = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/ft-core-login/div/div/div/wac-input-button/div/div/input"))
    )
    campo_senha.send_keys(os.environ["DOCS_PASSWORD"])

    time.sleep(1)

    # Esperar e clicar no botão de login
    botao_entrar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/ft-core-login/div/div/div/wac-button[1]/button"))
    )
    botao_entrar.click()

    # Esperar que o login seja concluído antes de prosseguir
    time.sleep(5)

    # Percorrer cada item na lista
    for item in lista:
        # Navegar até o link do item
        driver.get(item["link"])
        time.sleep(2)  # Espera inicial

        # Pressionar F5 para atualizar a página
        driver.refresh()
        time.sleep(3)  # Esperar alguns segundos para o carregamento após o refresh

        # Verificar se a nova página carregou completamente ao esperar um elemento específico dessa página
        try:
            elemento_unico = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/ft-home/div/main/div/ft-central-ajuda-detalhes/div/main/div/div[1]/p[1]"))
            )

            # Extrair texto do primeiro elemento
            elemento1 = elemento_unico.text

            # Extrair texto do segundo elemento
            elemento2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/ft-home/div/main/div/ft-central-ajuda-detalhes/div/main/div/div[1]/p[2]"))
            ).text

            # Extrair texto do terceiro elemento
            elemento3 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/app-root/ft-home/div/main/div/ft-central-ajuda-detalhes/div/main/div/div[2]"))
            ).text

            # Criar um arquivo .txt com o nome do item e salvar os textos extraídos
            with open(f"{item['nome']}.txt", "w", encoding="utf-8") as file:
                file.write("Ultima Atualização:\n" + elemento1 + "\n\n")
                file.write(elemento2 + "\n\n")
                file.write(elemento3 + "\n\n")

            print(f"Dados extraídos e salvos em {item['nome']}.txt")

        except Exception as e:
            print(f"Ocorreu um erro ao extrair dados para {item['nome']}: {e}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Manter o navegador aberto até que seja fechado manualmente
#input("Pressione Enter para encerrar o programa e fechar o navegador manualmente...")