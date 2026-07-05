from openvisionx.engine.pipeline_status import PipelineStatus


def test_status():

    assert PipelineStatus.IDLE == "idle"

    assert PipelineStatus.SUCCESS == "success"