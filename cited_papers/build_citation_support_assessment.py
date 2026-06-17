import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AUDIT_ROWS = json.loads((ROOT / "citation_audit_rows.json").read_text(encoding="utf-8"))
OUT = ROOT / "citation_support_assessment.json"


DEFAULT_ACTION = "No thesis wording change needed."


CITED_INFO = {
    "zengx2021ckm": "El concepto de CKM como base de datos específica del entorno con información de canal útil para comunicaciones conscientes del entorno y para reducir la adquisición online de CSI.",
    "ckmtutorial2024": "La definición tutorial de CKM y sus tipos de información, incluyendo ganancia, ángulos y retardo, como marco para 6G consciente del entorno.",
    "threegpp22125": "La terminología 3GPP UxNB y la idea de un nodo de acceso radio montado en un UAV.",
    "ckmdata2024": "La relación entre densidad de muestras, vecinos usados y error de construcción de un CKM.",
    "dataset2212": "El dataset público de mapas de path loss y ToA, el marco RadioMapSeer y el rango de path loss de 80 dB usado para convertir errores normalizados.",
    "icassp2023challenge": "El contrato del reto ICASSP 2023: dataset RadioMap3DSeer, conjunto de test oculto y métrica RMSE para mapas de path loss.",
    "jaensch2024directiverme": "Un dataset abierto de estimación de radio maps con antenas transmisoras directivas.",
    "ckmimagenet2025": "CKMImageNet como ejemplo reciente de dataset CKM rico para comunicación y sensado conscientes del entorno.",
    "rappaport": "Los fundamentos clásicos de FSPL, propagación de dos rayos y vocabulario de propagación a gran escala.",
    "wocc2021": "El modelo A2G UAV con reflexión de suelo de dos rayos y su uso para path loss.",
    "cost231": "El modelo COST 231 Hata y su papel como referencia empírica de path loss urbano NLoS.",
    "tr38901": "El modelo 3GPP TR 38.901 para LoS/NLoS, parámetros a gran escala y estadísticas de spread en dominio logarítmico.",
    "alhourani2014": "La dependencia de la probabilidad LoS y la cobertura A2G con el ángulo de elevación y la altitud.",
    "khawaja_survey": "La motivación general de modelos de canal UAV A2G, incluyendo elevación, shadowing y condiciones de propagación.",
    "saboor2025height": "La dependencia del path loss y del shadowing mmWave UAV con la altura, separando comportamiento LoS y NLoS.",
    "vinogradov2026shadow": "Las proyecciones de sombra 3D para generar mapas LoS A2G espacialmente consistentes sin ray tracing completo.",
    "winner2": "Los parámetros a gran escala WINNER, incluyendo delay spread, angular spread, shadowing lognormal y estados LoS/NLoS.",
    "isola2017pix2pix": "La formulación image to image con cGAN y U-Net como antecedente de predicción densa.",
    "radiounet2020": "RadioUNet como baseline CNN de radio maps y sus valores RMSE normalizados en escala de imagen.",
    "radiogunet2025": "RadioGUNet como extensión equivarante de RadioMapSeer y sus métricas DPM, IRT y DPM con coches.",
    "pmnet_icassp2023": "PMNet como ganador del reto ICASSP 2023 y su RMSE normalizado en test.",
    "rmtransformer2025": "RMTransformer como encoder-decoder MaxViT/CNN de 256 por 256 píxeles y sus métricas normalizadas.",
    "wicopg2025": "WiCo-PG como modelo cross modal con VQGANs, Transformer, MoE guiado por frecuencia, imágenes RGB desde UAV y NMSE reportado.",
    "fmrme2026": "FM-RME como modelo fundacional para radio map estimation con preentrenamiento autosupervisado.",
    "radiolam2025": "RadioLAM como pipeline generativo para mapas radio 3D finos con tasas de muestreo ultrabajas.",
    "geomDL2024": "La reconstrucción de radio maps con geometría asistida, diffraction, scattering, obstáculos virtuales y multi screen knife edge.",
    "reveal2025": "ReVeal como PINN con residuo PDE de segundo orden y su RMSE outdoor sparse de 1.95 dB.",
    "huang2025a2gtransformer": "El predictor Transformer A2G mmWave de características de canal, incluyendo path loss o potencia recibida, delay spread y angular spread.",
    "kendall2017uncertainties": "La pérdida de incertidumbre aleatoria heteroscedástica usada como base para modelar varianza dependiente de la entrada.",
    "saleh2021probabilistic": "El uso de mixture density networks para predecir distribuciones probabilísticas de path loss mmWave.",
    "garciamarti2020mixture": "El modelo de canal estocástico basado en mezcla gaussiana para diseño de capa física con deep learning.",
    "lee2024timevarying": "El modelado de canales variables en el tiempo con fading y shadowing usando una red y mezcla de gaussianas.",
    "radiodiff2025": "La difusión condicional para construir radio maps dinámicos usando localización de BS y características del entorno como prompts.",
    "perez2018film": "FiLM como modulación lineal feature wise mediante transformaciones afines condicionadas.",
    "izmailov2018swa": "SWA como promedio de pesos que busca óptimos más anchos y mejor generalización.",
    "airmap2025": "AIRMap como U-Net adaptativa con mapas de elevación 200 por 200, RMSE sub 4 dB de path gain, inferencia rápida y calibración con medidas.",
    "gao2026": "El predictor de path loss con mapas de profundidad Tx/Rx, mapa de distancia, weighting map de corredor y resultados RMSE de la Tabla III.",
    "tarhouni2025": "Un caso medido de predicción de path loss suburbano sub 6 GHz usado como comparación cualitativa no densa.",
    "pathfinder2025": "PathFinder para distribution shift en path loss, con atención mask guided low rank y métricas MSE, RMSE y DS-RPP.",
    "icassp2025indoor": "El reto indoor ICASSP 2025 y su tabla de weighted RMSE para los métodos participantes.",
    "indoor2025results": "La página oficial de resultados con los weighted RMSE finales de SIP2Net, IPP-Net, TerRaIn y TransPathNet.",
    "sip2net2025": "La solución SIP2Net y su weighted RMSE de 9.411 dB como primer puesto del reto indoor.",
    "ippnet2025": "La solución IPP-Net y su weighted RMSE de 9.501 dB como segundo puesto del reto indoor.",
    "transPathNet2025": "La solución TransPathNet de dos etapas y su RMSE final de 10.397 dB en el reto indoor.",
    "radiopit2025": "RadioPiT como generación de radio maps con Pixel Transformer a partir de datos reales ultraescasos.",
    "yang2019a2gml": "La predicción ML de path loss y delay spread en canales A2G mmWave a nivel de enlace.",
    "pmnet2023": "PMNet como método supervisado encoder-decoder para predicción robusta de mapas de path loss.",
    "goldsmith": "La base teórica de propagación coherente de dos rayos y coeficientes de reflexión.",
    "walfisch1988": "La influencia de filas o bloques de edificios y difracción urbana en la propagación UHF.",
    "ikegami1984": "Los factores urbanos de calle, altura de edificios, anchura de calle, orientación y altura de antena móvil.",
    "juang2021pathprofile": "El uso de path profiles y características derivadas del mapa para predicción explicable de path loss.",
    "cai2019": "Medidas A2G LTE y dependencia del path loss con ángulo de elevación en escenarios UAV.",
    "izydorczyk2019": "La variación de AoA y angular spread con la altura del UAV en escenarios urbanos y rurales.",
    "moreno2026tfgprogress": "El repositorio de historial experimental y notas internas de desarrollo que documentan intentos y módulos del proyecto.",
    "mi2024pointcloud": "La predicción con PointNet de path loss, RMS delay spread, angular spread y factor K a partir de nubes de puntos indoor.",
    "moreno2026ckmgenerator": "El repositorio del generador público de mapas CKM para path loss, delay spread y angular spread.",
    "moreno2026finalcode": "El repositorio del código final de entrenamiento y evaluación.",
    "moreno2026tfgtext": "El repositorio con el texto fuente LaTeX de la tesis.",
}


SUPPORT = {
    "zengx2021ckm": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports CKM as a site specific database of channel related information for environment aware wireless communications and reduced online CSI acquisition.",
    },
    "ckmtutorial2024": {
        "status": "SUPPORTED",
        "evidence": "Local tutorial PDF supports CKMs as location tagged channel knowledge, including channel gain, angles, and delay information for environment aware 6G.",
    },
    "threegpp22125": {
        "status": "SUPPORTED WITH CAVEAT",
        "evidence": "Official 3GPP/ETSI TS 22.125 material supports UxNB as a radio access node on board a UAV and requirements for UxNB operation. The audit folder does not include a local copy of the whole standard.",
        "action": "No thesis wording change needed; keep the source as an official specification rather than a paper.",
    },
    "ckmdata2024": {
        "status": "SUPPORTED",
        "evidence": "Local PDF studies CKM construction error versus spatial sample density and number of neighbouring samples, matching the measurement density/cost accuracy tradeoff citation.",
    },
    "dataset2212": {
        "status": "SUPPORTED AFTER TEXT CHANGE",
        "evidence": "Local PDF supports the RadioMapSeer style pathloss/ToA radio map dataset and states that pathloss values were scaled as images with an 80 dB PL range.",
        "action": "Added this citation to the RadioUNet conversion sentence in state_of_art.tex so the 80 dB range is attributed to the dataset source.",
    },
    "icassp2023challenge": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports the ICASSP 2023 pathloss radio map prediction challenge, RadioMap3DSeer training data, held out challenge test data, and RMSE evaluation contract.",
    },
    "jaensch2024directiverme": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports an open radio map estimation dataset with directive transmitter antennas and initial experiments.",
    },
    "ckmimagenet2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports CKMImageNet as an AI based CKM dataset for environment aware communication and sensing.",
    },
    "rappaport": {
        "status": "SUPPORTED WITH CAVEAT",
        "evidence": "Book reference is appropriate for FSPL, two ray, and large scale propagation vocabulary, but the book is not locally text extracted in the audit folder.",
        "action": "No thesis wording change needed; source is used as a whole textbook reference.",
    },
    "wocc2021": {
        "status": "SUPPORTED",
        "evidence": "Local PDF directly studies A2G UAV signal measurement with a two ray ground reflection model and path loss comparison.",
    },
    "cost231": {
        "status": "SUPPORTED",
        "evidence": "Local extracted COST 231 report parts contain the COST 231 Hata model, urban macrocell context, Hata/Okumura basis, and path loss formula material used for the NLoS prior.",
    },
    "tr38901": {
        "status": "SUPPORTED WITH CAVEAT",
        "evidence": "3GPP TR 38.901 is the correct standard source for 0.5 to 100 GHz channel models, LoS/NLoS states, large scale parameters, and spread modelling. The full report was not locally downloaded because it is a standard source.",
        "action": "No thesis wording change needed; keep it as an official technical report citation.",
    },
    "alhourani2014": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports elevation angle and LoS probability as central A2G modelling axes and motivates altitude dependent coverage.",
    },
    "khawaja_survey": {
        "status": "SUPPORTED",
        "evidence": "Local survey PDF supports A2G UAV channel modelling, elevation angle dependence, and shadowing/fading context.",
    },
    "saboor2025height": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports height dependent mmWave UAV path loss and shadowing in urban scenarios; it reports LoS exponent near free space and NLoS/shadowing changes with altitude.",
    },
    "vinogradov2026shadow": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports 3D shadow projections for fast, spatially consistent A2G LoS map generation and LoS aware deterministic path loss with stochastic shadow fading.",
    },
    "winner2": {
        "status": "SUPPORTED",
        "evidence": "Local report PDF supports large scale parameters, delay spread, angular spread, lognormal shadowing, and LOS/NLOS condition tables.",
    },
    "isola2017pix2pix": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports image to image translation with conditional GANs and U-Net style dense prediction baseline context.",
    },
    "radiounet2020": {
        "status": "SUPPORTED AFTER TEXT CHANGE",
        "evidence": "Local PDF supports RadioUNet as the canonical CNN radio map baseline and contains the 0.0203 to 0.0384 grey level RMSE values. The 80 dB scaling is supported by dataset2212, not by this paper alone.",
        "action": "Changed state_of_art.tex so the 80 dB conversion is attributed to the RadioMapSeer dataset citation.",
    },
    "radiogunet2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports group equivariant pathloss estimation and the exact reported metrics: 1.304 dB DPM, 1.936 dB IRT, and 1.392 dB with cars.",
    },
    "pmnet_icassp2023": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports PMNet's 1st rank challenge result and normalized RMSE 0.0383 on the challenge test set. The approximate dB conversion uses the dataset scale described elsewhere.",
    },
    "rmtransformer2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports RMTransformer as a MaxViT/CNN encoder decoder on 256 by 256 maps, with RMSE 0.007148, PMNet 0.01046, and channel prediction error 0.008099.",
    },
    "wicopg2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports dual VQGANs, a transformer, frequency guided mixture of experts, RGB images from UAV capture as auxiliary modality, U2G scenarios, and NMSE 0.012.",
    },
    "fmrme2026": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports FM-RME as a radio map foundation model with self supervised pretraining and zero shot/general inference framing.",
    },
    "radiolam2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports fine grained 3D radio map construction at ultra low sampling rates using a large generative model pipeline.",
    },
    "geomDL2024": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports diffraction and scattering aware radio map reconstruction using geometry assisted learning, virtual obstacles, and multi screen knife edge features.",
    },
    "reveal2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports ReVeal as a physics informed neural network with a second order PDE residual and reports 1.95 dB RMSE in its rural/suburban radio environment setting.",
    },
    "huang2025a2gtransformer": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports Transformer based A2G mmWave prediction of received power/path loss, delay spread, and angular spread. Table 18 contains RMS DS 4.577 ns and the cited angle spread RMSE values.",
    },
    "kendall2017uncertainties": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports aleatoric and heteroscedastic uncertainty, learned attenuation, and the regression loss basis used for uncertainty modelling.",
    },
    "saleh2021probabilistic": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports mixture density networks for probabilistic mmWave path loss distributions.",
    },
    "garciamarti2020mixture": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports a stochastic channel model learned as a Gaussian mixture distribution for physical layer design.",
    },
    "lee2024timevarying": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports a deep learning plus mixture density network model using Gaussian kernels for time varying channels with fading and shadowing.",
    },
    "radiodiff2025": {
        "status": "SUPPORTED AFTER TEXT CHANGE",
        "evidence": "Local PDF supports conditional diffusion for sampling free dynamic radio map construction using BS location and environment features as prompts.",
        "action": "Changed state_of_art.tex from obstacle prompts to environment features.",
    },
    "perez2018film": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports FiLM as feature wise linear modulation by learned affine transformations based on conditioning inputs.",
    },
    "izmailov2018swa": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports stochastic weight averaging, weight averaging, wider optima, and improved generalization.",
    },
    "airmap2025": {
        "status": "SUPPORTED WITH CAVEAT",
        "evidence": "Local PDF supports adaptive U-Net/elevation map radio maps, 200 by 200 tensors, 2.5 to 15 m/pixel resolution, sub 4 dB path gain RMSE, 4 ms inference, 20 percent field calibration, and about 5 percent median error.",
        "action": "No thesis wording change needed; the thesis already warns that AIRMap reports path gain, not the same path loss calibration.",
    },
    "gao2026": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports depth maps, a distance map, and weighting map inputs; Table III contains 5.59 dB for the proposed method, 8.09 dB PPNet, 9.56 dB RPNet, and 8.72 dB ViT-12.",
    },
    "tarhouni2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports machine learning based path loss prediction in a measured sub 6 GHz suburban environment, matching the qualitative comparison role in the thesis.",
    },
    "pathfinder2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports distribution shift radio path loss prediction, mask guided low rank attention, 0.1068 MSE, 0.3263 RMSE, and DS-RPP RMSE 0.033069, which rounds to 0.0331.",
    },
    "icassp2025indoor": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports the ICASSP 2025 indoor pathloss challenge and lists weighted RMSE values around 9.41, 9.50, 10.32, and 10.39 for the cited methods.",
    },
    "indoor2025results": {
        "status": "SUPPORTED",
        "evidence": "Official challenge results page verified on 2026-06-17 lists final weighted RMSE 9.411 for SIP2Net, 9.501 for IPP-Net, 10.325 for TerRaIn, and 10.397 for TransPathNet.",
    },
    "sip2net2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports SIP2Net's 9.411 dB weighted RMSE and 1st place indoor challenge result.",
    },
    "ippnet2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports IPP-Net's 9.501 dB weighted RMSE and second overall ranking.",
    },
    "transPathNet2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports TransPathNet's 10.397 dB overall RMSE on the indoor challenge full test set.",
    },
    "radiopit2025": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports RadioPiT as radio map generation using a pixel transformer driven by ultra sparse real world data.",
    },
    "yang2019a2gml": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports machine learning based prediction of A2G mmWave path loss and delay spread, and it is correctly described as scalar/link level rather than dense CKM map prediction.",
    },
    "pmnet2023": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports PMNet as supervised robust pathloss map prediction with an encoder decoder style radio map model, matching the dense prediction neighbour citation.",
    },
    "goldsmith": {
        "status": "SUPPORTED WITH CAVEAT",
        "evidence": "Book reference is appropriate for coherent two ray propagation and reflection coefficient vocabulary, but the book is not locally text extracted in the audit folder.",
        "action": "No thesis wording change needed; source is used as a whole textbook reference.",
    },
    "walfisch1988": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports urban UHF propagation modelling with rows or blocks of buildings treated as diffracting structures.",
    },
    "ikegami1984": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports building height, street width, street orientation, and mobile antenna height as controlling urban street propagation factors.",
    },
    "juang2021pathprofile": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports explainable path loss prediction from map derived path profile features in urban environments.",
    },
    "cai2019": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports passive LTE A2G measurements, UAV channel modelling, and elevation angle dependence in path loss modelling.",
    },
    "izydorczyk2019": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports Angle of Arrival and Angular Spread variation with height in urban and rural UAV LTE measurements.",
    },
    "moreno2026tfgprogress": {
        "status": "SOURCE RECORD",
        "evidence": "Repository citation is a reproducibility/source record for the broader development history and internal spread prior notes, not an external paper claim.",
        "action": "No thesis wording change needed; keep empty paper page fields.",
    },
    "mi2024pointcloud": {
        "status": "SUPPORTED",
        "evidence": "Local PDF supports indoor 60 GHz point cloud based prediction of path loss, RMS delay spread, azimuth angular spread, and Rician K factor; it reports average angular spread RMSE 7.39 degrees.",
    },
    "moreno2026ckmgenerator": {
        "status": "SOURCE RECORD",
        "evidence": "Repository citation supports the standalone CKM generator source record, not a paper claim.",
        "action": "No thesis wording change needed; keep empty paper page fields.",
    },
    "moreno2026finalcode": {
        "status": "SOURCE RECORD",
        "evidence": "Repository citation supports the final training and evaluation code source record, not a paper claim.",
        "action": "No thesis wording change needed; keep empty paper page fields.",
    },
    "moreno2026tfgtext": {
        "status": "SOURCE RECORD",
        "evidence": "Repository citation supports the thesis source record, not a paper claim.",
        "action": "No thesis wording change needed; keep empty paper page fields.",
    },
}


def main() -> None:
    missing = [row["_key"] for row in AUDIT_ROWS if row["_key"] not in SUPPORT]
    if missing:
        raise SystemExit(f"Missing support assessments for: {', '.join(missing)}")
    missing_info = [row["_key"] for row in AUDIT_ROWS if row["_key"] not in CITED_INFO]
    if missing_info:
        raise SystemExit(f"Missing cited information summaries for: {', '.join(missing_info)}")

    assessments = []
    for row in AUDIT_ROWS:
        key = row["_key"]
        item = SUPPORT[key]
        assessments.append(
            {
                "key": key,
                "number": row["Number of citation"],
                "status": item["status"],
                "cited_info": CITED_INFO[key],
                "evidence": item["evidence"],
                "action": item.get("action", DEFAULT_ACTION),
            }
        )

    OUT.write_text(json.dumps(assessments, indent=2, ensure_ascii=False), encoding="utf-8")
    counts = {}
    for item in assessments:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    print(json.dumps({"path": str(OUT), "entries": len(assessments), "counts": counts}, indent=2))


if __name__ == "__main__":
    main()
