
"""
--------------------------------------------------
TPI - Organización Empresarial

Sistema de Gestión de Solicitudes de Vacaciones
Estudio Jurídico Madryn
--------------------------------------------------
"""

import pandas as pd
from datetime import datetime
from pathlib import Path


# ----------------------------------
# CONFIGURACIÓN
# ----------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_EXCEL = BASE_DIR / "Base_Datos" / "base_datos_vacaciones.xlsx"

HOJA_EMPLEADOS = "empleados"
HOJA_SOLICITUDES = "solicitudes"


# ----------------------------------
# BASE DE DATOS
# ----------------------------------

def cargar_base_datos():
    """
    Carga las hojas Empleados y Solicitudes.
    """

    try:
        df_empleados = pd.read_excel(
            ARCHIVO_EXCEL,
            sheet_name=HOJA_EMPLEADOS
        )

        df_solicitudes = pd.read_excel(
            ARCHIVO_EXCEL,
            sheet_name=HOJA_SOLICITUDES
        )

        return df_empleados, df_solicitudes

    except FileNotFoundError:
        raise FileNotFoundError(
            "No se encontró el archivo de base de datos."
        )

    except Exception as error:
        raise Exception(
            f"Error al cargar la base de datos: {error}"
        )


def guardar_base_datos(df_empleados, df_solicitudes):
    """
    Guarda los cambios realizados en el Excel.
    """

    with pd.ExcelWriter(
        ARCHIVO_EXCEL,
        engine="openpyxl",
        mode="w"
    ) as writer:

        df_empleados.to_excel(
            writer,
            sheet_name=HOJA_EMPLEADOS,
            index=False
        )

        df_solicitudes.to_excel(
            writer,
            sheet_name=HOJA_SOLICITUDES,
            index=False
        )


# ----------------------------------
# EMPLEADOS
# ----------------------------------

def buscar_empleado(df_empleados, legajo):
    """
    Busca un empleado por legajo.
    """

    resultado = df_empleados[
        df_empleados["legajo"] == legajo
    ]

    if resultado.empty:
        return None

    return resultado.iloc[0]


def consultar_saldo(empleado):
    """
    Devuelve los días disponibles.
    """

    return int(empleado["dias_disponibles"])


# ----------------------------------
# VALIDACIONES
# ----------------------------------

def validar_dias():
    """
    Solicita y valida los días.
    """

    while True:

        entrada = input(
            "\nIngrese la cantidad de días que desea solicitar: "
        ).strip()

        if not entrada:
            print(
                "Debe ingresar una cantidad de días."
            )
            continue

        try:

            dias = int(entrada)

            if dias <= 0:
                raise ValueError

            return dias

        except ValueError:

            print(
                "La cantidad de días debe ser un número mayor a cero."
            )


# ----------------------------------
# SOLICITUDES
# ----------------------------------

def registrar_solicitud(
    df_solicitudes,
    legajo,
    dias_solicitados,
    estado,
    motivo
):
    """
    Registra una nueva solicitud.
    """

    nuevo_id = (
        int(df_solicitudes["id_solicitud"].max())
        + 1
    )

    nueva_solicitud = {
        "id_solicitud": nuevo_id,
        "legajo": legajo,
        "fecha_solicitud":
            datetime.now().strftime("%d/%m/%Y"),
        "dias_solicitados": dias_solicitados,
        "estado": estado,
        "motivo": motivo
    }

    df_solicitudes.loc[
        len(df_solicitudes)
    ] = nueva_solicitud


def aprobar_solicitud(
    df_empleados,
    empleado,
    dias_solicitados
):
    """
    Actualiza el saldo del empleado.
    """

    indice = empleado.name

    saldo_actual = int(
        empleado["dias_disponibles"]
    )

    nuevo_saldo = (
        saldo_actual - dias_solicitados
    )

    df_empleados.at[
        indice,
        "dias_disponibles"
    ] = nuevo_saldo

    return nuevo_saldo


# ----------------------------------
# PROGRAMA PRINCIPAL
# ----------------------------------

def main():

    print("=" * 50)
    print("Estudio Jurídico Madryn")
    print("Gestión de Solicitudes de Vacaciones")
    print("=" * 50)

    try:

        df_empleados, df_solicitudes = (
            cargar_base_datos()
        )

        while True:

            entrada = input(
                "\nIngrese su número de legajo: "
            ).strip()

            if not entrada:
                print(
                    "Debe ingresar un número de legajo."
                )
                continue

            try:
                legajo = int(entrada)

            except ValueError:
                print(
                    "El legajo debe ser numérico."
                )
                continue

            empleado = buscar_empleado(
                df_empleados,
                legajo
            )

            if empleado is None:

                print(
                    "Legajo no encontrado."
                )
                continue

            break

        print(
            f"\nBienvenido/a "
            f"{empleado['nombre_empleado']}"
        )

        dias_solicitados = validar_dias()

        saldo_disponible = consultar_saldo(
            empleado
        )

        if saldo_disponible >= dias_solicitados:

            saldo_restante = aprobar_solicitud(
                df_empleados,
                empleado,
                dias_solicitados
            )

            registrar_solicitud(
                df_solicitudes,
                legajo,
                dias_solicitados,
                "Aprobada",
                "Saldo suficiente"
            )

            guardar_base_datos(
                df_empleados,
                df_solicitudes
            )

            print(
                "\nSolicitud aprobada."
            )

            print(
                f"Días solicitados: "
                f"{dias_solicitados}"
            )

            print(
                f"Saldo restante: "
                f"{saldo_restante}"
            )

        else:

            motivo = (
                "Saldo insuficiente"
            )

            if saldo_disponible == 0:
                motivo = (
                    "Sin días disponibles"
                )

            registrar_solicitud(
                df_solicitudes,
                legajo,
                dias_solicitados,
                "Rechazada",
                motivo
            )

            guardar_base_datos(
                df_empleados,
                df_solicitudes
            )

            print(
                "\nSolicitud rechazada."
            )

            print(
                f"Saldo disponible: "
                f"{saldo_disponible}"
            )

            print(
                f"Días solicitados: "
                f"{dias_solicitados}"
            )

            print(
                f"Motivo: {motivo}"
            )

    except Exception as error:

        print(
            f"\nError del sistema: "
            f"{error}"
        )


if __name__ == "__main__":
    main()

