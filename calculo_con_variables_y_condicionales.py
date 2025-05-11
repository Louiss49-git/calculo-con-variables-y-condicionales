# Cálculo de sueldo neto en República Dominicana en pesos dominicanos en python dependiendo el sueldo, bonificacion, descuentos, etc.

#  cosas que se tienen al pendiente al calcular  el Salario
TSS_PORCENTAJE = 0.0591     # 5.91% Seguridad Social
ISR_PORCENTAJE = 0.15       # 15% ISR 
BONIFICACION_PORCENTAJE = 0.10  # 10% bonificación si aplica

#lo que le pide al que esta usando el programa

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
        retencion_isr = sueldo_bruto * ISR_PORCENTAJE
        bonificacion = sueldo_bruto * BONIFICACION_PORCENTAJE if aplica_bonificacion == 'si' else 0

        sueldo_neto = sueldo_bruto - descuento_tss - retencion_isr - otros_descuentos + bonificacion

        # Luego de los calculos se muestran los resultados
        print("\n===== Detalle del Cálculo del Salario =====")
        print(f"Sueldo Bruto: RD$ {sueldo_bruto:,.2f}")
        
        print(f"Descuento por Seguridad Social (TSS): RD$ {descuento_tss:,.2f}")
        print(f"Retención ISR: RD$ {retencion_isr:,.2f}")
        print(f"Otros Descuentos: RD$ {otros_descuentos:,.2f}")
        print(f"Bonificación: RD$ {bonificacion:,.2f}")
        print(f"Sueldo Neto: RD$ {sueldo_neto:,.2f}")

    #si pone algo como una letra cuando se le pide sueldo o otras cosas que son expresadas en numeros le dara error
    except ValueError as e:
        print(f"Error en la entrada de datos: {e}")

# Bucle para poder volver a calcular el sueldo 
while True:
    calcular_sueldo()
    repetir = input("\n¿Desea realizar otro cálculo? (si/no): ").strip().lower()
    if repetir != 'si':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
