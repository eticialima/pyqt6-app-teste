# Projeto PyQt6 - Contador Simples

Um exemplo didático de aplicação com PyQt6, demonstrando a estrutura adequada de um projeto gráfico.

## 📁 Estrutura do Projeto

```
pyqt6_app/
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
├── README.md              # Este arquivo
└── app/                   # Pacote principal
    ├── __init__.py
    ├── ui/                # Interface Gráfica (View)
    │   ├── __init__.py
    │   └── main_window.py # Janela principal
    ├── logic/             # Lógica da Aplicação (Model)
    │   ├── __init__.py
    │   └── counter.py    # Classe do contador
    └── resources/         # Recursos (ícones, imagens, etc)
```

## 🎯 Conceitos Implementados

### 1. **Arquitetura MVC** (Modelo-Visão-Controlador)
   - **Model** (`app/logic/counter.py`): Lógica de negócio
   - **View** (`app/ui/main_window.py`): Interface gráfica
   - **Controller**: Conexões entre sinais e slots

### 2. **Separação de Responsabilidades**
   - Lógica separada da interface
   - Fácil de testar e manter
   - Reutilizável em diferentes UIs

### 3. **Padrões PyQt6**
   - Signals e Slots (conexões de eventos)
   - Layouts para posicionamento responsivo
   - QFont para estilos
   - Separação em módulos

## 🚀 Como Executar

### 1. Criar ambiente virtual (opcional mas recomendado)
```bash
cd pyqt6_app
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Executar a aplicação
```bash
python main.py
```

## 📝 O que a Aplicação Faz

A aplicação é um **Contador** simples com:
- **Botão +1**: Incrementa o contador
- **Botão -1**: Decrementa o contador
- **Botão Reset**: Retorna o contador para 0
- **Display grande**: Mostra o valor atual
- **Histórico**: Mostra todos os valores registrados

## 💡 Pontos-chave para Aprender

### Classes PyQt6 Utilizadas:
- `QMainWindow`: Janela principal com menu e barra de ferramentas
- `QWidget`: Widget genérico para contêineres
- `QVBoxLayout`/`QHBoxLayout`: Layouts verticais e horizontais
- `QPushButton`: Botões
- `QLabel`: Rótulos de texto
- `QFont`: Tipografia

### Padrão de Sinais e Slots:
```python
button.clicked.connect(self.on_button_clicked)
```

### Estrutura de Pacotes:
- Cada módulo tem responsabilidade clara
- `__init__.py` define o pacote
- Imports relativos mantêm organização

## 🔧 Expandindo o Projeto

Ideias para expandir:
1. Adicionar input numérico para incrementar/decrementar por valores personalizados
2. Salvar histórico em arquivo
3. Adicionar menu com opções
4. Criar temas (estilos CSS)
5. Adicionar testes unitários
6. Implementar desfazer/refazer

## 📚 Recursos Úteis

- [Documentação PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Padrão MVC](https://pt.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)
- [Python Packaging](https://packaging.python.org/)
# pyqt6-app-teste
