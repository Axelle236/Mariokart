# Kart-Engine v2.3

import math

from constants import (
    CAR_ACCELERATION,
    CAR_TURN_SPEED,
    CAR_WIDTH,
    CAR_HEIGHT,
    TILE_SIZE,
    CAR_GRIP,
    CAR_MAX_SPEED,
    CAR_MAX_REVERSE_SPEED,
    CAR_FRICTION,
    TERRAIN_GRIP
)


class Car:
    """
    Représente une voiture du jeu.

    Gère sa position, sa vitesse, son orientation
    et son adhérence.
    """

    def __init__(
        self,
        start_col: int,
        start_row: int,
        color: tuple[int, int, int] = (255, 0, 0)
    ) -> None:
        """
        Initialise la voiture au centre de sa case de départ.
        """
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.vx: float = 0.0
        self.vy: float = 0.0
        self.grip: float = CAR_GRIP
        self.color = color

    def accelerate(self) -> None:
        """
        Augmente la vitesse sans dépasser
        la vitesse maximale autorisée.
        """
        self.speed = min(
            self.speed + CAR_ACCELERATION,
            CAR_MAX_SPEED
        )

    def brake(self) -> None:
        """
        Freine la voiture et limite
        la vitesse en marche arrière.
        """
        self.speed = max(
            self.speed - CAR_ACCELERATION,
            -CAR_MAX_REVERSE_SPEED
        )

    def decelerate(self) -> None:
        """
        Réduit progressivement la vitesse
        en l'absence d'accélération et de freinage.
        """
        self.speed *= (1 - CAR_FRICTION)

        if abs(self.speed) < 0.01:
            self.speed = 0.0

    def turn_left(self) -> None:
        """
        Tourne la voiture vers la gauche.
        """
        self.angle -= CAR_TURN_SPEED

    def turn_right(self) -> None:
        """
        Tourne la voiture vers la droite.
        """
        self.angle += CAR_TURN_SPEED

    def set_terrain(self, terrain: str) -> None:
        """
        Adapte l'adhérence de la voiture
        en fonction du terrain.
        """
        self.grip = TERRAIN_GRIP.get(terrain, CAR_GRIP)

    def update_position(self) -> None:
        """
        Met à jour la position de la voiture
        en tenant compte de son orientation
        et de son glissement.
        """
        angle_rad = math.radians(self.angle)

        # Vitesse souhaitée selon l'orientation
        target_vx = self.speed * math.sin(angle_rad)
        target_vy = -self.speed * math.cos(angle_rad)

        # Transition progressive vers cette direction
        self.vx += (target_vx - self.vx) * self.grip
        self.vy += (target_vy - self.vy) * self.grip

        # Mise à jour de la position
        self.x += self.vx
        self.y += self.vy

    def check_boundaries(self, width: int, height: int) -> None:
        """
        Empêche la voiture de sortir des limites du circuit.
        """
        margin = math.hypot(CAR_WIDTH, CAR_HEIGHT) / 2

        if self.x < margin:
            self.x = margin
            self.vx = 0.0
            self.speed = 0.0

        elif self.x > width - margin:
            self.x = width - margin
            self.vx = 0.0
            self.speed = 0.0

        if self.y < margin:
            self.y = margin
            self.vy = 0.0
            self.speed = 0.0

        elif self.y > height - margin:
            self.y = height - margin
            self.vy = 0.0
            self.speed = 0.0