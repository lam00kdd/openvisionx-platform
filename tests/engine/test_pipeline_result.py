from openvisionx.engine.pipeline_result import PipelineResult


def test_result():

    result = PipelineResult()

    assert result.status.name == "IDLE"

    assert result.elapsed_ms == 0