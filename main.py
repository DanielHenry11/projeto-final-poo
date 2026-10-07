from nado_livre import NadoLivre
from interface.menus.menu_principal import MenuPrincipal

def main():
    app = NadoLivre()
    try:
        MenuPrincipal(app).executar()
    finally:
        app.salvar_dados()

if __name__ == "__main__":
    main()