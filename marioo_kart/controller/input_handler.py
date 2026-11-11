import pygame


MAPPING = {
    pygame.K_UP:     "accelerate",
    pygame.K_DOWN: "brake",
}


class InputHandler:
    """
    Gère les commandes du joueur au clavier.

    Associe les touches aux actions du jeu et indique
    quelles commandes sont actuellement activées.
    """

    def __init__(self):
        self.mapping = MAPPING

    def get_inputs(self) -> dict:
        """
        Récupère les commandes actuellement activées au clavier.

        Retourne un dictionnaire associant chaque action
        à un booléen indiquant si sa touche est enfoncée.
        """

        keys = pygame.key.get_pressed()
        p = {action: False for action in self.mapping.values()}

        for key, action in self.mapping.items():
            if keys[key]:
                p[action] = True

        return p
