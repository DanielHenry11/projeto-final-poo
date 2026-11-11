from nado_livre import NadoLivre
from interface.menus.menu_principal import MenuPrincipal
from persistencia.banco import inicializar_banco

if __name__ == "__main__":
    inicializar_banco()
    MenuPrincipal(NadoLivre()).executar()