# Estudo de Caso: Simulador de Máquina de Vendas Assíncrona com Django

Este repositório contém o desenvolvimento de uma aplicação web que simula uma máquina de venda de refrigerantes automática. O objetivo principal deste projeto foi estudar a integração do **Django (Backend)** com **JavaScript nativo (Frontend)** utilizando comunicação assíncrona (API REST/JSON) e controle de estado de interface.

## 🚀 Arquitetura e Fluxo do Projeto

Em vez de seguir o fluxo tradicional do Django de recarregar a página a cada interação (Full Page Reload), o projeto foi desenhado como uma **Single Page Application (SPA)** simplificada:

1. **Renderização Inicial:** A rota raiz (`/`) mapeia para a view `index`, que entrega o HTML/CSS da estrutura da máquina.
2. **Requisição Assíncrona:** Ao clicar em um botão de bebida, o JavaScript bloqueia a interface e dispara um método `POST` contendo um payload JSON (ex: `{"bebida": "coca"}`) para o endpoint `/liberar/`.
3. **Processamento no Backend:** A view do Django intercepta o `POST`, valida a entrada através de uma estrutura de dicionário (atuando como um switch-case) e retorna um `JsonResponse`.
4. **Animação e Feedback:** O frontend recebe o JSON de sucesso, atualiza um painel digital de LED com a mensagem gerada pelo servidor e engaja a animação física de queda da lata via CSS Keyframes.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Django 5.x / 6.x:** Configuração de URLconf modularizado (`include`), criação de views baseadas em funções (FBVs) e manipulação de objetos `JsonResponse`.
* **API REST Semântica:** Uso correto dos métodos HTTP, onde a rota `/liberar/` rejeita requisições `GET` com o status **405 Method Not Allowed** e processa dados via `POST`.
* **Segurança Restrita (Ambiente de Testes):** Uso do decorador `@csrf_exempt` para viabilizar testes rápidos de endpoints de API locais via Fetch (em produção, substitui-se pelo cabeçalho `X-CSRFToken`).
* **JavaScript Moderno (Fetch API):** Manipulação assíncrona baseada em Promises para envio e recebimento de JSON sem travar a experiência do usuário.
* **UX/UI & Animações CSS:** Criação de estados visuais dinâmicos no DOM (botões `:disabled` para evitar *double-click*) e manipulação de física visual com propriedades de transição e `keyframes`.

---

## 📂 Estrutura de Rotas Implementada

O roteamento foi modularizado para desacoplar a configuração global do projeto das regras de negócio do aplicativo de gerenciamento da máquina:

```python
# Mapeamento Global (maquina/urls.py)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")), # Delegação da rota raiz para o app
]

# Mapeamento do Aplicativo (app/urls.py)
urlpatterns = [
    path('', views.index, name='index'),              # GET -> Roda a interface
    path('liberar/', views.liberar_bebida, name='liberar_bebida'), # POST -> Processa a API
]

