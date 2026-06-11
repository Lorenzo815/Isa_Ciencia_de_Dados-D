"""Baixa datasets publicos do Kaggle para praticas extras do curso.

Alguns datasets publicos podem exigir login no Kaggle e aceite dos termos na pagina
do dataset. Se um download falhar, acesse o link do dataset no navegador, aceite os
termos e rode o script novamente.
"""

from pathlib import Path
import shutil

import kagglehub

DATASETS = {
    "ibm_hr_attrition": "pavansubhasht/ibm-hr-analytics-attrition-dataset",
    "job_change_data_scientists": "arashnic/hr-analytics-job-change-of-data-scientists",
    "hr_analytics_prediction": "rishikeshkonapure/hr-analytics-prediction",
}


def main() -> None:
    destino = Path("dados_kaggle")
    destino.mkdir(exist_ok=True)

    print("Baixando datasets publicos do Kaggle...")
    for nome, slug in DATASETS.items():
        print(f"\nDataset: {nome}")
        print(f"Slug: {slug}")
        try:
            caminho_cache = Path(kagglehub.dataset_download(slug))
            destino_dataset = destino / nome
            if destino_dataset.exists():
                shutil.rmtree(destino_dataset)
            shutil.copytree(caminho_cache, destino_dataset)
            print(f"Baixado em cache: {caminho_cache}")
            print(f"Copia local: {destino_dataset}")
        except Exception as erro:
            print("Nao foi possivel baixar este dataset agora.")
            print(f"Motivo: {erro}")
            print("Dica: confira login, internet e aceite dos termos no Kaggle.")

    print("\nConcluido. As copias locais ficam em dados_kaggle/.")


if __name__ == "__main__":
    main()
