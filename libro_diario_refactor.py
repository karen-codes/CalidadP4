"""
Módulo para la gestión de un libro diario contable.
Permite registrar transacciones financieras y obtener resúmenes de saldos.
"""

from typing import List, Dict, Union


class LibroDiario:
    """Clase que gestiona el registro de transacciones contables."""

    # Constantes para evitar literales mágicos (Punto 104 de la guía)
    TIPO_INGRESO = "ingreso"
    TIPO_EGRESO = "egreso"

    def __init__(self) -> None:
        """Inicializa el libro diario con una lista vacía de transacciones."""
        self.transacciones: List[Dict[str, Union[str, float]]] = []

    def agregar_transaccion(
        self, fecha: str, descripcion: str, monto: float, tipo: str
    ) -> None:
        """
        Agrega una nueva transacción validando los datos de entrada.

        Args:
            fecha: Fecha de la operación (YYYY-MM-DD).
            descripcion: Concepto del movimiento.
            monto: Valor numérico (debe ser positivo).
            tipo: Debe ser 'ingreso' o 'egreso'.
        """
        if monto <= 0:
            raise ValueError("El monto debe ser un número positivo.")

        tipo_normalizado = tipo.lower().strip()
        if tipo_normalizado not in [self.TIPO_INGRESO, self.TIPO_EGRESO]:
            raise ValueError("Tipo de transacción inválido.")

        self.transacciones.append({
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": float(monto),
            "tipo": tipo_normalizado
        })

    def calcular_resumen(self) -> Dict[str, float]:
        """
        Calcula el total de ingresos y egresos registrados.

        Returns:
            Dict: Estructura de datos con los totales calculados.
        """
        totales = {self.TIPO_INGRESO: 0.0, self.TIPO_EGRESO: 0.0}

        for movimiento in self.transacciones:
            tipo = movimiento["tipo"]
            totales[tipo] += movimiento["monto"]

        return totales