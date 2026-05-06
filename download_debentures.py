from playwright.sync_api import sync_playwright
import os
from datetime import datetime

# ============================================
# CONFIGURAÇÃO - MUDE AQUI
# ============================================
DOWNLOAD_DIR = r"C:\BigData\Codes\AnbimaRep"   # <-- ALTERE PARA O SEU CAMINHO
URL = "https://data.anbima.com.br/datasets/data-debentures-precificacao-anbima"

def main():
    # Cria a pasta se não existir
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    print("🚀 Iniciando download da planilha ANBIMA...")
    
    with sync_playwright() as p:
        # headless=False = abre o navegador (bom para testar)
        # headless=True  = roda invisível (produção)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()
        
        print("📡 Acessando página...")
        page.goto(URL, wait_until="networkidle", timeout=60000)
        
        # Espera um pouco para a página carregar completamente
        page.wait_for_timeout(2000)
        
        # Tenta encontrar o botão de Download
        try:
            # Opção 1: botão com texto "Download"
            download_button = page.get_by_role("button", name="Download").first
            
            # Se não encontrar, tenta outra forma comum
            if not download_button.is_visible():
                download_button = page.locator('button:has-text("Download")').first
            
            print("🖱️ Clicando no botão Download...")
            
            #with page.expect_download() as download_info:
            #  download_button.click()
            
            download = download_info.value
            
            # Nome do arquivo com data
            today = datetime.now().strftime("%Y-%m-%d")
            filename = f"debentures_precificacao_anbima_{today}.xlsx"
            save_path = os.path.join(DOWNLOAD_DIR, filename)
            
            download.save_as(save_path)
            
            print(f"✅ Planilha salva com sucesso!")
            print(f"📁 Local: {save_path}")
            
        except Exception as e:
            print(f"❌ Erro ao baixar: {e}")
            print("Dica: Abra o site no navegador e veja como está o botão de Download.")
            print("Você pode ajustar o seletor no script (linha do get_by_role).")
        
        finally:
            browser.close()

if __name__ == "__main__":
    main()

    qualquer coisa
    