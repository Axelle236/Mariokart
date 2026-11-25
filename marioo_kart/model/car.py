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
    TERRAIN_GRIP,
    TERRAIN_TRACTION,
    TERRAIN_FRICTION,
    AIR_FRICTION,
    DRIFT_ANGLE_THRESHOLD,
    TERRAIN_DRIFT_FRICTION,
    CAR_BOOST_SPEED,
    CAR_MAX_BOOST_SPEED
)
GRIP_SCALE = 0.87

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
        self.traction: float = 1.0
        self.friction: float = CAR_FRICTION
        self.drift_friction: float = TERRAIN_DRIFT_FRICTION["road"]
        self.color = color

    def accelerate(self) -> None:
        """
        Accélère la voiture jusqu'à sa vitesse maximale
        normale sans annuler l'effet d'un boost.
        """
        if self.speed < CAR_MAX_SPEED:
            self.speed = min(
                self.speed + CAR_ACCELERATION * self.traction,
                CAR_MAX_SPEED
            )

    def brake(self) -> None:
        """
        Freine la voiture et limite
        la vitesse en marche arrière.
        """
        self.speed = max(
            self.speed - CAR_ACCELERATION * self.traction,
            -CAR_MAX_REVERSE_SPEED
        )

    def decelerate(self) -> None:
        """
        Réduit progressivement la vitesse
        en l'absence d'accélération et de freinage.
        """
        self.speed *= (1 - self.friction)

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
        Adapte l'adhérence et la traction au terrain.
        """
        self.grip = TERRAIN_GRIP.get(terrain, CAR_GRIP) * GRIP_SCALE

        self.traction = TERRAIN_TRACTION.get(terrain, 1.0)

        self.friction = TERRAIN_FRICTION.get(terrain, CAR_FRICTION)

        self.drift_friction = TERRAIN_DRIFT_FRICTION.get(
            terrain, TERRAIN_DRIFT_FRICTION["road"]
        )

    def get_drift_angle(self) -> float:
        """
        Calcule l'angle de dérapage de la voiture
        en marche avant et en marche arrière.
        """

        if math.hypot(self.vx, self.vy) < 0.01:
            return 0.0

        direction = math.degrees(
            math.atan2(self.vx, -self.vy)
        )

        orientation = self.angle

        if self.speed < 0:
            orientation += 180

        ecart = (direction - orientation + 180) % 360 - 180

        return abs(ecart)

    def apply_drift_friction(self) -> None:
        """
        Applique des frottements supplémentaires
        lorsque la voiture dérape.
        """
        drift_angle = self.get_drift_angle()

        if drift_angle > DRIFT_ANGLE_THRESHOLD:

            facteur = 1 - self.drift_friction

            self.speed *= facteur
            self.vx *= facteur
            self.vy *= facteur

    def apply_air_friction(self) -> None:
        """
        Applique les frottements de l'air.
        """
        self.speed *= (1 - AIR_FRICTION)
        self.vx *= (1 - AIR_FRICTION)
        self.vy *= (1 - AIR_FRICTION)

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

        # Application des frottements
        self.apply_drift_friction()
        self.apply_air_friction()

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

    def reset_position(
        self,
        x: float,
        y: float,
        angle: float
    ) -> None:
        """
        Réinitialise la position et l'orientation
        de la voiture en annulant sa vitesse.
        """
        self.x = x
        self.y = y
        self.angle = angle

        self.speed = 0.0
        self.vx = 0.0
        self.vy = 0.0

    def apply_boost(self) -> None:
        """
        Augmente la vitesse de la voiture
        sans dépasser la vitesse maximale du boost.
        """

        if self.speed >= 0:
            self.speed = min(
                self.speed + CAR_BOOST_SPEED,
                CAR_MAX_BOOST_SPEED
        )