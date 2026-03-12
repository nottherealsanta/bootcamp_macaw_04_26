# Continuous Integration (Safety Net)

CI passes when all the test and checks are done.

- Code Validation - linting, formatting, type checking, security checks, etc.
- Data Validation - Schemas(cols having types) - stats
- Unit Testing - model outputs are checked. 
(Experiment Tracking )

# Continuous Deployment ( Release )

- Containerization 

- shadow depolyment
  - model B also get the same traffic and make prediction as your model A - but these results are not used.
- Canary deployment 
  - say take 5% of traffic and route it to your model B
- A/B Testing

| Category | Top Tools | Why? |
|----------|-----------|------|
| Pipeline/Runner | GitHub Actions, GitLab CI, CircleCI, Jenkins | Standard for triggering workflows on code changes. |
| Version Control | DVC (Data Version Control) | It's like "Git for Data." It tracks 10GB datasets without slowing down Git. |
| Testing | Deepchecks, Pytest | Specifically designed for validating ML models and data. |
| Automation | CML (Continuous Machine Learning) | Automatically posts model performance graphs as comments on your Pull Request. |
| Registry | MLflow, SageMaker Registry | A "library" of your trained models, showing who trained what and when. |


# Continuous Training

- Drift
  - Data
    - Feature
    - Target
  - Concept 
- Monitoring

Trigger -> retrain

- Performanced-based
- Schedule-based 
- Availability
- On-demand