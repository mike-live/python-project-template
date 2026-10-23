from kedro.pipeline import Pipeline

from project.modeling.pipeline import create_pipeline

"""
or you can use find_pipelines() to automatically find all pipelines in the project
"""

def register_pipelines() -> dict[str, Pipeline]:
    modeling_pipeline = create_pipeline()

#    pipelines = find_pipelines()
#    pipelines["__default__"] = sum(pipelines.values())
#    return pipelines

    return {
        "modeling": modeling_pipeline,
        "__default__": modeling_pipeline
    }

