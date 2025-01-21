# ClearML (End-to-End AI Platform)

## [Experiment Tracking](https://clear.ml/docs/latest/docs/fundamentals/task)
## [Data Versioning](https://clear.ml/docs/latest/docs/clearml_data/)

Example: [Basics](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_simple)

### Uploading a dataset

```sh
  # Create an empty dataset
  clearml-data create --project <project name> --name <dataset-name>
  
  # Add files and folders to the dataset
  clearml-data add --files <file/folder>
  
  # Compress and upload the added files and folders
  clearml-data close
  
  # List dataset contents
  clearml-data --name <dataset-name>
```

### Using the uploaded dataset

```python
  from clearml import Dataset
  
  path = Dataset.get(dataset_name="", dataset_project="").get_local_copy()
```

## [Pipelines (CI/CD)](https://clear.ml/docs/latest/docs/pipelines/)
## [Model Serving and Monitoring](https://clear.ml/docs/latest/docs/clearml_serving/)
## References

  - [Website](https://clear.ml/)
  - [Documentation](https://clear.ml/docs/latest/docs/)
  - [Examples](https://github.com/clearml/clearml/tree/master/examples)
  - [Comparision with alternatives](https://clear.ml/blog/stacking-up-against-the-competition)
