from kedro.pipeline import Pipeline

from project.modeling.local_pipeline import create__local_pipeline
from project.modeling.pipeline import create_pipeline

"""
or you can use find_pipelines() to automatically find all pipelines in the project
"""

def register_pipelines() -> dict[str, Pipeline]:
    modeling_pipeline = create_pipeline()
    local_modeling_pipeline = create__local_pipeline()

#    pipelines = find_pipelines()
#    pipelines["__default__"] = sum(pipelines.values())
#    return pipelines

    return {
        "modeling": modeling_pipeline,
        "local_modeling": local_modeling_pipeline,
        "__default__": modeling_pipeline + local_modeling_pipeline
    }

