from clinical_nlp_pipeline.pipeline import run_pipeline

if __name__ == "__main__":
    sample = "Patient denies chest pain but reports fever and cough. History of hypertension."
    result = run_pipeline(sample)
    print(result)
