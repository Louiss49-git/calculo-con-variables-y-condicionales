# Cálculo de sueldo neto en República Dominicana en pesos dominicanos en python dependiendo el sueldo, bonificación, descuentos, etc.

#  cosas que se tienen al pendiente al calcular el Salario
TSS_PORCENTAJE = 0.0591     # 5.91% Seguridad Social
BONIFICACION_PORCENTAJE = 0.10  # 10% bonificación solo si se aplica

# lo que calcula el porcentaje del ISR según tramos oficiales de la DGII (2025)
def calcular_isr(ingreso_anual):
    if ingreso_anual <= 416220.00:
        return 0
    elif ingreso_anual <= 624329.00:
        excedente = ingreso_anual - 416220.01
        return excedente * 0.15
    elif ingreso_anual <= 867123.00:
        excedente = ingreso_anual - 624329.01
        return 31216.00 + excedente * 0.20
    else:
        excedente = ingreso_anual - 867123.01
        return 79776.00 + excedente * 0.25

# Lo que le pide al que está usando el programa
def calcular_sueldo():
    try:
        sueldo_bruto = float(input("\nIngrese el sueldo bruto del empleado (RD$): "))
        if sueldo_bruto <= 0:
            raise ValueError("El sueldo debe ser un valor positivo.")
        
        otros_descuentos = float(input("Ingrese el monto por otros descuentos (RD$): "))
        if otros_descuentos < 0:
            raise ValueError("Los descuentos no pueden ser negativos.")
        
        aplica_bonificacion = input("¿Aplica bonificación? (si/no): ").strip().lower()
        if aplica_bonificacion not in ('si', 'no'):
            raise ValueError("Debe ingresar 'si' o 'no'.")

        # Cálculos
        descuento_tss = sueldo_bruto * TSS_PORCENTAJE
        ingreso_anual = sueldo_bruto * 12
        isr_anual = calcular_isr(ingreso_anual)
        retencion_isr = isr_anual / 12  # Se mensualiza
        bonificacion = sueldo_bruto * BONIFICACION_PORCENTAJE if aplica_bonificacion == 'si' else 0

        sueldo_neto = sueldo_bruto - descuento_tss - retencion_isr - otros_descuentos + bonificacion

        # Luego de los cálculos se muestran los resultados
        print("\n===== Detalle del Cálculo del Salario =====")
        print(f"Sueldo Bruto: RD$ {sueldo_bruto:,.2f}")
        print(f"Descuento por Seguridad Social (TSS): RD$ {descuento_tss:,.2f}")
        print(f"Retención ISR (mensual): RD$ {retencion_isr:,.2f}")
        print(f"Otros Descuentos: RD$ {otros_descuentos:,.2f}")
        print(f"Bonificación: RD$ {bonificacion:,.2f}")
        print(f"Sueldo Neto: RD$ {sueldo_neto:,.2f}")

    # Si pone algo como una letra cuando se le pide sueldo u otros datos, mostrará error
    except ValueError as e:
        print(f"Error en la entrada de datos: {e}")

# Bucle para poder volver a calcular el sueldo 
while True:
    calcular_sueldo()
    repetir = input("\n¿Desea realizar otro cálculo? (si/no): ").strip().lower()
    if repetir != 'si':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
