import pygame


MAPPING_P1 = {
    pygame.K_z: "accelerate",
    pygame.K_w: "accelerate",
    pygame.K_s: "brake",
    pygame.K_q: "left",
    pygame.K_a: "left",
    pygame.K_d: "right",
}

MAPPING_P2 = {
    pygame.K_UP: "accelerate",
    pygame.K_DOWN: "brake",
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right",
}


class InputHandler:
    """
    Gère les commandes des deux joueurs au clavier.
    """


    def __init__(self):
        self.mapping_p1 = MAPPING_P1
        self.mapping_p2 = MAPPING_P2
        

    def get_inputs(self) -> tuple[dict, dict]:
        """
        Retourne les actions activées pour chaque joueur.
        """
        keys = pygame.key.get_pressed()

        def read_mapping(mapping):
            actions = {action: False for action in mapping.values()}

            for key, action in mapping.items():
                if keys[key]:
                    actions[action] = True

            return actions

        p1 = read_mapping(self.mapping_p1)
        p2 = read_mapping(self.mapping_p2)

        return p1, p2
