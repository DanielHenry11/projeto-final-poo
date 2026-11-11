from nado_livre import NadoLivre
from interface.menus.menu_principal import MenuPrincipal
 banco-de-dados
from persistencia.banco import inicializar_banco

if __name__ == "__main__":
    inicializar_banco()
    MenuPrincipal(NadoLivre()).executar()


def main():
    app = NadoLivre()
    try:
        MenuPrincipal(app).executar()
    finally:
        app.salvar_dados()

if __name__ == "__main__":
    main()

