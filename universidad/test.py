path_raiz = "C:/Users/francisco.cadavid/Documents/DESCARGAR_S3/"
s3_dir_conn = os.path.join(path_raiz, 's3_connection.json')
s3 = ExplorerS3(s3_dir_conn)
ruta_salida = "D:/CCO/00.INFORME RECAUDO/pagos_gestion/"

seguimiento_anno = []
carteras_anno = []
cuotas_ap_anno = []
pagos_anno = []
pagos_anno_ap = []

for anno in annos:
    data_oper = operaciones.get(operacion)
    ruta_seguimiento = os.path.join("Quipux", "Comunicaciones", "seguimientos", operacion, f"{data_oper['3']}_seguimiento_{anno}.snappy.parquet")
    seguimiento = leer_parquet(ruta_seguimiento)
    seguimiento_anno.append(seguimiento)

    archivos = s3.list_files(f"director_hermes/data/{operacion}/")
    cuotas_ap = []
    pagos_ap = []
    pagos_comp = []

    for archivo in archivos:
        if any(substring in archivo for substring in ["pagos_comparendo_morosos_2023"]):
            ruta_datos = os.path.join("director_hermes", "data", operacion, "process_data", "pago_comparendos_morosos", archivo)
            data = extraction_data(ruta_datos)
            data = data[cols_pago]
            pagos_comp.append(data)
        elif any(substring in archivo for substring in ["pago_cuotas_ap_dia_anterior"]):
            ruta_datos = os.path.join("director_hermes", "data", operacion, "process_data", "pagos_cuotas_ap_dia_anterior", archivo)
            data = extraction_data(ruta_datos)
            data = data[cols_pago_AP]
            pagos_ap.append(data)
        elif any(substring in archivo for substring in ["cuotas_ap_vencidas_dia"]):
            ruta_datos = os.path.join("director_hermes", "data", operacion, "process_data", "cuotas_ap_dia_vencido", archivo)
            data = extraction_data(ruta_datos)
            data = data[cols_ap]
            cuotas_ap.append(data)
        elif any(substring in archivo for substring in ["gral_cartera_morosa_2023"]):
            ruta_datos = os.path.join("director_hermes", "data", operacion, "process_data", "cartera_general", archivo)
            data = extraction_data(ruta_datos)
            data = data[cols_cartera]
            carteras = data
